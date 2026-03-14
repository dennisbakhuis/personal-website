"""Main application entry point."""

import reflex as rx

from .pages import index_page

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&family=Inter:wght@300;400;500;600&family=Lato:wght@900&display=swap",
        "/styles.css",
    ],
    head_components=[
        rx.el.script(src="/site.js", defer=True),
    ],
)

app.add_page(
    component=index_page,
    route="/",
    title="Dennis Bakhuis",
)
