<div style="page-break-before: always"></div>

<!-- hlm. 65 -->

# LAMPIRAN

## LAMPIRAN 1
## Kata Kunci dan Parameter Pencarian Data dengan NodeXL Pro dan Brand24

### A. String Pencarian NodeXL Pro

**Platform:** Twitter (X)  
**Periode:** 2 Maret 2026 – 24 Mei 2026  
**Bahasa:** Indonesia  
**Jenis data:** Unggahan publik (termasuk reply dan quote tweet)

**String pencarian:**
```
"Makan Bergizi Gratis" OR "MBG" OR "Makan Siang Gratis" OR #MakanBergizisGratis OR #MBG
```

**Parameter tambahan:**
- Filter bahasa: `lang:id` (bahasa Indonesia)
- Exclude retweet murni: `-filter:retweets`
- Hanya unggahan publik (akun non-private)

<!-- hlm. 66 -->

### B. Atribut Data yang Dikumpulkan

| No | Atribut | Keterangan |
|---|---|---|
| 1 | Tweet ID | ID unik setiap unggahan |
| 2 | Text | Teks lengkap unggahan beserta emoji |
| 3 | Created At | Tanggal dan waktu unggah (format: YYYY-MM-DD HH:MM:SS) |
| 4 | Author | Username akun penulis (dengan @) |
| 5 | Author Followers | Jumlah pengikut akun penulis |
| 6 | Tweet Type | Jenis unggahan (original, reply, quote) |
| 7 | In Reply To | Akun yang dibalas (jika reply) |
| 8 | Mentioned Users | Daftar akun yang disebut dengan @ |
| 9 | Like Count | Jumlah suka |
| 10 | Reply Count | Jumlah balasan |
| 11 | Retweet Count | Jumlah sebar ulang |
| 12 | Quote Count | Jumlah kutipan |
| 13 | Views | Jumlah tayangan (jika tersedia) |

### C. Pengaturan Brand24

**Proyek:** Program MBG Twitter Monitoring  
**Periode monitoring:** 2 Maret 2026 – 24 Mei 2026  
**Sumber data:** Import CSV dari NodeXL Pro

**Metric yang dianalisis:**
1. **Reach:** Estimasi jangkauan berdasarkan jumlah pengikut × engagement rate
2. **Interaction Rate:** (Like + Reply + Retweet + Quote) ÷ Followers × 100%
3. **Virality Score:** Retweet ÷ (Like + Reply) × 100
4. **Influence Score:** Skor gabungan (40% reach + 30% interaction + 30% centrality)

<!-- hlm. 67 -->

### D. Workflow Integrasi Data

```
1. NodeXL Pro → Twitter API → Download data mentah (5.272 unggahan)
         ↓
2. Filter periode → Buang Nov 2025 (9 unggahan) → 5.263 unggahan
         ↓
3. Export to CSV → File: mbg_data_5263.csv
         ↓
4. Import ke Brand24 → Custom Data Import
         ↓
5. Brand24 → Enrichment: tambah data profil akun (followers, bio, lokasi)
         ↓
6. Brand24 → Calculate: reach, interaction rate, influence score
         ↓
7. Export dari Brand24 → File: mbg_engagement_analysis.xlsx
         ↓
8. Merge dengan NodeXL → Gabung data engagement + network centrality
         ↓
9. Final dataset → 5.263 unggahan + 971 akun + metrics lengkap
         ↓
10. Pembersihan data (Subbagian 3.7.2) → Siap analisis
```

### E. Catatan Teknis

1. **Deduplikasi:** Unggahan identik dari akun + waktu yang sama hanya diambil 1×
2. **Bot filtering:** Akun yang memenuhi ≥2 dari 4 kriteria bot dikeluarkan (lihat Subbagian 3.7.2)
3. **Missing data:** Jika "views" tidak tersedia, estimasi reach menggunakan rumus Brand24: `Followers × (1 + Retweet Rate)`
4. **Emoji handling:** Emoji dipertahankan dalam format Unicode asli untuk analisis
5. **Mention extraction:** Setiap @ dalam teks diekstrak sebagai directed edge dalam jaringan

---

<!-- hlm. 68 -->

## LAMPIRAN 2
## Buku Panduan Penilaian 9 Emoji, Sindiran, dan Isu

### A. Definisi Operasional Sembilan Kategori Emosi

