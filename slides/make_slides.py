#!/usr/bin/env python3
"""Week 2 carousel: Canada and Türkiye (The Median Canadian), draft 3.

python3 values.py && python3 make_slides.py
-> slides.html, out/the-median-canadian-canada-turkiye-n-of-9.png and .jpg, out/contact-sheet.jpg,
   out/cover-options.jpg (two cover photos side by side) and a fit report.
Every number on a slide is read from values.json, which values.py builds from the analysis files and facts.json.
"""
import html, json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
V = json.load(open(os.path.join(HERE, "values.json")))
PH = json.load(open(os.path.join(HERE, "photos_used.json")))
N = 9
ALT_COVER_HEAD = None
ALT_COVER_BODY = ('<p class="lead">Both countries back free trade talks, and Carney\'s visit brought new agreements.</p>'
                  '<p class="body">It was the first official visit by a Canadian PM. Here is where Türkiye fits as Canada looks beyond the US.</p>')
OUTDIR = os.path.join(HERE, "out")
os.makedirs(OUTDIR, exist_ok=True)

CA = "#64c4ee"      # Canada's side
CA_LIGHT = "#bfe6f8"
TR = "#ffc14d"      # Türkiye's side
GREY = "#9aa3ae"
GRID = "rgba(255,255,255,0.18)"
TEXT = "#ffffff"
MUTED = "#c9d0d9"
FONT = 'ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif'

POS = {"1": "45% 50%", "1b": "55% 45%", "2": "75% 50%", "3": "50% 50%", "4": "50% 50%", "5": "40% 50%",
       "6": "60% 50%", "7": "55% 50%", "8": "50% 40%", "9": "50% 50%"}


def esc(s):
    return html.escape(str(s), quote=True)


def bn(x, d=1):
    return f"${x / 1e9:.{d}f} billion"


def mn(x):
    return f"${x / 1e6:,.0f} million"


def mshort(x):
    return f"${x / 1e6:,.0f}M"


def usd_short(x):
    return f"US${x / 1e9:.1f}B" if x >= 1e9 else f"US${x / 1e6:,.0f}M"


def times(x):
    r = round(x)
    w = {2: "twice", 3: "three times", 4: "four times"}.get(r, f"{r} times")
    return ("almost " if x < r else "") + w


def halo(x, y, txt, size=24, fill=TEXT, anchor="start", weight=700):
    s = f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" font-family=\'{FONT}\''
    return (f'<text x="{x:.1f}" y="{y:.1f}" {s} fill="none" stroke="rgba(8,11,16,0.9)" stroke-width="6" stroke-linejoin="round">{esc(txt)}</text>'
            f'<text x="{x:.1f}" y="{y:.1f}" {s} fill="{fill}">{esc(txt)}</text>')


def svg(W, H, g):
    return f'<svg width="{W}" height="{H:.0f}" viewBox="0 0 {W} {H:.0f}">{g}</svg>'


# ------------------------------------------------------------------ 2. what Türkiye buys
def v_tr_buys():
    rows = V["tr_buys"]
    W = 900
    mx = max(r["world"] for r in rows)
    X = lambda val: 560 * val / mx
    g, y = "", 8
    for r in rows:
        g += halo(0, y + 22, r["name"], 23, weight=800)
        g += f'<rect x="0" y="{y + 34}" width="{max(X(r["world"]), 2):.1f}" height="34" fill="{GREY}" opacity="0.55"/>'
        g += f'<rect x="0" y="{y + 34}" width="{max(X(r["canada"]), 3):.1f}" height="34" fill="{CA}"/>'
        xe = max(X(r["world"]), X(r["canada"])) + 14
        g += halo(xe, y + 59, usd_short(r["world"]), 23, weight=800)
        g += halo(W, y + 22, f"from Canada {usd_short(r['canada'])}", 22, fill=CA, anchor="end", weight=800)
        y += 84
    return svg(W, y + 4, g)


# ------------------------------------------------------------------ 3. receipt and trade deficit
def v_goods_receipts():
    def rc(title, rows, col, total):
        out = f'<div class="rc"><div class="rct" style="color:{col}">{esc(title)}</div>'
        for name, val in rows.items():
            out += f'<div class="rr"><span>{esc(name)}</span><b>${val:,}M</b></div>'
        out += f'<div class="rr tot"><span>Total</span><b style="color:{col}">{bn(total)}</b></div>'
        return out + "</div>"
    return ('<div class="rcs">' + rc("Canada sold Türkiye", V["receipt_goods_to_tr"], CA, V["tr_exports_2025"])
            + rc("Canada bought from Türkiye", V["receipt_goods_to_ca"], TR, V["tr_imports_2025"]) + "</div>")


