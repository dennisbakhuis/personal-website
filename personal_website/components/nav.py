"""Sticky navigation bar."""

import reflex as rx


def nav_section() -> rx.Component:
    """Sticky nav with name and section links."""
    return rx.el.nav(
        rx.el.div(
            rx.el.span("Dennis Bakhuis", class_name="nav-name"),
            rx.el.div(
                rx.el.a("About", href="#about"),
                rx.el.a("Work", href="#work"),
                rx.el.a("TIL", href="#til"),
                rx.el.a("Contact", href="#contact"),
                class_name="nav-links",
            ),
            class_name="container",
        ),
        class_name="page-nav",
    )