| Emoji | Kategori | Definisi Operasional | Kata Kunci dalam Teks |
|---|---|---|---|
| 😡 | Marah | Perasaan kesal karena merasa diperlakukan tidak adil atau janji tidak ditepati | "kecewa", "bohong", "tipu", "maling", "korupsi", "gagal", tone mengecam |
| 😊 | Bahagia | Perasaan senang karena sesuatu berhasil atau harapan terwujud | "alhamdulillah", "senang", "terima kasih", "bagus", "mantap", tone memuji tulus |
| 😢 | Sedih | Perasaan sedih karena kehilangan sesuatu atau kecewa | "kasihan", "prihatin", "sedih", "miris", "anak-anak kelaparan", tone berempati |
| 🤔 | Tertarik | Perasaan penasaran atau ingin tahu saat menemukan informasi baru | "gimana ya", "kok bisa", "penasaran", "info dong", tone bertanya netral |
| 😐 | Netral | Unggahan tidak menunjukkan perasaan yang kuat | Hanya menyampaikan fakta, angka, berita tanpa opini; tone informatif |
| 🤝 | Percaya | Perasaan yakin bahwa sumber informasi dapat dipercaya | "yakin", "percaya", "pasti bisa", "BGN terpercaya", tone mendukung pemerintah |
| 🤢 | Jijik | Perasaan muak atau menolak terhadap sesuatu yang dianggap tidak pantas | "jorok", "kotor", "menjijikkan", "ngeri", tone menolak dengan keras |
| 😲 | Kaget | Reaksi emosi saat menerima informasi yang tidak disangka-sangka | "loh", "kok", "gila", "astaga", "serius?!", tone terkejut |
| 😨 | Takut | Perasaan khawatir atau cemas karena merasa ada bahaya atau risiko | "bahaya", "khawatir", "takut", "ngeri", "keracunan", tone warning |

<!-- hlm. 69 -->

### B. Kriteria Penanda Sindiran

Unggahan dikategorikan **SINDIRAN** jika memenuhi salah satu dari kriteria berikut:

#### 1. Pembalik Harapan

Penulis menyampaikan sesuatu yang terdengar positif, tapi konteksnya jelas negatif, sehingga terasa ironis.

**Ciri-ciri:**
- Kata-kata pujian + konteks kegagalan program
- Emoji tertawa/badut setelah keluhan
- Frasa "ternyata", "hebat ya", "keren nih"

**Contoh:**
> "Wah hebat ya programnya triliun-triliunan, anak-anak malah keracunan 🤡"

#### 2. Penghina Halus

Penulis tidak langsung menghina, tapi menyiratkan bahwa pihak tertentu konyol/bodoh.

**Ciri-ciri:**
- Emoji badut 🤡 atau wajah terbalik 🙃
- Pertanyaan retoris yang mengejek
- Membandingkan dengan kasus lain untuk merendahkan

**Contoh:**
> "Anggaran Rp335T tiba-tiba jadi Rp268T... math nya gimana sih? 🙃"

#### 3. Pujian Palsu

Penulis memuji berlebihan padahal maksudnya mengejek.

**Ciri-ciri:**
- Deretan emoji malaikat 😇😇😇 atau tepuk tangan 👏👏👏
- Kata "katanya", "konon", dalam tanda kutip "..."
- Pujian yang tidak masuk akal/berlebihan

**Contoh:**
> "Demi program 'perbaikan gizi' tapi dapur fiktif 😇😇😇"

<!-- hlm. 70 -->

### C. Penanda **BUKAN SINDIRAN**

Unggahan dikategorikan **TIDAK SINDIRAN** jika:

1. **Kritik lugas:** Marah/kecewa disampaikan secara langsung tanpa pura-pura memuji
   - Contoh: "Program MBG gagal total! Banyak anak keracunan 😡"

2. **Pujian tulus:** Senang dengan program, emoji sesuai dengan teks positif
   - Contoh: "Alhamdulillah anak saya dapat makan bergizi gratis, terima kasih pemerintah 😊"

3. **Netral informatif:** Hanya menyampaikan fakta tanpa opini
   - Contoh: "Anggaran MBG 2026 dipangkas dari Rp335T menjadi Rp268T (sumber: ANTARA)"

### D. Kamus Isu (5 Kelompok Utama)