# ------------------------------------------------------------------ 4. duties
def v_duties():
    A, B = V["duty_ca_goods"], V["duty_tr_goods"]
    W = 900
    mx = max(A["base"], B["base"])
    X = lambda val: 860 * val / mx
    g, y = "", 0
    for title, d, col, light, item in (("Canadian-made goods sold to Türkiye", A, CA, CA_LIGHT, f"Lentils pay {V['lentil_duty_pct']:.1f}%"),
                                       ("Turkish goods sold to Canada", B, TR, "#ffe2a6", f"Clothing pays about {V['clothing_duty_rate']:.0f}%")):
        w = X(d["base"])
        wf = w * d["free_pct"] / 100
        g += halo(0, y + 24, f"{title}: {bn(d['base'])}", 23, weight=800, fill=col)
        g += f'<rect x="0" y="{y + 38}" width="{wf - 2:.1f}" height="46" fill="{light}" opacity="0.55"/>'
        g += f'<rect x="{wf:.1f}" y="{y + 38}" width="{w - wf:.1f}" height="46" fill="{col}"/>'
        g += halo(0, y + 114, f"{d['free_pct']:.0f}% duty-free", 22, fill=MUTED, weight=700)
        g += halo(230, y + 114, f"{100 - d['free_pct']:.0f}% pays duty", 22, fill=col, weight=800)
        g += halo(0, y + 154, f"Estimated duty: {mn(d['duty'])}, {d['rate']:.1f}% on average", 23, weight=800)
        y += 196
    return svg(W, y - 20, g)


