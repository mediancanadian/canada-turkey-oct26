"use strict";
const D = JSON.parse(document.getElementById("data").textContent);
const $ = s => document.querySelector(s);
const esc = s => String(s).replace(/[&<>"]/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]));
const nf = (v, d = 0) => Number(v).toLocaleString("en-CA", {minimumFractionDigits: d, maximumFractionDigits: d});
const pc = (x, d = 1) => nf(x, d) + "%";
const ord = n => { const s = ["th", "st", "nd", "rd"], v = n % 100; return n + (s[(v - 20) % 10] || s[v] || s[0]); };
function money(x, cur = "$") {
  const a = Math.abs(x);
  if (a >= 1e9) return cur + nf(x / 1e9, a >= 1e11 ? 0 : (a >= 1e10 ? 1 : 2)) + " billion";
  if (a >= 1e6) return cur + nf(x / 1e6, a >= 1e7 ? 0 : 1) + " million";
  if (a >= 1e4) return cur + nf(Math.round(x / 1e3) * 1e3);
  return cur + nf(x);
}
const share = (part, whole) => { const s = part / whole * 100; return s < 0.01 ? "less than 0.01%" : pc(s, s < 1 ? 2 : 1); };
function short(x, cur = "$") {
  const a = Math.abs(x);
  if (a >= 1e9) return cur + nf(x / 1e9, a >= 1e11 ? 0 : 1) + "B";
  if (a >= 1e6) return cur + nf(x / 1e6, a >= 1e7 ? 0 : 1) + "M";
  if (a >= 1e3) return cur + nf(x / 1e3) + "K";
  return cur + nf(x);
}
const usd = x => money(x, "US$");

// ------------------------------------------------------------------ helpers
const resizers = [];
let rT;
window.addEventListener("resize", () => { clearTimeout(rT); rT = setTimeout(() => resizers.forEach(f => f()), 120); });
function scale(v) {
  const p = Math.pow(10, Math.floor(Math.log10(v))), f = v / p;
  const [m, n] = [[1, 4], [1.5, 3], [2, 4], [2.5, 5], [3, 3], [4, 4], [5, 5], [6, 3], [8, 4], [10, 5]].find(([c]) => f <= c + 1e-9);
  return {max: m * p, n};
}
function ticks(max, n) { const out = []; for (let i = 0; i <= n; i++) out.push(max * i / n); return out; }
function seg(el, onChange) {
  const bs = [...el.querySelectorAll("button")];
  bs.forEach(b => {
    b.setAttribute("aria-selected", String(b.classList.contains("on")));
    b.addEventListener("click", () => {
      bs.forEach(x => { x.classList.toggle("on", x === b); x.setAttribute("aria-selected", String(x === b)); });
      onChange(b.dataset.k);
    });
  });
}
function mini(vals, labels, sel, cls = "") {
  const mx = Math.max(...vals) || 1;
  return `<div class="mini ${cls}">` + vals.map((v, i) => `<div class="${i === sel ? "last" : ""}"><i style="height:${Math.max(2, v / mx * 46).toFixed(1)}px"></i><span>${labels[i]}</span></div>`).join("") + "</div>";
}

// horizontal bars; items: {label, a, b (part shown over a), right, cls, me, gap}
function hbars(el, items, o = {}) {
  const max = o.max || Math.max(...items.filter(i => !i.gap).map(i => i.a)) || 1;
  el.innerHTML = items.map((it, i) => it.gap ? `<div class="hb gap">${esc(it.label)}</div>` :
    `<button type="button" class="hb${it.me ? " me" : ""}${o.onPick ? "" : " static"}" data-i="${i}" aria-pressed="false"${o.onPick ? "" : ' tabindex="-1"'}>` +
    `<span class="hl">${esc(it.label)}</span><span class="hv">${it.right}</span>` +
    `<span class="ht"><i class="${it.cls || "c"}${it.a > 0 ? " min" : ""}" style="width:${(it.a / max * 100).toFixed(2)}%"></i>` +
    (it.b != null ? `<i class="c${it.b > 0 ? " min" : ""}" style="width:${(it.b / max * 100).toFixed(2)}%"></i>` : "") + `</span></button>`).join("");
  if (!o.onPick) return;
  const bs = [...el.querySelectorAll("button.hb")];
  const pick = i => { bs.forEach(b => b.setAttribute("aria-pressed", String(+b.dataset.i === i))); o.onPick(items[i], i); };
  bs.forEach(b => b.addEventListener("click", () => pick(+b.dataset.i)));
  pick(o.sel != null ? o.sel : 0);
}

// line chart over years, drawn at the container's width; tap or drag to pick a year
function lineChart(el, o) {
  let sel = o.sel != null ? o.sel : o.x.length - 1;
  const n = o.x.length;
  function draw() {
    const W = Math.max(280, Math.round(el.clientWidth || 600)), H = o.h || 220, m = {l: o.ml || 44, r: 14, t: 14, b: 26};
    const all = o.series.flatMap(s => s.v.filter(v => v != null));
    const sc = o.ymax ? {max: o.ymax, n: 4} : scale(Math.max(...all)), ymax = sc.max, ymin = o.ymin || 0;
    const X = i => m.l + (W - m.l - m.r) * (i / (n - 1));
    const Y = v => m.t + (H - m.t - m.b) * (1 - (v - ymin) / (ymax - ymin));
    let s = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="${esc(o.aria)}">`;
    ticks(ymax - ymin, sc.n).forEach(t => { const v = ymin + t; s += `<line class="grid" x1="${m.l}" x2="${W - m.r}" y1="${Y(v).toFixed(1)}" y2="${Y(v).toFixed(1)}"/><text class="ax" x="${m.l - 6}" y="${(Y(v) + 4).toFixed(1)}" text-anchor="end">${o.tick(v)}</text>`; });
    const step = Math.max(1, Math.ceil(n / Math.max(3, Math.floor((W - m.l) / 62))));
    o.x.forEach((yr, i) => { if ((n - 1 - i) % step === 0) s += `<text class="ax" x="${X(i).toFixed(1)}" y="${H - 6}" text-anchor="middle">${yr}</text>`; });
    o.series.forEach(se => {
      const pts = se.v.map((v, i) => v == null ? null : [X(i), Y(v)]).filter(Boolean);
      const d = pts.map((p, j) => (j ? "L" : "M") + p[0].toFixed(1) + "," + p[1].toFixed(1)).join("");
      if (se.area) s += `<path class="ar-${se.cls}" d="${d}L${pts[pts.length - 1][0].toFixed(1)},${Y(ymin).toFixed(1)}L${pts[0][0].toFixed(1)},${Y(ymin).toFixed(1)}Z"/>`;
      s += `<path class="ln-${se.cls}" d="${d}"/>`;
    });
    s += `<line class="rule" x1="${X(sel).toFixed(1)}" x2="${X(sel).toFixed(1)}" y1="${m.t}" y2="${H - m.b}"/>`;
    o.series.forEach(se => { const v = se.v[sel]; if (v != null) s += `<circle class="dot-${se.cls}" cx="${X(sel).toFixed(1)}" cy="${Y(v).toFixed(1)}" r="5"/>`; });
    el.innerHTML = s + "</svg>";
    el._g = {m, W};
  }
  function at(clientX) {
    const r = el.getBoundingClientRect(), g = el._g;
    const i = Math.max(0, Math.min(n - 1, Math.round((clientX - r.left - g.m.l) / (g.W - g.m.l - g.m.r) * (n - 1))));
    if (i !== sel) { sel = i; draw(); o.onPick(i); }
  }
  el.tabIndex = 0;
  el.setAttribute("aria-label", o.aria + ". Use the left and right arrow keys to pick a year.");
  el.addEventListener("pointerdown", e => at(e.clientX));
  el.addEventListener("pointermove", e => { if (e.pointerType === "mouse" || e.buttons) at(e.clientX); });
  el.addEventListener("keydown", e => {
    if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
    e.preventDefault(); sel = Math.max(0, Math.min(n - 1, sel + (e.key === "ArrowRight" ? 1 : -1))); draw(); o.onPick(sel);
  });
  draw(); o.onPick(sel); resizers.push(draw);
}

// columns over years; optional status band and numbered markers under the columns
function columns(el, o) {
  let sel = o.sel != null ? o.sel : o.x.length - 1, mark = -1;
  const n = o.x.length;
  function draw() {
    const W = Math.max(280, Math.round(el.clientWidth || 600)), H = o.h || 210, m = {l: o.ml || 44, r: 8, t: 24, b: o.band ? 74 : 26};
    const sc = o.ymax ? {max: o.ymax, n: 4} : scale(Math.max(...o.v.filter(v => v != null))), ymax = sc.max;
    const bw = (W - m.l - m.r) / n, Y = v => m.t + (H - m.t - m.b) * (1 - v / ymax);
    const XY = yf => m.l + (yf - o.x[0]) * bw;    // a year with a fraction, for the band
    let s = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="${esc(o.aria)}">`;
    ticks(ymax, sc.n).forEach(t => s += `<line class="grid" x1="${m.l}" x2="${W - m.r}" y1="${Y(t).toFixed(1)}" y2="${Y(t).toFixed(1)}"/><text class="ax" x="${m.l - 6}" y="${(Y(t) + 4).toFixed(1)}" text-anchor="end">${o.tick(t)}</text>`);
    o.v.forEach((v, i) => {
      const x = m.l + i * bw;
      if (v != null) { const y = Y(v), h = Math.max(Y(0) - y, v > 0 ? 1.5 : 0); s += `<rect class="col ${o.cls || ""}${i === sel ? " sel" : ""}" x="${(x + bw * .16).toFixed(1)}" y="${(Y(0) - h).toFixed(1)}" width="${(bw * .68).toFixed(1)}" height="${h.toFixed(1)}" rx="2"/>`; }
      s += `<rect class="colhit" data-i="${i}" x="${x.toFixed(1)}" y="${m.t}" width="${bw.toFixed(1)}" height="${(H - m.t - m.b + 22).toFixed(1)}"/>`;
    });
    const step = Math.max(1, Math.ceil(n / Math.max(3, Math.floor((W - m.l) / 46))));
    o.x.forEach((yr, i) => { if (((n - 1 - i) % step === 0 && Math.abs(i - sel) > step / 2) || i === sel) s += `<text class="ax" x="${(m.l + (i + .5) * bw).toFixed(1)}" y="${(Y(0) + 15).toFixed(1)}" text-anchor="middle"${i === sel ? ' style="font-weight:700;fill:var(--text)"' : ""}>${yr}</text>`; });
    if (o.v[sel] != null) {
      const cx = m.l + (sel + .5) * bw, near = W - m.r - cx < 34 ? "end" : cx - m.l < 30 ? "start" : "middle";
      const lx = near === "end" ? m.l + (sel + .84) * bw : near === "start" ? m.l + (sel + .16) * bw : cx;
      const top = Math.max(...[sel - 1, sel, sel + 1].filter(k => k >= 0 && k < n && o.v[k] != null).map(k => o.v[k]));
      s += `<text class="lab" x="${lx.toFixed(1)}" y="${Math.max(m.t - 4, Y(top) - 7).toFixed(1)}" text-anchor="${near}">${o.lab(o.v[sel])}</text>`;
    }
    if (o.band) {
      const by = Y(0) + 26;
      o.band.forEach(b => {
        const x1 = XY(b.from), x2 = XY(b.to);
        s += `<rect class="band-${b.cls}" x="${x1.toFixed(1)}" y="${by}" width="${(x2 - x1).toFixed(1)}" height="20" rx="3"/>`;
        s += `<text class="bandtx" data-w="${(x2 - x1 - 6).toFixed(1)}" x="${(x1 + 4).toFixed(1)}" y="${by + 14}">${b.label}</text>`;
      });
      o.marks.forEach((mk, k) => {
        const x = XY(mk.at);
        s += `<line class="base" x1="${x.toFixed(1)}" x2="${x.toFixed(1)}" y1="${by + 20}" y2="${by + 30}"/>`;
        s += `<circle class="mark${k === mark ? " sel" : ""}" data-k="${k}" cx="${x.toFixed(1)}" cy="${by + 38}" r="8"/><text class="marktx${k === mark ? " sel" : ""}" x="${x.toFixed(1)}" y="${by + 41.5}" text-anchor="middle">${k + 1}</text>`;
      });
    }
    el.innerHTML = s + "</svg>";
    el.querySelectorAll(".bandtx").forEach(tx => { if (tx.getComputedTextLength() > +tx.dataset.w) tx.remove(); });
    el.querySelectorAll(".colhit").forEach(r => r.addEventListener("click", () => api.pick(+r.dataset.i)));
    el.querySelectorAll(".mark").forEach(c => c.addEventListener("click", () => o.onMark && o.onMark(+c.dataset.k)));
  }
  const api = {
    pick(i, k = -1) { sel = i; mark = k; draw(); o.onPick(i); },
  };
  el.tabIndex = 0;
  el.setAttribute("aria-label", o.aria + ". Use the left and right arrow keys to pick a year.");
  el.addEventListener("keydown", e => {
    if (e.key !== "ArrowLeft" && e.key !== "ArrowRight") return;
    e.preventDefault(); api.pick(Math.max(0, Math.min(n - 1, sel + (e.key === "ArrowRight" ? 1 : -1))));
  });
  draw(); o.onPick(sel); resizers.push(draw);
  return api;
}

// ------------------------------------------------------------------ the visit
document.querySelectorAll("#agree button").forEach(b => b.addEventListener("click", () => {
  const p = b.nextElementSibling, open = p.hidden;
  p.hidden = !open; b.setAttribute("aria-expanded", String(open)); b.querySelector(".ar").textContent = open ? "\u2212" : "+";
}));

// ------------------------------------------------------------------ 1. the opportunity
(function () {
  const all = D.buys.slice();
  const draw = k => {
    const list = all.slice().sort((a, b) => b[k] - a[k]).slice(0, 15);
    hbars($("#buyBars"), list.map(r => ({label: r.n, a: r.w, b: r.ca, cls: "w", right: `<b>${short(r.w, "US$")}</b> · Canada ${short(r.ca, "US$")}`})), {
      onPick: r => {
        const x = list.find(z => z.n === r.label);
        $("#buyCard").innerHTML = `<b>${esc(x.n)}</b><span class="big">${usd(x.w)}</span>bought by Türkiye from the world in 2025. From Canada: <b>${usd(x.ca)}</b>, ${pc(x.ca / x.w * 100, x.ca / x.w < .01 ? 2 : 1)} of it.`;
      }
    });
  };
  seg($("#buySeg"), draw); draw("w");
  const sup = D.suppliers, items = [];
  sup.forEach((s, i) => {
    if (i > 0 && s.r - sup[i - 1].r > 1) items.push({gap: true, label: `${ord(sup[i - 1].r + 1)} to ${ord(s.r - 1)}`});
    items.push({label: `${s.r}. ${s.n}`, a: s.v, cls: s.n === "Canada" ? "c" : "w", me: s.n === "Canada", right: `<b>${short(s.v, "US$")}</b> · ${pc(s.s)}`, s});
  });
  const ci = items.findIndex(x => x.me);
  hbars($("#supBars"), items, {
    sel: ci, onPick: it => {
      $("#supCard").innerHTML = it.me ? `<b>Canada</b><span class="big">${usd(it.s.v)}</span>sold to Türkiye in 2025, ${pc(it.s.s)} of Türkiye's imports and the ${ord(it.s.r)} largest of its trading partners.`
        : `<b>${esc(it.s.n)}</b><span class="big">${usd(it.s.v)}</span>sold to Türkiye in 2025, ${pc(it.s.s)} of Türkiye's imports.`;
    }
  });
  const U = D.usShare;
  lineChart($("#usLine"), {
    x: U.y, series: [{v: U.v, cls: "ca", area: true}], ymax: 100, tick: v => nf(v) + "%", aria: "Share of Canada's goods exports sold to the United States, 1999 to 2025",
    onPick: i => { $("#usCard").innerHTML = `<b>${U.y[i]}</b><span class="big">${pc(U.v[i])}</span>of the goods Canada sold abroad went to the United States.`; }
  });
})();

// ------------------------------------------------------------------ 2. trade deficit
(function () {
  const T = D.trade;
  lineChart($("#tradeLine"), {
    x: T.y, series: [{v: T.m, cls: "tr", area: true}, {v: T.x, cls: "ca"}], tick: v => "$" + (Number.isInteger(v) ? nf(v) : nf(v, 1)) + "B",
    aria: "Canada's goods exports to and imports from Türkiye, 1988 to 2025",
    onPick: i => {
      const x = T.x[i] * 1e9, m = T.m[i] * 1e9, bal = x - m;
      $("#tradeCard").innerHTML = `<b>${T.y[i]}</b>: Canada sold <b>${money(x)}</b> and bought <b>${money(m)}</b>.<span class="big">${money(Math.abs(bal))}</span>trade ${bal < 0 ? "deficit" : "surplus"} with Türkiye.`;
    }
  });
  const yrs = ["'21", "'22", "'23", "'24", "'25"];
  const draw = k => {
    const g = D[k], tot = k === "sold" ? D.trade.x[D.trade.x.length - 1] * 1e9 : D.trade.m[D.trade.m.length - 1] * 1e9;
    hbars($("#goodsBars"), g.map(r => ({label: r.n, a: r.v[4], cls: k === "sold" ? "c" : "t", right: `<b>${short(r.v[4])}</b>`, r})), {
      onPick: it => {
        const r = it.r;
        $("#goodsCard").innerHTML = `<b>${esc(r.n)}</b><span class="big">${money(r.v[4])}</span>${k === "sold" ? "sold to" : "bought from"} Türkiye in 2025, ${pc(r.v[4] / tot * 100)} of the total. 2021 to 2025:` + mini(r.v, yrs, 4, k === "sold" ? "" : "tr") +
          `<span class="m">${r.v.map((v, i) => `20${yrs[i].slice(1)}: ${short(v)}`).join(" · ")}</span>`;
      }
    });
  };
  seg($("#goodsSeg"), draw); draw("sold");
})();

// ------------------------------------------------------------------ 3. duties
(function () {
  const draw = k => {
    const rows = k === "ca" ? D.dutyCA : D.dutyTR, t = D.dutyTot[k];
    const free = t.free_pct;
    $("#dutySum").innerHTML = `<div class="xcard"><b>${k === "ca" ? "Canadian-made goods sold to Türkiye, without durum wheat" : "Turkish goods sold to Canada"}: ${money(t.base)}</b>` +
      `<div class="hb static" style="padding:6px 0 2px"><span class="ht" style="height:16px"><i class="w" style="width:${free.toFixed(1)}%"></i><i class="${k === "ca" ? "c" : "t"}" style="left:${free.toFixed(1)}%;width:${(100 - free).toFixed(1)}%"></i></span></div>` +
      `<span class="m">${nf(free)}% duty-free · ${nf(100 - free)}% pays duty</span><br>Estimated duty: <b>${money(t.duty)}</b>, ${pc(t.rate)} on average.</div>`;
    const list = rows.filter(r => r.d > 0).slice(0, 12);
    hbars($("#dutyBars"), list.map(r => ({label: r.n, a: r.d, cls: k === "ca" ? "c" : "t", right: `<b>${short(r.d)}</b>`, r})), {
      onPick: it => {
        const r = it.r;
        $("#dutyCard").innerHTML = `<b>${esc(r.n)}</b><span class="big">${money(r.d)}</span>estimated duty on ${money(r.v)} of goods, ${pc(r.d / r.v * 100)} of their value. ${nf(r.p / r.v * 100)}% of these goods pay duty.`;
      }
    });
  };
  seg($("#dutySeg"), draw); draw("ca");
})();

// ------------------------------------------------------------------ 4. provinces
(function () {
  const P = D.prov.slice().sort((a, b) => b.s[4] - a.s[4]), M = D.map, byC = {};
  P.forEach(p => byC[p.c] = p);
  const mx = Math.max(...P.map(p => p.s[4]));
  let s = `<svg viewBox="0 0 ${M.w} ${M.h}" role="group" aria-label="Map of Canada's provinces and territories">`;
  for (const [c, d] of Object.entries(M.paths)) {
    const p = byC[c], v = p ? p.s[4] : 0, t = v > 0 ? .16 + .84 * Math.pow(v / mx, .55) : 0;
    s += `<path d="${d}" data-c="${c}" tabindex="0" role="button" aria-label="${esc(p ? p.n : c)}" style="fill:${v > 0 ? "var(--ca)" : "var(--land)"};fill-opacity:${v > 0 ? t.toFixed(2) : 1}"/>`;
  }
  $("#provMap").innerHTML = s + "</svg>";
  const chips = $("#provChips");
  chips.innerHTML = P.map(p => `<button type="button" class="chip" data-c="${p.c}" aria-pressed="false">${esc(p.n)}</button>`).join("");
  const yrs = ["'21", "'22", "'23", "'24", "'25"];
  const inN = n => n === "Northwest Territories" ? "the Northwest Territories" : n;
  function pick(c) {
    const p = byC[c];
    document.querySelectorAll("#provMap path").forEach(x => x.classList.toggle("sel", x.dataset.c === c));
    chips.querySelectorAll(".chip").forEach(x => { const on = x.dataset.c === c; x.classList.toggle("on", on); x.setAttribute("aria-pressed", String(on)); });
    let h = `<b>${esc(p.n)}</b>`;
    if (p.s[4] > 0) {
      h += `<span class="big">${money(p.s[4])}</span>of goods made in ${esc(inN(p.n))} sold to Türkiye in 2025, ${share(p.s[4], P.reduce((a, q) => a + q.s[4], 0))} of Canada's total. 2021 to 2025:` + mini(p.s, yrs, 4);
      if (p.p.length) h += `Top products: <ul>${p.p.map(x => `<li>${esc(x.n)}: <b>${money(x.v)}</b></li>`).join("")}</ul>`;
    } else h += `<span class="big">No recorded sales</span>to Türkiye in 2025.`;
    if (p.imp > 0) h += `<div style="margin-top:6px">Goods from Türkiye that cleared customs in ${esc(inN(p.n))}: <b>${money(p.imp)}</b>.</div>`;
    if (p.tk > 0) h += `<div style="margin-top:6px"><b>${nf(p.tk)}</b> people of Turkish origin${p.born > 0 ? ` and <b>${nf(p.born)}</b> people born in Türkiye` : ""} lived in ${esc(inN(p.n))} in 2021.</div>`;
    $("#provCard").innerHTML = h;
  }
  document.querySelectorAll("#provMap path").forEach(x => {
    x.addEventListener("click", () => pick(x.dataset.c));
    x.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); pick(x.dataset.c); } });
  });
  chips.querySelectorAll(".chip").forEach(x => x.addEventListener("click", () => pick(x.dataset.c)));
  pick(P[0].c);
})();

