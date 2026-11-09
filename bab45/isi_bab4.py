"""Pengisian awal Bab IV: isu (kamus Tabel 3.6), kandidat sindiran (penanda Bab III 3.8.1), puncak harian, lembar pengodean."""
import pandas as pd, numpy as np, re, json, collections, random
D = pd.read_csv('data/indobert_9_emosi_fixed.csv', low_memory=False)
D['t'] = pd.to_datetime(D.created_at, utc=True, errors='coerce').dt.tz_convert('Asia/Jakarta')
D = D[D.t.notna()].copy(); D['tgl'] = D.t.dt.date.astype(str)
D['periode'] = np.where(D.t < pd.Timestamp('2026-05-01', tz='Asia/Jakarta'), 'P1', 'P2')
for k in ['like_count','retweet_count','reply_count','quote_count','view_count']: D[k] = pd.to_numeric(D[k], errors='coerce').fillna(0)
D['eng'] = D[['like_count','retweet_count','reply_count','quote_count']].sum(axis=1)
txt = D.text.astype(str)
low = txt.str.lower().str.replace('badan gizi nasional', 'bgn', regex=False).str.replace('satuan pelayanan pemenuhan gizi', 'sppg', regex=False)
promo = txt.str.contains(r'\b(?:oferta|ofertas|promo[cç][aã]o|desconto|frete|cupom|compre|loja|pre[cç]o)\b', case=False, regex=True) | txt.str.contains('🇧🇷') | txt.str.contains(r'R\$')
D['promo_pt'] = promo
K = json.load(open('bab45/kamus_isu.json', encoding='utf-8'))
pats = {c: [re.compile(r'(?<![\w])' + re.escape(k) + r'(?![\w])') for k in v] for c, v in K.items()}
isu, nmatch, tie = [], [], []
for s in low:
    cnt = {}; first = {}
    for c, ps in pats.items():
        n = 0; f = None
        for p in ps:
            for m in p.finditer(s):
                n += 1; f = m.start() if f is None or m.start() < f else f
        if n: cnt[c] = n; first[c] = f
    if not cnt: isu.append('Lainnya'); nmatch.append(0); tie.append(False); continue
    mx = max(cnt.values()); top = [c for c in cnt if cnt[c] == mx]
    tie.append(len(top) > 1); isu.append(min(top, key=lambda c: first[c])); nmatch.append(mx)
D['isu'] = isu; D['isu_seri'] = tie
D.loc[D.promo_pt, 'isu'] = 'Lainnya'
EM = lambda s, e: s.count(e)
def markers(s):
    sl = s.lower(); m = set()
    if '🤡' in s or '🙃' in s: m.add('Penghinaan halus')
    if EM(s, '😇') >= 2 or EM(s, '👏') >= 2 or re.search(r'\b(katanya|konon)\b', sl): m.add('Pujian palsu')
    if re.search(r'\bternyata\b|\bhebat ya\b|\bkeren nih\b', sl): m.add('Pembalik harapan')
    return m
D['penanda'] = [markers(s) for s in txt]
D.loc[D.promo_pt, 'penanda'] = [set()] * int(D.promo_pt.sum())
D['kandidat_sindiran'] = D.penanda.map(bool)
R = {}
order = ['Manfaat Gizi dan Sosial', 'Pelaksanaan & Distribusi', 'Keamanan & Mutu Makanan', 'Anggaran & Akuntabilitas', 'Politik & Ekonomi', 'Lainnya']
for c in order:
    g = D[D.isu == c]
    R.setdefault('isu', {})[c] = {'n': int(len(g)), 'pct': round(len(g) / len(D) * 100, 2),
        'emosi_dominan': g.predicted_emotion.value_counts().idxmax() if len(g) else '-',
        'emosi_dominan_pct': round(g.predicted_emotion.value_counts(normalize=True).max() * 100, 2) if len(g) else 0,
        'pct_kandidat_sindiran': round(g.kandidat_sindiran.mean() * 100, 2) if len(g) else 0,
        'P1': int((g.periode == 'P1').sum()), 'P2': int((g.periode == 'P2').sum()),
        'rata_eng': round(g.eng.mean(), 2) if len(g) else 0, 'median_eng': float(g.eng.median()) if len(g) else 0}
