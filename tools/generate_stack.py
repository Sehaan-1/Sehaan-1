#!/usr/bin/env python3
#!/usr/bin/env python3
"""Generate assets/stack-dark.svg and assets/stack-light.svg for the profile README.

Language shares are measured live from the public repositories via the GitHub
CLI, so the bar is a fact rather than a claim. Chip widths are computed from
monospace metrics and pinned with textLength, so labels cannot overflow in any
renderer.

    python3 tools/generate_stack.py          # write both SVGs
    python3 tools/generate_stack.py --print  # just show the measured shares

Requires: gh (authenticated), python3.10+
"""
import subprocess, json, collections, os, sys

W = 1200
MARGIN = 56
CONTENT_W = W - 2 * MARGIN

CHIP_FS = 13.0
CHAR_W = 0.600 * CHIP_FS
PAD_X = 12
CHIP_H = 28
GAP = 8
ROW_GAP = 9
LABEL_W = 168
CHIP_X0 = MARGIN + LABEL_W

LAYERS = [
    ("01", "Interfaces", "#22D3EE", [
        "React 19", "Next.js", "Vite", "Tailwind CSS", "Three.js",
        "Leaflet", "D3", "TanStack Query", "Jetpack Compose", "Flutter", "WebSockets",
    ]),
    ("02", "Services", "#60A5FA", [
        "FastAPI", "Pydantic v2", "SQLAlchemy 2.0", "Uvicorn", "Node.js",
        "Express", "Spring Boot", "REST + OpenAPI", "BFF pattern",
    ]),
    ("03", "Intelligence", "#818CF8", [
        "PyTorch", "scikit-learn", "XGBoost", "SHAP", "Transformers",
        "FAISS", "BM25", "YOLOv8", "ByteTrack", "CLIP", "OpenCV",
        "Thompson sampling", "ADWIN", "off-policy evaluation",
    ]),
    ("04", "Data", "#A78BFA", [
        "PostgreSQL", "SQLite · WAL", "Redis", "MySQL", "DuckDB", "dbt",
        "Airflow", "Drizzle ORM", "Flyway", "pandas", "NumPy",
        "Cohen · Fleiss · Krippendorff",
    ]),
    ("05", "Platform", "#2DD4BF", [
        "Docker Compose", "GitHub Actions", "Prometheus", "Grafana",
        "nginx", "Caddy", "AWS", "GCP", "Cloudflare", "Vercel",
    ]),
]

# Languages in the diagram's footer: real bytes from the public repos,
# notebooks/markup/CSS excluded so the bar means "shipped source".
LANG_ORDER = ["Python", "TypeScript", "C#", "JavaScript", "C++",
              "Kotlin", "Rust", "Go", "Dart"]
LANG_COLORS = ["#22D3EE", "#38BDF8", "#60A5FA", "#818CF8", "#A78BFA",
               "#C084FC", "#F472B6", "#FB923C", "#FBBF24"]

THEMES = {
    "dark": dict(
        panel="#0D1117", border="#232C38", head="#E6EDF3", muted="#8B949E",
        chip_fill="#161B22", chip_border="#263140", chip_text="#C6D0DB",
        track="#161B22", note="#6E7B8B", rule="#1C2430", shadow=False,
    ),
    "light": dict(
        panel="#FFFFFF", border="#E4E8EE", head="#0F172A", muted="#5A6673",
        chip_fill="#F7F9FB", chip_border="#E1E6EC", chip_text="#3B4652",
        track="#F2F5F8", note="#6A7684", rule="#EAEDF2", shadow=True,
    ),
}


def chip_width(label):
    return len(label) * CHAR_W + 2 * PAD_X


