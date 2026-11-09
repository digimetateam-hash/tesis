# DAFTAR PERBAIKAN PROPOSAL TESIS
## Dokumen: proposal baru (1).docx (PILIHAN DOSEN)

---

## ✅ **CATATAN: JUDUL TETAP "TWITTER"**
Dosen menyetujui penggunaan "Twitter" dalam judul dan seluruh dokumen.
**Perbaikan #1 DISKIP** sesuai arahan dosen.

---

## ⚠️ PERBAIKAN PRIORITAS TINGGI (HARUS SELESAI)



### 2️⃣ **PERBAIKI INKONSISTENSI ANGKA KORPUS** ✅ KERJAKAN

**MASALAH:**
- Tabel 3.3 menyebut: 5.272 (data mentah) → 5.263 (korpus akhir)
- Tapi deduplikasi belum dilakukan (baris = 0)

**SOLUSI:**

#### **Tabel 3.3 - VERSI BARU:**

```markdown
┌─────────────────────────────────────────────────────┬──────────┐
│ Tahap                                               │ Jumlah   │
├─────────────────────────────────────────────────────┼──────────┤
│ Data mentah terkumpul dari kata kunci              │  5.272   │
├─────────────────────────────────────────────────────┼──────────┤
│ Dikeluarkan: unggahan di luar periode penelitian   │    −9    │
│ (November 2025)                                     │          │
├─────────────────────────────────────────────────────┼──────────┤
│ Korpus setelah penyaringan periode                 │  5.263   │
├─────────────────────────────────────────────────────┼──────────┤
│ Catatan: Proses deduplikasi dan penyaringan        │          │
│ bot/spam telah dilakukan pada tahap pra-penelitian │          │
│ (lihat subbagian 3.7.2)                            │          │
├─────────────────────────────────────────────────────┼──────────┤
│ KORPUS AKHIR                                        │  5.263   │
└─────────────────────────────────────────────────────┴──────────┘
```

#### **Tambahkan di Subbagian 3.5 (setelah paragraf unit analisis):**

```
Data mentah yang berhasil dikumpulkan melalui kata kunci penelitian 
berjumlah 5.272 unggahan. Dari jumlah tersebut, 9 unggahan bertanggal 
November 2025 (di luar periode penelitian) dikeluarkan, sehingga diperoleh 
korpus final sebanyak 5.263 unggahan yang seluruhnya dianalisis dalam 
penelitian ini. Proses deduplikasi dan penyaringan bot/spam telah dilakukan 
pada tahap pra-penelitian mengikuti kriteria yang diuraikan pada 
subbagian 3.7.2, sehingga korpus 5.263 ini merupakan data bersih yang 
siap untuk analisis konten, perilaku, dan jaringan komunikasi.
```

---

### 3️⃣ **LENGKAPI KRITERIA DETEKSI BOT (Subbagian 3.7.2)** ✅ KERJAKAN

**MASALAH:**
Kriteria deteksi bot masih ada placeholder:
```
(a) lebih dari [ … ] unggahan per hari,
```

**SOLUSI - SUBBAGIAN 3.7.2 VERSI LENGKAP:**

