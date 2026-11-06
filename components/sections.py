"""HTML builders for each portfolio section. Each function returns a flat HTML string."""
from __future__ import annotations

from . import data as d
from .utils import clean, esc, image_data_uri

ARROW = '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
GH_ICON = '<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-3.16 19.49c.5.09.68-.22.68-.48v-1.7c-2.78.6-3.37-1.34-3.37-1.34-.45-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.9 1.52 2.34 1.08 2.9.83.09-.65.35-1.08.63-1.33-2.22-.25-4.55-1.11-4.55-4.94 0-1.09.39-1.98 1.03-2.68-.1-.25-.45-1.27.1-2.64 0 0 .84-.27 2.75 1.02a9.5 9.5 0 0 1 5 0c1.9-1.29 2.74-1.02 2.74-1.02.55 1.37.2 2.39.1 2.64.64.7 1.03 1.59 1.03 2.68 0 3.84-2.34 4.69-4.57 4.94.36.31.68.92.68 1.85v2.74c0 .27.18.58.69.48A10 10 0 0 0 12 2Z"/></svg>'


def _chips(items: list[str]) -> str:
    return "".join(f'<span class="chip">{esc(i)}</span>' for i in items)


def _head(kicker: str, title: str, lead: str = "") -> str:
    # Scroll-linked typewriter treatment for each section's supporting copy.
    steps = max(12, min(len(lead), 88))
    lead_html = (
        f'<p class="lead typewrite" style="--steps:{steps}">{esc(lead)}</p>'
        if lead else ""
    )
    return clean(f"""
    <header class="sec-head reveal">
      <span class="kicker"><i class="chapter-dot"></i>{esc(kicker)}</span>
      <h2>{esc(title)}</h2>
      {lead_html}
    </header>
    """)


# ---------------------------------------------------------------- navigation
def nav(mode: str) -> str:
    links = "".join(f'<a href="#{k}">{esc(v)}</a>' for k, v in d.NAV)
    other = "light" if mode == "dark" else "dark"
    label = "Light" if mode == "dark" else "Dark"
    return clean(f"""
    <nav class="topnav" aria-label="Primary">
    <a class="brand" href="#home" aria-label="Muhammad Saad Ahmed, home"><span class="mark">MSA</span></a>
    <div class="navlinks">{links}</div>
    <a class="theme-toggle" href="?theme={other}" target="_self" aria-label="Switch to {label.lower()} theme">{label}</a>
    </nav>
    """)


# ---------------------------------------------------------------- hero
def hero() -> str:
    uri = image_data_uri(d.PORTRAIT_FILE)
    if uri:
        portrait = f'<img src="{uri}" alt="Portrait of Muhammad Saad Ahmed" decoding="async" fetchpriority="high">'
    else:
        portrait = '<div class="portrait-fallback" role="img" aria-label="Portrait placeholder"><span>MSA</span></div>'
    facts = "".join(
        f'<div><span>{esc(k)}</span><strong>{esc(v)}</strong></div>' for k, v in d.HERO["facts"]
    )
    return clean(f"""
    <section id="home" class="hero wrap">
    <div class="hero-copy">
    <span class="eyebrow rise r1">{esc(d.HERO["eyebrow"])}</span>
    <h1 class="rise r2"><span>Muhammad</span> <span>Saad</span> <span class="grad">Ahmed</span></h1>
    <p class="subtitle rise r3">{esc(d.HERO["subtitle"])}</p>
    <p class="intro rise r4">{esc(d.HERO["intro"])}</p>
    <div class="hero-note rise r4"><span class="note-index">01 / APPROACH</span><span>Understand the problem. Build with evidence. Keep improving.</span></div>
    <div class="btn-row rise r5">
    <a class="btn primary" href="#projects">Explore My Work {ARROW}</a>
    <a class="btn ghost" href="{d.GITHUB}" target="_blank" rel="noopener noreferrer">{GH_ICON} View GitHub</a>
    <a class="btn ghost" href="{d.LINKEDIN}" target="_blank" rel="noopener noreferrer">Connect on LinkedIn</a>
    <a class="btn ghost" href="{d.FIVERR}" target="_blank" rel="noopener noreferrer">Fiverr Portfolio</a>
    <a class="btn ghost" href="{d.GITHUB_LEGACY}" target="_blank" rel="noopener noreferrer">Second GitHub</a>
    </div>
    <div class="facts rise r6">{facts}</div>
    </div>
    <div class="hero-visual rise r3">
    <div class="orbit" aria-hidden="true"></div>
    <div class="frame"><div class="portrait">{portrait}</div></div>
    <div class="tag t1" aria-hidden="true"><i></i>Python Developer</div>
    <div class="tag t2" aria-hidden="true"><i></i>Aspiring Aerospace Engineer</div>
    </div>
    </section>
    """)