// ------------------------------------------------------------------ 5. travel and people
(function () {
  const old = 12, neu = 21;
  $("#flights").innerHTML = `<span>Before</span><div class="fb old" style="width:${(old / neu * 100).toFixed(1)}%"></div>` +
    `<span><b>New limit</b></span><div class="fb" style="width:100%"></div>` +
    `<span class="fnt"><b>${old}</b> passenger flights a week for each country before, up to <b>${neu}</b> under the new agreement</span>`;
  const T = D.trips;
  lineChart($("#tripLine"), {
    x: T.y, series: [{v: T.v, cls: "ca", area: true}], tick: v => v >= 1000 ? nf(v / 1000) + "K" : nf(v), aria: "Trips to Türkiye by Canadians each year, 2010 to 2025",
    onPick: i => { $("#tripCard").innerHTML = `<b>${T.y[i]}</b><span class="big">${nf(T.v[i])}</span>trips to Türkiye by Canadians, the ${ord(T.rank[i])} most of any nationality.`; }
  });
  const L = {
    pr: ["became permanent residents of Canada", "IRCC; citizens of Türkiye"],
    study: ["held a Canadian study permit on December 31", "IRCC"],
    work: ["held a Canadian work permit on December 31", "IRCC"],
  };
  let api;
  const draw = k => {
    const S = D.people[k];
    const el = $("#pplCols");
    el.replaceWith(el.cloneNode(false));
    const el2 = $("#pplCols");
    api = columns(el2, {
      x: S.y, v: S.v, cls: "", tick: v => v >= 1000 ? nf(v / 1000) + "K" : nf(v), lab: v => nf(v), aria: "People from Türkiye in Canada by year",
      onPick: i => {
        $("#pplCard").innerHTML = `<b>${S.y[i]}</b><span class="big">${nf(S.v[i])}</span>citizens of Türkiye ${L[k][0]}${S.rank ? `, the ${ord(S.rank[i])} most of any country` : ""}.`;
      }
    });
  };
  seg($("#pplSeg"), draw); draw("pr");
  hbars($("#cityBars"), D.cities.map(c => ({label: c.n, a: c.v, cls: "c", right: `<b>${nf(c.v)}</b>`})));
})();

