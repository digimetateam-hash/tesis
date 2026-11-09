#!/usr/bin/env python3
"""
Visualisasi jaringan komunikasi bergaya NodeXL "Group-in-a-Box".
Setiap klaster (komunitas Louvain) digambar di kotaknya sendiri dan diberi label.

Pemakaian:
    python3 jaringan_klaster.py <file_relasi.csv|xlsx> [--top 12] [--min 3] [--out gambar_jaringan_klaster.png]

File relasi = sheet/ekspor "Edges" NodeXL (kolom Vertex 1 dan Vertex 2),
atau CSV apa pun yang punya dua kolom akun pengirim dan akun yang disebut.
"""
import argparse, re, sys
import pandas as pd
import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import squarify

ap = argparse.ArgumentParser()
ap.add_argument("file")
ap.add_argument("--sheet", default=None, help="nama sheet bila file .xlsx (default: 'Edges' bila ada)")
ap.add_argument("--top", type=int, default=12, help="jumlah klaster terbesar yang digambar")
ap.add_argument("--min", type=int, default=3, help="ukuran minimum klaster yang digambar")
ap.add_argument("--seed", type=int, default=42)
ap.add_argument("--out", default="gambar_jaringan_klaster.png")
a = ap.parse_args()

# ---------- 1. Baca data relasi ----------
if a.file.lower().endswith((".xlsx", ".xls")):
    xl = pd.ExcelFile(a.file)
    sheet = a.sheet or ("Edges" if "Edges" in xl.sheet_names else xl.sheet_names[0])
    df = pd.read_excel(a.file, sheet_name=sheet, header=None)
    # NodeXL menaruh judul kolom di baris pertama atau kedua
    hdr = next(i for i in range(min(5, len(df))) if df.iloc[i].astype(str).str.contains("Vertex 1", case=False).any()) \
        if df.astype(str).apply(lambda c: c.str.contains("Vertex 1", case=False)).any().any() else 0
    df.columns = df.iloc[hdr].astype(str); df = df.iloc[hdr + 1:]
else:
    df = pd.read_csv(a.file, low_memory=False)

norm = {re.sub(r"[^a-z0-9]", "", str(c).lower()): c for c in df.columns}
def pick(*names):
    for n in names:
        k = re.sub(r"[^a-z0-9]", "", n.lower())
        if k in norm: return norm[k]
src = pick("Vertex 1", "source", "from", "author", "username")
dst = pick("Vertex 2", "target", "to", "mentioned", "mention")
if not (src and dst):
    sys.exit(f"Kolom relasi tidak ditemukan. Kolom yang ada: {list(df.columns)}")
rel = pick("Relationship", "type")
print(f"Kolom dipakai: {src} -> {dst}" + (f" (jenis relasi: {rel})" if rel else ""))

E = df[[src, dst] + ([rel] if rel else [])].dropna(subset=[src, dst]).copy()
E[src] = E[src].astype(str).str.strip().str.lstrip("@")
E[dst] = E[dst].astype(str).str.strip().str.lstrip("@")
if rel:
    print("Jenis relasi:", E[rel].value_counts().to_dict())
# self-loop dipertahankan agar hitungan akun & relasi sama dengan NodeXL

G = nx.DiGraph()
for u, v in E[[src, dst]].itertuples(index=False):
    G.add_edge(u, v, weight=G[u][v]["weight"] + 1 if G.has_edge(u, v) else 1)
U = G.to_undirected()
U.remove_edges_from(list(nx.selfloop_edges(U)))
print(f"Akun: {G.number_of_nodes()} | relasi unik berarah: {G.number_of_edges()} | "
      f"komponen: {nx.number_weakly_connected_components(G)} | kepadatan: {nx.density(G):.6f}")

# ---------- 2. Komunitas Louvain ----------
comms = None
if a.file.lower().endswith((".xlsx", ".xls")) and "Vertices" in pd.ExcelFile(a.file).sheet_names:
    V = pd.read_excel(a.file, sheet_name="Vertices", header=None)
    hv = next((i for i in range(min(5, len(V))) if V.iloc[i].astype(str).str.fullmatch("Vertex").any()), None)
    if hv is not None:
        V.columns = V.iloc[hv].astype(str); V = V.iloc[hv + 1:]
        if "Community" in V.columns:
            m = dict(zip(V["Vertex"].astype(str).str.strip().str.lstrip("@"), V["Community"]))
            if all(n in m for n in U.nodes()):
                grp = {}
                for n in U.nodes(): grp.setdefault(m[n], set()).add(n)
                comms = list(grp.values())
                print("Komunitas diambil dari kolom 'Community' di sheet Vertices (hasil yang sudah ada).")
