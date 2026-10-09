"""A small server-rendered portfolio. Edit public content in content.py."""
from datetime import date

from flask import Flask, redirect, render_template, url_for
from content import (COPY, CURRENT_FOCUS, FILTERS, LINKS, NAVIGATION, PROFILE,
                     PROJECTS, PROJECT_SECTIONS)

app = Flask(__name__)


@app.context_processor
def shared_content():
    return {"profile": PROFILE, "links": LINKS, "navigation": NAVIGATION,
            "copy": COPY, "year": date.today().year}


@app.get("/")
def index():
    return render_template("index.html", current_focus=CURRENT_FOCUS)


@app.get("/projects")
def projects():
    projects_by_slug = {project["slug"]: project for project in PROJECTS}
    project_sections = [
        {
            **section,
            "projects": [projects_by_slug[slug] for slug in section["slugs"]],
        }
        for section in PROJECT_SECTIONS
    ]
    return render_template("projects.html", projects=PROJECTS,
                           project_sections=project_sections, filters=FILTERS)


@app.get("/projects/python-task-tracker")
def task_tracker_redirect():
    # Preserve the old bookmark; the tracker is now part of its repository entry.
    return redirect(url_for("projects", _anchor="task-tracker"), code=301)


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404
