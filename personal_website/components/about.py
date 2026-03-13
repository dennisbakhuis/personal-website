"""About section."""

import reflex as rx


_SKILLS = [
    "Python",
    "NLP",
    "Machine Learning",
    "Data Engineering",
    "Deep Learning",
    "Rust",
    "Docker",
    "MLOps",
    "Open Source",
]


def about_section() -> rx.Component:
    """About section with grid layout, portrait, and skills tags."""
    return rx.el.section(
        rx.el.div(
            rx.el.div("About", class_name="label reveal"),
            rx.el.div(
                # Left column
                rx.el.div(
                    rx.el.h2(
                        rx.html(
                            "Crafting systems that make data <span>useful</span>"
                        ),
                    ),
                    rx.el.div(
                        rx.el.img(
                            src="/images/bg1.jpg",
                            alt="Dennis Bakhuis",
                        ),
                        class_name="about-portrait",
                    ),
                    class_name="about-left reveal",
                ),
                # Right column
                rx.el.div(
                    rx.el.p(
                        rx.html(
                            "I'm a Data Scientist &amp; Engineer based in the "
                            "Netherlands with a PhD in Physics. I specialize in "
                            "building end-to-end ML systems — from document parsing "
                            "and NLP pipelines to production-ready models. I've "
                            "delivered solutions for large-scale energy "
                            "infrastructure, built validation frameworks, and turned "
                            "messy unstructured data into actionable insights."
                        ),
                    ),
                    rx.el.p(
                        rx.html(
                            "With 15+ years in the Python ecosystem, I build things "
                            "that ship. I've created open-source tools like "
                            "<strong>pigeonXT</strong> for data annotation in "
                            "Jupyter, published a 25-part \"Python 10 Minutes a "
                            'Day" series on Towards Data Science, and I\'m currently '
                            "exploring Rust for performance-critical components."
                        ),
                    ),
                    rx.el.p(
                        rx.html(
                            "I'm available for short-term assignments in data "
                            "science, NLP, and ML engineering. I "
                            '<a href="#til">share things I learn</a> about data '
                            "engineering, Python, and AI — and I believe in clean "
                            "code, reproducible pipelines, and making complex topics "
                            "accessible."
                        ),
                    ),
                    rx.el.div(
                        *[
                            rx.el.span(skill, class_name="skill")
                            for skill in _SKILLS
                        ],
                        class_name="skills",
                    ),
                    class_name="about-right reveal",
                ),
                class_name="about-grid",
            ),
            class_name="container",
        ),
        id="about",
    )
