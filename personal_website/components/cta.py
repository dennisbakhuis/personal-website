"""CTA / Highlight section (warm beige panel)."""

import reflex as rx


_CTA_CARDS = [
    {
        "title": "Consulting",
        "text": (
            "Need help building ML systems or data infrastructure? I work with "
            "teams to design and implement production-grade pipelines."
        ),
        "link_text": "Get in touch ↗",
        "link_href": "#contact",
        "external": False,
    },
    {
        "title": "Open Source",
        "text": (
            "I contribute to and maintain open-source tools for data engineering "
            "and machine learning workflows."
        ),
        "link_text": "View on GitHub ↗",
        "link_href": "https://github.com/dennisbakhuis",
        "external": True,
    },
    {
        "title": "Speaking",
        "text": (
            "I speak at meetups and conferences about data engineering, MLOps, "
            "and building effective data teams."
        ),
        "link_text": "Invite me ↗",
        "link_href": "#contact",
        "external": False,
    },
]


def _cta_card(card: dict[str, str | bool]) -> rx.Component:
    """Render a single CTA card."""
    link_props: dict[str, str] = {"href": str(card["link_href"])}
    if card["external"]:
        link_props["target"] = "_blank"
        link_props["rel"] = "noopener"
    return rx.el.div(
        rx.el.h3(str(card["title"])),
        rx.el.p(str(card["text"])),
        rx.el.a(str(card["link_text"]), **link_props),
        class_name="cta-card reveal",
    )


def cta_section() -> rx.Component:
    """Warm beige CTA panel with 3 cards."""
    return rx.el.div(
        rx.el.div(
            *[_cta_card(c) for c in _CTA_CARDS],
            class_name="cta-inner",
        ),
        class_name="cta-section",
    )
