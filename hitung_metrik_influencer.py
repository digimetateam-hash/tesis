"""Hitung metrik keterlibatan & influencer dari data NodeXL (pengganti klaim Brand24).
Pemakaian:
  python3 hitung_metrik_influencer.py "<csv unggahan>" "<csv node jaringan>"
Hasil: results/metrik_influencer_top20.csv dan results/metrik_influencer_top20.md
Tidak ada angka yang dikarang: kolom yang tidak ada di data ditulis "tidak tersedia".
"""
import sys, os, re
import pandas as pd

def find(df, names):
    low = {re.sub(r'[^a-z0-9]', '', c.lower()): c for c in df.columns}
    for n in names:
        k = re.sub(r'[^a-z0-9]', '', n.lower())
        if k in low:
            return low[k]
    return None

def num(s):
    return pd.to_numeric(s.astype(str).str.replace(r'[^0-9.\-]', '', regex=True), errors='coerce')

posts_path, nodes_path = sys.argv[1], sys.argv[2]
P = pd.read_csv(posts_path, low_memory=False)
N = pd.read_csv(nodes_path, low_memory=False)
print("Kolom data unggahan :", list(P.columns))
print("Kolom data node     :", list(N.columns))

c_author = find(P, ['Author', 'Vertex 1', 'username', 'screen_name', 'Screen Name', 'user', 'author_username'])
c_fol = find(P, ['Author Followers', 'Followers', 'followers_count', 'Vertex 1 Followers', 'user_followers'])
c_like = find(P, ['Like Count', 'Likes', 'favorite_count', 'like_count', 'Favorites'])
c_rep = find(P, ['Reply Count', 'Replies', 'reply_count'])
c_rt = find(P, ['Retweet Count', 'Retweets', 'retweet_count'])
c_quo = find(P, ['Quote Count', 'Quotes', 'quote_count'])
c_view = find(P, ['Views', 'View Count', 'impression_count', 'views'])
print("\nKolom terdeteksi:", dict(author=c_author, followers=c_fol, like=c_like, reply=c_rep,
                                   retweet=c_rt, quote=c_quo, views=c_view))
if not c_author:
    sys.exit("GAGAL: kolom nama akun tidak ditemukan. Kirim daftar kolom di atas ke Claude.")

P['_acc'] = P[c_author].astype(str).str.strip().str.lstrip('@').str.lower()
eng_cols = [c for c in (c_like, c_rep, c_rt, c_quo) if c]
for c in eng_cols + [x for x in (c_fol, c_view) if x]:
    P[c] = num(P[c])
P['_eng'] = P[eng_cols].fillna(0).sum(axis=1) if eng_cols else float('nan')
if c_fol:
    P['_ir'] = P['_eng'] / P[c_fol].where(P[c_fol] > 0) * 100

g = P.groupby('_acc')
A = pd.DataFrame({'unggahan': g.size(), 'total_keterlibatan': g['_eng'].sum()})
if c_fol:
    A['pengikut'] = g[c_fol].max()
    A['interaction_rate_median_%'] = g['_ir'].median().round(2)
    A['jml_unggahan_IR_ge_2%'] = g['_ir'].apply(lambda s: int((s >= 2).sum()))
if c_view:
    A['rata2_tayangan'] = g[c_view].mean().round(0)

v_id = find(N, ['Vertex', 'Id', 'Label', 'username', 'Name'])
c_in = find(N, ['In-Degree', 'indegree', 'in_degree'])
c_out = find(N, ['Out-Degree', 'outdegree', 'out_degree'])
c_bet = find(N, ['Betweenness Centrality', 'betweenness', 'Betweenness'])
c_pr = find(N, ['PageRank', 'pagerank'])
print("Kolom node terdeteksi:", dict(id=v_id, indeg=c_in, outdeg=c_out, betweenness=c_bet, pagerank=c_pr))
if not (v_id and c_in and c_out):
    sys.exit("GAGAL: kolom Vertex/In-Degree/Out-Degree tidak ditemukan di file node.")
N['_acc'] = N[v_id].astype(str).str.strip().str.lstrip('@').str.lower()
for c in (c_in, c_out, c_bet, c_pr):
    if c: N[c] = num(N[c])
N['total_degree'] = N[c_in].fillna(0) + N[c_out].fillna(0)
cols = ['_acc', c_in, c_out, 'total_degree'] + [c for c in (c_bet, c_pr) if c]
M = N[cols].merge(A, left_on='_acc', right_index=True, how='left')

# Kriteria influencer (Bab III): minimal 2 dari 3
top10 = set(N.nlargest(10, c_in)['_acc'])
if c_bet: top10 |= set(N.nlargest(10, c_bet)['_acc'])
M['K1_jangkauan'] = ((M.get('pengikut', 0) >= 10000) & (M.get('rata2_tayangan', 0) >= 50000)) if (c_fol and c_view) else pd.NA
M['K2_interaksi'] = (M['jml_unggahan_IR_ge_2%'] >= 3) if c_fol else pd.NA
M['K3_sentralitas'] = M['_acc'].isin(top10)
M['jumlah_kriteria'] = M[['K1_jangkauan', 'K2_interaksi', 'K3_sentralitas']].fillna(False).astype(bool).sum(axis=1)
M['influencer'] = M['jumlah_kriteria'] >= 2

# Skor gabungan peneliti: 40% jangkauan + 30% interaksi + 30% sentralitas (min-max)
def mm(s):
    s = pd.to_numeric(s, errors='coerce')
    return (s - s.min()) / (s.max() - s.min()) if s.max() != s.min() else s * 0
reach = M['rata2_tayangan'] if c_view else (M['pengikut'] if c_fol else None)
if reach is not None and c_fol:
    cent = M[c_bet] if c_bet else M['total_degree']
    M['skor_gabungan'] = (0.4 * mm(reach).fillna(0) + 0.3 * mm(M['interaction_rate_median_%']).fillna(0)
                          + 0.3 * mm(cent).fillna(0)).round(3)

T = M.sort_values('total_degree', ascending=False).head(20).rename(columns={'_acc': 'akun'})
T['akun'] = '@' + T['akun']
os.makedirs('results', exist_ok=True)
T.to_csv('results/metrik_influencer_top20.csv', index=False)
with open('results/metrik_influencer_top20.md', 'w') as f:
    f.write('Sumber: diolah peneliti dari data NodeXL Pro (2026). Bukan keluaran Brand24.\n\n')
    f.write(T.fillna('tidak tersedia').to_markdown(index=False))
print("\nSelesai. Akun memenuhi >=2 kriteria influencer:", int(M['influencer'].sum()))
print(T.fillna('-').to_string(index=False))
