"""Editable portfolio content. Projects are verified snapshots, not live API data."""

PROFILE = {
    "name": "Irusha Pettanayaka",
    "first_name": "Irusha",
    "last_name": "Pettanayaka",
    "initials": "I.P.",
    "location": "Sri Lanka",
    "introduction": "I’m Irusha, a computing student at IIT exploring Python, AI, and data engineering.",
    "about": "I enjoy understanding the logic behind things, especially where mathematics and programming meet. I’m developing that foundation through my studies at IIT, Python practice, and projects. I also participated in Cipher 2.0, where our team built Aegis.",
    "personal": "I’ve also freelanced in graphic design and uploaded my photography to Shutterstock.",
    "education": "Currently studying Foundation in Computing at IIT, Sri Lanka.",
    "next_step": "BEng in AI & Data Engineering — planned for January 2027.",
    "email": None,
}
LINKS = {
    "github": "https://github.com/IrushaPettanayaka",
    "linkedin": "https://www.linkedin.com/in/irusha-pettanayaka/",
}
NAVIGATION = [
    {"label": "Home", "endpoint": "index", "anchor": None},
    {"label": "Projects", "endpoint": "projects", "anchor": None},
    {"label": "About", "endpoint": "index", "anchor": "about"},
]
COPY = {
    "site_title": "Computing student",
    "hero_label": "Mathematics / Programming / AI",
    "about_heading": "About",
    "focus_heading": "Current focus",
    "projects_heading": "Projects",
    "projects_intro": "A Flask learning lab, collaborative work, Python practice, and experiments — collected in one place.",
    "projects_link": "View projects",
    "projects_page_intro": "An archive of my learning so far: individual exercises, small applications, and collaborative work.",
    "projects_page_label": "Project archive",
    "filter_label": "Filter projects",
    "project_count_label": "projects shown",
    "contact_heading": "Contact",
    "contact_title": "Say hello.",
    "source_link": "View source",
    "back_home": "Back to home",
    "skip_link": "Skip to content",
    "back_top": "Back to top",
    "not_found_title": "A little off course.",
    "not_found_text": "That page doesn’t exist. You can explore the archive on the Projects page.",
}
CURRENT_FOCUS = [
    {"title": "Mathematics", "description": "Developing my mathematical foundations and problem-solving skills."},
    {"title": "Python", "description": "Practising through exercises and small applications."},
    {"title": "AI & data engineering", "description": "Exploring the ideas behind intelligent systems and working with data."},
]
FILTERS = [
    {"key": "all", "label": "All"},
    {"key": "web", "label": "Web applications"},
    {"key": "python", "label": "Python practice"},
    {"key": "course", "label": "Course exercises"},
    {"key": "team", "label": "Team projects"},
    {"key": "assisted", "label": "AI-assisted"},
]

PROJECT_SECTIONS = [
    {
        "key": "selected",
        "label": "Selected work",
        "description": "Applications and collaborative work that best show how I approach a problem.",
        "slugs": ["python-learning-lab", "aegis-engine", "gesture-defender", "python-calculator"],
    },
    {
        "key": "practice",
        "label": "Practice & course exercises",
        "description": "Focused command-line applications and coursework that document steady Python progress.",
        "slugs": ["task-tracker", "number-guesser", "rock-paper-scissors", "caesar-cipher", "pin-extractor", "dice-roller", "number-guessing-early"],
    },
]

