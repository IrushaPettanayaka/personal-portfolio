"""Run with: python -m unittest discover -s tests -v"""
from html.parser import HTMLParser
from pathlib import Path
import unittest
from unittest.mock import patch
from app import app
from content import FILTERS, PROFILE, PROJECTS, PROJECT_SECTIONS


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings = 0
        self.links = []
        self.assets = []
        self.ids = set()
        self.cards = []
        self.filters = None

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == 'h1':
            self.headings += 1
        if tag == 'a':
            self.links.append(attrs.get('href', ''))
        if tag in ('script', 'img') and attrs.get('src'):
            self.assets.append(attrs['src'])
        if tag == 'link':
            self.assets.append(attrs.get('href', ''))
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if 'project-card' in attrs.get('class', '').split():
            self.cards.append(attrs)
        if attrs.get('class') == 'project-filters':
            self.filters = attrs


class PortfolioTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_routes_navigation_and_assets(self):
        for path in ['/', '/projects']:
            response = self.client.get(path)
            self.assertEqual(response.status_code, 200)
            page = PageParser()
            page.feed(response.get_data(as_text=True))
            self.assertEqual(page.headings, 1)
            for asset in page.assets:
                with self.client.get(asset) as result:
                    self.assertEqual(result.status_code, 200)
            for link in page.links:
                self.assertNotIn(link, ['', '#'])
                if link.startswith(('/', '#')):
                    route, _, fragment = link.partition('#')
                    result = self.client.get(route or path)
                    self.assertEqual(result.status_code, 200)
                    target = PageParser()
                    target.feed(result.get_data(as_text=True))
                    if fragment:
                        self.assertIn(fragment, target.ids)

    def test_complete_archive_without_javascript(self):
        page = PageParser()
        page.feed(self.client.get('/projects').get_data(as_text=True))
        expected = {'python-learning-lab', 'task-tracker', 'number-guesser', 'number-guessing-early',
                    'rock-paper-scissors', 'dice-roller', 'caesar-cipher',
                    'pin-extractor', 'python-calculator', 'aegis-engine', 'gesture-defender'}
        self.assertEqual({c['id'] for c in page.cards}, expected)
        self.assertTrue(all('hidden' not in c for c in page.cards))
        self.assertIn('hidden', page.filters)
        self.assertEqual(len(page.cards), 11)
        self.assertEqual(len({p['source_url'] for p in PROJECTS}), 11)

    def test_exact_source_paths_and_distinct_versions(self):
        paths = {p['slug']: p['source_url'] for p in PROJECTS}
        self.assertTrue(paths['task-tracker'].endswith('/task_tracker/task_tracker.py'))
        self.assertTrue(paths['number-guesser'].endswith('/number_guesser.py'))
        self.assertTrue(paths['number-guessing-early'].endswith('/Number_guessing.py'))
        self.assertTrue(paths['dice-roller'].endswith('/Python_mini_projects/blob/main/game.py'))
        self.assertTrue(paths['pin-extractor'].endswith('/pin_extractor/main.py'))
        self.assertTrue(paths['python-calculator'].endswith('/Python_calculator/calculator.py'))
        self.assertEqual(paths['aegis-engine'], 'https://github.com/aasim10-Volt/aegis')
        self.assertEqual(paths['python-learning-lab'], 'https://github.com/IrushaPettanayaka/python-learning-lab')

    def test_categories_and_attribution(self):
        counts = {f['key']: sum(p['filter'] == f['key'] for p in PROJECTS) for f in FILTERS if f['key'] != 'all'}
        self.assertEqual(counts, {'web': 1, 'python': 6, 'course': 2, 'team': 1, 'assisted': 1})
        html = self.client.get('/projects').get_data(as_text=True)
        self.assertIn('Built with substantial Codex assistance; my role involved direction, testing, and small edits.', html)
        self.assertIn('Our Cipher 2.0 team project', html)
        self.assertNotIn('ZAID-EHT', html)
        self.assertNotIn('<img', html)

    def test_project_grouping_and_clear_source_links(self):
        self.assertEqual(
            PROJECT_SECTIONS[0]['slugs'],
            ['python-learning-lab', 'aegis-engine', 'gesture-defender', 'python-calculator'],
        )
        html = self.client.get('/projects').get_data(as_text=True)
        self.assertLess(html.index('id="python-learning-lab"'), html.index('id="aegis-engine"'))
        self.assertLess(html.index('id="gesture-defender"'), html.index('id="number-guesser"'))
        self.assertIn('Practice &amp; course exercises', html)
        for project in PROJECTS:
            self.assertIn(f'<a href="{project["source_url"]}">{project["title"]}</a>', html)
            self.assertIn(f'aria-label="View {project["title"]} source on GitHub">Source', html)

    def test_positioning_and_missing_contact(self):
        html = self.client.get('/').get_data(as_text=True)
        self.assertIn('Drawn to <em>mathematics.</em>', html)
        self.assertIn('<span>Learning</span> <span>through code.</span>', html)
        self.assertIn('I’m Irusha, a computing student at IIT exploring Python, AI, and data engineering.', html)
        self.assertIn('Foundation in Computing', html)
        self.assertIn('planned for January 2027', html)
        self.assertIn('I’ve also freelanced in graphic design', html)
        self.assertNotIn('Graphic design — Fiverr', html)
        self.assertNotIn('mailto:', html)
        self.assertIn('href="/projects"', html)
        self.assertNotIn('CURRENT FOCUS', html)
        self.assertNotIn('focus-summary', html)
        self.assertNotIn('>Focus</a>', html)
        with patch.dict(PROFILE, email='hello@example.com'):
            self.assertIn('mailto:hello@example.com', self.client.get('/').get_data(as_text=True))

    def test_theme_system_and_no_script_fallback(self):
        html = self.client.get('/').get_data(as_text=True)
        self.assertIn('<html lang="en" data-theme="dark">', html)
        self.assertIn('data-theme-toggle', html)
        self.assertIn('aria-label="Switch to light theme" hidden', html)
        self.assertIn("localStorage.getItem('portfolio-theme')", html)

        css = Path('static/css/style.css').read_text(encoding='utf-8').lower()
        for color in ['#0c0d0f', '#17181b', '#1d1f23', '#f3f0e9', '#aaaeb6',
                      '#33363d', '#a8bde7', '#f2efe8', '#fbfaf7', '#eceae5',
                      '#1b1c20', '#5a606a', '#ced0d4', '#365f9f']:
            self.assertIn(color, css)
        self.assertIn(':root[data-theme="light"]', css)
        self.assertIn('@media (prefers-reduced-motion: reduce)', css)

        theme_js = Path('static/js/theme.js').read_text(encoding='utf-8')
        self.assertIn("localStorage.setItem('portfolio-theme'", theme_js)
        self.assertIn('toggle.hidden = false', theme_js)

    def test_metadata_contact_and_woff2_font(self):
        home = self.client.get('/').get_data(as_text=True)
        projects = self.client.get('/projects').get_data(as_text=True)
        self.assertIn('Message me on LinkedIn', home)
        self.assertIn('property="og:image"', projects)
        self.assertIn('Projects — Irusha Pettanayaka', projects)
        self.assertIn('Explore Irusha Pettanayaka’s selected applications', projects)
        self.assertIn('Manrope-Variable.woff2', projects)
        font = Path('static/fonts/Manrope-Variable.woff2').read_bytes()
        self.assertEqual(font[:4], b'wOF2')
        with self.client.get('/static/images/social-preview.png') as preview:
            self.assertEqual(preview.status_code, 200)
            self.assertEqual(preview.mimetype, 'image/png')
        css = Path('static/css/style.css').read_text(encoding='utf-8')
        self.assertIn('outline: 3px solid var(--accent)', css)

    def test_obsolete_widget_is_removed(self):
        for path in ['/', '/projects']:
            html = self.client.get(path).get_data(as_text=True)
            self.assertNotIn('phase-slider', html)
            self.assertNotIn('wave-plot', html)
        self.assertFalse(Path('static/js/main.js').exists())

    def test_redirect_and_missing_pages(self):
        response = self.client.get('/projects/python-task-tracker')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.headers['Location'], '/projects#task-tracker')
        self.assertEqual(self.client.get('/projects/unknown').status_code, 404)

    def test_editable_content_is_autoescaped(self):
        with patch.dict(PROFILE, introduction='<script>alert("test")</script>'):
            html = self.client.get('/').get_data(as_text=True)
            self.assertNotIn('<script>alert("test")</script>', html)
            self.assertIn('&lt;script&gt;', html)


if __name__ == '__main__':
    unittest.main()
