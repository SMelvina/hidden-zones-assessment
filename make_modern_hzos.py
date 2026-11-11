import re

with open('hzos-assessment.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Extract header
header_match = re.search(r'<header>.*?</header>', orig, re.DOTALL)
header_html = header_match.group(0)

# Extract Z, Q, ACT, LK
z_match = re.search(r'const Z=\[(.*?)\];\s*const Q=', orig, re.DOTALL)
z_content = z_match.group(1)

q_match = re.search(r'const Q=\[(.*?)\];\s*const EV=', orig, re.DOTALL)
q_content = q_match.group(1)

act_match = re.search(r'const ACT=\[(.*?)\];\s*const LK=', orig, re.DOTALL)
act_content = act_match.group(1)

lk_match = re.search(r'const LK=\[(.*?)\];\s*function sections', orig, re.DOTALL)
lk_content = lk_match.group(1)

html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>The Hidden Zones of Stagnation (HZOS) | Phoszade</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root {{
  --g: #00522a;
  --g-hover: #073f22;
  --g-light: #eaf6ef;
  --g-border: #a3d9bc;
  --au: #d97706;
  --au-hover: #b45309;
  --au-light: #fef3c7;
  --au-border: #fcd34d;
  --bg: #f8fafc;
  --card: #ffffff;
  --card-border: #e2e8f0;
  --card-hover: #f1f5f9;
  --tx: #0f172a;
  --tx-muted: #64748b;
  --mu: #64748b;
  --mu-light: #94a3b8;
  --bd: #e2e8f0;
  --bad: #dc2626;
  --bad-light: #fef2f2;
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 14px -2px rgba(0, 0, 0, 0.07), 0 2px 6px -1px rgba(0, 0, 0, 0.04);
  --shadow-lg: 0 12px 28px -4px rgba(0, 0, 0, 0.09), 0 4px 10px -2px rgba(0, 0, 0, 0.04);
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 18px;
  box-sizing: border-box;
  padding-top: env(safe-area-inset-top, 0px);
  padding-bottom: env(safe-area-inset-bottom, 0px);
  color-scheme: light;
}}

@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --g: #10b981;
    --g-hover: #059669;
    --g-light: rgba(16, 185, 129, 0.12);
    --g-border: rgba(16, 185, 129, 0.3);
    --au: #fbbf24;
    --au-hover: #f59e0b;
    --au-light: rgba(251, 191, 36, 0.14);
    --au-border: rgba(251, 191, 36, 0.35);
    --bg: #090d16;
    --card: #131c2e;
    --card-border: #1e293b;
    --card-hover: #1b263b;
    --tx: #f8fafc;
    --tx-muted: #94a3b8;
    --mu: #94a3b8;
    --mu-light: #64748b;
    --bd: #243044;
    --bad: #f87171;
    --bad-light: rgba(239, 68, 68, 0.15);
    color-scheme: dark;
  }}
}}

:root[data-theme="dark"] {{
  --g: #10b981;
  --g-hover: #059669;
  --g-light: rgba(16, 185, 129, 0.12);
  --g-border: rgba(16, 185, 129, 0.3);
  --au: #fbbf24;
  --au-hover: #f59e0b;
  --au-light: rgba(251, 191, 36, 0.14);
  --au-border: rgba(251, 191, 36, 0.35);
  --bg: #090d16;
  --card: #131c2e;
  --card-border: #1e293b;
  --card-hover: #1b263b;
  --tx: #f8fafc;
  --tx-muted: #94a3b8;
  --mu: #94a3b8;
  --mu-light: #64748b;
  --bd: #243044;
  --bad: #f87171;
  --bad-light: rgba(239, 68, 68, 0.15);
  color-scheme: dark;
}}

* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}

html {{
  scroll-behavior: smooth;
  scroll-padding-top: env(safe-area-inset-top, 0px);
}}

body {{
  background: var(--bg);
  color: var(--tx);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  min-height: 100vh;
}}

header {{
  background: var(--card);
  border-bottom: 2px solid var(--bd);
  padding: 14px 28px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 50;
  box-shadow: var(--shadow-sm);
}}
header img {{
  height: 40px;
  display: block;
}}
header span {{
  font-weight: 700;
  font-size: 13px;
  letter-spacing: 0.12em;
  color: var(--g);
  text-transform: uppercase;
}}

main {{
  max-width: 800px;
  margin: 0 auto;
  padding: 32px 20px 80px;
}}

/* Top Progress Header */
.top-nav-bar {{
  margin-bottom: 24px;
}}
.top-prog {{
  height: 7px;
  background: var(--bd);
  border-radius: 999px;
  overflow: hidden;
  margin-bottom: 12px;
}}
.top-prog-fill {{
  height: 100%;
  background: linear-gradient(90deg, var(--g), var(--au));
  border-radius: 999px;
  transition: width 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}}
.top-meta {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
  font-weight: 600;
  color: var(--mu);
}}

/* Animation Container */
.slide-stage {{
  position: relative;
  width: 100%;
  overflow: hidden;
}}

.anim-slide-in-right {{
  animation: slideInRight 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}}
.anim-slide-out-left {{
  animation: slideOutLeft 0.22s cubic-bezier(0.7, 0, 0.84, 0) forwards;
}}
.anim-slide-in-left {{
  animation: slideInLeft 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}}
.anim-slide-out-right {{
  animation: slideOutRight 0.22s cubic-bezier(0.7, 0, 0.84, 0) forwards;
}}

@keyframes slideInRight {{
  from {{ opacity: 0; transform: translateX(36px); }}
  to {{ opacity: 1; transform: translateX(0); }}
}}
@keyframes slideOutLeft {{
  from {{ opacity: 1; transform: translateX(0); }}
  to {{ opacity: 0; transform: translateX(-36px); }}
}}
@keyframes slideInLeft {{
  from {{ opacity: 0; transform: translateX(-36px); }}
  to {{ opacity: 1; transform: translateX(0); }}
}}
@keyframes slideOutRight {{
  from {{ opacity: 1; transform: translateX(0); }}
  to {{ opacity: 0; transform: translateX(36px); }}
}}

/* Card & Content Styles */
.card {{
  background: var(--card);
  border: 1px solid var(--bd);
  border-radius: var(--radius-lg);
  padding: 32px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-md);
  transition: box-shadow 0.2s ease, border-color 0.2s ease;
}}

.pill-badge {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--g-light);
  color: var(--g);
  border: 1px solid var(--g-border);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  padding: 4px 12px;
  border-radius: 9999px;
  text-transform: uppercase;
  margin-bottom: 14px;
}}
.pill-badge.gold {{
  background: var(--au-light);
  color: var(--au);
  border-color: var(--au-border);
}}