| No | Kelompok Isu | Kata Kunci (contoh) | Definisi |
|---|---|---|---|
| 1 | **Manfaat Gizi dan Sosial** | "stunting", "gizi anak", "kesehatan", "tumbuh kembang", "perbaikan gizi", "menu sehat" | Unggahan yang membahas tujuan program, manfaat kesehatan, atau dampak positif terhadap anak |
| 2 | **Pelaksanaan & Distribusi** | "pembagian", "tempe separo", "porsi", "akses", "pemerataan", "daerah terpencil", "distribusi" | Unggahan tentang proses pembagian makanan, masalah logistik, ketidakmerataan akses |
| 3 | **Keamanan & Mutu Makanan** | "keracunan", "kadaluarsa", "kotor", "tidak layak", "kualitas", "kebersihan", "BPOM" | Unggahan tentang kasus keracunan, kualitas makanan buruk, atau masalah keamanan pangan |
| 4 | **Anggaran & Akuntabilitas** | "Rp335T", "Rp268T", "korupsi", "dapur fiktif", "rekening ganda", "transparansi", "audit" | Unggahan tentang pemangkasan anggaran, dugaan korupsi, pengadaan fiktif, pertanggungjawaban |
| 5 | **Politik & Ekonomi** | "Prabowo", "pemilu", "janji kampanye", "politik pencitraan", "impor", "ompreng", "ekonomi" | Unggahan yang mengaitkan MBG dengan politik, pencitraan, atau dampak ekonomi makro |
| 6 | **Lainnya** | - | Unggahan yang tidak masuk ke 5 kategori di atas |

<!-- hlm. 71 -->

### E. Prosedur Penilaian

**Langkah 1:** Baca teks unggahan lengkap + emoji + konteks isu

**Langkah 2:** Tentukan emosi dominan (pilih 1 dari 9 kategori)
- Prioritas: Jika ada konflik emosi, pilih yang paling kuat
- Jika benar-benar netral (hanya fakta), pilih 😐 Netral

**Langkah 3:** Periksa sindiran
- Apakah ada ketidaksesuaian teks vs emoji?
- Apakah ada penanda sindiran (pembalik harapan / penghina halus / pujian palsu)?
- Jika YA → catat jenis penandanya
- Jika TIDAK → catat "tidak sindiran"

**Langkah 4:** Tentukan isu dominan (pilih 1 dari 6 kategori)
- Gunakan kamus isu untuk mencocokkan kata kunci
- Jika membahas >1 isu, pilih yang paling menonjol
- Jika tidak jelas, pilih "Lainnya"

**Langkah 5:** Catat hasil penilaian ke spreadsheet:

| Tweet ID | Text | Emosi | Sindiran | Jenis Penanda | Isu |
|---|---|---|---|---|---|
| 12345... | "Wah hebat..." | Marah | Ya | Pembalik harapan | Anggaran & Akuntabilitas |

### F. Contoh Penilaian Lengkap

**Unggahan 1:**
> "Anggaran MBG Rp268 triliun untuk 27.952 SPPG, realisasi Rp75 triliun per 30 April 2026 (sumber: ANTARA)"

- **Emosi:** 😐 Netral (hanya menyampaikan fakta)
- **Sindiran:** Tidak
- **Isu:** Anggaran & Akuntabilitas

**Unggahan 2:**
> "Alhamdulillah anak saya akhirnya dapat makanan bergizi gratis di sekolah 😊 Terima kasih Pak Prabowo!"

- **Emosi:** 😊 Bahagia (senang, berterima kasih)
- **Sindiran:** Tidak
- **Isu:** Manfaat Gizi dan Sosial

**Unggahan 3:**
> "Program 'perbaikan gizi' katanya, tapi kok banyak anak keracunan ya? 🤡"

- **Emosi:** 😡 Marah (kecewa dengan program)
- **Sindiran:** Ya → Pujian Palsu (kata "katanya" + emoji badut)
- **Isu:** Keamanan & Mutu Makanan

---

<!-- hlm. 72 -->

## LAMPIRAN 3
## Kamus Isu Program Makan Bergizi Gratis (MBG)

### Kelompok 1: Manfaat Gizi dan Sosial

**Kata kunci positif:**
- stunting, gizi, nutrisi, kesehatan, tumbuh kembang, perkembangan anak
- menu sehat, makanan bergizi, protein, vitamin, sayur, buah
- perbaikan, peningkatan, manfaat, dampak positif, anak sehat
- prestasi belajar, konsentrasi, fokus, energi, kecerdasan

**Kata kunci netral/campuran:**
- sasaran penerima, ibu hamil, anak balita, anak sekolah
- capaian, target, penerima manfaat, cakupan program

