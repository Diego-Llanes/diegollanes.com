from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import json, shutil, re

ROOT = Path(__file__).resolve().parents[1]
TPL  = ROOT / "templates"
OUT  = ROOT / "docs"
OUT.mkdir(parents=True, exist_ok=True)

env = Environment(loader=FileSystemLoader(str(TPL)))

def _ensure_meta_charset(html: str) -> str:
    if "charset=" in html.lower():
        return html
    return re.sub(r"(?i)<head(.*?)>", r"<head\1>\n\t<meta charset=\"utf-8\" />", html, count=1)

def render_to(path: Path, template_name: str, **ctx):
    html = env.get_template(template_name).render(**ctx)
    html = _ensure_meta_charset(html)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")

# ---- build research context ----
projects = json.loads((ROOT / "static/json/research.json").read_text(encoding="utf-8"))
for p in projects:
    p["authors"] = p["authors"].replace("Diego Llanes", "<u>Diego Llanes</u>")

# ---- write pages as /route/index.html so /route works ----
render_to(OUT / "index.html",      "index.html")
render_to(OUT / "about"   / "index.html", "about.html")
render_to(OUT / "contact" / "index.html", "contact.html")
render_to(OUT / "calendar"/ "index.html", "calendar.html")
render_to(OUT / "research"/ "index.html", "research.html", projects=projects)

# ---- assets ----
if (ROOT / "static").exists():
    shutil.copytree(ROOT / "static", OUT / "static", dirs_exist_ok=True)

src_figs = ROOT / "static/figs"
if src_figs.exists():
    shutil.copytree(src_figs, OUT / "figs", dirs_exist_ok=True)

(OUT / ".nojekyll").write_text("", encoding="utf-8")