h1.hero-title {{
  font-size: 32px;
  font-weight: 800;
  letter-spacing: -0.025em;
  line-height: 1.25;
  color: var(--tx);
  margin-bottom: 12px;
}}
.tagline {{
  font-size: 17px;
  font-weight: 500;
  color: var(--mu);
  margin-bottom: 24px;
}}

/* Stats Grid on Landing */
.stats-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin: 28px 0;
}}
.stat-box {{
  background: linear-gradient(135deg, var(--card), var(--bg));
  border: 1px solid var(--bd);
  border-radius: var(--radius-md);
  padding: 20px 16px;
  text-align: center;
  box-shadow: var(--shadow-sm);
}}
.stat-num {{
  font-size: 32px;
  font-weight: 800;
  color: var(--g);
  line-height: 1;
  margin-bottom: 6px;
}}
.stat-label {{
  font-size: 13px;
  font-weight: 600;
  color: var(--mu);
}}

/* Instructions box */
.info-box {{
  background: var(--g-light);
  border: 1px solid var(--g-border);
  border-left: 5px solid var(--g);
  border-radius: var(--radius-md);
  padding: 20px 24px;
  margin: 24px 0;
}}
.info-box h4 {{
  font-size: 15px;
  font-weight: 700;
  color: var(--g);
  margin-bottom: 8px;
}}
.info-box p {{
  font-size: 14px;
  line-height: 1.6;
  color: var(--tx);
}}
.info-box ul {{
  margin-top: 10px;
  padding-left: 20px;
  font-size: 14px;
}}
.info-box li {{
  margin-bottom: 6px;
}}

/* Zone Splash Screen */
.splash-title {{
  font-size: 28px;
  font-weight: 800;
  letter-spacing: -0.02em;
  margin-bottom: 12px;
  line-height: 1.3;
}}
.focus-container {{
  background: var(--bg);
  border: 1px solid var(--bd);
  border-left: 4px solid var(--au);
  border-radius: var(--radius-md);
  padding: 20px 24px;
  margin: 24px 0;
}}
.focus-heading {{
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--au);
  margin-bottom: 6px;
}}
.focus-desc {{
  font-size: 16px;
  font-weight: 500;
  line-height: 1.55;
  color: var(--tx);
}}
.splash-checklist {{
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin: 24px 0 32px;
}}
.check-item {{
  display: flex;
  align-items: flex-start;
  gap: 12px;
  font-size: 14px;
  color: var(--tx-muted);
}}
.check-icon {{
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--g-light);
  color: var(--g);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 12px;
  flex-shrink: 0;
  margin-top: 2px;
}}

/* Question Step View */
.sub-step-tracker {{
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 24px;
}}
.sub-step-pill {{
  flex: 1;
  height: 6px;
  background: var(--bd);
  border-radius: 999px;
  transition: background 0.3s ease;
}}
.sub-step-pill.done {{
  background: var(--g);
}}
.sub-step-pill.active {{
  background: var(--au);
}}

.q-label {{
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--mu);
  margin-bottom: 8px;
}}
.q-title {{
  font-size: 21px;
  font-weight: 700;
  line-height: 1.45;
  color: var(--tx);
  margin-bottom: 28px;
}}

/* Modern Options Cards */
.options-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  margin-bottom: 28px;
}}
@media (max-width: 600px) {{
  .options-grid {{
    grid-template-columns: 1fr;
  }}
}}
.opt-btn {{
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 16px 18px;
  background: var(--card);
  border: 1.5px solid var(--bd);
  border-radius: var(--radius-md);
  color: var(--tx);
  cursor: pointer;
  text-align: left;
  transition: all 0.2s ease;
  position: relative;
}}
.opt-btn:hover {{
  border-color: var(--g);
  background: var(--card-hover);
  transform: translateY(-1px);
}}
.opt-btn.active {{
  background: var(--g-light);
  border-color: var(--g);
  box-shadow: 0 0 0 2px var(--g);
}}
.opt-btn.active.na {{
  background: var(--bg);
  border-color: var(--mu);
  box-shadow: 0 0 0 2px var(--mu);
}}
.opt-badge {{
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--bd);
  color: var(--tx);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 14px;
  flex-shrink: 0;
  transition: all 0.2s ease;
}}
.opt-btn.active .opt-badge {{
  background: var(--g);
  color: #fff;
}}
.opt-btn.active.na .opt-badge {{
  background: var(--mu);
  color: #fff;
}}
.opt-text {{
  display: flex;
  flex-direction: column;
}}
.opt-name {{
  font-size: 15px;
  font-weight: 600;
  color: var(--tx);
}}
.opt-hint {{
  font-size: 12px;
  color: var(--mu);
  margin-top: 2px;
}}

/* Form elements */
label.form-label {{
  display: block;
  font-size: 14px;
  font-weight: 600;
  color: var(--tx);
  margin-bottom: 8px;
}}
input.modern-input, textarea.modern-input, select.modern-input {{
  width: 100%;
  font-family: inherit;
  font-size: 15px;
  padding: 14px 16px;
  background: var(--bg);
  border: 1.5px solid var(--bd);
  border-radius: var(--radius-md);
  color: var(--tx);
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
  outline: none;
}}
input.modern-input:focus, textarea.modern-input:focus, select.modern-input:focus {{
  border-color: var(--g);
  box-shadow: 0 0 0 3px var(--g-light);
  background: var(--card);
}}
textarea.modern-input {{
  min-height: 100px;
  line-height: 1.55;
  resize: vertical;
}}

/* Navigation Footer */
.nav-actions {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-top: 28px;
}}
.btn {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-family: inherit;
  font-size: 15px;
  font-weight: 600;
  padding: 12px 24px;
  border-radius: var(--radius-md);
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
}}
.btn-primary {{
  background: var(--g);
  color: #ffffff;
  box-shadow: var(--shadow-sm);
}}
.btn-primary:hover {{
  background: var(--g-hover);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}}
.btn-gold {{
  background: var(--au);
  color: #ffffff;
  box-shadow: var(--shadow-sm);
}}
.btn-gold:hover {{
  background: var(--au-hover);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}}
.btn-secondary {{
  background: transparent;
  color: var(--tx);
  border: 1.5px solid var(--bd);
}}
.btn-secondary:hover {{
  background: var(--card-hover);
  border-color: var(--mu);
}}
.btn:disabled {{
  opacity: 0.5;
  cursor: not-allowed;
  transform: none !important;
}}

.validation-error {{
  color: var(--bad);
  font-size: 13px;
  font-weight: 600;
  margin-top: 10px;
  min-height: 18px;
}}

