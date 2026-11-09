import pandas as pd, numpy as np, networkx as nx, re, json, collections
R={}
d=pd.read_csv('data/indobert_9_emosi_fixed.csv',low_memory=False)
d['t']=pd.to_datetime(d.created_at,utc=True,errors='coerce').dt.tz_convert('Asia/Jakarta')
d=d[d.t.notna()].copy()
d['periode']=np.where(d.t<pd.Timestamp('2026-05-01',tz='Asia/Jakarta'),'P1','P2')
d['tgl']=d.t.dt.date.astype(str)
R['n_posts']=len(d); R['n_akun']=int(d.author_username.nunique())
R['per_periode']=d.periode.value_counts().to_dict()
R['akun_per_periode']=d.groupby('periode').author_username.nunique().to_dict()
R['rentang']=[str(d.t.min()),str(d.t.max())]
day=d.groupby('tgl').size(); R['hari_aktif']=int(len(day)); R['top_hari']=day.sort_values(ascending=False).head(8).to_dict()
R['rata_per_hari_periode']={p:round(g.groupby('tgl').size().mean(),1) for p,g in d.groupby('periode')}
R['median_per_hari']=float(day.median())
wk=d.set_index('t').resample('W-SUN').size(); R['mingguan']={str(k.date()):int(v) for k,v in wk.items()}
mp={'disgust':'Jijik','trust':'Percaya','neutral':'Netral','anticipation':'Tertarik','joy':'Bahagia','anger':'Marah','surprise':'Kaget','sadness':'Sedih','fear':'Takut'}
d['emosi']=d.predicted_emotion.map(lambda x: mp.get(str(x).lower(),str(x)))
R['emosi']=d.emosi.value_counts().to_dict()
R['emosi_periode']=pd.crosstab(d.emosi,d.periode).to_dict()
R['emosi_periode_pct']=(pd.crosstab(d.emosi,d.periode,normalize='columns')*100).round(2).to_dict()
EM=re.compile('[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF⭐⭕‼⁉™ℹ↔-↪⌚-⏿▪-◾⤴⤵〰〽㊗㊙]')
SK=set('‍️\U0001F3FB\U0001F3FC\U0001F3FD\U0001F3FE\U0001F3FF')
cnt=collections.Counter(); posts_with=0; perpost=collections.Counter()
for t in d.text.astype(str):
    e=[ch for ch in EM.findall(t) if ch not in SK]
    if e: posts_with+=1
    cnt.update(e); perpost.update(set(e))
R['emoji_unggahan_memuat']=posts_with; R['emoji_total']=sum(cnt.values()); R['emoji_jenis']=len(cnt)
R['emoji_top10']=[(k,v,perpost[k]) for k,v in cnt.most_common(10)]
for k in ['like_count','retweet_count','reply_count','quote_count','view_count']: d[k]=pd.to_numeric(d[k],errors='coerce').fillna(0)
d['eng']=d[['like_count','retweet_count','reply_count','quote_count']].sum(axis=1)
def summ(g):
    return {k:{'jumlah':int(g[k].sum()),'rata':round(g[k].mean(),2),'median':float(g[k].median())} for k in ['like_count','retweet_count','reply_count','quote_count','view_count','eng']}
