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
    "projects_intro": "Python practice, course exercises, a team hackathon project, and an AI-assisted experiment — collected in one place.",
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
        "slugs": ["aegis-engine", "task-tracker", "python-calculator", "gesture-defender"],
    },
    {
        "key": "practice",
        "label": "Practice & course exercises",
        "description": "Smaller programs that document steady Python practice and course progress.",
        "slugs": ["number-guesser", "rock-paper-scissors", "caesar-cipher", "pin-extractor", "dice-roller", "number-guessing-early"],
    },
]

# Keep individual exercises explicit, even when they share a repository.
# Use the exact file path and case from GitHub. No invented demo links.
PROJECTS = [
    {
        "slug": "task-tracker", "title": "Task Tracker",
        "category": "Python practice", "filter": "python",
        "summary": "A CLI tool to add, view, complete, and delete tasks, with input validation and in-memory storage for the current session.",
        "technologies": ["Python"],
        "source_url": "https://github.com/IrushaPettanayaka/Python_mini_projects/blob/main/task_tracker/task_tracker.py",
        "note": None,
    },
    {
        "slug": "number-guesser", "title": "Number Guesser",
        "category": "Python practice", "filter": "python",
        "summary": "A number-guessing game with difficulty levels, limited attempts, proximity hints, and numeric input validation.",
        "technologies": ["Python"],
        "source_url": "https://github.com/IrushaPettanayaka/Python_mini_projects/blob/main/number_guesser.py",
        "note": None,
    },
    {
        "slug": "number-guessing-early", "title": "Number Guessing: Early Version",
        "category": "Python practice", "filter": "python",
        "summary": "An early single-guess exercise that compares a number with a random target and reports whether it is too high, too low, or correct.",
        "technologies": ["Python"],
        "source_url": "https://github.com/IrushaPettanayaka/Python_mini_projects/blob/main/Number_guessing.py",
        "note": None,
    },
    {
        "slug": "rock-paper-scissors", "title": "Rock–Paper–Scissors",
        "category": "Python practice", "filter": "python",
        "summary": "A command-line game against randomly selected computer choices, with the option to play again.",
        "technologies": ["Python"],
        "source_url": "https://github.com/IrushaPettanayaka/Python_mini_projects/blob/main/Rock_paper_scissors.py",
        "note": None,
    },
    {
        "slug": "dice-roller", "title": "Dice Roller",
        "category": "Python practice", "filter": "python",
        "summary": "A command-line program that rolls a user-selected number of six-sided dice.",
        "technologies": ["Python"],
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