# ---------------------------------------------------------------- about
def about() -> str:
    paras = "".join(f"<p>{esc(p)}</p>" for p in d.ABOUT["paragraphs"])
    pillars = "".join(
        f'<div class="pillar"><span class="num">0{i}</span><h3>{esc(t)}</h3><p>{esc(s)}</p></div>'
        for i, (t, s) in enumerate(d.ABOUT["pillars"], 1)
    )
    return clean(f"""
    <section id="about" class="sec wrap">
    {_head("About", d.ABOUT["title"], "A practical path from mathematics and physics to software, data, and applied engineering.")}
    <div class="about-grid">
    <div class="prose reveal">{paras}</div>
    <div class="pillars reveal">{pillars}</div>
    </div>
    </section>
    """)


# ---------------------------------------------------------------- expertise
def expertise() -> str:
    cards = []
    for cat, items in d.SKILLS:
        pills = "".join(f'<span class="skill {lvl}">{esc(n)}</span>' for n, lvl in items)
        cards.append(f'<article class="card skillcard reveal"><h3>{esc(cat)}</h3><div class="skills">{pills}</div></article>')
    legend = (
        '<div class="legend reveal"><span><i class="dot practical"></i>Used in projects</span>'
        '<span><i class="dot training"></i>Learned in training, building experience</span>'
        '<span><i class="dot interest"></i>Area of interest</span></div>'
    )
    return clean(f"""
    <section id="expertise" class="sec wrap">
    {_head("Expertise", "A practical toolkit, honestly labelled.", "Skills are grouped by how I use them, so the list reflects real experience rather than inflated ratings.")}
    {legend}
    <div class="grid skills-grid">{"".join(cards)}</div>
    </section>
    """)


# ---------------------------------------------------------------- projects
def _risk_matrix() -> str:
    # Illustrative 5x5 heat grid (likelihood x impact). Decorative; not data.
    cells = []
    for r in range(5):
        for c in range(5):
            level = (4 - r) + c  # higher likelihood (top) and impact (right) = stronger
            cells.append(f'<i class="m l{level}"></i>')
    return f'<div class="matrix" role="img" aria-label="Illustrative 5 by 5 likelihood and impact risk matrix">{"".join(cells)}</div>'


def _motif(kind: str) -> str:
    if kind == "graph":
        return ('<svg viewBox="0 0 320 180" class="motif" role="img" aria-label="Illustrative function graph">'
                '<g stroke="currentColor" stroke-opacity=".18"><path d="M20 90H300M160 15V165"/></g>'
                '<path d="M20 150C70 150 90 30 160 30S250 150 300 150" fill="none" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>'
                '<path d="M20 120C80 60 120 140 170 90S250 60 300 40" fill="none" stroke="currentColor" stroke-opacity=".5" stroke-width="2" stroke-dasharray="4 6"/>'
                '</svg>')
    return ('<svg viewBox="0 0 320 180" class="motif" role="img" aria-label="Illustrative code editor">'
            '<rect x="24" y="20" width="272" height="140" rx="12" fill="none" stroke="currentColor" stroke-opacity=".25"/>'
            '<g stroke-linecap="round" stroke-width="6"><path d="M48 56h60" stroke="var(--accent)"/><path d="M120 56h90" stroke="currentColor" stroke-opacity=".35"/>'
            '<path d="M64 84h80" stroke="currentColor" stroke-opacity=".35"/><path d="M156 84h50" stroke="var(--accent)"/>'
            '<path d="M64 112h110" stroke="currentColor" stroke-opacity=".35"/><path d="M48 140h40" stroke="var(--accent)"/></g></svg>')


def _links(repo: str | None, label: str = "View repository") -> str:
    if not repo:
        return ""
    return f'<a class="btn ghost sm" href="{repo}" target="_blank" rel="noopener noreferrer">{GH_ICON} {label}</a>'


def _flagship() -> str:
    k = d.KRYPTA
    caps = "".join(f"<li>{esc(c)}</li>" for c in k["capabilities"])
    return clean(f"""
    <article class="flagship reveal" aria-labelledby="krypta-title">
    <div class="flag-visual" aria-label="KRYPTA project identity">
    <div class="grid-bg" aria-hidden="true"></div>
    <div class="project-logo-shell flagship-logo-shell">
    <img class="project-logo krypta-logo" src="{image_data_uri("krypta-logo.webp")}" alt="KRYPTA — Karachi Risk and YOLO-driven Platform for Terrain Analysis" width="520" height="520" loading="eager" decoding="async">
    <span class="logo-caption">KARACHI INFRASTRUCTURE RISK INTELLIGENCE</span>
    </div>
    </div>
    <div class="flag-body">
    <span class="badge">{esc(k["badge"])}</span>
    <h3 id="krypta-title">{esc(k["name"])}</h3>
    <p class="fullname">{esc(k["full"])}</p>
    <p class="summary">{esc(k["summary"])}</p>
    <div class="ps">
    <div><h4>Problem</h4><p>{esc(k["problem"])}</p></div>
    <div><h4>Approach</h4><p>{esc(k["solution"])}</p></div>
    </div>
    <ul class="caps">{caps}</ul>
    <p class="honesty">{esc(k["honesty"])}</p>
    <div class="chips">{_chips(k["tech"])}</div>
    <div class="btn-row project-actions">{_links(k["repo"], "View on GitHub")}<a class="btn primary sm" href="{k["live"]}" target="_blank" rel="noopener noreferrer">Open Live Project {ARROW}</a></div>
    </div>
    </article>
    """)