/* Part Two Styling */
.interview-card {{
  padding: 24px 28px;
  margin-bottom: 20px;
}}
.interview-num {{
  font-size: 12px;
  font-weight: 700;
  color: var(--au);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 6px;
}}
.interview-q {{
  font-size: 16px;
  font-weight: 600;
  color: var(--tx);
  margin-bottom: 14px;
}}

/* Report Styling */
.report-hero {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 20px;
  padding: 28px 32px;
  background: linear-gradient(135deg, var(--card), var(--bg));
  border: 1px solid var(--bd);
  border-radius: var(--radius-lg);
  margin-bottom: 28px;
}}
.report-score-block {{
  display: flex;
  flex-direction: column;
}}
.report-score-title {{
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--mu);
  margin-bottom: 4px;
}}
.report-score-value {{
  font-size: 48px;
  font-weight: 800;
  color: var(--g);
  line-height: 1.1;
}}
.report-score-value span {{
  font-size: 20px;
  color: var(--mu);
  font-weight: 600;
}}
.status-pill {{
  display: inline-block;
  padding: 6px 14px;
  border-radius: 9999px;
  font-size: 13px;
  font-weight: 700;
  color: #fff;
  margin-top: 8px;
}}

.radar-wrapper {{
  background: var(--card);
  border: 1px solid var(--bd);
  border-radius: var(--radius-lg);
  padding: 28px;
  margin-bottom: 28px;
  text-align: center;
}}
.rad {{
  width: 100%;
  max-width: 460px;
  display: block;
  margin: 0 auto;
}}
.rad text {{
  fill: var(--tx);
  font-family: 'Inter', sans-serif;
  font-size: 11px;
}}
.rad .rl {{
  fill: var(--mu);
  font-size: 9px;
}}
.rad .gr {{
  fill: none;
  stroke: var(--bd);
  stroke-width: 1;
}}

.tiles {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(170px, 1fr));
  gap: 16px;
  margin: 24px 0 32px;
}}
.tile {{
  background: var(--card);
  border: 1px solid var(--bd);
  border-top: 4px solid var(--c);
  border-radius: var(--radius-md);
  padding: 16px 12px;
  text-align: center;
  box-shadow: var(--shadow-sm);
  transition: transform 0.2s ease;
}}
.tile:hover {{
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}}
.tile svg {{
  width: 64px;
  height: 64px;
  margin: 0 auto 8px;
}}
.tile .tn {{
  font-size: 13px;
  font-weight: 600;
  margin-bottom: 8px;
  min-height: 34px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--tx);
}}
.tile .tg {{
  stroke: var(--bd);
}}
.tile text {{
  fill: var(--tx);
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  font-size: 16px;
}}

.legend-row {{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px 18px;
  font-size: 12px;
  font-weight: 600;
  color: var(--mu);
  margin-top: 14px;
}}
.legend-row i {{
  display: inline-block;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin-right: 6px;
  vertical-align: middle;
}}

/* Section Cards in Report */
.section-card {{
  background: var(--card);
  border: 1px solid var(--bd);
  border-radius: var(--radius-lg);
  padding: 28px;
  margin-bottom: 20px;
  box-shadow: var(--shadow-sm);
}}
.section-card h3 {{
  font-size: 18px;
  font-weight: 700;
  color: var(--tx);
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 16px;
}}
.section-card h3 em {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: var(--g);
  color: #fff;
  font-style: normal;
  font-size: 13px;
}}
.section-card h4 {{
  font-size: 14px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--mu);
  margin: 18px 0 8px;
}}
.section-card p, .section-card li {{
  font-size: 15px;
  line-height: 1.6;
  color: var(--tx-muted);
}}
.section-card ul {{
  padding-left: 20px;
  margin: 10px 0;
}}
.section-card li {{
  margin-bottom: 6px;
}}
.section-card .pl {{
  display: grid;
  grid-template-columns: 110px 1fr;
  gap: 8px 14px;
  background: var(--bg);
  padding: 16px;
  border-radius: var(--radius-md);
  margin: 14px 0;
  font-size: 14px;
}}
.section-card .pl b {{
  font-weight: 700;
  color: var(--g);
}}

@media print {{
  header, .top-nav-bar, .nav-actions, .noprint {{
    display: none !important;
  }}
  body {{
    background: #fff;
    color: #000;
  }}
  .card, .section-card, .report-hero, .radar-wrapper {{
    box-shadow: none;
    border: 1px solid #ccc;
    break-inside: avoid;
  }}
}}
</style>
</head>
<body>
{header_html}
<main>
  <div id="app"></div>
</main>

<script>
const Z = [{z_content}];

const Q = [{q_content}];

const EV = ["E0 – No evidence", "E1 – Claimed", "E2 – Demonstrated (specific example)", "E3 – Documented (records/results)", "E4 – Sustained (multiple periods)"];

const CL = [
  [1.8, "Low restriction", "Relatively healthy", "#1f8a4c"],
  [2.6, "Emerging restriction", "Monitor and strengthen", "#8a9a1f"],
  [3.4, "Moderate restriction", "Development required", "#c78a00"],
  [4.2, "High restriction", "Priority intervention", "#d0661a"],
  [9.0, "Critical restriction", "Urgent investigation", "#b3401a"]
];

let S = {{
  nm: "",
  p: 0,
  s: 0,
  a: Z.map(() => []),
  t: Z.map(() => ""),
  l: Z.map(() => ""),
  q: Q.map(() => "")
}};

try {{
  const x = localStorage.getItem("hzos");
  if (x) {{
    const parsed = JSON.parse(x);
    S = Object.assign(S, parsed);
    if (S.s === undefined) S.s = 0;
  }}
}} catch (e) {{}}

const $ = id => document.getElementById(id);
const esc = s => String(s || "").replace(/&/g, "&amp;").replace(/</g, "&lt;");
function save() {{
  try {{
    localStorage.setItem("hzos", JSON.stringify(S));
  }} catch (e) {{}}
}}

let isTransitioning = false;
function transitionTo(nextP, nextS, direction = "next") {{
  if (isTransitioning) return;
  const stage = $("step-stage");
  if (!stage) {{
    S.p = nextP;
    S.s = nextS;
    save();
    render();
    window.scrollTo({{ top: 0, behavior: "smooth" }});
    return;
  }}
  isTransitioning = true;
  stage.classList.remove("anim-slide-in-right", "anim-slide-in-left", "anim-slide-out-left", "anim-slide-out-right");
  stage.classList.add(direction === "next" ? "anim-slide-out-left" : "anim-slide-out-right");

  setTimeout(() => {{
    S.p = nextP;
    S.s = nextS;
    save();
    render(direction);
    isTransitioning = false;
    window.scrollTo({{ top: 0, behavior: "smooth" }});
  }}, 220);
}}

