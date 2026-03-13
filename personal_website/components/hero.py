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
                        rx.html("Data Scientist &amp;<br>Engineer"),
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
                        rx.html("Dennis<br>Bakhuis"),
                        class_name="hero-name",
                    ),
                    rx.el.p(
                        rx.html(
                            "A data scientist and engineer<br>"
                            "building scalable ML systems<br>"
                            "and data pipelines."
                        ),
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
                rx.html('Denn<span class="tittle-i">i</span>s'),
                class_name="fn-line fn-line1",
            ),
            rx.el.span(
                rx.html('Bakhu<span class="tittle-i">i</span>s'),
                class_name="fn-line fn-line2",
            ),
            class_name="floating-name",
        ),
    )