def _project(p: dict, flip: bool) -> str:
    caps = "".join(f"<li>{esc(c)}</li>" for c in p["capabilities"])
    cls = "project reveal flip" if flip else "project reveal"
    logo = image_data_uri(p.get("logo", "")) if p.get("logo") else None
    visual = (f'<div class="project-logo-shell"><img class="project-logo" src="{logo}" '
              f'alt="{esc(p["name"])} official project logo" loading="lazy"></div>') if logo else _motif(p["motif"])
    actions = _links(p.get("repo"))
    if p.get("live"):
        actions += f'<a class="btn primary sm" href="{p["live"]}" target="_blank" rel="noopener noreferrer">Open Live Project {ARROW}</a>'
    return clean(f"""
    <article class="{cls}">
    <div class="p-visual">{visual}</div>
    <div class="p-body">
    <span class="badge soft">{esc(p["tag"])}</span>
    <h3>{esc(p["name"])}</h3>
    <p class="summary">{esc(p["summary"])}</p>
    <div class="ps">
    <div><h4>Problem</h4><p>{esc(p["problem"])}</p></div>
    <div><h4>Approach</h4><p>{esc(p["solution"])}</p></div>
    </div>
    <ul class="caps">{caps}</ul>
    <div class="chips">{_chips(p["tech"])}</div>
    <div class="btn-row">{actions}</div>
    </div>
    </article>
    """)


def projects() -> str:
    more = "".join(
        f'<article class="card morecard reveal"><span class="badge soft">{esc(m["tag"])}</span>'
        f'<h3>{esc(m["name"])}</h3><p>{esc(m["summary"])}</p>'
        f'<div class="chips">{_chips(m["tech"])}</div>'
        + (f'<div class="btn-row">{_links(m.get("repo"))}</div>' if m.get("repo") else '')
        + (f'<div class="repo-links">{"".join(f"""<a href="{url}" target="_blank" rel="noopener noreferrer">{esc(label)}</a>""" for label, url in m.get("links", []))}</div>' if m.get("links") else '')
        + '</article>'
        for m in d.MORE_WORK
    )
    body = _flagship() + "".join(_project(p, i % 2 == 0) for i, p in enumerate(d.PROJECTS))
    return clean(f"""
    <section id="projects" class="sec wrap">
    {_head("Projects", "Selected work, presented as case studies.", "Each project states the problem, the approach, and what it does and does not claim.")}
    <div class="stack">{body}</div>
    <h3 class="subhead reveal">More work in progress</h3>
    <div class="grid more-grid">{more}</div>
    </section>
    """)


# ---------------------------------------------------------------- experience
def experience() -> str:
    items = []
    for e in d.EXPERIENCE:
        dates = f'<span class="dates">{esc(e["dates"])}</span>' if e["dates"] else ""
        pts = "".join(f"<li>{esc(p)}</li>" for p in e["points"])
        pts_html = f'<ul class="caps">{pts}</ul>' if pts else ""
        tech = f'<div class="chips">{_chips(e["tech"])}</div>' if e["tech"] else ""
        items.append(
            f'<div class="tl-item reveal"><span class="tl-dot"></span><div class="tl-card">'
            f'<div class="tl-top"><h3>{esc(e["org"])}</h3>{dates}</div>'
            f'<p class="role">{esc(e["role"])}</p>{pts_html}{tech}</div></div>'
        )
    return clean(f"""
    <section id="experience" class="sec wrap">
    {_head("Experience", "Internship and technical training.", "Learning in teams, strengthening fundamentals, and applying ideas through practical work.")}
    <div class="timeline">{"".join(items)}</div>
    </section>
    """)


