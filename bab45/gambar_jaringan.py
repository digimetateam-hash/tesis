import pandas as pd, numpy as np, networkx as nx, collections
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import Patch
plt.rcParams["font.family"] = "DejaVu Sans"
U_ = "/mnt/user-data/uploads/tesis simple--ThisIsEconomy/"
X = U_ + "NodeXL_MBG_Tesis_Indri_Anjar.xlsx"
E = pd.read_excel(X, sheet_name="Edges"); V = pd.read_excel(X, sheet_name="Vertices")
for c in ["Vertex 1", "Vertex 2"]: E[c] = E[c].astype(str).str.strip()
G = nx.DiGraph(); G.add_edges_from(E[["Vertex 1", "Vertex 2"]].itertuples(index=False))
U = G.to_undirected(); U.remove_edges_from(list(nx.selfloop_edges(U)))
ind = dict(G.in_degree()); outd = dict(G.out_degree()); deg = {n: ind[n] + outd[n] for n in G}
TEAL, OR, PUR, NAVY, YEL, GR = "#2A9D8F", "#E76F51", "#7B4FA0", "#1F3864", "#F4A261", "#94A3B8"
KEY = {"prabowo": OR, "grok": TEAL, "4Y4NKZ": PUR, "newIding30": PUR, "regar_op0sisi": YEL, "dbdbidip": PUR, "tanyakanrl": NAVY, "tanyarlfes": NAVY, "Casagrande10939": PUR}

def layout(H, seed=7):
    comps = sorted(nx.connected_components(H), key=len, reverse=True)
    pos = {}; import math
    big = [c for c in comps if len(c) >= 6]; small = [c for c in comps if len(c) < 6]
    # big components on spiral, small ones on outer ring grid
    R = 0
    for i, c in enumerate(big):
        sub = H.subgraph(c); p = nx.spring_layout(sub, seed=seed, k=2.2 / len(c) ** 0.5, iterations=300)
        mx = max(max(abs(x), abs(y)) for x, y in p.values()) or 1; p = {n: (x / mx, y / mx) for n, (x, y) in p.items()}
        ang = i * 2.4; r = 0 if i == 0 else 1.35 + 0.16 * i ** 0.9
        s = 0.24 * (len(c) / 10) ** 0.5 + 0.05
        cx, cy = r * math.cos(ang), r * math.sin(ang)
        for n, (x, y) in p.items(): pos[n] = (cx + x * s, cy + y * s)
        R = max(R, r + s)
    k = 0; ring = R + 0.35
    per = max(1, int(2 * math.pi * ring / 0.11))
    for c in small:
        ang = 2 * math.pi * (k % per) / per; rr = ring + 0.13 * (k // per)
        cx, cy = rr * math.cos(ang), rr * math.sin(ang)
        for j, n in enumerate(sorted(c)):
            pos[n] = (cx + 0.025 * math.cos(j * 2.1), cy + 0.025 * math.sin(j * 2.1))
        k += 1
    return pos

def draw(ax, H, Gd, title, label_min=5):
    pos = layout(H)
    for u, v in H.edges():
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], color="#B8C2CC", lw=0.35, zorder=1)
    dg = dict(Gd.in_degree()); do = dict(Gd.out_degree())
    xs = [pos[n][0] for n in H]; ys = [pos[n][1] for n in H]
    sz = [4 + 9 * (dg.get(n, 0) + do.get(n, 0)) ** 0.95 for n in H]
    col = [KEY.get(n, GR) for n in H]
    ax.scatter(xs, ys, s=sz, c=col, edgecolors="white", linewidths=0.25, zorder=2)
    for n in H:
        if dg.get(n, 0) + do.get(n, 0) >= label_min or n in ("prabowo", "grok"):
            ax.text(pos[n][0], pos[n][1] + 0.06, "@" + n, fontsize=6, ha="center", zorder=3,
                    bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.85))
    ax.set_title(title, fontsize=9, pad=14); ax.axis("off"); ax.set_aspect("equal")

# ---------- Gambar A: jaringan keseluruhan ----------
fig, ax = plt.subplots(figsize=(9, 8), dpi=250)
draw(ax, U, G, "", 8)
ax.legend(handles=[Patch(color=OR, label="@prabowo (paling banyak disebut)"), Patch(color=TEAL, label="@grok (paling banyak menyebut)"),
                   Patch(color=PUR, label="akun penyebut aktif"), Patch(color=YEL, label="@regar_op0sisi (penghubung)"),
                   Patch(color=GR, label="akun lain")], fontsize=7, frameon=False, loc="lower left")
plt.tight_layout(); plt.savefig("ga_jaringan_keseluruhan.png", facecolor="white"); plt.close()

# ---------- Gambar B: sentralitas ----------
bc = nx.betweenness_centrality(U, normalized=True)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.2), dpi=250)
xs = [outd[n] for n in G]; ys = [ind[n] for n in G]
a1.scatter(xs, ys, s=12, c=[KEY.get(n, GR) for n in G], edgecolors="white", linewidths=0.3)
for n, off in [("prabowo", (5, -3)), ("grok", (-12, 8)), ("4Y4NKZ", (4, 4)), ("newIding30", (4, -9)), ("regar_op0sisi", (6, 2)), ("dbdbidip", (-10, 6)), ("tanyakanrl", (-4, 10))]:
    a1.annotate("@" + n, (outd[n], ind[n]), xytext=off, textcoords="offset points", fontsize=6.5)