**Frasa khas:**
- "agar anak tidak stunting"
- "meningkatkan gizi anak Indonesia"
- "dukung tumbuh kembang optimal"

---

### Kelompok 2: Pelaksanaan dan Distribusi

**Kata kunci teknis:**
- SPPG, dapur, pelayanan, distribusi, pembagian, penyaluran
- logistik, pengiriman, akses, pemerataan, jangkauan
- daerah terpencil, 3T (terdepan terluar tertinggal), pelosok
- jadwal, frekuensi, reguler, konsistensi

**Kata kunci masalah:**
- telat, terlambat, tidak merata, timpang, diskriminasi
- tempe separo, porsi kecil, kurang, tidak cukup
- antri, rebutan, kehabisan, tidak kebagian
- jauh, sulit dijangkau, belum tercover

**Frasa khas:**
- "pembagian tidak merata"
- "daerah terpencil belum mendapat"
- "porsinya kok cuma tempe separo"

<!-- hlm. 73 -->

### Kelompok 3: Keamanan dan Mutu Makanan

**Kata kunci bahaya:**
- keracunan, diare, muntah, sakit perut, mual
- kadaluarsa, expired, basi, busuk, berjamur
- tidak layak, tidak higienis, jorok, kotor, najis
- kontaminasi, bakteri, E.coli, salmonella

**Kata kunci kualitas:**
- mutu, kualitas, standar, BPOM, sertifikasi, izin edar
- kebersihan, sanitasi, IPAL, SLHS (Sertifikat Laik Hygiene Sanitasi)
- inspeksi, pemeriksaan, audit, pengawasan
- wadah, kemasan, food tray, ompreng (wadah impor)

**Frasa khas:**
- "puluhan anak keracunan"
- "makanan tidak layak konsumsi"
- "dapur tidak bersih"
- "wadah makanan impor dari China"

---

### Kelompok 4: Anggaran dan Akuntabilitas

**Kata kunci fiskal:**
- Rp71 triliun, Rp335 triliun, Rp268 triliun, Rp67 triliun (BA BUN)
- anggaran, pagu, alokasi, realisasi, serapan
- pemangkasan, pemotongan, pengurangan, revisi, penyesuaian
- APBN, APBD, keuangan negara, Kemenkeu

**Kata kunci akuntabilitas:**
- korupsi, markup, inflasi harga, penggelembungan
- dapur fiktif, rekening ganda, pengadaan fiktif
- audit, BPK, KPK, transparansi, pertanggungjawaban
- suspend, dihentikan sementara, ditangguhkan, sanksi

**Kata kunci lembaga:**
- BGN (Badan Gizi Nasional), Dadan Hindayana
- SPPG (Satuan Pelayanan Pemenuhan Gizi)
- Kemenkeu, Kementerian Keuangan, Sri Mulyani (jika disebut)

**Frasa khas:**
- "anggaran Rp335T dipangkas jadi Rp268T"
- "dapur MBG fiktif dikembalikan Rp311 miliar"
- "1.152 SPPG masih ditangguhkan"
- "transparansi dana MBG"

<!-- hlm. 74 -->

### Kelompok 5: Politik dan Ekonomi

**Kata kunci politik:**
- Prabowo, presiden, pemerintah, rezim, kampanye
- janji politik, janji kampanye, pencitraan, popularitas
- oposisi, kritik, pro-kontra, polemik, kontroversi
- pemilu, Pilpres 2024, koalisi, partai

**Kata kunci ekonomi:**
- impor, ekspor, perdagangan, industri lokal, UMKM
- ompreng (wadah makanan impor), food tray, pengusaha lokal
- ekonomi makro, inflasi, defisit, utang negara
- lapangan kerja, tenaga kerja, PHK

**Kata kunci dampak sosial:**
- kesenjangan, ketimpangan, kelas menengah, rakyat kecil
- subsidi, bantuan sosial, program sosial, jaring pengaman
- keadilan sosial, pemerataan kesejahteraan

**Frasa khas:**
- "janji kampanye Prabowo"
- "hanya pencitraan politik"
- "kenapa impor ompreng, bukan produk lokal?"
- "triliun rupiah untuk popularitas"

---

### Kelompok 6: Lainnya

**Termasuk di sini:**
- Unggahan yang membahas hal-hal di luar 5 kelompok utama
- Meme/lelucon tanpa isu spesifik yang jelas
- Promosi produk/jasa yang tidak relevan
- Spam atau unggahan tidak jelas konteksnya

