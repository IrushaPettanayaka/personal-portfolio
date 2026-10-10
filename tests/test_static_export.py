"""Verification for the Cloudflare Pages static export."""

from html.parser import HTMLParser
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from export_static import PROJECT_ROOT, export_site


class ExportedPageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.assets = []
        self.meta = {}

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "script" and attrs.get("src"):
            self.assets.append(attrs["src"])
        if tag == "link" and attrs.get("href"):
            self.assets.append(attrs["href"])
        if tag == "meta" and attrs.get("property"):
            self.meta[attrs["property"]] = attrs.get("content", "")


class StaticExportTests(unittest.TestCase):
    def setUp(self):
        test_temp_root = PROJECT_ROOT / ".local-tmp"
        test_temp_root.mkdir(exist_ok=True)
        self.temp_dir = TemporaryDirectory(dir=test_temp_root)
        self.output = Path(self.temp_dir.name) / "site"
        export_site(self.output, "https://portfolio.example")

    def tearDown(self):
        self.temp_dir.cleanup()

    def _parse(self, relative_path):
        page = ExportedPageParser()
        page.feed((self.output / relative_path).read_text(encoding="utf-8"))
        return page

    def test_exports_every_page_and_cloudflare_files(self):
        for relative_path in ["index.html", "projects/index.html", "404.html",
                              "_redirects"]:
            self.assertTrue((self.output / relative_path).is_file())
        self.assertEqual(
            (self.output / "_redirects").read_text(encoding="utf-8"),
            "/projects/python-task-tracker /projects#task-tracker 301\n",
        )

    def test_navigation_targets_exist_in_the_export(self):
        route_files = {"/": "index.html", "/projects": "projects/index.html"}
        for relative_path in route_files.values():
            page = self._parse(relative_path)
            for href in page.links:
                if href.startswith("#"):
                    self.assertIn(href[1:], page.ids)
                elif href.startswith("/"):
                    path, _, fragment = href.partition("#")
                    self.assertIn(path, route_files)
                    target = self._parse(route_files[path])
                    if fragment:
                        self.assertIn(fragment, target.ids)

    def test_asset_paths_resolve_and_metadata_uses_site_url(self):
        for relative_path in ["index.html", "projects/index.html", "404.html"]:
            page = self._parse(relative_path)
            self.assertEqual(
                page.meta["og:image"],
                "https://portfolio.example/static/images/social-preview.png",
            )
            for asset in page.assets:
                if asset.startswith("/"):
                    self.assertTrue((self.output / asset.lstrip("/")).is_file(), asset)

    def test_local_only_screenshots_are_not_published(self):
        self.assertFalse((self.output / "static/images/gesture-defender.png").exists())
        self.assertFalse((self.output / "static/images/task-tracker-source.png").exists())

    def test_direct_url_files_exist(self):
        # Cloudflare maps / to index.html and /projects/ to projects/index.html;
        # its documented clean-URL handling redirects /projects to /projects/.
        direct_urls = {
            "/": self.output / "index.html",
            "/projects/": self.output / "projects/index.html",
            "/static/css/style.css": self.output / "static/css/style.css",
        }
        for path, target in direct_urls.items():
            self.assertTrue(target.is_file(), path)

    def test_repeated_export_removes_stale_files(self):
        stale = self.output / "stale.txt"
        stale.write_text("old build", encoding="utf-8")
        export_site(self.output, "https://portfolio.example")
        self.assertFalse(stale.exists())


if __name__ == "__main__":
    unittest.main()