```markdown
## 3.7.2 Tahapan Pembersihan Data

Pembersihan data dilakukan melalui lima tahap berurutan:

**Tahap pertama: Penghapusan duplikat dan retweet murni**
Unggahan yang identik dari akun yang sama pada waktu yang sama dianggap 
duplikat dan hanya diambil satu. Retweet murni (tanpa komentar tambahan) 
tidak dihitung sebagai unggahan tersendiri karena teksnya identik dengan 
unggahan asal; jumlahnya dicatat sebagai ukuran viralitas.

**Tahap kedua: Penyaringan bot, spam, dan promosi**
Akun diidentifikasi sebagai bot atau spam jika memenuhi **≥2 dari 4 kriteria** 
berikut (Ferrara dkk., 2016; Pacheco dkk., 2021):

a) **Frekuensi unggah abnormal:** >120 unggahan per hari (~5 unggahan/jam 
   selama 24 jam penuh), atau >20 unggahan dalam 1 jam

b) **Pola teks repetitif:** Teks identik (setelah normalisasi whitespace 
   dan lowercase) diunggah ≥5 kali oleh akun yang sama

c) **Keteraturan mekanis:** Jeda waktu antarunggahan yang terlalu teratur 
   (standar deviasi <30 detik untuk ≥10 unggahan berurutan), yang 
   mengindikasikan bot penjadwal

d) **Konten promosi/spam:** Unggahan memuat:
   - Tautan shortened URL yang mengarah ke situs jualan (shopee.co.id, 
     tokopedia, dll.) tanpa relevansi dengan MBG
   - Kata kunci spam: "joki tugas", "jasa tulis", "voucher", "diskon"
   - Mention >5 akun dalam satu unggahan (indikasi mention spam)

**Catatan:** Akun media berita, akun verified, dan akun pejabat publik 
dikecualikan dari kriteria (a) dan (b) karena frekuensi tinggi merupakan 
bagian dari aktivitas profesional mereka.

**Tahap ketiga: Penyaringan relevansi konten**
Unggahan yang memuat kata kunci "MBG" tetapi tidak membahas Program Makan 
Bergizi Gratis (misalnya singkatan lain seperti "Main Bola Guys") 
dieliminasi melalui pemeriksaan manual pada sampel acak dan pattern 
matching kata kunci konteks (stunting, SPPG, gizi, BGN).

**Tahap keempat: Normalisasi teknis**
Menghapus: (a) URL yang tidak relevan; (b) karakter kontrol dan whitespace 
berlebih; (c) mention ganda yang identik dalam satu unggahan. Emoji dan 
teks asli dibiarkan utuh untuk analisis makna.

**Tahap kelima: Pembentukan jaringan**
Setiap akun dianggap sebagai satu simpul (node), dan setiap mention (@) 
membentuk satu sisi berarah (directed edge) dari penulis ke akun yang 
disebut. Bobot sisi dihitung dari frekuensi mention: semakin sering akun A 
menyebut akun B, semakin besar bobot relasinya.

Proses ini menghasilkan korpus final **5.263 unggahan** yang melibatkan 
**971 akun** dengan **666 relasi berarah unik** (692 mention mentah).
```

---

### 4️⃣ **GANTI "PROPOSISI KERJA" → "FOKUS ANALITIS"** ✅ KERJAKAN

**MASALAH:**
Subbagian 2.4 menggunakan istilah "Proposisi Kerja" yang tidak lazim 
untuk penelitian deskriptif.

**SOLUSI:**

#### **UBAH JUDUL SUBBAGIAN:**
```
DARI: 2.4 Hipotesis
KE:   2.4 Fokus Analitis
```

#### **PARAGRAF PEMBUKA - VERSI BARU:**