// ------------------------------------------------------------------ 6. energy
(function () {
  const p = D.power;
  const items = [
    {label: "Wind and solar, December 2025", a: p.ws, cls: "c", right: `<b>${nf(p.ws)} GW</b>`, t: `Türkiye had <b>${nf(p.ws, 1)} gigawatts</b> of wind and solar power installed in December 2025.`},
    {label: "Wind and solar goal for 2035", a: p.wsGoal, cls: "w", right: `<b>${nf(p.wsGoal)} GW</b>`, t: `Türkiye's goal is <b>${nf(p.wsGoal)} gigawatts</b> of wind and solar power by 2035, about three times December 2025.`},
    {label: "Nuclear being built: Akkuyu, by Rosatom", a: p.nucBuild, cls: "t", right: `<b>${nf(p.nucBuild, 1)} GW</b>`, t: `Akkuyu, Türkiye's first nuclear plant, has four reactors under construction by Russia's Rosatom, <b>${nf(p.nucBuild, 1)} gigawatts</b> in all.`},
    {label: "Nuclear goal for 2035", a: p.nuc2035, cls: "w", right: `<b>${nf(p.nuc2035, 1)} GW</b>`, t: `By the end of 2035, Türkiye wants <b>${nf(p.nuc2035, 1)} gigawatts</b> of nuclear power, including Akkuyu.`},
    {label: "Nuclear goal for 2050", a: p.nuc2050, cls: "w", right: `<b>over ${nf(p.nuc2050)} GW</b>`, t: `By 2050, Türkiye wants <b>over ${nf(p.nuc2050)} gigawatts</b> of nuclear power. Canada's CANDU reactors are being studied for Türkiye's new plants.`},
  ];
  hbars($("#powBars"), items, {onPick: it => { $("#powCard").innerHTML = it.t; }});
  const tot = D.gas.reduce((a, g) => a + g.v, 0);
  const gi = D.gas.map(g => ({label: g.n, a: g.v, cls: "t", right: `<b>${nf(g.v, 1)}</b>`, g}));
  gi.push({label: "For comparison: all of Canada's LNG exports in 2025", a: D.gasCA, cls: "c", me: true, right: `<b>${nf(D.gasCA, 1)}</b>`, ca: true});
  hbars($("#gasBars"), gi, {
    onPick: it => {
      $("#gasCard").innerHTML = it.ca ? `<b>For comparison</b><span class="big">${nf(D.gasCA, 1)} billion m³</span>All of Canada's liquefied natural gas exports in 2025 came to about ${pc(D.gasCA / tot * 100, 0)} of what Türkiye imported.`
        : `<b>${esc(it.g.n)}</b><span class="big">${nf(it.g.v, 1)} billion m³</span>of natural gas sold to Türkiye in 2025, ${pc(it.g.v / tot * 100, 0)} of Türkiye's gas imports.`;
    }
  });
  const X = D.energyX;
  columns($("#enCols"), {
    x: X.y, v: X.v, tick: v => "$" + nf(v / 1e6) + "M", lab: v => short(v), aria: "Canada's energy sales to Türkiye, 2021 to 2025",
    onPick: i => { $("#enCard").innerHTML = `<b>${X.y[i]}</b><span class="big">${money(X.v[i])}</span>of oil, gas and coal sold to Türkiye${X.y[i] === 2025 ? ", mostly coal from British Columbia" : ""}.`; }
  });
})();