function go(n) {{
  transitionTo(n, 0, n > S.p ? "next" : "prev");
}}

function selectRating(zoneIdx, qIdx, val) {{
  S.a[zoneIdx][qIdx] = val;
  save();
  renderFast();
  setTimeout(() => {{
    if (S.s < 5) {{
      transitionTo(S.p, S.s + 1, "next");
    }} else {{
      transitionTo(S.p, 6, "next");
    }}
  }}, 240);
}}

function cl(i) {{
  return CL.find(c => i < c[0]) || CL[CL.length - 1];
}}

function calc() {{
  return Z.map((z, k) => {{
    const v = S.a[k].filter(x => typeof x === "number");
    const avg = v.length ? v.reduce((a, b) => a + b, 0) / v.length : null;
    return {{
      n: z[0],
      avg,
      idx: avg === null ? null : 6 - avg,
      lv: S.l[k]
    }};
  }});
}}

function renderFast() {{
  const options = document.querySelectorAll(".opt-btn");
  if (!options.length) return;
  const zoneIdx = S.p - 1;
  const qIdx = S.s - 1;
  const curVal = S.a[zoneIdx] ? S.a[zoneIdx][qIdx] : undefined;
  options.forEach(btn => {{
    const valStr = btn.getAttribute("data-val");
    const val = valStr === "na" ? "na" : Number(valStr);
    if (val === curVal) {{
      btn.classList.add("active");
    }} else {{
      btn.classList.remove("active");
    }}
  }});
}}