# ------------------------------------------------------------------ 5. province map
def v_provinces():
    topo = json.load(open(os.path.join(HERE, "data", "base.json")))
    from pyproj import Transformer
    tf = Transformer.from_crs(4326, 3978, always_xy=True)
    sx, sy = topo["transform"]["scale"]; tx, ty = topo["transform"]["translate"]
    arcs = []
    for arc in topo["arcs"]:
        x = y = 0; pts = []
        for dx, dy in arc:
            x += dx; y += dy; pts.append((x * sx + tx, y * sy + ty))
        arcs.append(pts)

    def ring(idx):
        out = []
        for i in idx:
            a_ = arcs[i] if i >= 0 else list(reversed(arcs[~i]))
            out.extend(a_ if not out else a_[1:])
        return out
    geoms = topo["objects"]["provs"]["geometries"]
    prov_pts = [p for g_ in geoms if g_["properties"]["p"] not in ("YT", "NT", "NU")
                for poly in ([g_["arcs"]] if g_["type"] == "Polygon" else g_["arcs"]) for r in poly for p in ring(r)]
    minx, maxx = min(p[0] for p in prov_pts), max(p[0] for p in prov_pts)
    miny, maxy = min(p[1] for p in prov_pts), max(p[1] for p in prov_pts)
    W = 880; TOP = 150
    sc = W / (maxx - minx); H = (maxy - miny) * sc + TOP
    P = {"QC": "Quebec", "ON": "Ontario", "SK": "Saskatchewan", "BC": "British Columbia", "AB": "Alberta", "MB": "Manitoba",
         "NL": "Newfoundland and Labrador", "NS": "Nova Scotia", "NB": "New Brunswick", "PE": "Prince Edward Island"}
    val = {d["name"]: d for d in V["provinces"]}
    mx = max(d["value"] for d in V["provinces"])

    def fill(code):
        d = val.get(P.get(code, ""))
        if not d or d["value"] <= 0:
            return "rgba(255,255,255,0.08)"
        t = (d["value"] / mx) ** 0.6
        return f"rgba(100,196,238,{0.10 + 0.85 * t:.2f})"
    g = f'<clipPath id="mapclip"><rect x="0" y="0" width="{W}" height="{H:.0f}"/></clipPath><g clip-path="url(#mapclip)">'
    for geo in geoms:
        polys = [geo["arcs"]] if geo["type"] == "Polygon" else geo["arcs"]
        dd = ""
        for poly in polys:
            for r in poly:
                pts = ring(r)
                if len(pts) < 3:
                    continue
                dd += "M" + "L".join(f"{(x - minx) * sc:.1f},{(maxy - y) * sc + TOP:.1f}" for x, y in pts[::2] + [pts[-1]]) + "Z"
        g += f'<path d="{dd}" fill="{fill(geo["properties"]["p"])}" stroke="rgba(255,255,255,0.45)" stroke-width="1"/>'
    g += "</g>"

    def xy(lon, lat):
        x, y = tf.transform(lon, lat)
        return (x - minx) * sc, (maxy - y) * sc + TOP

    def block(name, x, y, anchor="start"):
        d = val[name]
        short = {"British Columbia": "B.C."}.get(name, name)
        out = halo(x, y, f"{short} {mshort(d['value'])}", 22, anchor=anchor, weight=800)
        for k, (prod, pv) in enumerate(V["province_products"][name]):
            out += halo(x, y + 25 + 23 * k, f"{prod} {mshort(pv)}", 19, fill=CA_LIGHT, anchor=anchor, weight=600)
        return out
    def lead(lon, lat, x2, y2):
        px, py = xy(lon, lat)
        return (f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{CA_LIGHT}" stroke-width="1.5" opacity="0.8"/>'
                f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="{CA_LIGHT}"/>')
    # western provinces: labels above the map with leader lines
    for name, lon, lat, lx in (("British Columbia", -123.5, 56.0, 0), ("Alberta", -114.5, 56.5, 255), ("Saskatchewan", -105.8, 55.5, 520)):
        g += lead(lon, lat, lx + 40, TOP - 34)
        g += '<g class="lblock">' + block(name, lx, 26) + '</g>'
    # Quebec: label inside northern Quebec
    qx, qy = xy(-73.5, 54.2)
    g += '<g class="lblock">' + block("Quebec", qx, qy - 30, anchor="middle") + '</g>'
    # Ontario: label in the open space south-west of the province, with a leader line
    g += lead(-86.5, 50.5, 196, H - 93)
    g += '<g class="lblock">' + block("Ontario", 20, H - 86) + '</g>'
    return svg(W, H, g)


# ------------------------------------------------------------------ 6. trips
def v_trips():
    yrs, ser = V["ca_arrivals_years"], V["ca_arrivals"]
    W, H, L, R, T, B = 900, 320, 92, 860, 30, 270
    ymax = 350000
    X = lambda i: L + (R - L) * i / (len(yrs) - 1)
    Y = lambda val: B - (B - T) * val / ymax
    g = ""
    for gv in (100000, 200000, 300000):
        g += f'<line x1="{L}" x2="{R}" y1="{Y(gv):.1f}" y2="{Y(gv):.1f}" stroke="{GRID}" stroke-width="1.5"/>'
        g += halo(L - 12, Y(gv) + 8, f"{gv // 1000}k", 22, fill=MUTED, anchor="end", weight=600)
    pts = " ".join(f"{X(i):.1f},{Y(val):.1f}" for i, val in enumerate(ser))
    g += f'<polygon points="{X(0):.1f},{B} {pts} {X(len(yrs) - 1):.1f},{B}" fill="{CA}" opacity="0.28"/>'
    g += f'<polyline points="{pts}" fill="none" stroke="{CA}" stroke-width="6" stroke-linejoin="round"/>'
    g += f'<line x1="{L}" x2="{R}" y1="{B}" y2="{B}" stroke="{GRID}" stroke-width="2"/>'
    for yy in (2010, 2015, 2020, 2025):
        g += halo(X(yrs.index(yy)), B + 34, str(yy), 22, fill=MUTED, anchor="middle", weight=600)
    for yy, dy in ((2019, -18), (2025, -18)):
        i = yrs.index(yy)
        g += f'<circle cx="{X(i):.1f}" cy="{Y(ser[i]):.1f}" r="7" fill="{CA}"/>'
        g += halo(X(i) - (60 if yy == 2025 else 0), Y(ser[i]) + dy, f"{ser[i]:,} in {yy}", 21, anchor="middle")
    return svg(W, H, g)


# ------------------------------------------------------------------ 7. energy plans
def v_energy():
    W, BW = 900, 860
    g = ""
    # wind and solar, bar = 2035 goal
    gw, goal = V["tr_wind_solar_gw_dec2025"], V["tr_wind_solar_goal_2035_gw"]
    g += halo(0, 26, "Wind and solar power", 24, weight=800)
    g += f'<rect x="0" y="40" width="{BW}" height="44" fill="none" stroke="{CA_LIGHT}" stroke-width="2" stroke-dasharray="7 6"/>'
    g += f'<rect x="0" y="40" width="{BW * gw / goal:.1f}" height="44" fill="{CA}"/>'
    g += halo(0, 114, f"{gw:.0f} GW in December 2025", 21, fill=CA, weight=800)
    g += halo(BW, 114, f"Goal: {goal:.0f} GW by 2035", 21, fill=CA_LIGHT, anchor="end", weight=700)
    # nuclear, bar = 2050 goal
    y0 = 168
    n35, n50, ak = V["tr_nuclear_goal_2035_gw"], V["tr_nuclear_goal_2050_gw"], V["akkuyu_gw"]
    g += halo(0, y0 + 26, "Nuclear power", 24, weight=800)
    g += f'<rect x="0" y="{y0 + 40}" width="{BW}" height="44" fill="none" stroke="{CA_LIGHT}" stroke-width="2" stroke-dasharray="7 6"/>'
    g += f'<rect x="0" y="{y0 + 40}" width="{BW * ak / n50:.1f}" height="44" fill="{TR}" opacity="0.9"/>'
    x35 = BW * n35 / n50
    g += f'<line x1="{x35:.1f}" x2="{x35:.1f}" y1="{y0 + 34}" y2="{y0 + 90}" stroke="{TEXT}" stroke-width="3"/>'
    g += halo(x35 + 10, y0 + 26, f"Goal: {n35:.1f} GW by 2035", 21, fill=TEXT, weight=800)
    g += halo(0, y0 + 114, f"{ak:.1f} GW being built by Russia's Rosatom", 21, fill=TR, weight=800)
    g += halo(BW, y0 + 114, "Goal for 2050", 21, fill=CA_LIGHT, anchor="end", weight=700)
    return svg(W, y0 + 124, g)


# ------------------------------------------------------------------ 8. defence timeline
def ym(s):
    if "-" not in s:
        return int(s) + 0.5
    a, b = s.split("-")
    return int(a) + (int(b) - 1) / 12


def v_defence():
    yrs, vals = V["military_years"], V["military_m"]
    W = 900
    t0, t1 = 2010.0, 2027.0
    X = lambda t: 10 + 870 * (t - t0) / (t1 - t0)
    T, B = 34, 140
    ymax = 160
    Y = lambda val: B - (B - T) * val / ymax
    g = ""
    pts = " ".join(f"{X(y + 0.5):.1f},{Y(v_):.1f}" for y, v_ in zip(yrs, vals))
    g += f'<polygon points="{X(yrs[0] + 0.5):.1f},{B} {pts} {X(yrs[-1] + 0.5):.1f},{B}" fill="{CA}" opacity="0.30"/>'
    g += f'<polyline points="{pts}" fill="none" stroke="{CA}" stroke-width="5" stroke-linejoin="round"/>'
    for yy in (2019, 2024):
        i = yrs.index(yy)
        g += halo(X(yy + 0.5), Y(vals[i]) - 12, f"{mshort(vals[i] * 1e6)} in {yy}", 21, anchor="middle")
    ms = V["defence_milestones"]
    p1, p2 = ym(ms[0][0]), ym(ms[2][0])
    by = 176
    p15 = ym(ms[1][0])
    for a, b, col, lab, tx in ((t0, p1, "rgba(100,196,238,0.45)", "Open", t0), (p1, p2, "rgba(255,193,77,0.80)", "Suspended", p15),
                               (p2, t1, CA, "Reopened", p2)):
        g += f'<rect x="{X(a):.1f}" y="{by}" width="{X(b) - X(a) - 2:.1f}" height="36" fill="{col}"/>'
        g += f'<text x="{X(tx) + 8:.1f}" y="{by + 25}" font-size="19" font-weight="800" fill="#0c1016" font-family=\'{FONT}\'>{esc(lab)}</text>'
    for yy in (2010, 2015, 2020, 2025):
        g += halo(X(yy), by + 62, str(yy), 20, fill=MUTED, anchor="start" if yy == 2010 else "middle", weight=600)
    nudge = {}
    for k in range(1, len(ms)):
        if X(ym(ms[k][0])) - X(ym(ms[k - 1][0])) < 30:
            nudge[k - 1] = nudge.get(k - 1, 0) - 15; nudge[k] = nudge.get(k, 0) + 15
    for k, (d, txt) in enumerate(ms, 1):
        x = X(ym(d)) + nudge.get(k - 1, 0)
        xt = X(ym(d))
        g += f'<line x1="{xt:.1f}" x2="{xt:.1f}" y1="{by - 3}" y2="{by + 7}" stroke="{TEXT}" stroke-width="2"/>'
        g += f'<circle cx="{x:.1f}" cy="{by - 16:.1f}" r="13" fill="#0c1016" stroke="{TEXT}" stroke-width="2"/>'
        g += f'<text x="{x:.1f}" y="{by - 10:.1f}" font-size="17" font-weight="800" fill="{TEXT}" text-anchor="middle" font-family=\'{FONT}\'>{k}</text>'
    return svg(W, by + 74, g)


def defence_legend():
    out = '<div class="legend">'
    for k, (d, txt) in enumerate(V["defence_milestones"], 1):
        if "-" in d:
            y, m = d.split("-")
            when = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][int(m) - 1] + " " + y
        else:
            when = d
        out += f'<div class="li"><span class="ln">{k}</span><span><b>{when}.</b> {esc(txt)}</span></div>'
    return out + "</div>"


