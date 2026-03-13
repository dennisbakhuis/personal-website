"""Contact section."""

import reflex as rx


_LINKS = [
    {"label": "hello@dennisbakhuis.com", "href": "mailto:hello@dennisbakhuis.com", "external": False},
    {"label": "LinkedIn", "href": "https://linkedin.com/in/dennisbakhuis", "external": True},
    {"label": "GitHub", "href": "https://github.com/dennisbakhuis", "external": True},
    {"label": "Twitter / X", "href": "https://twitter.com/dennisbakhuis", "external": True},
]


def _contact_link(link: dict[str, str | bool]) -> rx.Component:
    """Render a single contact link row."""
    props: dict[str, str] = {"href": str(link["href"])}
    if link["external"]:
        props["target"] = "_blank"
        props["rel"] = "noopener"
    return rx.el.a(
        rx.el.span(str(link["label"])),
        rx.el.span("↗", class_name="arrow"),
        class_name="contact-link",
        **props,
    )


def contact_section() -> rx.Component:
    """Big heading + contact link list."""
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    rx.html("Let's build<br>something<br><span>together</span>"),
                ),
                rx.el.div(
                    *[_contact_link(l) for l in _LINKS],
                    class_name="contact-links",
                ),
                class_name="contact-grid reveal",
            ),
            class_name="container",
        ),
        id="contact",
    )