R['isu_seri'] = int(D.isu_seri.sum()); R['isu_tanpa_kata_kunci'] = int(((D.isu == 'Lainnya') & ~D.promo_pt).sum()); R['promo_lainnya'] = int(D.promo_pt.sum())
R['isu_periode_pct'] = (pd.crosstab(D.isu, D.periode, normalize='columns') * 100).round(2).to_dict()
R['isu_x_emosi'] = pd.crosstab(D.isu, D.predicted_emotion).to_dict()
R['n_kandidat'] = int(D.kandidat_sindiran.sum()); R['pct_kandidat'] = round(D.kandidat_sindiran.mean() * 100, 2)
emo_re = re.compile('[\U0001F300-\U0001FAFF☀-➿]')
for mk in ['Pembalik harapan', 'Penghinaan halus', 'Pujian palsu']:
    g = D[D.penanda.map(lambda s: mk in s)]
    ec = collections.Counter(e for s in g.text.astype(str) for e in set(emo_re.findall(s)) if e not in '️')
    R.setdefault('penanda', {})[mk] = {'n': int(len(g)), 'pct_dari_kandidat': round(len(g) / max(R['n_kandidat'], 1) * 100, 2), 'emoji_top3': ec.most_common(3)}
R['multi_penanda'] = int((D.penanda.map(len) > 1).sum())
R['kandidat_periode'] = D.groupby('periode').kandidat_sindiran.agg(['sum', 'mean']).round(4).to_dict()
R['kandidat_emosi'] = D[D.kandidat_sindiran].predicted_emotion.value_counts().to_dict()
R['eng_kandidat_vs_bukan'] = {str(k): {'n': int(len(g)), 'rata': round(g.eng.mean(), 2), 'median': float(g.eng.median()), 'rata_view': round(g.view_count.mean(), 2)} for k, g in D.groupby('kandidat_sindiran')}
# puncak harian
pk = {}
for day in ['2026-04-12', '2026-05-10', '2026-05-13', '2026-05-23', '2026-05-24']:
    g = D[D.tgl == day]
    tags = collections.Counter(h.lower() for s in g.text.astype(str) for h in re.findall(r'#\w+', s))
    pk[day] = {'n': int(len(g)), 'isu': g.isu.value_counts().head(3).to_dict(), 'emosi': g.predicted_emotion.value_counts().head(3).to_dict(),
               'tagar': tags.most_common(6), 'kandidat_sindiran_pct': round(g.kandidat_sindiran.mean() * 100, 1),
               'akun_teratas': g.author_username.value_counts().head(3).to_dict(),
               'unggahan_viral': [s[:220].replace('\n', ' ') for s in g.sort_values('eng', ascending=False).text.astype(str).head(5)]}
R['puncak'] = pk
json.dump(R, open('bab45/hasil_isi_bab4.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
D[['id', 'tgl', 'periode', 'author_username', 'isu', 'isu_seri', 'kandidat_sindiran']].assign(penanda=D.penanda.map(lambda s: '; '.join(sorted(s)))).to_csv('bab45/kode_otomatis_isu_sindiran.csv', index=False)
# lembar pengodean: 150 sampel acak (seed 2026), label IndoBERT disembunyikan di sheet terpisah
S = D[~D.promo_pt].sample(150, random_state=2026)
lem = pd.DataFrame({'no': range(1, 151), 'tweet_id': S.id.astype('int64').astype(str), 'tanggal': S.tgl, 'teks': S.text,
                    'emosi_peneliti (Marah/Bahagia/Sedih/Tertarik/Netral/Percaya/Jijik/Kaget/Takut)': '', 'sindiran (Ya/Tidak)': '',
                    'jenis_penanda (Pembalik harapan/Penghinaan halus/Pujian palsu)': '', 'isu_peneliti': '', 'catatan': ''})
kunci = pd.DataFrame({'no': range(1, 151), 'tweet_id': lem.tweet_id, 'emosi_indobert': S.predicted_emotion.values, 'isu_kamus': S.isu.values, 'kandidat_sindiran_otomatis': S.kandidat_sindiran.values})
with pd.ExcelWriter('bab45/Lembar_Pengodean_150_Unggahan.xlsx') as w:
    lem.to_excel(w, 'Isi_oleh_peneliti', index=False); kunci.to_excel(w, 'Kunci_JANGAN_DIBUKA_dulu', index=False)
print(json.dumps({k: R[k] for k in ['isu', 'isu_seri', 'isu_tanpa_kata_kunci', 'n_kandidat', 'pct_kandidat', 'penanda', 'multi_penanda', 'eng_kandidat_vs_bukan', 'kandidat_emosi']}, ensure_ascii=False, default=str, indent=0)[:6000])
for d_, v in pk.items(): print(d_, v['n'], v['isu'], v['tagar'], v['akun_teratas'])
