"""Small helpers: asset loading, CSS loading and HTML cleanup."""
from __future__ import annotations

import base64
import html as _html
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
STYLES = ROOT / "styles"


def esc(text: str) -> str:
    """Escape text for safe inclusion in HTML."""
    return _html.escape(str(text), quote=True)


def clean(markup: str) -> str:
    """Strip indentation and blank lines.

    Streamlit renders st.markdown through a Markdown parser: a blank line ends an HTML block and
    four leading spaces start a code block. Flattening the markup avoids both problems.
    """
    return "\n".join(line.strip() for line in markup.splitlines() if line.strip())


@lru_cache(maxsize=None)
def image_data_uri(filename: str) -> str | None:
    """Return a base64 data URI for an image in assets/, or None if it is missing."""
    path = ASSETS / filename
    if not path.is_file():
        return None
    suffix = path.suffix.lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(suffix, "jpeg")
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/{mime};base64,{encoded}"


@lru_cache(maxsize=None)
def read_css(filename: str) -> str:
    path = STYLES / filename
    return path.read_text(encoding="utf-8") if path.is_file() else ""


THEMES = {
    "dark": {
        "bg": "#080B12", "surface": "#101722", "elevated": "#151F2C",
        "text": "#F5F7FA", "muted": "#A0ACBA", "accent": "#8ADBD2",
        "accent-soft": "rgba(138,219,210,.09)", "line": "rgba(190,205,220,.13)",
        "nav-bg": "rgba(8,11,18,.78)", "glow": "rgba(138,219,210,.10)",
        "shadow": "0 30px 90px -42px rgba(0,0,0,.78)", "on-accent": "#071311",
    },
    "light": {
        "bg": "#F5F6F8", "surface": "#FFFFFF", "elevated": "#EEF1F4",
        "text": "#11151C", "muted": "#596575", "accent": "#287F79",
        "accent-soft": "rgba(40,127,121,.08)", "line": "rgba(17,24,39,.10)",
        "nav-bg": "rgba(245,246,248,.82)", "glow": "rgba(40,127,121,.09)",
        "shadow": "0 24px 64px -32px rgba(17,24,39,.22)", "on-accent": "#FFFFFF",
    },
}


def theme_css(mode: str) -> str:
    tokens = THEMES.get(mode, THEMES["dark"])
    body = ";".join(f"--{k}:{v}" for k, v in tokens.items())
    return f":root{{{body}}}"
