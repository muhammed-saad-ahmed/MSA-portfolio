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
        "bg": "#070A12", "surface": "#0D1421", "elevated": "#121D2D",
        "text": "#F2F7FA", "muted": "#91A2B5", "accent": "#65E7DF",
        "accent-soft": "rgba(101,231,223,.10)", "line": "rgba(143,169,190,.15)",
        "nav-bg": "rgba(7,10,18,.82)", "glow": "rgba(101,231,223,.13)",
        "shadow": "0 28px 80px -34px rgba(0,0,0,.82)", "on-accent": "#061312",
    },
    "light": {
        "bg": "#F8FAFC", "surface": "#FFFFFF", "elevated": "#EEF2F8",
        "text": "#111827", "muted": "#4B5A70", "accent": "#087F83",
        "accent-soft": "rgba(8,127,131,.10)", "line": "rgba(17,24,39,.12)",
        "nav-bg": "rgba(248,250,252,.82)", "glow": "rgba(8,127,131,.12)",
        "shadow": "0 24px 60px -28px rgba(17,24,39,.28)", "on-accent": "#FFFFFF",
    },
}


def theme_css(mode: str) -> str:
    tokens = THEMES.get(mode, THEMES["dark"])
    body = ";".join(f"--{k}:{v}" for k, v in tokens.items())
    return f":root{{{body}}}"
