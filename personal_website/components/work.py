"""Work / Selected Projects section."""

import reflex as rx


_PROJECTS = [
    {
        "image": "/images/work-fraud.svg",
        "alt": "Fraud Detection Pipeline",
        "chips": ["ML", "Streaming"],
        "year": "2024",
        "title": "Real-Time Fraud Detection Pipeline",
        "desc": (
            "Low-latency streaming pipeline processing millions of transactions "
            "with sub-second model inference and automated alerting."
        ),
    },
    {
        "image": "/images/work-features.svg",
        "alt": "Feature Store",
        "chips": ["MLOps", "Python"],
        "year": "2024",
        "title": "Feature Store for E-commerce",
        "desc": (
            "Centralized feature platform serving real-time and batch features "
            "to recommendation models across multiple teams."
        ),
    },
    {
        "image": "/images/work-quality.svg",
        "alt": "Data Quality Framework",
        "chips": ["dbt", "SQL"],
        "year": "2023",
        "title": "Automated Data Quality Framework",
        "desc": (
            "Comprehensive testing and monitoring layer that catches data issues "
            "before they reach downstream consumers."
        ),
    },
    {
        "image": "/images/work-nlp.svg",
        "alt": "NLP Pipeline",
        "chips": ["NLP", "Transformers"],
        "year": "2023",
        "title": "NLP Pipeline for Document Classification",
        "desc": (
            "Transformer-based classification system handling millions of "
            "documents with active learning for continuous improvement."
        ),
    },
]


def _work_card(project: dict[str, str | list[str]]) -> rx.Component:
    """Render a single work card."""
    chips = project["chips"]
    assert isinstance(chips, list)
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src=str(project["image"]),
                alt=str(project["alt"]),
            ),
            class_name="work-card-image",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    *[rx.el.span(c, class_name="chip") for c in chips],
                    class_name="chips",
                ),
                rx.el.span(str(project["year"]), class_name="year"),
                class_name="work-card-meta",
            ),
            rx.el.h3(str(project["title"])),
            rx.el.p(str(project["desc"])),
            class_name="work-card-body",
        ),
        class_name="work-card reveal",
    )


def work_section() -> rx.Component:
    """2×2 grid of selected work cards."""
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div("Selected Work", class_name="label"),
                rx.el.a("View all ↗", href="#", class_name="view-all"),
                class_name="section-header reveal",
            ),
            rx.el.div(
                *[_work_card(p) for p in _PROJECTS],
                class_name="work-grid",
            ),
            class_name="container",
        ),
        id="work",
    )