// ------------------------------------------------------------------ 7. defence
(function () {
  const M = D.mil.slice(), yrs = M.map(d => d.y).concat([2026]), vals = M.map(d => d.v).concat([null]);
  const ym = s => { const [y, mo] = String(s).split("-"); return +y + (mo ? (+mo - 1) / 12 : .5); };
  const marks = D.miles.map(([d, t]) => ({at: ym(d), d, t}));
  const band = [
    {from: 2010, to: ym("2019-10"), cls: "open", label: "Open"},
    {from: ym("2019-10"), to: ym("2024-01"), cls: "sus", label: "Suspended"},
    {from: ym("2024-01"), to: 2027, cls: "re", label: "Reopened"},
  ];
  const mon = d => { const [y, m] = d.split("-"); return m ? ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][+m - 1] + " " + y : y; };
  const list = $("#miles");
  list.innerHTML = marks.map((m, k) => `<li><button type="button" data-k="${k}" aria-pressed="false"><span class="n">${k + 1}</span><span><b>${mon(m.d)}.</b> ${esc(m.t)}</span></button></li>`).join("");
  const api = columns($("#milCols"), {
    x: yrs, v: vals, tick: v => "$" + nf(v / 1e6) + "M", lab: v => short(v), band, marks, h: 250, aria: "Canadian military exports to Türkiye by year, 2010 to 2025",
    onPick: i => {
      const d = M[i];
      $("#milCard").innerHTML = d ? `<b>${d.y}</b><span class="big">${money(d.v)}</span>of military goods exported to Türkiye, the ${ord(d.r)} largest of ${d.n} destinations outside the United States.`
        : `<b>2026</b><span class="big">No figures published for 2026</span>`;
      list.querySelectorAll("button").forEach(b => b.setAttribute("aria-pressed", "false"));
    },
    onMark: k => pickMark(k),
  });
  function pickMark(k) {
    const y = Math.floor(marks[k].at), i = Math.min(yrs.indexOf(y), yrs.length - 1);
    api.pick(i, k);
    list.querySelectorAll("button").forEach(b => b.setAttribute("aria-pressed", String(+b.dataset.k === k)));
  }
  list.querySelectorAll("button").forEach(b => b.addEventListener("click", () => pickMark(+b.dataset.k)));
  api.pick(yrs.indexOf(2019));
})();