# Keep individual exercises explicit, even when they share a repository.
# Use the exact file path and case from GitHub. No invented demo links.
PROJECTS = [
    {
        "slug": "python-learning-lab", "title": "Python Learning Lab",
        "category": "Flask web application", "filter": "web",
        "summary": "Four beginner Python exercises rebuilt as one interactive application with an SQLite student planner, algorithm visualisations, probability simulation, validation, sessions, and tests.",
        "technologies": ["Python", "Flask", "SQLite", "Jinja", "JavaScript"],
        "source_url": "https://github.com/IrushaPettanayaka/python-learning-lab",
        "note": "Expanded from my original CLI exercises with Codex assistance; I directed the scope, reviewed the behaviour, and kept the original scripts for comparison.",
    },
    {
        "slug": "task-tracker", "title": "Persistent Task Tracker",
        "category": "Python practice", "filter": "python",
        "summary": "A persistent CLI task manager with JSON storage, priorities, categories, due dates, overdue detection, filters, search, and guarded deletion.",
        "technologies": ["Python", "JSON", "unittest"],
        "source_url": "https://github.com/IrushaPettanayaka/Python_mini_projects/blob/main/task_tracker/task_tracker.py",
        "note": None,
    },
    {
        "slug": "number-guesser", "title": "Number Guesser",
        "category": "Python practice", "filter": "python",
        "summary": "A configurable guessing challenge with three difficulty profiles, warmer-or-colder feedback, guess history, duplicate prevention, and session statistics.",
        "technologies": ["Python", "dataclasses", "unittest"],
        "source_url": "https://github.com/IrushaPettanayaka/Python_mini_projects/blob/main/number_guesser.py",
        "note": None,
    },
    {
        "slug": "number-guessing-early", "title": "Quick Guess",
        "category": "Python practice", "filter": "python",
        "summary": "A compact object-oriented guessing game with limited attempts, graduated proximity hints, replay support, and a running session score.",
        "technologies": ["Python", "dataclasses"],
        "source_url": "https://github.com/IrushaPettanayaka/Python_mini_projects/blob/main/Number_guessing.py",
        "note": None,
    },
    {
        "slug": "rock-paper-scissors", "title": "Adaptive Rock–Paper–Scissors",
        "category": "Python practice", "filter": "python",
        "summary": "A best-of command-line game with a live scoreboard and an opponent that learns the player’s most frequent move and sometimes counters it.",
        "technologies": ["Python", "collections", "enums"],
        "source_url": "https://github.com/IrushaPettanayaka/Python_mini_projects/blob/main/Rock_paper_scissors.py",
        "note": None,
    },
    {
        "slug": "dice-roller", "title": "Dice Lab",
        "category": "Python practice", "filter": "python",
        "summary": "A dice-notation parser and probability lab for custom rolls, modifiers, theoretical ranges, expected averages, and 10,000-roll simulations.",
        "technologies": ["Python", "regular expressions", "probability"],
        "source_url": "https://github.com/IrushaPettanayaka/Python_mini_projects/blob/main/game.py",
        "note": None,
    },
    {
        "slug": "caesar-cipher", "title": "Caesar Cipher",
        "category": "Course exercise", "filter": "course",
        "summary": "A freeCodeCamp exercise for shifting letters to encrypt and decrypt text.",
        "technologies": ["Python"],
        "source_url": "https://github.com/IrushaPettanayaka/FreeCodeCamp_projects_python/blob/main/caesar_cipher/main.py",
        "note": None,
    },
    {
        "slug": "pin-extractor", "title": "PIN Extractor",
        "category": "Course exercise", "filter": "course",
        "summary": "A freeCodeCamp exercise that derives codes from word lengths at successive positions in lines of poems.",
        "technologies": ["Python"],
        "source_url": "https://github.com/IrushaPettanayaka/FreeCodeCamp_projects_python/blob/main/pin_extractor/main.py",
        "note": None,
    },
    {
        "slug": "python-calculator", "title": "Python Calculator",
        "category": "Python practice", "filter": "python",
        "summary": "A menu-driven calculator for arithmetic, powers, square roots, modulus, and floor division, with numeric-input and invalid-operation checks.",
        "technologies": ["Python"],
        "source_url": "https://github.com/IrushaPettanayaka/PythonProject_Irusha_Pettanayaka/blob/main/Python_calculator/calculator.py",
        "note": None,
    },
    {
        "slug": "aegis-engine", "title": "Aegis Engine",
        "category": "Team project", "filter": "team",
        "summary": "Our Cipher 2.0 team project: a platform for forming balanced student project teams and monitoring team health.",
        "technologies": ["Python", "TypeScript", "Next.js", "Supabase"],
        "source_url": "https://github.com/aasim10-Volt/aegis",
        "note": None,
    },
    {
        "slug": "gesture-defender", "title": "Gesture Defender",
        "category": "AI-assisted experiment", "filter": "assisted",
        "summary": "A Python arcade game with webcam gesture controls.",
        "technologies": ["Python", "Pygame", "OpenCV", "MediaPipe"],
        "source_url": "https://github.com/IrushaPettanayaka/gesture-defender",
        "note": "Built with substantial Codex assistance; my role involved direction, testing, and small edits.",
    },
]
