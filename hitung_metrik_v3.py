import pandas as pd, os
P = pd.read_csv("data/data_bersih_sudah_dicleaning_5272.csv", low_memory=False)
N = pd.read_csv("results/mbg_network_nodes_final.csv", low_memory=False)
P["akun"] = P["author_username"].astype(str).str.strip().str.lstrip("@").str.lower()
for c in ["like_count", "retweet_count"]:
    P[c] = pd.to_numeric(P[c], errors="coerce").fillna(0)
A = P.groupby("akun").agg(unggahan=("akun", "size"), suka=("like_count", "sum"), retweet=("retweet_count", "sum"))
A["total_keterlibatan"] = A["suka"] + A["retweet"]
N["akun"] = N["Label"].astype(str).str.strip().str.lstrip("@").str.lower()
M = N[["akun", "Degree", "Betweenness", "Community", "Dominant_Emotion"]].merge(A, left_on="akun", right_index=True, how="left")
top = set(N.nlargest(10, "Degree")["akun"]) | set(N.nlargest(10, "Betweenness")["akun"])
M["sentralitas_10_besar"] = M["akun"].isin(top)
T = M.sort_values("Degree", ascending=False).head(20)
T["akun"] = "@" + T["akun"]
os.makedirs("results", exist_ok=True)
T.to_csv("results/metrik_top20_nodexl.csv", index=False)
open("results/metrik_top20_nodexl.md", "w").write("Sumber: diolah peneliti dari data NodeXL Pro (2026).\n\n" + T.fillna("-").to_markdown(index=False))
print("Jumlah unggahan:", len(P), "| akun penulis:", P["akun"].nunique(), "| node jaringan:", len(N))
print("\nSebaran predicted_emotion:\n", P["predicted_emotion"].value_counts(dropna=False).to_string())
print("\nTOP 20 menurut Degree:\n", T.fillna("-").to_string(index=False))
