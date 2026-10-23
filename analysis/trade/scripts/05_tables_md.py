"""Render markdown tables from output CSV/JSON for results.md (values in C$ millions, 1 decimal).
Usage: python3 -I 05_tables_md.py OUT > OUT/tables.md
"""
import sys, csv, json, os
OUT = sys.argv[1]
m = lambda v: "%.1f" % (float(v) / 1e6)

print("### T1 Annual totals (C$ millions, customs basis)\n")
print("| Year | Exports | of which re-exports | Imports | Two-way | Balance | Imports/exports |")
print("|---|---|---|---|---|---|---|")
for r in csv.DictReader(open(os.path.join(OUT, "annual_totals_1988_2026ytd.csv"))):
    if int(r["year"]) < 1990:
        continue
    lab = r["year"] if r["period"] == "Jan-Dec" else "%s (%s)" % (r["year"], r["period"])
    print("| %s | %s | %s | %s | %s | %s | %.2f |" % (lab, m(r["total_exports"]), m(r["re_exports"]), m(r["imports"]),
                                                    m(r["two_way"]), m(r["balance"]), float(r["import_to_export_ratio"])))

rows = list(csv.DictReader(open(os.path.join(OUT, "hs2_chapters_2021_2025.csv"))))
for flow in ("exports", "imports"):
    tot = {y: sum(float(r["%s_%d" % (flow, y)]) for r in rows) for y in (2024, 2025)}
    print("\n### T2-%s Top 10 HS chapters, %s, 2025 (with 2024)\n" % (flow, flow))
    print("| HS2 | Chapter | 2025 | Share 2025 | 2024 |")
    print("|---|---|---|---|---|")
    for r in sorted(rows, key=lambda r: -float(r["%s_2025" % flow]))[:10]:
        d = r["description"].split(" - ", 1)[-1]
        d = (d[:48] + "...") if len(d) > 50 else d
        print("| %s | %s | %s | %.1f%% | %s |" % (r["hs2"], d, m(r["%s_2025" % flow]),
                                              100 * float(r["%s_2025" % flow]) / tot[2025], m(r["%s_2024" % flow])))

top = list(csv.DictReader(open(os.path.join(OUT, "top15_hs6_2024_2025.csv"))))
for flow in ("total_exports", "imports"):
    for y in ("2025", "2024"):
        print("\n### T3 Top 15 HS6, %s, %s\n" % (flow.replace("_", " "), y))
        print("| # | HS6 | Product | C$ M | Share |")
        print("|---|---|---|---|---|")
        for r in top:
            if r["flow"] == flow and r["year"] == y:
                d = r["description"]
                d = (d[:55] + "...") if len(d) > 57 else d
                print("| %s | %s | %s | %s | %.1f%% |" % (r["rank"], r["hs6"], d, m(r["value"]), 100 * float(r["share"])))

print("\n### T4 Provinces (C$ millions)\n")
print("| Province | Dom. exports 2025 | Avg 2021-25 | Imports 2025 (clearance) | Avg 2021-25 |")
print("|---|---|---|---|---|")
for r in csv.DictReader(open(os.path.join(OUT, "provinces_2021_2025.csv"))):
    print("| %s | %s | %s | %s | %s |" % (r["geo"], m(r["domestic_exports_2025"]), m(r["domestic_exports_avg_2021_2025"]),
                                          m(r["imports_clearance_2025"]), m(r["imports_clearance_avg_2021_2025"])))

print("\n### T5 Top 3 HS6 per province, 2025 (C$ millions; 5-yr avg in brackets)\n")
print("| Province | Flow | Products |")
print("|---|---|---|")
pt = list(csv.DictReader(open(os.path.join(OUT, "province_top_hs6.csv"))))
for prov in dict.fromkeys(r["province"] for r in pt):
    for flow in ("domestic_exports", "imports_clearance"):
        items = [r for r in pt if r["province"] == prov and r["flow"] == flow and int(r["rank_2025"]) <= 3]
        if items:
            s = "; ".join("%s %s %s (%s)" % (r["hs6"], r["description"].split(";")[0][:28] if not r["description"].startswith(("Vegetables", "Cereals", "Fruit", "Iron", "Machinery", "Vehicles", "Aeroplanes", "Turb", "Coal", "Blood", "Medicaments", "Wood", "Engines", "Plastics", "Food", "Aluminium", "Carbonates", "Oxides", "Borates", "Fertilizers", "Nuts", "Juice", "Insulated", "Boards", "Electrical", "Refrigerat", "Motorboats", "Fishing", "Ferrous", "Newsprint", "Optical", "Surveying", "Boring", "Instruments", "Tractors", "Carpets")) else r["description"][:28], m(r["value_2025"]), m(r["avg_2021_2025"]))
                          for r in items)
            print("| %s | %s | %s |" % (prov, "Exports" if flow.startswith("dom") else "Imports", s))