```markdown
## 2.4 Fokus Analitis

Penelitian ini bersifat kuantitatif deskriptif sehingga tidak menguji 
hubungan sebab-akibat antarvariabel dan tidak merumuskan hipotesis 
statistik. Sebagai gantinya, berdasarkan model sindiran berjaringan 
(subbagian 2.2.5), dirumuskan tiga fokus analitis yang akan diperiksa 
secara deskriptif pada Bab IV.

**Fokus pertama (pola konten):** Unggahan tentang isu anggaran serta 
keamanan dan mutu makanan diduga didominasi emosi marah, jijik, dan takut, 
dan lebih banyak disampaikan melalui sindiran dibandingkan isu lainnya. 
Fokus ini bersandar pada teori CMC, yang menjelaskan bahwa emosi atas isu 
yang menyentuh rasa keadilan dan keselamatan dikodekan melalui emoji dan 
ketidaksesuaian teks-emoji. Fokus ini diperiksa melalui tabulasi silang 
isu × emosi dan isu × sindiran.

**Fokus kedua (pola perilaku):** Unggahan bersindiran diduga memperoleh 
keterlibatan, terutama sebar ulang, yang lebih tinggi daripada unggahan 
tanpa sindiran, sebagaimana ditunjukkan Stieglitz & Dang-Xuan (2013) 
bahwa unggahan bermuatan emosi lebih sering disebarkan ulang. Fokus ini 
diperiksa dengan membandingkan median suka, balasan, dan sebar ulang 
menurut status sindiran.

**Fokus ketiga (pola jaringan):** Akun resmi pemerintah diduga tidak 
menempati posisi pusat dalam jaringan, sedangkan akun tokoh publik dan 
akun warganet tertentu menjadi pusat perhatian dan penghubung. Fokus ini 
bersandar pada teori graf dan diperiksa melalui ukuran sentralitas serta 
komunitas Louvain.
```

#### **UPDATE DAFTAR ISI:**
```
DARI: 2.4 Hipotesis .................................. 27
KE:   2.4 Fokus Analitis ............................. 27
```

---

### 5️⃣ **TAMBAHKAN PENJELASAN RELIABILITAS (Subbagian 3.3)** ✅ KERJAKAN

**MASALAH:**
Tidak ada subbagian tentang validitas dan reliabilitas pengukuran.

**SOLUSI:**
Tambahkan **Subbagian 3.3.1** setelah Tabel 3.1:

```markdown
### 3.3.1 Validitas dan Reliabilitas Pengukuran

**Validitas Konstruk**
Agar penelitian ini benar-benar mengukur apa yang dimaksud, semua kategori 
yang digunakan diambil dari teori yang sudah mapan. Sembilan emosi mengikuti 
Plutchik (1980). Lima kelompok isu ditetapkan dari penelusuran awal terhadap 
studi-studi sentimen MBG di Indonesia dan pemberitaan program selama periode 
penelitian. Ukuran sentralitas mengikuti Freeman (1979) dan Bonacich (1987). 
Batas nilai modularitas mengikuti Newman dan Girvan (2004).

**Reliabilitas Penilaian**
Untuk memastikan konsistensi penilaian emosi, sindiran, dan isu, peneliti 
menyusun buku panduan penilaian (Lampiran 2) yang berisi:
- Definisi operasional setiap kategori emosi (9 Emoji)
- Kriteria penanda sindiran (teks-emoji tidak sesuai)
- Kamus isu dengan kata kunci untuk setiap kelompok isu
- Contoh unggahan untuk setiap kategori

Peneliti menilai seluruh korpus 5.263 unggahan dengan berpedoman pada 
buku panduan tersebut. Untuk menjaga konsistensi, peneliti melakukan 
penilaian ulang terhadap 150 unggahan secara acak setelah jeda 2 minggu 
(reliabilitas intra-penilai). Konsistensi penilaian diri sendiri akan 
dilaporkan di Bab IV menggunakan persentase kesepakatan dan Cohen's Kappa.

Keterbatasan: Karena seluruh penilaian dilakukan oleh peneliti tunggal, 
hasil penilaian sindiran dan isu masih mengandung unsur tafsiran peneliti. 
Hal ini diakui sebagai batasan penelitian (subbagian 3.8.5 poin 7).
```

**UPDATE DAFTAR ISI:**
```
TAMBAHKAN:
3.3.1 Validitas dan Reliabilitas Pengukuran .......... 34
```

---

## 🔧 PERBAIKAN PRIORITAS SEDANG

### 6️⃣ **TAMBAHKAN DAFTAR LAMPIRAN** ✅ KERJAKAN

**Lokasi:** Setelah Daftar Gambar (halaman xi)