**Catatan:** Jika unggahan menyinggung >1 isu, pilih isu yang paling dominan (paling banyak kata kunci atau paling ditekankan oleh penulis).

---

<!-- hlm. 75 -->

## LAMPIRAN 4
## Laporan Identifikasi Influencer dari Brand24

### A. Kriteria Influencer

Akun dikategorikan sebagai **influencer** dalam wacana MBG apabila memenuhi minimal **2 dari 3 kriteria** berikut berdasarkan analisis Brand24:

1. **Reach tinggi:** Jumlah pengikut (followers) ≥10.000 dan estimasi reach per unggahan ≥50.000 tayangan.

2. **Interaction rate tinggi:** Rasio keterlibatan (like + reply + retweet + quote) terhadap jumlah pengikut ≥2% untuk minimal 3 unggahan tentang MBG.

3. **Network centrality tinggi:** Masuk dalam 10 besar peringkat in-degree (paling banyak disebut) atau betweenness centrality (penghubung utama antarkomunitas) berdasarkan analisis jaringan NodeXL Pro.

---

### B. Daftar Top 20 Influencer

Tabel berikut menampilkan 20 akun dengan pengaruh tertinggi dalam wacana MBG periode 2 Maret–24 Mei 2026 berdasarkan skor gabungan dari ketiga kriteria di atas. Skor pengaruh (influence score) dihitung secara otomatis oleh Brand24 dengan bobot: **40% reach + 30% interaction rate + 30% network centrality**.

| No | Username | Followers | Avg. Reach | Interact. % | Infl. Score | Jenis Akun |
|---|---|---|---|---|---|---|
| 1 | [NAMA_AKUN_1] | [DATA] | [DATA] | [DATA] | [DATA] | [Jenis] |
| 2 | [NAMA_AKUN_2] | [DATA] | [DATA] | [DATA] | [DATA] | [Jenis] |
| 3 | [NAMA_AKUN_3] | [DATA] | [DATA] | [DATA] | [DATA] | [Jenis] |
| ... | ... | ... | ... | ... | ... | ... |
| 20 | [NAMA_AKUN_20] | [DATA] | [DATA] | [DATA] | [DATA] | [Jenis] |

**Catatan:** Data username sebenarnya akan dilengkapi pada fase analisis data (Bab IV).

<!-- hlm. 76 -->

### C. Kategorisasi Influencer Berdasarkan Jenis Akun

Brand24 secara otomatis mengklasifikasikan influencer berdasarkan jenis akun:

1. **Media Berita:** Akun media massa dan portal berita (contoh: @detikcom, @kompascom) – [X] akun ([X]%)

2. **Tokoh Publik:** Politisi, aktivis, akademisi, dan public figure lainnya – [X] akun ([X]%)

3. **Warganet Biasa:** Akun individu tanpa afiliasi institusional yang memiliki pengaruh tinggi karena frekuensi unggah dan kualitas konten – [X] akun ([X]%)

4. **Organisasi/Lembaga:** Akun resmi lembaga pemerintah, NGO, atau organisasi masyarakat sipil – [X] akun ([X]%)

---

### D. Pola Engagement Influencer

Analisis temporal Brand24 menunjukkan bahwa influencer paling aktif pada:

- **Minggu pertama Maret 2026:** Peluncuran awal program (volume unggahan tertinggi)

- **Pertengahan April 2026:** Kontroversi pemberhentian ribuan SPPG (puncak interaction rate)

- **Akhir Mei 2026:** Penyesuaian anggaran dari Rp335T ke Rp268T (puncak sentimen negatif)

---

### E. Metode Identifikasi

Data influencer diperoleh melalui tahapan berikut:

1. Data mentah 5.263 unggahan dari NodeXL Pro diekspor dalam format CSV
2. File CSV diimpor ke Brand24 menggunakan fitur "Custom Data Import"
3. Brand24 secara otomatis memperkaya data dengan informasi profil akun (jumlah pengikut, bio, lokasi) melalui Twitter API
4. Algoritma Brand24 menghitung reach estimation, interaction rate, dan influence score untuk setiap akun
5. Hasil analisis diekspor dalam format Excel untuk digabungkan dengan data sentralitas dari NodeXL Pro

Hasil akhir berupa daftar influencer yang diurutkan berdasarkan skor pengaruh gabungan (influence score) kemudian digunakan untuk interpretasi pada Bab IV, khususnya dalam menjawab rumusan masalah ketiga tentang struktur jaringan dan aktor dominan.