a1.set_xlabel("Out-degree (jumlah menyebut akun lain)", fontsize=8); a1.set_ylabel("In-degree (jumlah disebut)", fontsize=8)
a1.set_title("(a) Arah sebutan setiap akun (n = 971)", fontsize=9); a1.tick_params(labelsize=7); a1.spines[["top", "right"]].set_visible(False)
top = sorted(bc.items(), key=lambda x: -x[1])[:10][::-1]
a2.barh(["@" + k for k, _ in top], [v for _, v in top], color=[KEY.get(k, GR) for k, _ in top])
for i, (k, v) in enumerate(top): a2.text(v, i, f" {v:.6f}".replace(".", ","), va="center", fontsize=6.5)
a2.set_title("(b) Sepuluh nilai betweenness tertinggi (graf tak berarah)", fontsize=9)
a2.tick_params(labelsize=7); a2.set_xlim(0, max(v for _, v in top) * 1.35); a2.spines[["top", "right"]].set_visible(False)
a2.set_xlabel("Betweenness (ternormalisasi)", fontsize=8)
plt.tight_layout(); plt.savefig("gb_sentralitas.png", facecolor="white"); plt.close()

# ---------- Gambar C: emosi unggahan anggota komunitas ----------
cm = dict(zip(V.Vertex.astype(str).str.strip(), V.Community))
grp = collections.defaultdict(set)
for n in U: grp[cm[n]].add(n)
comms = sorted(grp.values(), key=len, reverse=True)[:8]
D = pd.read_csv(U_ + "data/results/indobert_9_emosi_fixed.csv", low_memory=False)
D = D[pd.to_datetime(D.created_at, errors="coerce", utc=True).notna()]
order = ["Jijik", "Percaya", "Netral", "Tertarik", "Lainnya"]
CL = {"Jijik": OR, "Percaya": TEAL, "Netral": GR, "Tertarik": YEL, "Lainnya": PUR}
rows = []; labs = []
for c in comms:
    hub = sorted(c, key=lambda n: -deg[n])[0]
    em = D[D.author_username.astype(str).isin(c)].predicted_emotion
    vc = em.value_counts(); tot = len(em)
    r = {k: vc.get(k, 0) for k in order[:-1]}; r["Lainnya"] = tot - sum(r.values()); r["n"] = tot
    rows.append(r); labs.append(f"@{hub}\n({len(c)} akun; {tot} unggahan)")
fig, ax = plt.subplots(figsize=(9, 4.4), dpi=250)
left = np.zeros(len(rows))
for k in order:
    vals = np.array([r[k] / r["n"] * 100 if r["n"] else 0 for r in rows])
    ax.barh(labs[::-1], vals[::-1], left=left[::-1], color=CL[k], label=k)
    left += vals
ax.set_xlabel("Persentase unggahan anggota komunitas (%)", fontsize=8); ax.tick_params(labelsize=7)
ax.legend(fontsize=7, frameon=False, ncol=5, loc="upper center", bbox_to_anchor=(0.5, 1.12)); ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout(); plt.savefig("gc_emosi_komunitas.png", facecolor="white"); plt.close()
pd.DataFrame(rows, index=labs).to_csv("emosi_komunitas.csv")

# ---------- Gambar D: peran akun (Tabel 3.9) ----------
roles = [("Warganet biasa", 805), ("Penggerak wacana", 123), ("Penyebar wacana", 29), ("Rujukan keluhan", 5), ("Perantara opini", 5), ("Otoritas kebijakan", 3), ("Penjawab otomatis", 1)]
fig, ax = plt.subplots(figsize=(8, 3.6), dpi=250)
cols = [GR, TEAL, OR, PUR, YEL, NAVY, "#3C8D40"]
ax.barh([r for r, _ in roles][::-1], [v for _, v in roles][::-1], color=cols[::-1])
for i, (r, v) in enumerate(roles[::-1]): ax.text(v + 8, i, f"{v} ({v / 971 * 100:.1f}%)".replace(".", ","), va="center", fontsize=7)
ax.set_xlim(0, 950); ax.set_xlabel("Jumlah akun", fontsize=8); ax.tick_params(labelsize=7.5); ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout(); plt.savefig("gd_peran_akun.png", facecolor="white"); plt.close()

# ---------- Gambar E: jaringan per periode ----------
t = pd.to_datetime(E["Date"])
fig, axs = plt.subplots(1, 2, figsize=(11, 5.6), dpi=250)
for ax, (nm, lo, hi) in zip(axs, [("Periode 1 (2 Maret–30 April 2026)", "2026-03-01", "2026-05-01"), ("Periode 2 (1–24 Mei 2026)", "2026-05-01", "2026-06-01")]):
    e = E[(t >= lo) & (t < hi)]
    g = nx.DiGraph(); g.add_edges_from(e[["Vertex 1", "Vertex 2"]].itertuples(index=False))
    h = g.to_undirected(); h.remove_edges_from(list(nx.selfloop_edges(h)))
    draw(ax, h, g, f"{nm}\n{g.number_of_nodes()} akun · {g.number_of_edges()} relasi unik · {nx.number_weakly_connected_components(g)} komponen", 4 if nm.startswith("Periode 1") else 8)
plt.tight_layout(); plt.savefig("ge_jaringan_periode.png", facecolor="white"); plt.close()
print(pd.DataFrame(rows, index=[l.replace("\n", " ") for l in labs]))