function render(direction = "next") {{
  const p = S.p;
  const s = S.s || 0;
  let h = "";
  const animClass = direction === "prev" ? "anim-slide-in-left" : "anim-slide-in-right";

  // Global Progress computation
  let progressPct = 0;
  let metaTitle = "";
  if (p === 0) {{
    progressPct = 2;
    metaTitle = "Welcome & Instructions";
  }} else if (p >= 1 && p <= 13) {{
    const currentStepInZone = s === 0 ? 0 : s;
    const completedUnits = (p - 1) * 6 + currentStepInZone;
    progressPct = Math.round((completedUnits / (13 * 6 + 2)) * 100);
    metaTitle = s === 0 
      ? `Zone ${{p}} of 13: ${{Z[p-1][0]}} • Introduction`
      : s <= 5 
      ? `Zone ${{p}} of 13: ${{Z[p-1][0]}} • Question ${{s}} of 5`
      : `Zone ${{p}} of 13: ${{Z[p-1][0]}} • Evidence Validation`;
  }} else if (p === 14) {{
    progressPct = 90;
    metaTitle = "Part Two: Constraint Discovery Interview";
  }} else {{
    progressPct = 100;
    metaTitle = "Personal Stagnation Report";
  }}

  const topNav = (p === 15) ? "" : `
    <div class="top-nav-bar">
      <div class="top-prog"><div class="top-prog-fill" style="width: ${{progressPct}}%"></div></div>
      <div class="top-meta">
        <span>${{metaTitle}}</span>
        <span>${{progressPct}}% Completed</span>
      </div>
    </div>
  `;

  if (p === 0) {{
    // Start page
    h = `
    <div id="step-stage" class="slide-stage ${{animClass}}">
      <div class="card">
        <span class="pill-badge">DIAGNOSTIC INSTRUMENT</span>
        <h1 class="hero-title">The Hidden Zones of Stagnation</h1>
        <p class="tagline">A Multidimensional Visionary Constraint Assessment</p>
        <p style="color:var(--tx-muted);font-size:16px;">
          Identify the invisible bottlenecks, systemic friction, and subconscious constraints that hinder your momentum, execution, and leadership expansion.
        </p>

        <div class="stats-grid">
          <div class="stat-box">
            <div class="stat-num">65</div>
            <div class="stat-label">Diagnostic Statements</div>
          </div>
          <div class="stat-box">
            <div class="stat-num">13</div>
            <div class="stat-label">Growth Dimensions</div>
          </div>
          <div class="stat-box">
            <div class="stat-num">90</div>
            <div class="stat-label">Day Focus Horizon</div>
          </div>
        </div>

        <div class="info-box">
          <h4>Before you begin</h4>
          <p>
            Stagnation is not always inactivity. You may be working harder than ever while key areas remain stalled. 
            Evaluate each statement based on your <b>actual demonstrated experience over the last 90 days</b>—not on what you intend, hope, or know you should do.
          </p>
          <ul>
            <li><b>1 (Never)</b> to <b>5 (Consistently)</b>: Choose the rating that matches your day-to-day reality.</li>
            <li><b>N/A (Not Applicable)</b>: Only select if the concept genuinely does not apply to your life or work.</li>
            <li>Each zone includes a brief evidence check to substantiate your ratings.</li>
            <li>Your progress is continuously auto-saved in your browser.</li>
          </ul>
        </div>

        <div style="margin: 24px 0 8px;">
          <label class="form-label">Your Name (optional, included in your generated report):</label>
          <input type="text" class="modern-input" placeholder="e.g. Alex Taylor" value="${{esc(S.nm || '')}}" oninput="S.nm=this.value;save()">
        </div>

        <div class="nav-actions" style="justify-content: flex-end;">
          <button class="btn btn-gold" onclick="transitionTo(1, 0, 'next')">Begin Assessment →</button>
        </div>
      </div>
    </div>`;
  }} else if (p >= 1 && p <= 13) {{
    const z = Z[p - 1];
    const k = p - 1;

    if (s === 0) {{
      // Zone Splash Screen
      h = `
      <div id="step-stage" class="slide-stage ${{animClass}}">
        <div class="card">
          <span class="pill-badge">ZONE ${{p}} OF 13</span>
          <h1 class="splash-title">Let's assess Zone ${{p}}:<br><span style="color:var(--g);">${{z[0]}}</span></h1>
          
          <div class="focus-container">
            <div class="focus-heading">ZONE FOCUS & DEFINITION</div>
            <div class="focus-desc">${{z[1]}}</div>
          </div>

          <div class="splash-checklist">
            <div class="check-item">
              <div class="check-icon">1</div>
              <div><b>5 Focused Questions:</b> You will evaluate 5 targeted statements one by one.</div>
            </div>
            <div class="check-item">
              <div class="check-icon">2</div>
              <div><b>90-Day Reality:</b> Score your actual operational consistency, not aspirations.</div>
            </div>
            <div class="check-item">
              <div class="check-icon">3</div>
              <div><b>Evidence Validation:</b> Capture concrete proof of progress or identify missing structures.</div>
            </div>
          </div>

          <div class="nav-actions">
            ${{p > 1 
              ? `<button class="btn btn-secondary" onclick="transitionTo(${{p - 1}}, 6, 'prev')">← Previous Zone</button>` 
              : `<button class="btn btn-secondary" onclick="transitionTo(0, 0, 'prev')">← Overview</button>`}}
            <button class="btn btn-primary" onclick="transitionTo(${{p}}, 1, 'next')">Start Zone ${{p}} Questions →</button>
          </div>
        </div>
      </div>`;
    }} else if (s >= 1 && s <= 5) {{
      // Question 1..5 Step
      const qIdx = s - 1;
      const statement = z[2][qIdx];
      const curAnswer = S.a[k][qIdx];

      h = `
      <div id="step-stage" class="slide-stage ${{animClass}}">
        <div class="card">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
            <span class="pill-badge">ZONE ${{p}}: ${{z[0]}}</span>
            <span style="font-size:13px; font-weight:700; color:var(--mu);">Question ${{s}} of 5</span>
          </div>

          <div class="sub-step-tracker">
            ${{[0,1,2,3,4].map(idx => {{
              let cls = "sub-step-pill";
              if (idx === qIdx) cls += " active";
              else if (S.a[k][idx] !== undefined && S.a[k][idx] !== null) cls += " done";
              return `<div class="${{cls}}"></div>`;
            }}).join("")}
          </div>

          <div class="q-label">STATEMENT ${{s}} OF 5</div>
          <div class="q-title">${{statement}}</div>

          <div class="options-grid">
            <button type="button" class="opt-btn ${{curAnswer === 1 ? 'active' : ''}}" data-val="1" onclick="selectRating(${{k}}, ${{qIdx}}, 1)">
              <div class="opt-badge">1</div>
              <div class="opt-text">
                <span class="opt-name">Never</span>
                <span class="opt-hint">Does not describe my practice</span>
              </div>
            </button>
            <button type="button" class="opt-btn ${{curAnswer === 2 ? 'active' : ''}}" data-val="2" onclick="selectRating(${{k}}, ${{qIdx}}, 2)">
              <div class="opt-badge">2</div>
              <div class="opt-text">
                <span class="opt-name">Rarely</span>
                <span class="opt-hint">Infrequently or under pressure only</span>
              </div>
            </button>
            <button type="button" class="opt-btn ${{curAnswer === 3 ? 'active' : ''}}" data-val="3" onclick="selectRating(${{k}}, ${{qIdx}}, 3)">
              <div class="opt-badge">3</div>
              <div class="opt-text">
                <span class="opt-name">Occasionally</span>
                <span class="opt-hint">Sporadic, inconsistent execution</span>
              </div>
            </button>
            <button type="button" class="opt-btn ${{curAnswer === 4 ? 'active' : ''}}" data-val="4" onclick="selectRating(${{k}}, ${{qIdx}}, 4)">
              <div class="opt-badge">4</div>
              <div class="opt-text">
                <span class="opt-name">Frequently</span>
                <span class="opt-hint">Regular habit and reliable standard</span>
              </div>
            </button>
            <button type="button" class="opt-btn ${{curAnswer === 5 ? 'active' : ''}}" data-val="5" onclick="selectRating(${{k}}, ${{qIdx}}, 5)">
              <div class="opt-badge">5</div>
              <div class="opt-text">
                <span class="opt-name">Consistently</span>
                <span class="opt-hint">Deeply ingrained, disciplined norm</span>
              </div>
            </button>
            <button type="button" class="opt-btn na ${{curAnswer === 'na' ? 'active' : ''}}" data-val="na" onclick="selectRating(${{k}}, ${{qIdx}}, 'na')">
              <div class="opt-badge">N/A</div>
              <div class="opt-text">
                <span class="opt-name">Not Applicable</span>
                <span class="opt-hint">Does not apply to my situation</span>
              </div>
            </button>
          </div>

          <div class="validation-error" id="step-err"></div>

          <div class="nav-actions">
            <button class="btn btn-secondary" onclick="transitionTo(${{p}}, ${{s - 1}}, 'prev')">← Previous</button>
            <button class="btn btn-primary" onclick="${{curAnswer !== undefined ? `transitionTo(${{p}}, ${{s === 5 ? 6 : s + 1}}, 'next')` : `document.getElementById('step-err').textContent='Please select an option to proceed.'`}}">
              ${{s === 5 ? 'Continue to Evidence →' : 'Next Question →'}}
            </button>
          </div>
        </div>
      </div>`;
    }} else if (s === 6) {{
      // Evidence & Level step
      h = `
      <div id="step-stage" class="slide-stage ${{animClass}}">
        <div class="card">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
            <span class="pill-badge gold">ZONE ${{p}} · EVIDENCE VALIDATION</span>
            <span style="font-size:13px; font-weight:700; color:var(--mu);">Verification</span>
          </div>

          <h2 style="font-size:22px; margin-bottom:8px;">Supporting Evidence for ${{z[0]}}</h2>
          <p style="color:var(--tx-muted); margin-bottom:20px;">
            To ensure objectivity, document the concrete proof or measurable results that substantiate your scores.
          </p>

          <div class="focus-container" style="border-left-color:var(--g); margin:16px 0 24px;">
            <div class="focus-heading" style="color:var(--g);">PROMPT FOR REFLECTION</div>
            <div class="focus-desc" style="font-size:15px;">${{z[3]}}</div>
          </div>

          <div style="margin-bottom:20px;">
            <label class="form-label">What documented evidence, records, or examples can you demonstrate?</label>
            <textarea class="modern-input" placeholder="Type specific evidence or note if this area currently lacks documentation..." oninput="S.t[${{k}}]=this.value;save()">${{esc(S.t[k] || "")}}</textarea>
          </div>

          <div style="margin-bottom:24px;">
            <label class="form-label">Strength of Your Evidence</label>
            <select class="modern-input" onchange="S.l[${{k}}]=this.value;save()">
              <option value="">-- Select evidence validation level --</option>
              ${{EV.map((e, i) => `<option value="${{i}}" ${{S.l[k] == i && S.l[k] !== "" ? "selected" : ""}}>${{e}}</option>`).join("")}}
            </select>
          </div>

          <div class="validation-error" id="zone-err"></div>

          <div class="nav-actions">
            <button class="btn btn-secondary" onclick="transitionTo(${{p}}, 5, 'prev')">← Question 5</button>
            <button class="btn btn-primary" onclick="completeZone(${{p}})">
              ${{p === 13 ? "Complete All Zones & Go to Part Two →" : `Finish Zone ${{p}} & Next Zone →`}}
            </button>
          </div>
        </div>
      </div>`;
    }}
  }} else if (p === 14) {{
    // Part Two: Interview
    h = `
    <div id="step-stage" class="slide-stage ${{animClass}}">
      <div class="card" style="margin-bottom:24px;">
        <span class="pill-badge gold">QUALITATIVE DIAGNOSTIC</span>
        <h1 class="hero-title">Part Two: The Constraint Discovery Interview</h1>
        <p class="tagline">The scores highlight where growth is constrained. These 10 strategic questions uncover the root causes.</p>
        <p style="color:var(--tx-muted);font-size:15px;">Take your time to articulate specific, honest responses. Your insights will be synthesized directly into your personal stagnation roadmap.</p>
      </div>

      ${{Q.map((q, i) => `
        <div class="card interview-card">
          <div class="interview-num">QUESTION ${{i + 1}} OF 10</div>
          <div class="interview-q">${{q}}</div>
          <textarea class="modern-input" placeholder="Your thoughtful response..." oninput="S.q[${{i}}]=this.value;save()">${{esc(S.q[i] || "")}}</textarea>
        </div>
      `).join("")}}

      <div class="card">
        <div class="nav-actions">
          <button class="btn btn-secondary" onclick="transitionTo(13, 6, 'prev')">← Back to Zone 13</button>
          <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <button class="btn btn-secondary" onclick="dlWork()">Download Interview Workbook (.doc)</button>
            <button class="btn btn-gold" onclick="transitionTo(15, 0, 'next')">Generate My Report →</button>
          </div>
        </div>
      </div>
    </div>`;
  }} else {{
    // Report Page
    h = report();
  }}

  $("app").innerHTML = topNav + h;
}}