# ---------------------------------------------------------------- education
def education() -> str:
    items = []
    for e in d.EDUCATION:
        dates = f'<span class="dates">{esc(e["dates"])}</span>' if e["dates"] else ""
        items.append(
            f'<div class="tl-item reveal"><span class="tl-dot"></span><div class="tl-card">'
            f'<div class="tl-top"><h3>{esc(e["school"])}</h3>{dates}</div>'
            f'<p class="role">{esc(e["detail"])}</p><p class="muted">{esc(e["note"])}</p></div></div>'
        )
    return clean(f"""
    <section id="education" class="sec wrap">
    {_head("Education", "Building the foundations for aerospace engineering.", "My goal is to pursue Aerospace Engineering at university level, including internationally.")}
    <div class="timeline">{"".join(items)}</div>
    </section>
    """)


# ---------------------------------------------------------------- achievements
def achievements() -> str:
    cards = "".join(
        f'<article class="card ach reveal"><span class="num">0{i}</span><h3>{esc(t)}</h3><p>{esc(s)}</p></article>'
        for i, (t, s) in enumerate(d.ACHIEVEMENTS, 1)
    )
    certs = ""
    if d.CERTIFICATIONS:
        rows = "".join(
            f'<li><strong>{esc(c["title"])}</strong><span>{esc(c.get("issuer", ""))} {esc(c.get("year", ""))}</span></li>'
            for c in d.CERTIFICATIONS
        )
        certs = f'<h3 class="subhead reveal">Certifications</h3><ul class="certs reveal">{rows}</ul>'
    beyond = "".join(f'<div><strong>{esc(a)}</strong><span>{esc(b)}</span></div>' for a, b in d.BEYOND)
    return clean(f"""
    <section id="achievements" class="sec wrap">
    {_head("Achievements", "Work that stands up to inspection.", "A few milestones that reflect consistency, curiosity, and a bias toward building.")}
    <div class="grid ach-grid">{cards}</div>
    {certs}
    <h3 class="subhead reveal">Beyond engineering</h3>
    <div class="beyond reveal">{beyond}</div>
    </section>
    """)


# ---------------------------------------------------------------- vision + philosophy
def vision() -> str:
    threads = "".join(f"<span>{esc(t)}</span>" for t in d.VISION["threads"])
    return clean(f"""
    <section class="vision">
    <div class="vision-bg" aria-hidden="true">
    <svg viewBox="0 0 800 400" preserveAspectRatio="xMidYMid slice"><g fill="none" stroke="currentColor" stroke-opacity=".16"><ellipse cx="400" cy="200" rx="360" ry="120"/><ellipse cx="400" cy="200" rx="260" ry="86" transform="rotate(-14 400 200)"/><ellipse cx="400" cy="200" rx="160" ry="52" transform="rotate(12 400 200)"/></g><circle cx="716" cy="168" r="4" fill="var(--accent)"/></svg>
    </div>
    <div class="wrap vision-in">
    <span class="kicker reveal">Engineering the Future</span>
    <h2 class="reveal">{esc(d.VISION["headline"])}</h2>
    <p class="reveal typewrite vision-type" style="--steps:{max(12, min(len(d.VISION["body"]), 88))}">{esc(d.VISION["body"])}</p>
    <div class="threads reveal">{threads}</div>
    </div>
    </section>
    """)


def philosophy() -> str:
    cards = "".join(
        f'<div class="phil reveal"><span>{esc(t)}.</span><p>{esc(s)}</p></div>' for t, s in d.PHILOSOPHY
    )
    return clean(f"""
    <section class="sec wrap">
    {_head("Philosophy", "Learn. Build. Experiment. Improve.")}
    <div class="phil-grid">{cards}</div>
    </section>
    """)


# ---------------------------------------------------------------- contact + footer
def contact() -> str:
    return clean(f"""
    <section id="contact" class="contact wrap">
    <div class="contact-card reveal">
    <h2>{esc(d.CONTACT["headline"])}</h2>
    <p class="typewrite contact-type" style="--steps:{max(12, min(len(d.CONTACT["text"]), 88))}">{esc(d.CONTACT["text"])}</p>
    <div class="btn-row center contact-actions">
    <a class="btn primary email-link" href="mailto:{d.EMAIL}" aria-label="Send an email to {d.EMAIL}"><span class="email-label">{esc(d.EMAIL)}</span>{ARROW}</a>
    <a class="btn ghost" href="{d.GITHUB}" target="_blank" rel="noopener noreferrer">{GH_ICON} GitHub</a>
    <a class="btn ghost" href="{d.LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
    <a class="btn ghost" href="{d.FIVERR}" target="_blank" rel="noopener noreferrer">Fiverr</a>
    <a class="btn ghost" href="{d.GITHUB_LEGACY}" target="_blank" rel="noopener noreferrer">Second GitHub</a>
    </div>
    </div>
    </section>
    """)


def footer() -> str:
    return clean(f"""
    <footer class="foot wrap">
    <span>© 2026 {esc(d.NAME)}</span>
    <span>Designed with purpose. Built with curiosity.</span>
    </footer>
    """)