# ------------------------------------------------------------------ 9. what comes next
def v_timeline():
    items = [(V["air_transat_montreal_istanbul_start"], "Air Transat starts flights from Montréal to Istanbul"),
             (V["cop31_dates"], "Türkiye hosts COP31, the UN climate conference, in Antalya"),
             (V["trade_mission_2027"], "Canadian trade mission to Türkiye, led by the trade minister"),
             (V["erdogan_visit"], "President Erdoğan visits Canada")]
    out = '<div class="tl">'
    for d, t in items:
        out += f'<div class="ti"><div class="td">{esc(d)}</div><div class="tt">{esc(t)}</div></div>'
    return out + "</div>"


# ------------------------------------------------------------------ slides
def build():
    S = []
    S.append(dict(kicker="The Median Canadian · Week 2",
                  head="Talking trade with Türkiye",
                  body='<p class="lead">A Canadian PM\'s first bilateral visit brought agreements on flights, energy and defence.</p>'
                       '<p class="body">Here is what they mean for Canadians.</p>',
                  source="PMO; StatCan; Global Affairs Canada; CBSA; Türkiye ministries · 2010 to 2026 · Oct 2026 · Charts CC BY 4.0", cover=True))
    S.append(dict(kicker="The opportunity",
                  head="Türkiye is a big market where Canada sells little",
                  body=f'<p class="lead">Türkiye imported US${V["tr_imports_world_usd"] / 1e9:.0f} billion of goods in 2025, and {V["ca_share_of_tr_imports_pct"]:.1f}% came from Canada.</p>'
                       f'<div class="card"><div class="note">What Türkiye\'s {V["tr_population"] / 1e6:.0f} million people bought from the world, and the part from Canada, US dollars</div>'
                       f'<div class="chart">{v_tr_buys()}</div>'
                       f'<p class="foot">Canada sold {V["us_share_pct"]:.0f}% of its goods to the United States in 2025. Canada\'s government wants to double sales to other countries within a decade.</p></div>',
                  source="UN Comtrade, as reported by Türkiye · 2025; Statistics Canada; TurkStat · Charts CC BY 4.0"))
    drop = (1 - V["deficit_ytd_2026"] / V["deficit_ytd_2025"]) * 100
    S.append(dict(kicker="Trade deficit",
                  head="Canada buys more from Türkiye than it sells",
                  body=f'<p class="lead">The trade deficit was {bn(V["deficit_2025"])} in 2025. It shrank by {"almost a quarter" if 20 <= drop < 25 else str(round(drop)) + "%"} from January to August 2026.</p>'
                       f'<div class="card"><div class="note">Goods trade with Türkiye, 2025</div>{v_goods_receipts()}'
                       f'<p class="foot">January to August 2026: Canada sold {V["ytd_exports_change_pct"]:.0f}% more to Türkiye and bought {abs(V["ytd_imports_change_pct"]):.0f}% less than a year earlier.</p></div>',
                  source="Statistics Canada, international merchandise trade · 2025 and January to August 2026 · Charts CC BY 4.0"))
    A, B = V["duty_ca_goods"], V["duty_tr_goods"]
    S.append(dict(kicker="Duties",
                  head="A trade deal could help farmers and shoppers",
                  body=f'<p class="lead">Türkiye charges {V["lentil_duty_pct"]:.1f}% on Canadian lentils, and Canada about {V["clothing_duty_rate"]:.0f}% on Turkish clothing.</p>'
                       f'<div class="card"><div class="chart">{v_duties()}</div>'
                       '<p class="foot">Lower duties could also bring Canadian clothing makers more competition.<br>Estimates leave out durum wheat, which can enter Türkiye duty-free when used to make exports.</p></div>',
                  source="CBSA customs tariff 2026; Türkiye Ministry of Trade tariff 2026; Statistics Canada · 2025 · Charts CC BY 4.0"))
    S.append(dict(kicker="Who sells",
                  head="Three provinces have the most at stake",
                  body=f'<p class="lead">Quebec, Ontario and Saskatchewan make {"three-quarters" if 73 <= V["top3_share_pct"] <= 78 else str(round(V["top3_share_pct"])) + "%"} of Canada\'s sales to Türkiye.</p>'
                       f'<div class="card"><div class="note">Sales to Türkiye by province and top products, 2025. Brighter means more.</div>'
                       f'<div class="chart">{v_provinces()}</div>'
                       f'<p class="foot">Saskatchewan\'s lentil sales to Türkiye fell by {"almost two-thirds" if 60 <= V["sk_lentil_drop_pct"] < 66.7 else str(round(V["sk_lentil_drop_pct"])) + "%"} from 2022 to 2025.</p></div>',
                  source="Statistics Canada, domestic exports by province of origin · 2022 to 2025 · Charts CC BY 4.0"))
    S.append(dict(kicker="Travel",
                  head="Canadians get more choice of flights",
                  body=f'<p class="lead">Istanbul is a global hub: Turkish Airlines flew to {V["tk_countries"]} countries in 2024, more than any other airline.</p>'
                       f'<div class="card"><div class="note">The new agreement allows up to {V["flights_new_per_week"]} flights a week for each country, up from {V["flights_old_per_week"]}, '
                       f'to any city. Trips to Türkiye by Canadians each year:</div>'
                       f'<div class="chart">{v_trips()}</div>'
                       '<p class="foot">In 2025, Air Canada and Air Transat opposed extra Turkish Airlines flights; '
                       'WestJet and the Toronto and Montréal airports supported them.</p></div>',
                  source="Türkiye tourism ministry; PMO; Canadian Transportation Agency; Guinness · Charts CC BY 4.0"))
    S.append(dict(kicker="Energy",
                  head="Türkiye's nuclear plans open a door for Canada",
                  body=f'<p class="lead">Türkiye aims for over {V["tr_nuclear_goal_2050_gw"]} gigawatts of nuclear power by 2050 and is studying Canada\'s CANDU reactors.</p>'
                       f'<div class="card"><div class="note">Türkiye\'s power goals, gigawatts</div><div class="chart">{v_energy()}</div>'
                       f'<p class="foot">In 2024, Canada produced about a quarter of the world\'s uranium. The energy statement the two countries signed in October 2026 has no commitments to buy or sell.</p></div>',
                  source="Türkiye Ministry of Energy; EPİAŞ; NRCan; AtkinsRéalis · 2023 to 2026 · Charts CC BY 4.0"))
    S.append(dict(kicker="Defence",
                  head="Military sales to Türkiye are back, with conditions",
                  body='<p class="lead">Canada\'s government says linking the two defence industries will create jobs and exports.</p>'
                       '<div class="card"><div class="note">Türkiye has NATO\'s second-largest military. '
                       'Canadian military exports to Türkiye each year, mostly imaging and targeting equipment:</div>'
                       f'<div class="chart">{v_defence()}</div>{defence_legend()}'
                       '<p class="foot">The Armenian National Committee of Canada asks that Canada keep full control of export permits in a trade deal. '
                       'Canada can cancel permits if goods are misused.</p></div>',
                  source="Global Affairs Canada, Reports on Exports of Military Goods · 2010 to 2025; DND; PMO · Charts CC BY 4.0"))
    S.append(dict(kicker="What comes next",
                  head=f"Free trade talks start in Ankara on {V['fta_round_month']}",
                  body='<p class="lead">A deal could lower duties in both countries. Once its terms are public, we will break them down in a new post.</p>'
                       f'<div class="card">{v_timeline()}</div>'
                       '<div class="explore"><div class="ex1">Explore the full story and the data</div>'
                       '<div class="ex2">Link in bio · sjvadrevu.github.io/the-median-canadian</div></div>',
                  source="Sources, methods and code on the website · Charts CC BY 4.0"))
    return S


