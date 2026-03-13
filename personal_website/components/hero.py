"""Hero section with strip reveal animation."""

import reflex as rx


def hero_section() -> rx.Component:
    """Full-viewport hero with strip reveal, status bar, big name, and tagline."""
    return rx.fragment(
        # Intro overlay
        rx.el.div(
            rx.el.span("Dennis Bakhuis", class_name="intro-name"),
            class_name="intro",
        ),
        # Hero
        rx.el.div(
            # Strips
            rx.el.div(
                rx.el.div(rx.el.div(class_name="strip-img"), class_name="strip"),
                rx.el.div(rx.el.div(class_name="strip-img"), class_name="strip"),
                rx.el.div(rx.el.div(class_name="strip-img"), class_name="strip"),
                class_name="strips",
            ),
            # Hero inner content
            rx.el.div(
                # Status bar
                rx.el.div(
                    rx.el.span(
                        "Data Scientist &",
                        rx.el.br(),
                        "Engineer",
                        class_name="status-role",
                    ),
                    rx.el.span(
                        rx.el.span(class_name="dot"),
                        "Available for projects",
                        class_name="status-avail",
                    ),
                    class_name="status-bar",
                ),
                # Bottom: big name + tagline
                rx.el.div(
                    rx.el.h1(
                        "Dennis",
                        rx.el.br(),
                        "Bakhuis",
                        class_name="hero-name",
                    ),
                    rx.el.p(
                        "A data scientist and engineer",
                        rx.el.br(),
                        "building scalable ML systems",
                        rx.el.br(),
                        "and data pipelines.",
                        class_name="hero-tagline",
                    ),
                    class_name="hero-bottom",
                ),
                class_name="hero-inner",
            ),
            class_name="hero",
        ),
        # Floating name for scroll transition
        rx.el.div(
            rx.el.span(
                "Denn",
                rx.el.span("i", class_name="tittle-i"),
                "s",
                class_name="fn-line fn-line1",
            ),
            rx.el.span(
                "Bakhu",
                rx.el.span("i", class_name="tittle-i"),
                "s",
                class_name="fn-line fn-line2",
            ),
            class_name="floating-name",
        ),
    )
