"""TIL (Today I Learned) section."""

import reflex as rx


_TILS = [
    {
        "date": "Mar 2026",
        "tag": "Python",
        "title": "DuckDB can query Parquet files directly from S3",
        "desc": (
            "No need to download first — just point DuckDB at an S3 path and "
            "run SQL. Great for quick exploratory analysis."
        ),
    },
    {
        "date": "Feb 2026",
        "tag": "LLM",
        "title": "Structured outputs make LLM pipelines much more reliable",
        "desc": (
            "Constrained decoding with JSON schemas eliminates most parsing "
            "failures in production LLM workflows."
        ),
    },
    {
        "date": "Feb 2026",
        "tag": "MLOps",
        "title": "uv is replacing pip, pyenv, and virtualenv for me",
        "desc": (
            "One tool for Python versions, dependencies, and environments. "
            "Blazing fast and just works."
        ),
    },
]


def _writing_card(til: dict[str, str]) -> rx.Component:
    """Render a single TIL card."""
    return rx.el.div(
        rx.el.div(
            rx.el.span(til["date"]),
            rx.el.span(til["tag"]),
            class_name="card-meta",
        ),
        rx.el.h3(til["title"]),
        rx.el.p(til["desc"]),
        rx.el.span("↗", class_name="card-arrow"),
        class_name="writing-card",
    )


def til_section() -> rx.Component:
    """3-column grid of TIL cards."""
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div("Today I Learned", class_name="label"),
                rx.el.a("All TILs ↗", href="#", class_name="view-all"),
                class_name="section-header reveal",
            ),
            rx.el.div(
                *[_writing_card(t) for t in _TILS],
                class_name="writing-grid reveal",
            ),
            class_name="container",
        ),
        id="til",
    )