R['eng_total']=summ(d); R['eng_periode']={p:summ(g) for p,g in d.groupby('periode')}
R['nol_keterlibatan']=int((d.eng==0).sum())
R['eng_konsentrasi_top1pct']=round(d.eng.nlargest(int(len(d)*0.01)).sum()/d.eng.sum()*100,2)
R['eng_konsentrasi_top10pct']=round(d.eng.nlargest(int(len(d)*0.10)).sum()/d.eng.sum()*100,2)
R['eng_emosi']=d.groupby('emosi').agg(n=('eng','size'),rata_eng=('eng','mean'),median_eng=('eng','median'),rata_like=('like_count','mean'),rata_rt=('retweet_count','mean'),rata_reply=('reply_count','mean'),rata_view=('view_count','mean')).round(2).sort_values('n',ascending=False).to_dict('index')
ac=d.groupby('author_username').agg(unggahan=('id','size'),eng=('eng','sum')).sort_values('unggahan',ascending=False)
R['akun_aktif_top10']=ac.head(10).reset_index().values.tolist()
R['akun_1_unggahan']=int((ac.unggahan==1).sum())
R['akun_eng_top10']=ac.sort_values('eng',ascending=False).head(10).reset_index().values.tolist()
# network
E=pd.read_excel('NodeXL_MBG_Tesis_Indri_Anjar.xlsx',sheet_name='Edges')
E['Vertex 1']=E['Vertex 1'].astype(str).str.strip(); E['Vertex 2']=E['Vertex 2'].astype(str).str.strip()
G=nx.DiGraph(); G.add_edges_from(E[['Vertex 1','Vertex 2']].itertuples(index=False))
R['net']={'akun':G.number_of_nodes(),'relasi_baris':len(E),'relasi_unik':G.number_of_edges(),'kepadatan':round(nx.density(G),6),'komponen':nx.number_weakly_connected_components(G),'selfloop':nx.number_of_selfloops(G)}
H=G.copy(); H.remove_edges_from(nx.selfloop_edges(H))
R['net']['timbal_balik_pct']=round(nx.reciprocity(H)*100,2)
wcc=sorted(nx.weakly_connected_components(G),key=len,reverse=True); R['net']['komponen_terbesar']=len(wcc[0]); R['net']['ukuran_komponen_top5']=[len(c) for c in wcc[:5]]
R['net']['komponen_ukuran2']=sum(1 for c in wcc if len(c)==2)
ind=dict(G.in_degree()); outd=dict(G.out_degree())
R['net']['akun_disebut']=sum(1 for v in ind.values() if v>0); R['net']['akun_menyebut']=sum(1 for v in outd.values() if v>0)
top=lambda m,n=10: sorted(m.items(),key=lambda x:-x[1])[:n]
R['net']['top_in']=top(ind); R['net']['top_out']=top(outd); R['net']['top_total']=top({k:ind[k]+outd[k] for k in G})
bc=nx.betweenness_centrality(G,normalized=True); R['net']['top_betweenness']=[(k,round(v,6)) for k,v in top(bc,5)]
V=pd.read_excel('NodeXL_MBG_Tesis_Indri_Anjar.xlsx',sheet_name='Vertices')
cm=dict(zip(V.Vertex.astype(str).str.strip(),V.Community))
U=H.to_undirected(); grp=collections.defaultdict(set)
for n in U: grp[cm.get(n,'na_'+n)].add(n)
comms=sorted(grp.values(),key=len,reverse=True)
R['net']['komunitas']=len(comms); R['net']['modularitas']=round(nx.community.modularity(U,comms),4)
R['net']['komunitas_top10']=[(len(c),sorted(c,key=lambda n:-(ind[n]+outd[n]))[0]) for c in comms[:10]]
R['net']['komunitas_ukuran_ge5']=sum(1 for c in comms if len(c)>=5)
for p,lo,hi in [('P1','2026-03-01','2026-05-01'),('P2','2026-05-01','2026-06-01')]:
    t=pd.to_datetime(E['Date']); e=E[(t>=lo)&(t<hi)]
    g=nx.DiGraph(); g.add_edges_from(e[['Vertex 1','Vertex 2']].itertuples(index=False))
    h=g.copy(); h.remove_edges_from(nx.selfloop_edges(h))
    R['net'][p]={'akun':g.number_of_nodes(),'relasi_unik':g.number_of_edges(),'kepadatan':round(nx.density(g),6),'komponen':nx.number_weakly_connected_components(g),'timbal_balik_pct':round(nx.reciprocity(h)*100,2) if h.number_of_edges() else 0,'top_in':top(dict(g.in_degree()),3),'top_out':top(dict(g.out_degree()),3)}
json.dump(R,open('bab45/hasil_bab4.json','w'),ensure_ascii=False,indent=1,default=str)
print(json.dumps(R,ensure_ascii=False,default=str)[:9000])