function completeZone(p) {{
  const z = p - 1;
  for (let i = 0; i < 5; i++) {{
    if (S.a[z][i] === undefined || S.a[z][i] === null) {{
      const errBox = $("zone-err");
      if (errBox) {{
        errBox.innerHTML = `Question ${{i + 1}} has not been rated yet. <a href="javascript:void(0)" onclick="transitionTo(${{p}}, ${{i + 1}}, 'prev')" style="color:var(--g);text-decoration:underline;margin-left:6px;font-weight:700;">Click here to answer Question ${{i + 1}}</a>`;
      }}
      return;
    }}
  }}
  if (p === 13) {{
    transitionTo(14, 0, "next");
  }} else {{
    transitionTo(p + 1, 0, "next");
  }}
}}

const SH = ["Vision", "Identity", "Conviction", "Knowledge", "Competency", "Execution", "Systems", "Relationships", "Resources", "Environment", "Energy", "Feedback", "Spirituality"];

function tile(r, i) {{
  if (r.idx === null) return `
    <div class="tile" style="--c:var(--mu)">
      <div class="tn">${{r.n}}</div>
      <span class="status-pill" style="background:var(--mu)">All N/A</span>
    </div>`;
  const q = cl(r.idx);
  const L = 2 * Math.PI * 26;
  return `
    <div class="tile" style="--c:${{q[3]}}">
      <svg viewBox="0 0 64 64">
        <circle class="tg" cx="32" cy="32" r="26" fill="none" stroke-width="5"/>
        <circle cx="32" cy="32" r="26" fill="none" stroke="${{q[3]}}" stroke-width="5" stroke-linecap="round" stroke-dasharray="${{(r.idx / 5 * L).toFixed(1)}} ${{L.toFixed(1)}}" transform="rotate(-90 32 32)"/>
        <text x="32" y="37" text-anchor="middle">${{r.idx.toFixed(1)}}</text>
      </svg>
      <div class="tn">${{r.n}}</div>
      <span class="status-pill" style="background:${{q[3]}}">${{q[1].replace(" restriction", "")}}</span>
    </div>`;
}}

function radar(R) {{
  const C = 230, Rd = 150, n = R.length;
  const P = (i, f) => {{
    const a = -Math.PI / 2 + i * 2 * Math.PI / n;
    return [C + Math.cos(a) * Rd * f, C + Math.sin(a) * Rd * f];
  }};
  let s = `<svg viewBox="0 0 460 460" class="rad" role="img" aria-label="Radar chart of stagnation index by zone">`;
  [1, 2, 3, 4, 5].forEach(k => {{
    s += `<polygon class="gr" points="${{R.map((_, i) => P(i, k / 5).join(",")).join(" ")}}"/>
          <text class="rl" x="${{C + 4}}" y="${{C - Rd * k / 5 + 10}}">${{k}}</text>`;
  }});
  R.forEach((_, i) => {{
    const [x, y] = P(i, 1);
    const [lx, ly] = P(i, 1.15);
    s += `<line class="gr" x1="${{C}}" y1="${{C}}" x2="${{x}}" y2="${{y}}"/>
          <text x="${{lx}}" y="${{ly + 4}}" text-anchor="${{lx < C - 8 ? "end" : lx > C + 8 ? "start" : "middle"}}">${{SH[i]}}</text>`;
  }});
  s += `<polygon points="${{R.map((r, i) => P(i, (r.idx || 0) / 5).join(",")).join(" ")}}" fill="#e4a000" fill-opacity=".35" stroke="#e4a000" stroke-width="2.5" stroke-linejoin="round"/>`;
  R.forEach((r, i) => {{
    if (r.idx !== null) {{
      const [x, y] = P(i, r.idx / 5);
      s += `<circle cx="${{x}}" cy="${{y}}" r="5" fill="${{cl(r.idx)[3]}}" stroke="#fff" stroke-width="1.5"/>`;
    }}
  }});
  return s + "</svg>";
}}

const INT = [0, 1, 2, 3, 4, 5, 6, 10, 11, 12];
const EXT = [7, 8, 9];
const CAP = [0, 1, 3, 4, 5, 6, 11];

const ACT = [{act_content}];

const LK = [{lk_content}];

