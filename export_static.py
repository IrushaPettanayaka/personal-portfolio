"""Export the Flask portfolio as a static site for Cloudflare Pages."""

from __future__ import annotations

import os
import shutil
from pathlib import Path

from app import app


PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT = PROJECT_ROOT / "dist"
ROUTES = {
    "/": Path("index.html"),
    "/projects": Path("projects/index.html"),
}
LOCAL_ONLY_ASSETS = {
    "gesture-defender.png",
    "task-tracker-source.png",
}


def _deployment_url(explicit_url: str | None = None) -> str:
    """Return the URL Flask should use for absolute metadata links."""
    url = explicit_url or os.getenv("SITE_URL") or os.getenv("CF_PAGES_URL")
    if not url:
        return "http://localhost"
    url = url.rstrip("/")
    if not url.startswith(("https://", "http://")):
        raise ValueError("SITE_URL must begin with https:// or http://")
    return url


def _ignore_local_assets(directory: str, names: list[str]) -> set[str]:
    """Keep locally preserved screenshots out of the deployable site."""
    if Path(directory).name != "images":
        return set()
    return LOCAL_ONLY_ASSETS.intersection(names)


def export_site(output_dir: Path = DEFAULT_OUTPUT,
                site_url: str | None = None) -> Path:
    """Render every public route and copy its static assets into output_dir."""
    output_dir = Path(output_dir).resolve()
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    shutil.copytree(
        PROJECT_ROOT / "static",
        output_dir / "static",
        ignore=_ignore_local_assets,
    )

    base_url = _deployment_url(site_url)
    with app.test_client() as client:
        for route, relative_path in ROUTES.items():
            response = client.get(route, base_url=base_url)
            if response.status_code != 200:
                raise RuntimeError(
                    f"Could not export {route}: HTTP {response.status_code}"
                )
            destination = output_dir / relative_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(response.data)

        missing = client.get("/__static-export-404__", base_url=base_url)
        if missing.status_code != 404:
            raise RuntimeError("The Flask 404 handler did not return HTTP 404")
        (output_dir / "404.html").write_bytes(missing.data)

    # Cloudflare Pages reads this file from the published output directory.
    (output_dir / "_redirects").write_text(
        "/projects/python-task-tracker /projects#task-tracker 301\n",
        encoding="utf-8",
    )
    return output_dir


if __name__ == "__main__":
    exported = export_site()
    print(f"Exported static site to {exported}")