def flow(labels, x0, x1):
    """Wrap chips into rows; returns list of rows of (label, x, w)."""
    rows, row, x = [], [], x0
    for label in labels:
        w = chip_width(label)
        if x + w > x1 and row:
            rows.append(row)
            row, x = [], x0
        row.append((label, x, w))
        x += w + GAP
    if row:
        rows.append(row)
    return rows


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def build(theme_name, langs):
    t = THEMES[theme_name]
    out, y = [], 0

    # --- header -------------------------------------------------------
    y = 58
    out.append(
        f'<text x="{MARGIN}" y="{y}" font-family="\'JetBrains Mono\',\'SF Mono\',Menlo,Consolas,monospace" '
        f'font-size="10.5" letter-spacing="3.4" fill="{t["muted"]}">TECH STACK</text>'
    )
    out.append(
        f'<text x="{W - MARGIN}" y="{y}" text-anchor="end" '
        f'font-family="\'JetBrains Mono\',\'SF Mono\',Menlo,Consolas,monospace" '
        f'font-size="10.5" letter-spacing="1.2" fill="{t["muted"]}" fill-opacity="0.75">'
        f'{len(LAYERS)} LAYERS · {len(langs)} LANGUAGES MEASURED</text>'
    )
    out.append(f'<line x1="{MARGIN}" y1="{y + 20}" x2="{W - MARGIN}" y2="{y + 20}" '
               f'stroke="{t["rule"]}" stroke-width="1"/>')
    y += 20

    body = []
    for num, name, accent, labels in LAYERS:
        rows = flow(labels, CHIP_X0, W - MARGIN)
        block_h = len(rows) * (CHIP_H + ROW_GAP) - ROW_GAP
        y += 34
        mid = y + block_h / 2

        # layer marker + name
        body.append(
            f'<text x="{MARGIN}" y="{mid - 9}" '
            f'font-family="\'JetBrains Mono\',\'SF Mono\',Menlo,Consolas,monospace" '
            f'font-size="10" letter-spacing="2.4" fill="{accent}">{num}</text>'
        )
        body.append(
            f'<text x="{MARGIN}" y="{mid + 9}" '
            f'font-family="Inter,\'Segoe UI\',-apple-system,Helvetica,Arial,sans-serif" '
            f'font-size="14.5" font-weight="600" fill="{t["head"]}">{esc(name)}</text>'
        )

        for r_i, row in enumerate(rows):
            cy = y + r_i * (CHIP_H + ROW_GAP)
            for label, cx, cw in row:
                body.append(
                    f'<rect x="{cx:g}" y="{cy:g}" width="{cw:g}" height="{CHIP_H}" rx="7" '
                    f'fill="{t["chip_fill"]}" stroke="{t["chip_border"]}" stroke-width="1"/>'
                )
                tl = len(label) * CHAR_W
                body.append(
                    f'<text x="{cx + cw / 2:g}" y="{cy + CHIP_H / 2 + 4.6:g}" text-anchor="middle" '
                    f'font-family="\'JetBrains Mono\',\'SF Mono\',Menlo,Consolas,monospace" '
                    f'font-size="{CHIP_FS:g}" fill="{t["chip_text"]}" '
                    f'textLength="{tl:g}" lengthAdjust="spacingAndGlyphs">{esc(label)}</text>'
                )
        y += block_h

    # --- language bar -------------------------------------------------
    y += 46
    body.append(f'<line x1="{MARGIN}" y1="{y - 22}" x2="{W - MARGIN}" y2="{y - 22}" '
                f'stroke="{t["rule"]}" stroke-width="1"/>')
    body.append(
        f'<text x="{MARGIN}" y="{y}" font-family="\'JetBrains Mono\',\'SF Mono\',Menlo,Consolas,monospace" '
        f'font-size="10" letter-spacing="2.4" fill="{t["muted"]}">BY SOURCE VOLUME ACROSS PUBLIC REPOS</text>'
    )
    body.append(
        f'<text x="{W - MARGIN}" y="{y}" text-anchor="end" '
        f'font-family="\'JetBrains Mono\',\'SF Mono\',Menlo,Consolas,monospace" '
        f'font-size="10" letter-spacing="0.6" fill="{t["note"]}">notebooks &amp; markup excluded</text>'
    )

    total = sum(v for _, v in langs)
    y += 14
    bar_x, bar_w, bar_h = MARGIN, CONTENT_W, 14
    # inset the last segment so the rounded ends never clip
    x = bar_x
    for i, (name, val) in enumerate(langs):
        seg = bar_w * val / total
        last = i == len(langs) - 1
        body.append(
            f'<rect x="{x:.2f}" y="{y}" width="{max(seg - 2, 1):.2f}" height="{bar_h}" '
            f'rx="{3 if not last else 3}" fill="{LANG_COLORS[i]}" fill-opacity="{0.92 - 0.03 * i:.2f}"/>'
        )
        x += seg

    # legend, two rows
    ly = y + bar_h + 26
    col_w = CONTENT_W / 5
    for i, (name, val) in enumerate(langs):
        cx = MARGIN + (i % 5) * col_w
        cyy = ly + (i // 5) * 24
        pct = 100 * val / total
        body.append(f'<rect x="{cx:.1f}" y="{cyy - 8}" width="7" height="7" rx="2" fill="{LANG_COLORS[i]}"/>')
        body.append(
            f'<text x="{cx + 15:.1f}" y="{cyy}" '
            f'font-family="Inter,\'Segoe UI\',-apple-system,Helvetica,Arial,sans-serif" '
            f'font-size="12.5" fill="{t["head"]}">{esc(name)}</text>'
        )
        body.append(
            f'<text x="{cx + 112:.1f}" y="{cyy}" '
            f'font-family="\'JetBrains Mono\',\'SF Mono\',Menlo,Consolas,monospace" '
            f'font-size="11" fill="{t["note"]}">{pct:.0f}%</text>'
        )
    y = ly + 24 * ((len(langs) - 1) // 5 + 1) + 4

    H = int(round(y + 26))
    header = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">'
        f'<title id="t">Sehaan Rahman — tech stack</title>'
        f'<desc id="d">Five layers: interfaces, services, intelligence, data, platform; '
        f'with languages measured by source volume.</desc>'
    )
    shadow = ('<filter id="sh" x="-2%" y="-2%" width="104%" height="108%">'
              '<feDropShadow dx="0" dy="1" stdDeviation="3" flood-color="#0F172A" flood-opacity="0.06"/>'
              '</filter>') if t["shadow"] else ""
    panel_filter = ' filter="url(#sh)"' if t["shadow"] else ""
    panel = (
        f'{shadow}<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="16" '
        f'fill="{t["panel"]}" stroke="{t["border"]}" stroke-width="1"{panel_filter}/>'
    )
    return header + panel + "".join(out) + "".join(body) + "</svg>"


def public_repos():
    out = subprocess.run(
        ["gh", "api", "users/Sehaan-1/repos?per_page=100", "--paginate",
         "--jq", ".[] | select(.fork == false) | .name"],
        capture_output=True, text=True, check=True).stdout
    return [line.strip() for line in out.splitlines() if line.strip()]


def lang_data():
    repos = public_repos()
    tot = collections.Counter()
    for r in repos:
        p = subprocess.run(["gh", "api", f"repos/Sehaan-1/{r}/languages"],
                           capture_output=True, text=True)
        if not p.stdout.strip():
            continue
        try:
            for k, v in json.loads(p.stdout).items():
                tot[k] += v
        except json.JSONDecodeError:
            continue
    excluded = {"Jupyter Notebook", "HTML", "CSS", "Dockerfile", "Makefile",
                "Shell", "CMake", "Batchfile", "PowerShell", "TeX"}
    return [(k, tot[k]) for k in LANG_ORDER if tot.get(k)]


if __name__ == "__main__":
    langs = lang_data()
    if "--print" in sys.argv:
        total = sum(v for _, v in langs)
        for name, val in langs:
            print(f"{name:12s} {100 * val / total:5.1f}%  {val:>9,} bytes")
        raise SystemExit(0)
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
    for theme in ("dark", "light"):
        svg = build(theme, langs)
        path = os.path.normpath(os.path.join(outdir, f"stack-{theme}.svg"))
        with open(path, "w") as fh:
            fh.write(svg)
        print(f"wrote {path} ({len(svg)} bytes)")