function sections(R) {{
  const nm = k => Z[k][0], ix = k => R[k].idx;
  const V = R.map((r, k) => k).filter(k => ix(k) !== null);
  const srt = [...V].sort((a, b) => ix(b) - ix(a));
  const str = [...V].sort((a, b) => ix(a) - ix(b)).slice(0, 3);
  let rs = srt.filter(k => ix(k) >= 2.6);
  const hot = rs.length >= 2 ? rs : srt.slice(0, 4);
  const soft = rs.length < 2;
  const li = a => a.length ? "<ul>" + a.map(x => "<li>" + x + "</li>").join("") + "</ul>" : "";
  const zl = a => li(a.map(k => `<b>${{nm(k)}}</b>: ${{ix(k).toFixed(2)}} (${{cl(ix(k))[1].toLowerCase()}})`));

  let o = `
  <div class="section-card">
    <h3><em>1</em>Where your growth is being restricted</h3>
    ${{soft ? `<p class="sm" style="color:var(--mu);margin-bottom:12px;">No zone reaches moderate restriction. These are the areas to monitor most closely.</p>` : ""}}
    ${{zl(hot.slice(0, 6))}}
    <h4>Strongest zones</h4>
    ${{zl(str)}}
  </div>`;

  const w = [];
  CAP.forEach(k => S.a[k].forEach((v, i) => {{
    if (typeof v === "number" && v <= 2) w.push([v, k, i]);
  }}));
  w.sort((a, b) => a[0] - b[0]);
  const cz = CAP.filter(k => ix(k) !== null && ix(k) >= 2.6).sort((a, b) => ix(b) - ix(a));

  o += `
  <div class="section-card">
    <h3><em>2</em>Which capacities are underdeveloped</h3>
    ${{cz.length ? zl(cz) : `<p class="sm" style="color:var(--mu);">No capacity zone reaches moderate restriction.</p>`}}
    ${{w.length ? `<h4>Specific capacities you rated 1 or 2</h4>` + li(w.slice(0, 8).map(x => `${{nm(x[1])}}: “${{Z[x[1]][2][x[2]]}}” (${{x[0]}}/5)`)) : ""}}
  </div>`;

  const av = a => {{
    const v = a.filter(k => ix(k) !== null);
    return v.length ? v.reduce((s, k) => s + ix(k), 0) / v.length : null;
  }};
  const ai = av(INT), ae = av(EXT);

  const side = (a, l, ave) => {{
    const t = a.filter(k => ix(k) !== null).sort((x, y) => ix(y) - ix(x)).slice(0, 2);
    return `<h4>${{l}}${{ave === null ? "" : " · average index " + ave.toFixed(2)}}</h4>` + (t.length ? zl(t) : "<p class='sm' style='color:var(--mu);'>No data.</p>");
  }};

  const dom = ai === null || ae === null ? "" : ae > ai + .3 
    ? "Your external conditions appear to be limiting you more than your internal capacities."
    : ai > ae + .3 
    ? "Your internal conditions appear to be limiting you more than your external environment."
    : "Internal and external conditions are restricting you to a similar degree.";

  const q4 = (S.q[3] || "").trim();
  const q6 = (S.q[5] || "").trim();

  o += `
  <div class="section-card">
    <h3><em>3</em>What internal or external conditions are limiting your progress</h3>
    ${{side(INT, "Internal: mindset, capacity, discipline, energy, spiritual", ai)}}
    ${{side(EXT, "External: relationships, resources, environment", ae)}}
    <p style="margin-top:14px;font-weight:600;color:var(--tx);">${{dom}}</p>
    ${{q4 ? `<h4>What you suspect is holding you back</h4><p>${{esc(q4)}}</p>` : ""}}
    ${{q6 ? `<h4>What you believe is missing</h4><p>${{esc(q6)}}</p>` : ""}}
  </div>`;

  const hs = new Set(hot.map(String));
  const pr = LK.filter(l => hs.has(String(l[0])) && hs.has(String(l[1]))).slice(0, 6);

  o += `
  <div class="section-card">
    <h3><em>4</em>Which constraints are interconnected</h3>
    ${{pr.length ? li(pr.map(l => `<b>${{nm(l[0])}} ↔ ${{nm(l[1])}}</b>: ${{l[2]}}.`)) : `<p class="sm" style="color:var(--mu);">No directly linked restricted zones were found. Review your Part Two answers for hidden connections.</p>`}}
    <p class="sm" style="color:var(--mu);margin-top:10px;">These links are hypotheses to test with an assessor, not proven causes.</p>
  </div>`;

  const t0 = hot[0], t1 = hot[1], t2 = hot[2];
  const q3 = (S.q[2] || "").trim();
  const ext = EXT.filter(k => ix(k) !== null).sort((a, b) => ix(b) - ix(a))[0];

  if (t0 === undefined) return o;

  o += `
  <div class="section-card">
    <h3><em>5</em>What needs to change to unlock your next level</h3>
    <p style="margin-bottom:12px;"><b>Primary constraint to address:</b> ${{nm(t0)}}. It has the highest restriction${{t1 !== undefined ? " and is linked to " + nm(t1) : ""}}.</p>
    <div class="pl">
      <b>STOP</b><span>${{q3 ? "Repeating what has not worked: " + esc(q3) : "Repeating approaches that have not produced results in " + nm(t0) + "."}}</span>
      <b>START</b><span>${{ACT[t0]}}</span>
      <b>STRENGTHEN</b><span>${{t1 !== undefined ? ACT[t1] : "Your next most restricted zone."}}</span>
      <b>ACQUIRE</b><span>${{q6 ? esc(q6) : ext !== undefined ? ACT[ext] : "The missing resource or relationship."}}</span>
      <b>REDESIGN</b><span>How you work in ${{nm(t0)}}: replace ad-hoc effort with a documented routine, a named owner and a review date.</span>
    </div>
    <h4>90-day plan</h4>
    <ul>
      <li><b>Days 1–30:</b> ${{ACT[t0]}}</li>
      <li><b>Days 31–60:</b> ${{t1 !== undefined ? ACT[t1] : "Consolidate the first month and measure results."}}</li>
      <li><b>Days 61–90:</b> ${{t2 !== undefined ? ACT[t2] : "Embed what worked into a routine."}} Hold a final review with documented evidence of change.</li>
    </ul>
  </div>`;

  const g = R.map((r, k) => k).filter(k => R[k].avg >= 4 && (S.l[k] === "" || S.l[k] === undefined || +S.l[k] <= 1));
  o += `
  <div class="section-card">
    <h3>Evidence check</h3>
    ${{g.length ? li(g.map(k => `<b>${{nm(k)}}</b>: self-score ${{R[k].avg.toFixed(1)}}/5 with evidence at E0–E1 or not given. A high score without proof is itself a finding.`)) : `<p class="sm" style="color:var(--mu);">No high self-scores are unsupported by evidence.</p>`}}
  </div>`;

  return o;
}}

const dd = () => new Date().toLocaleDateString("en-GB", {{ day: "numeric", month: "long", year: "numeric" }});

function docHTML(ti, body) {{
  return `<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word"><head><meta charset="utf-8"><title>${{ti}}</title><style>body{{font-family:Arial,sans-serif;color:#1b2a22;font-size:11pt;line-height:1.5}}h1,h2,h3,h4{{color:#00522a}}h1{{border-bottom:3px solid #e4a000;padding-bottom:4px}}table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid #bbb;padding:7px;font:10pt Arial,sans-serif;text-align:left;vertical-align:top}}th{{background:#00522a;color:#fff}}.card{{border:1px solid #ccc;border-left:4px solid #00522a;padding:8px 12px;margin:12px 0}}.sm{{color:#666;font-size:9.5pt}}.pl{{width:100%}}</style></head><body><p style="color:#c78a00;font:bold 9pt Arial;letter-spacing:2px">PHOSZADE · VISIONEERING 2027</p><h1>${{ti}}</h1><p>Participant: <b>${{esc(S.nm || "—")}}</b> &nbsp;|&nbsp; Date: ${{dd()}}</p>${{body}}</body></html>`;
}}

