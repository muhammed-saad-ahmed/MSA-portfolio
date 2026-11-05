"""Muhammad Saad Ahmed: personal portfolio (Streamlit)."""
from __future__ import annotations

import streamlit as st

from components import data as d
from components import sections as s
from components.utils import read_css, theme_css

st.set_page_config(
    page_title=f"{d.NAME} | Python Developer & Aspiring Aerospace Engineer",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def current_mode() -> str:
    """Theme comes from the ?theme= query parameter (dark by default)."""
    value = st.query_params.get("theme", "dark")
    if isinstance(value, list):
        value = value[0] if value else "dark"
    return "light" if str(value).lower() == "light" else "dark"


def render(markup: str) -> None:
    st.markdown(markup, unsafe_allow_html=True)


def main() -> None:
    mode = current_mode()
    render(f"<style>{theme_css(mode)}\n{read_css('main.css')}</style>")
    render(s.nav(mode))
    render(s.hero())
    render(s.about())
    render(s.expertise())
    render(s.projects())
    render(s.experience())
    render(s.education())
    render(s.achievements())
    render(s.vision())
    render(s.philosophy())
    render(s.contact())
    render(s.footer())


main()