if comms is None:
    comms = nx.community.louvain_communities(U, weight="weight", seed=a.seed)
comms = sorted(comms, key=len, reverse=True)
print(f"Komunitas Louvain: {len(comms)} | modularitas: {nx.community.modularity(U, comms, weight='weight'):.4f}")
indeg = dict(G.in_degree()); deg = dict(G.degree())

rows = []
for i, c in enumerate(comms, 1):
    top = sorted(c, key=lambda n: (deg[n], indeg[n]), reverse=True)
    for n in c:
        rows.append({"akun": "@" + n, "klaster": i, "ukuran_klaster": len(c), "in_degree": indeg[n],
                     "out_degree": G.out_degree(n), "total_degree": deg[n], "akun_teratas_klaster": "@" + top[0]})
pd.DataFrame(rows).sort_values(["klaster", "total_degree"], ascending=[True, False]) \
  .to_csv("anggota_klaster.csv", index=False)

show = [c for c in comms if len(c) >= a.min][: a.top]
if not show:
    sys.exit("Tidak ada klaster yang memenuhi --min. Coba --min 2.")

# ---------- 3. Tata letak kotak (treemap) ----------
W, H = 16.0, 9.0
sizes = squarify.normalize_sizes([len(c) for c in show], W, H)
boxes = squarify.squarify(sizes, 0, 0, W, H)
PAL = ["#2A9D8F", "#E76F51", "#7B4FA0", "#F4A261", "#1F3864", "#3C8D40",
       "#B5452B", "#2A6F97", "#C2185B", "#6D4C41", "#00838F", "#9E9D24"]

fig, ax = plt.subplots(figsize=(W, H), dpi=300)
ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")
pos_all = {}
for k, (c, b) in enumerate(zip(show, boxes)):
    x, y, w, h = b["x"], b["y"], b["dx"], b["dy"]
    col = PAL[k % len(PAL)]
    ax.add_patch(Rectangle((x, y), w, h, fill=False, ec="#C0392B", lw=0.8, ls="--"))
    sub = U.subgraph(c)
    p = nx.spring_layout(sub, seed=a.seed, k=1.5 / max(len(c), 1) ** 0.5, iterations=200)
    xs = [v[0] for v in p.values()]; ys = [v[1] for v in p.values()]
    mnx, mxx, mny, mxy = min(xs), max(xs), min(ys), max(ys)
    pad = 0.12; lab = 0.42
    for n, (px, py) in p.items():
        sx = x + w * pad + (px - mnx) / ((mxx - mnx) or 1) * w * (1 - 2 * pad)
        sy = y + h * pad + lab * 0.6 + (py - mny) / ((mxy - mny) or 1) * (h * (1 - 2 * pad) - lab * 0.6)
        pos_all[n] = (sx, sy)
    top = sorted(c, key=lambda n: (deg[n], indeg[n]), reverse=True)
    for u, v in sub.edges():
        ax.plot([pos_all[u][0], pos_all[v][0]], [pos_all[u][1], pos_all[v][1]], color="#9AA5B1", lw=0.4, alpha=0.6, zorder=1)
    for n in c:
        s = 6 + 10 * deg[n] ** 0.9
        ax.scatter(*pos_all[n], s=s, color=col, edgecolor="white", linewidth=0.3, zorder=2)
    for n in top[: 3 if len(c) > 10 else 1]:
        ax.text(pos_all[n][0], pos_all[n][1] + 0.08, "@" + n, fontsize=4.5, ha="center", va="bottom", zorder=3,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.8))
    ax.text(x + w / 2, y + 0.12, f"Klaster @{top[0]} ({len(c)} akun)", fontsize=6.5, ha="center", va="bottom",
            fontweight="bold", color=col, bbox=dict(boxstyle="square,pad=0.25", fc="white", ec="#555555", lw=0.5))

ax.set_title(f"Jaringan Komunikasi Percakapan MBG di Twitter: {len(show)} Klaster Terbesar "
             f"dari {len(comms)} Komunitas (Louvain)", fontsize=10, fontweight="bold", pad=8)
plt.tight_layout()
plt.savefig(a.out, dpi=300, bbox_inches="tight", facecolor="white")
print(f"Selesai -> {a.out} dan anggota_klaster.csv")