function dl(f, h) {{
  const b = new Blob(["\\ufeff" + h], {{ type: "application/msword" }});
  const a = document.createElement("a");
  a.href = URL.createObjectURL(b);
  a.download = f + (S.nm ? "-" + S.nm.trim().replace(/[^\\w]+/g, "-") : "") + ".doc";
  document.body.appendChild(a);
  a.click();
  a.remove();
}}

function dlWork() {{
  const R = calc();
  let b = `<h2>Part Two: Constraint Discovery Interview</h2><table><tr><th style="width:42%">Question</th><th>Your response</th></tr>${{Q.map((q, i) => `<tr><td>${{i + 1}}. ${{q}}</td><td>${{esc(S.q[i] || "—").replace(/\\n/g, "<br>")}}</td></tr>`).join("")}}</table><h2>Zone evidence log</h2><table><tr><th>Zone</th><th>Avg score</th><th>Evidence level</th><th>Evidence provided</th></tr>${{Z.map((z, k) => `<tr><td>${{z[0]}}</td><td>${{R[k].avg === null ? "N/A" : R[k].avg.toFixed(1)}}</td><td>${{S.l[k] === "" || S.l[k] === undefined ? "Not selected" : EV[S.l[k]]}}</td><td>${{esc(S.t[k] || "—").replace(/\\n/g, "<br>")}}</td></tr>`).join("")}}</table>`;
  dl("HZOS-Interview-Workbook", docHTML("HZOS Interview Workbook", b));
}}

function dlRep() {{
  const R = calc();
  const V = R.filter(r => r.idx !== null);
  const ov = V.length ? V.reduce((a, r) => a + r.idx, 0) / V.length : 0;
  const c = cl(ov);
  let b = `<h2>Overall stagnation index: ${{ov.toFixed(2)}} / 5 — ${{c[1]}}</h2><p class="sm">${{c[2]}}</p><h2>Zone performance</h2><table><tr><th>Zone</th><th>Avg score</th><th>Stagnation index</th><th>Status</th><th>Evidence</th></tr>${{R.map((r, k) => `<tr><td>${{r.n}}</td><td>${{r.avg === null ? "N/A" : r.avg.toFixed(2)}}</td><td>${{r.idx === null ? "N/A" : r.idx.toFixed(2)}}</td><td>${{r.idx === null ? "—" : cl(r.idx)[1]}}</td><td>${{S.l[k] === "" || S.l[k] === undefined ? "—" : "E" + S.l[k]}}</td></tr>`).join("")}}</table>${{sections(R)}}<p class="sm">This is a developmental diagnostic instrument, not a clinical or psychological test. Thresholds are proposed operational bands, not validated norms. Interpret scores with documented evidence and professional judgment.</p>`;
  dl("HZOS-Personal-Stagnation-Report", docHTML("The Hidden Zones of Stagnation: Personal Report", b));
}}

function report() {{
  const R = calc();
  const V = R.filter(r => r.idx !== null);
  const ov = V.length ? V.reduce((a, r) => a + r.idx, 0) / V.length : 0;
  const c = cl(ov);

  let h = `
  <div class="card" style="margin-bottom:24px;">
    <span class="pill-badge">EXECUTIVE SUMMARY</span>
    <h1 class="hero-title" style="margin-bottom:8px;">Personal Stagnation Report</h1>
    <p style="color:var(--tx-muted);font-size:15px;margin-bottom:24px;">
      Diagnostic results synthesized from your 13 developmental dimensions and 90-day evidence log.
    </p>

    <div class="report-hero">
      <div class="report-score-block">
        <span class="report-score-title">Overall Stagnation Index</span>
        <div class="report-score-value">
          ${{ov.toFixed(2)}}<span> / 5.00</span>
        </div>
        <div>
          <span class="status-pill" style="background:${{c[3]}}">${{c[1]}}</span>
        </div>
      </div>
      <div style="flex:1;min-width:240px;">
        <h4 style="font-size:14px;font-weight:700;color:var(--tx);margin-bottom:6px;">Interpretation</h4>
        <p style="font-size:14px;line-height:1.6;color:var(--tx-muted);">${{c[2]}}</p>
      </div>
    </div>

    <div class="radar-wrapper">
      <h3 style="font-size:18px;font-weight:700;margin-bottom:6px;">Constraint Profile Radar</h3>
      <p style="font-size:13px;color:var(--mu);margin-bottom:16px;">
        Points plotted further from the center indicate greater operational friction. A compact inner profile represents optimal momentum.
      </p>
      ${{radar(R)}}
      <div class="legend-row">
        ${{CL.map(c => `<span><i style="background:${{c[3]}}"></i>${{c[1]}}</span>`).join("")}}
      </div>
    </div>

    <h2 style="font-size:20px;font-weight:700;margin:32px 0 16px;">Zone Performance Breakdown</h2>
    <div class="tiles">
      ${{R.map((r, i) => tile(r, i)).join("")}}
    </div>

    ${{sections(R)}}

    <div class="info-box" style="margin:28px 0;background:var(--bg);border-left-color:var(--mu);">
      <h4 style="color:var(--tx);">Diagnostic Disclaimer</h4>
      <p style="font-size:13px;color:var(--mu);">
        This tool is a structured self-assessment instrument designed for personal development, leadership reflection, and strategic alignment. It does not constitute psychological or clinical diagnosis.
      </p>
    </div>

    <div class="nav-actions noprint" style="flex-wrap:wrap;gap:12px;">
      <button class="btn btn-secondary" onclick="transitionTo(14, 0, 'prev')">← Back to Interview</button>
      <div style="display:flex;gap:10px;flex-wrap:wrap;">
        <button class="btn btn-secondary" onclick="if(confirm('Clear all answers and reset assessment?')){{localStorage.removeItem('hzos');S={{nm:'',p:0,s:0,a:Z.map(()=>[]),t:Z.map(()=>''),l:Z.map(()=>''),q:Q.map(()=>'')}};save();render()}}">Reset All</button>
        <button class="btn btn-secondary" onclick="dlWork()">Download Workbook (.doc)</button>
        <button class="btn btn-gold" onclick="dlRep()">Download Full Report (.doc)</button>
      </div>
    </div>
  </div>`;
  return h;
}}

render();
</script>
</body>
</html>
'''

with open('hzos-assessment.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Updated hzos-assessment.html successfully!")