CSS = f"""
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ background:#0c1016; font-family:{FONT}; color:{TEXT}; }}
.slide {{ position:relative; width:1080px; height:1350px; overflow:hidden; background:#0c1016; }}
.photo {{ position:absolute; inset:0; background-size:cover; background-repeat:no-repeat; }}
.shade {{ position:absolute; inset:0; background:linear-gradient(180deg, rgba(8,11,16,0.66) 0%, rgba(8,11,16,0.46) 30%, rgba(8,11,16,0.34) 55%, rgba(8,11,16,0.62) 100%); }}
.cover .shade {{ background:linear-gradient(180deg, rgba(8,11,16,0.55) 0%, rgba(8,11,16,0.30) 14%, rgba(8,11,16,0.45) 30%, rgba(8,11,16,0.66) 62%, rgba(8,11,16,0.70) 100%); }}
.content {{ position:absolute; top:86px; left:76px; right:76px; }}
.kicker {{ font-size:27px; font-weight:700; text-transform:uppercase; letter-spacing:0.09em; color:#ffd2c7; text-shadow:0 2px 10px rgba(0,0,0,0.8); }}
h1 {{ font-size:74px; font-weight:800; line-height:1.07; letter-spacing:-0.022em; margin-top:18px; text-shadow:0 3px 18px rgba(0,0,0,0.85), 0 1px 3px rgba(0,0,0,0.9); }}
h1.long {{ font-size:60px; }}
h1.longer {{ font-size:54px; }}
.cover .content {{ top:520px; }}
.cover h1 {{ font-size:120px; margin-top:20px; }}
.lead {{ font-size:34px; font-weight:600; line-height:1.3; margin-top:20px; text-shadow:0 2px 12px rgba(0,0,0,0.9); }}
.cover .lead {{ font-size:44px; font-weight:600; line-height:1.25; margin-top:30px; }}
.cover .body {{ font-size:32px; margin-top:22px; }}
.body {{ font-size:32px; line-height:1.4; margin-top:20px; color:#f2f4f7; text-shadow:0 2px 12px rgba(0,0,0,0.9); }}
.card {{ margin:26px -30px 0; padding:22px 30px 24px; background:rgba(10,13,19,0.82); border-radius:26px; }}
.note {{ font-size:23px; color:{MUTED}; line-height:1.3; margin-bottom:8px; }}
.chart {{ line-height:0; }}
.foot {{ font-size:20px; color:{MUTED}; margin-top:14px; line-height:1.35; }}
.rcs {{ display:flex; gap:24px; margin-top:12px; }}
.rc {{ flex:1; background:rgba(255,255,255,0.06); border-radius:16px; padding:16px 20px; border-top:4px dashed rgba(255,255,255,0.35); }}
.rct {{ font-size:25px; font-weight:800; margin-bottom:6px; }}
.rr {{ display:flex; justify-content:space-between; gap:10px; font-size:23px; line-height:1.22; padding:8px 0; border-bottom:1.5px dotted rgba(255,255,255,0.25); }}
.rr b {{ font-weight:800; white-space:nowrap; }}
.rr.tot {{ border-bottom:none; border-top:3px solid rgba(255,255,255,0.5); margin-top:6px; font-size:25px; font-weight:800; }}
.legend {{ margin-top:6px; display:flex; flex-direction:column; gap:9px; }}
.li {{ display:flex; gap:14px; font-size:21px; line-height:1.3; }}
.ln {{ flex:0 0 28px; height:28px; border-radius:14px; border:2px solid #fff; text-align:center; font-size:17px; font-weight:800; line-height:24px; }}
.tl {{ display:flex; flex-direction:column; gap:18px; }}
.ti {{ display:flex; gap:24px; align-items:baseline; }}
.td {{ flex:0 0 250px; font-size:27px; font-weight:800; color:{TR}; }}
.tt {{ font-size:28px; line-height:1.3; }}
.explore {{ margin-top:26px; border:3px solid rgba(255,255,255,0.35); border-radius:22px; padding:24px 30px; background:rgba(10,13,19,0.55); }}
.ex1 {{ font-size:38px; font-weight:800; }}
.ex2 {{ font-size:27px; color:{MUTED}; margin-top:10px; }}
.footer-logo {{ position:absolute; left:76px; bottom:64px; height:78px; filter:drop-shadow(0 2px 8px rgba(0,0,0,0.7)); }}
.pagenum {{ position:absolute; right:76px; bottom:64px; height:78px; line-height:78px; font-size:27px; font-weight:700; text-shadow:0 2px 8px rgba(0,0,0,0.8); }}
.source {{ position:absolute; left:76px; right:76px; bottom:24px; font-size:18px; color:#d5dae1; white-space:nowrap; overflow:hidden; text-shadow:0 1px 6px rgba(0,0,0,0.9); }}
.credit {{ position:absolute; top:22px; right:30px; font-size:15px; color:rgba(255,255,255,0.85); text-shadow:0 1px 5px rgba(0,0,0,0.9); }}
"""


