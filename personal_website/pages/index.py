"""Home page — assembles all sections."""

import reflex as rx

from ..components import (
    hero_section,
    nav_section,
    about_section,
    work_section,
    cta_section,
    til_section,
    contact_section,
    footer_section,
)


def index_page() -> rx.Component:
    """Complete home page with all sections and injected JavaScript."""
    return rx.fragment(
        hero_section(),
        # Page wrapper
        rx.el.div(
            nav_section(),
            about_section(),
            rx.el.hr(),
            work_section(),
            rx.el.hr(),
            cta_section(),
            til_section(),
            rx.el.hr(),
            contact_section(),
            footer_section(),
            class_name="page",
        ),
        # Fixed CTA button
        rx.el.a(
            "Let's talk ↗",
            href="#contact",
            class_name="fixed-cta",
        ),
        # JS loaded via head_components in app config
    )
