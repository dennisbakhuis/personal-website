"""Footer section."""

import reflex as rx


def footer_section() -> rx.Component:
    """4-column footer with brand, nav, social, and elsewhere links."""
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                # Brand column
                rx.el.div(
                    rx.el.h3("Dennis Bakhuis"),
                    rx.el.p(
                        "Data Scientist & Engineer based in the Netherlands. "
                        "Building systems that make data useful."
                    ),
                    class_name="footer-brand",
                ),
                # Navigate column
                rx.el.div(
                    rx.el.h4("Navigate"),
                    rx.el.a("About", href="#about"),
                    rx.el.a("Work", href="#work"),
                    rx.el.a("TIL", href="#til"),
                    rx.el.a("Contact", href="#contact"),
                    class_name="footer-col",
                ),
                # Social column
                rx.el.div(
                    rx.el.h4("Social"),
                    rx.el.a(
                        "GitHub",
                        href="https://github.com/dennisbakhuis",
                        target="_blank",
                        rel="noopener",
                    ),
                    rx.el.a(
                        "LinkedIn",
                        href="https://linkedin.com/in/dennisbakhuis",
                        target="_blank",
                        rel="noopener",
                    ),
                    rx.el.a(
                        "Twitter / X",
                        href="https://twitter.com/dennisbakhuis",
                        target="_blank",
                        rel="noopener",
                    ),
                    class_name="footer-col",
                ),
                # Elsewhere column
                rx.el.div(
                    rx.el.h4("Elsewhere"),
                    rx.el.a("Blog", href="#"),
                    rx.el.a("Resume", href="#"),
                    class_name="footer-col",
                ),
                class_name="footer-top",
            ),
            rx.el.div(
                rx.el.span("© 2025 Dennis Bakhuis"),
                rx.el.span("Netherlands · UTC+1"),
                class_name="footer-bottom",
            ),
            class_name="container",
        ),
    )