def credit(key):
    d = PH[key]
    lic = d["licence"].replace("Public Domain Mark (Flickr PDM)", "public domain")
    return f"Photo: {d['author']}, {lic}"


def section(i, s, photo_key):
    cls = "slide cover" if s.get("cover") else "slide"
    sid = f"s{photo_key}"
    return (f'<section class="{cls}" id="{sid}"><div class="photo" style="background-image:url(\'photos/s{photo_key}.jpg\');background-position:{POS[photo_key]}"></div>'
            f'<div class="shade"></div><div class="content"><div class="kicker">{esc(s["kicker"])}</div><h1>{esc(s["head"])}</h1>{s["body"]}</div>'
            f'<img class="footer-logo" src="logo-dark.png" alt="The Median Canadian">'
            f'<div class="pagenum">{"Swipe to learn more →" if i == 1 else f"{i}/{N}"}</div>'
            f'<div class="source">{esc(s["source"])}</div><div class="credit">{esc(credit(photo_key))}</div></section>')


def page(S):
    out = [f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>Canada and Türkiye</title><style>{CSS}</style></head><body>"]
    for i, s in enumerate(S, 1):
        out.append(section(i, s, str(i)))
    if ALT_COVER_HEAD:
        alt = dict(S[0], head=ALT_COVER_HEAD, body=ALT_COVER_BODY or S[0]["body"])
        out.append(section(1, alt, "1").replace('id="s1"', 'id="s1alt"', 1))
    out.append("</body></html>")
    return "".join(out)


MEASURE = """(id) => { const s=document.getElementById(id), T=s.getBoundingClientRect().top, Lx=s.getBoundingClientRect().left;
 let bottom=0,right=0; for (const e of s.querySelector('.content').querySelectorAll('*')) { const r=e.getBoundingClientRect();
 if(!r.width&&!r.height) continue; bottom=Math.max(bottom,r.bottom-T); right=Math.max(right,r.right-Lx);}
 const logo=s.querySelector('.footer-logo'), src=s.querySelector('.source'), h=s.querySelector('h1');
 return {bottom,right,logoTop:logo.getBoundingClientRect().top-T, logoOk:logo.complete&&logo.naturalWidth>0,
  srcOne:src.scrollWidth<=src.clientWidth+1, lines:Math.round(h.getBoundingClientRect().height/parseFloat(getComputedStyle(h).lineHeight)),
  clash:(()=>{const ts=[...s.querySelectorAll('svg text')].filter(t=>t.getAttribute('fill')!=='none');
    const bx=ts.map(t=>({r:t.getBoundingClientRect(), g:t.closest('g.lblock'), s:t.textContent})); const out=[];
    for(let i=0;i<bx.length;i++) for(let j=i+1;j<bx.length;j++){ const a=bx[i], b=bx[j]; if(a.g && a.g===b.g) continue;
      const m=(a.g && b.g)?24:6, A=a.r, B=b.r;
      if(A.left<B.right+m && B.left<A.right+m && A.top<B.bottom+m && B.top<A.bottom+m) out.push(a.s+' | '+b.s); }
    return out;})(),
  leadLines:(()=>{const l=s.querySelector('.lead'); return l?Math.round(l.getBoundingClientRect().height/parseFloat(getComputedStyle(l).lineHeight)):0})(),
  size:getComputedStyle(h).fontSize}; }"""

BANNED = [r"\bnow\b", r"\btoday\b", r"\bcurrently\b", "—", r"\bwon\b", r"\blost\b", r"\bour (analysis|estimate|count)\b", r", not "]


def main():
    S = build()
    text = page(S)
    open(os.path.join(HERE, "slides.html"), "w").write(text)
    vis = re.sub(r"<script.*?</script>|<style.*?</style>|<[^>]+>", " ", text, flags=re.S)
    warn = []
    for pat in BANNED:
        for m in re.finditer(pat, vis, re.I):
            warn.append(f"banned {pat}: ...{vis[max(0, m.start() - 40):m.end() + 40]}...")
    os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    from playwright.sync_api import sync_playwright
    from PIL import Image
    ok = True
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        pg.goto("file://" + os.path.join(HERE, "slides.html"))
        pg.wait_for_load_state("networkidle")
        for sid in [f"s{i}" for i in range(1, N + 1)] + (["s1alt"] if ALT_COVER_HEAD else []):
            m = pg.evaluate(MEASURE, sid)
            gap = m["logoTop"] - m["bottom"]
            iss = []
            if gap < 18: iss.append(f"gap {gap:.0f}px to footer")
            if m["right"] > 1080 - 40: iss.append(f"right edge {m['right']:.0f}")
            if not m["srcOne"]: iss.append("source line wraps")
            if not m["logoOk"]: iss.append("logo missing")
            if m["lines"] > 2: iss.append(f"headline runs {m['lines']} lines (style guide: one or two)")
            if m["leadLines"] > 2: iss.append(f"line under the headline runs {m['leadLines']} lines")
            if m["clash"]: iss.append("labels too close: " + "; ".join(m["clash"][:4]))
            ok &= not iss
            print(f"{sid}: bottom {m['bottom']:.0f}, footer {m['logoTop']:.0f}, gap {gap:.0f}, heading {m['lines']} lines {m['size']}, line {m['leadLines']}", "!! " + "; ".join(iss) if iss else "ok")
            name = f"the-median-canadian-canada-turkiye-{sid[1:]}-of-{N}" if sid != "s1alt" else "cover-option-b"
            f = os.path.join(OUTDIR, name + ".png")
            pg.locator(f"#{sid}").screenshot(path=f)
            Image.open(f).convert("RGB").save(f[:-4] + ".jpg", quality=92)
        b.close()
    ims = [Image.open(os.path.join(OUTDIR, f"the-median-canadian-canada-turkiye-{i}-of-{N}.jpg")) for i in range(1, N + 1)]
    tw, th = 360, 450
    sheet = Image.new("RGB", (tw * 3 + 40, th * 3 + 40), "white")
    for k, im in enumerate(ims):
        sheet.paste(im.resize((tw, th)), (10 + (k % 3) * (tw + 10), 10 + (k // 3) * (th + 10)))
    sheet.save(os.path.join(OUTDIR, "contact-sheet.jpg"), quality=90)
    if ALT_COVER_HEAD:
        a = Image.open(os.path.join(OUTDIR, f"the-median-canadian-canada-turkiye-1-of-{N}.jpg"))
        bb = Image.open(os.path.join(OUTDIR, "cover-option-b.jpg"))
        pair = Image.new("RGB", (1080 * 2 + 30, 1350), "white")
        pair.paste(a, (0, 0)); pair.paste(bb, (1110, 0))
        pair.resize((1095, 675)).save(os.path.join(OUTDIR, "cover-options.jpg"), quality=90)
    for w in warn:
        print("WARNING", w)
    sys.exit(0 if ok and not warn else 1)


if __name__ == "__main__":
    main()