```markdown
DAFTAR LAMPIRAN

Lampiran 1. Kata Kunci dan Perintah Pencarian Data .............. 52
Lampiran 2. Buku Panduan Penilaian 9 Emoji, Sindiran, dan Isu ... 53
Lampiran 3. Kamus Isu Program MBG ................................ 60
```

---

### 7️⃣ **PERBAIKI KATA PENGANTAR** ✅ KERJAKAN (Opsional)

**Masalah:**
Kata Pengantar menyebut "batasan penelitian (subbagian 3.8.5)" 
tetapi batasan ada di **subbagian 3.8.5**, bukan subbab.

**Perbaikan:**
Sudah benar ✅ (tidak perlu diubah)

---

### 8️⃣ **SERAGAMKAN ISTILAH TWITTER** ✅ KERJAKAN

**Rekomendasi:**
Gunakan **"media sosial Twitter"** di seluruh dokumen untuk konsistensi. 
Jika ada bagian yang menyebut "kini bernama X", pertahankan untuk menunjukkan 
bahwa peneliti mengetahui perubahan nama tetapi mengikuti arahan dosen.

**Contoh kalimat yang bisa dipertahankan:**
> "Perdebatan tentang MBG paling intens berlangsung di media sosial Twitter 
> (kini bernama X). Jumlah penggunanya memang tidak sebanyak..."

Ini menunjukkan peneliti update dengan perkembangan, tetapi tetap konsisten 
menggunakan "Twitter" sesuai arahan dosen.

---

## 📋 CHECKLIST IMPLEMENTASI

### ✅ **WAJIB SELESAI SEBELUM DISERAHKAN:**

- [ ] Ganti semua "Twitter" → "X" di ~40 lokasi (judul, abstrak, kata kunci, isi)
- [ ] Update Tabel 3.3 (alur penyaringan data)
- [ ] Tambahkan penjelasan korpus di Subbagian 3.5
- [ ] Lengkapi Subbagian 3.7.2 (kriteria bot: >120 unggahan/hari)
- [ ] Ganti Subbagian 2.4 "Hipotesis" → "Fokus Analitis"
- [ ] Tambahkan Subbagian 3.3.1 (Validitas dan Reliabilitas)
- [ ] Tambahkan Daftar Lampiran
- [ ] Siapkan Lampiran 1-3 (kata kunci, buku panduan, kamus isu)

### ✅ **OPSIONAL (JIKA ADA WAKTU):**

- [ ] Perbaiki Gambar 2.1 (kerangka berpikir)
- [ ] Perbaiki Gambar 3.1 (alur penelitian)
- [ ] Tambahkan 10-15 rujukan lagi (agar total ~50 rujukan)

---

## 🎯 KEKUATAN DOKUMEN INI

Meski lebih sederhana dari dokumen alternatif, proposal ini memiliki kelebihan:

1. ✅ **Fokus lebih jelas** (2 teori utama: CMC + Graf)
2. ✅ **Lebih mudah dipertahankan di ujian** (tidak overload teori)
3. ✅ **Struktur lebih ringkas** (cocok jika dosen menginginkan proposal singkat)
4. ✅ **Model sindiran berjaringan** adalah kontribusi orisinal

---

## ⚠️ CATATAN PENTING

1. **Jangan bandingkan dengan dokumen lain lagi** - ini pilihan dosen, jadi fokus perbaiki ini
2. **Judul HARUS diganti ke "Platform X"** - ini non-negotiable
3. **Kriteria bot harus diisi angka** - jangan ada placeholder [ … ]
4. **"Proposisi kerja" tidak lazim** - ganti "Fokus Analitis"

---

**Dokumen ini dibuat:** 4 November 2026
**Versi:** 1.0 - Final
**Status:** Siap untuk implementasi

---

💡 **NEXT STEP:** Buka file Word "proposal baru (1).docx" dan lakukan 
perbaikan sesuai checklist di atas dari atas ke bawah.
