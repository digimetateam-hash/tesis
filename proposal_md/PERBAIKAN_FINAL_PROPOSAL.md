# PERBAIKAN FINAL PROPOSAL TESIS
## Dokumen: proposal baru (1).docx

---

## ✅ CATATAN PENTING
- **Judul tetap "TWITTER"** sesuai arahan dosen
- **Lakukan perbaikan #2-8** dari daftar sebelumnya
- **Tambahan:** Penelitian terdahulu + penjelasan NodeXL untuk pengumpulan data

---

## 1️⃣ TAMBAHKAN PENELITIAN TERDAHULU MBG DARI JURNAL BEREPUTASI

### **LOKASI: Tabel 2.1 - Tambahkan SEBELUM baris "Penelitian ini (2026)"**

**PENELITIAN BARU YANG DITAMBAHKAN:**

| No | Penulis (Tahun) | Judul | Metode | Celah Penelitian | Jurnal |
|----|-----------------|-------|--------|------------------|---------|
| **6** | **Sianturi dkk. (2025)** | **Politics on a Plate: Equivocal Communication in Indonesian Presidential Nutrition Policy** | **Analisis sentimen atas 4.041 laporan berita di media sosial menggunakan Talkwalker Analytics (6-12 Januari 2025)** | **Sentimen negatif dominan (41,2%), positif 13,1%, netral 45,7%; fokus pada komunikasi pemerintah, tidak menganalisis sindiran, emoji, atau struktur jaringan penyebar** | **Frontiers in Communication (Scopus Q2)** |

**PENJELASAN UNTUK DIMASUKKAN KE SUBBAGIAN 2.1:**

Tambahkan paragraf ini SETELAH paragraf "Penelusuran melalui Google Scholar..." dan SEBELUM paragraf "Dari pemetaan tersebut...":

```markdown
Selain kelima studi internasional di atas, penelusuran juga menemukan satu studi 
MBG yang terbit di jurnal terindeks Scopus. Sianturi, Lestari, Purba, Karim, dan 
Mulyani (2025) menganalisis sentimen 4.041 laporan berita di media sosial tentang 
MBG menggunakan Talkwalker Analytics pada periode 6–12 Januari 2025. Mereka 
menemukan bahwa sentimen negatif mendominasi (41,2%), diikuti netral (45,7%) 
dan positif (13,1%). Studi tersebut berfokus pada komunikasi pemerintah yang 
ambigu (equivocal communication), tetapi belum menganalisis sindiran, emoji, 
atau struktur jaringan penyebar informasi.
```

**UPDATE SUBBAGIAN 2.1.1 (Gap Penelitian) - Paragraf Pembuka:**

```markdown
DARI: 
"1. Pertama, penelitian tentang isi pesan masih membaca sentimen dari kata-kata 
saja (Stieglitz & Dang-Xuan, 2013; Ceron & Negri, 2016)..."

KE:
"1. Pertama, penelitian tentang isi pesan masih membaca sentimen dari kata-kata 
saja (Stieglitz & Dang-Xuan, 2013; Ceron & Negri, 2016; Sianturi dkk., 2025)..."
```

**TAMBAHKAN KE DAFTAR PUSTAKA:**

```
Sianturi, H. R. P., Lestari, A. D., Purba, Y. A., Karim, M. B., & Mulyani, H. 
(2025). Politics on a plate: Equivocal communication in Indonesian presidential 
nutrition policy. Frontiers in Communication, 10, 1612652. 
https://doi.org/10.3389/fcomm.2025.1612652
```

---

## 2️⃣ JELASKAN NODEXL SEBAGAI ALAT PENGUMPUL DATA

### **MASALAH:**
Dokumen saat ini hanya menyebut NodeXL sebagai alat analisis jaringan, padahal 
NodeXL juga bisa digunakan untuk **mengumpulkan data Twitter** secara langsung.

### **SOLUSI:**

#### **A. UBAH SUBBAGIAN 3.7 (Teknik Pengumpulan Data) - Paragraf 2:**

**VERSI LAMA:**
```
Data dikumpulkan dengan teknik dokumentasi daring, yaitu menghimpun pesan yang 
telah dipublikasikan di media sosial tanpa keterlibatan peneliti dalam 
percakapan (Kriyantono, 2014). Peneliti tidak berinteraksi dengan pengguna dan 
hanya mengunduh unggahan publik yang sudah ada. Alat yang digunakan ada tiga: 
[nama aplikasi pengumpul data] untuk mengunduh unggahan beserta atributnya, 
NodeXL Pro (Smith dkk., 2010) untuk menyusun, menghitung, dan menggambar 
jaringan, serta Microsoft Excel untuk menyimpan dan merekap data.
```

**VERSI BARU:**
```
Data dikumpulkan dengan teknik dokumentasi daring, yaitu menghimpun pesan yang 
telah dipublikasikan di media sosial tanpa keterlibatan peneliti dalam 
percakapan (Kriyantono, 2014). Peneliti tidak berinteraksi dengan pengguna dan 
hanya mengunduh unggahan publik yang sudah ada. 

Alat utama yang digunakan adalah NodeXL Pro (Network Overview, Discovery and 
Exploration for Excel), yaitu aplikasi tambahan untuk Microsoft Excel yang 
dikembangkan oleh Social Media Research Foundation (Smith dkk., 2010; Hansen 
dkk., 2020). NodeXL Pro dipilih karena memiliki tiga fungsi terintegrasi:

1. **Pengumpulan data Twitter:** NodeXL Pro dapat mengunduh unggahan publik 
   Twitter beserta metadata lengkap (waktu unggah, akun penulis, akun yang 
   disebut, jumlah suka, balasan, retweet, dan kutipan) melalui Twitter API 
   dengan kata kunci pencarian.

2. **Analisis jaringan komunikasi:** NodeXL Pro dapat menghitung kepadatan, 
   sentralitas (in-degree, out-degree, betweenness, closeness, eigenvector), 
   dan mendeteksi komunitas dengan metode Louvain (Blondel dkk., 2008).

3. **Visualisasi jaringan:** NodeXL Pro dapat menghasilkan grafik jaringan 
   dengan pewarnaan otomatis berdasarkan komunitas, ukuran simpul sesuai 
   sentralitas, dan tata letak yang dapat disesuaikan.

Ketiga fungsi ini menjadikan NodeXL Pro solusi terintegrasi untuk penelitian 
jaringan komunikasi media sosial (Hansen dkk., 2020). Data yang terkumpul 
disimpan dalam lembar kerja Microsoft Excel untuk tahap analisis isi.
```

#### **B. TAMBAHKAN PENJELASAN SPESIFIK DI PARAGRAF "Pencarian menggunakan kata kunci..."**

**VERSI LAMA:**
```
Pencarian menggunakan kata kunci "Makan Bergizi Gratis", "MBG", "Makan Siang 
Gratis", serta tagar yang berkaitan, yang digabung dengan operator OR sehingga 
unggahan yang memuat salah satu kata kunci ikut terjaring.
```

**VERSI BARU:**
```
Pencarian dilakukan melalui fitur "Import from Twitter Search Network" di NodeXL 
Pro dengan kata kunci "Makan Bergizi Gratis" OR "MBG" OR "Makan Siang Gratis" 
OR #MakanBergizisGratis OR #MBG. Operator OR digunakan sehingga unggahan yang 
memuat salah satu kata kunci ikut terjaring. NodeXL Pro secara otomatis 
mengekstrak:

- Teks unggahan lengkap beserta emoji
- Tanggal dan waktu unggah (timestamp)
- Nama akun penulis (@username)
- Jenis unggahan (tweet asli, reply, quote)
- Daftar akun yang disebut dengan mention (@)
- Metrik keterlibatan (like, reply count, retweet count, quote count, views)

Data ini langsung tersimpan dalam format tabel Excel dengan satu baris per 
unggahan dan satu kolom per atribut, sehingga siap untuk tahap pembersihan 
(subbagian 3.7.2) dan analisis (subbagian 3.8).
```

#### **C. UBAH SUBBAGIAN 2.2.2 (Dasar-Dasar Teori Graf) - HAPUS atau PINDAHKAN paragraf tentang NodeXL**

**CATATAN:** 
Paragraf "NodeXL sebagai Alat Analisis Jaringan" di Subbagian 2.2.2 (halaman ~20) 
sebaiknya **DIPINDAHKAN** ke Bab III (Metode), karena NodeXL adalah alat/instrumen, 
bukan bagian dari teori.

**OPSI 1 (DIREKOMENDASIKAN): HAPUS dari Bab II**
Hapus seluruh paragraf "NodeXL sebagai Alat Analisis Jaringan" dari Subbagian 2.2.2, 
karena sudah dijelaskan lengkap di Bab III.

**OPSI 2: RINGKAS MENJADI 1 KALIMAT**
Jika dosen minta tetap disebutkan di Bab II, ringkas jadi:
```
Pengolahan jaringan dalam penelitian ini menggunakan NodeXL Pro (Smith dkk., 
2010), yaitu aplikasi tambahan untuk Microsoft Excel yang dapat mengunduh data 
Twitter, menghitung sentralitas, dan memvisualisasikan jaringan (Hansen dkk., 
2020); penjelasan lengkap disajikan pada Bab III.
```

---

## 3️⃣ SESUAIKAN NOMOR HALAMAN

### **DAFTAR ISI - VERSI DIKOREKSI:**

Berdasarkan struktur dokumen Word standar dengan format tesis UPN:

```
LEMBAR PERSETUJUAN .......................................... i
LEMBAR PENGESAHAN ........................................... ii
PERNYATAAN BEBAS PLAGIAT .................................... iii
KATA PENGANTAR .............................................. iv
ABSTRAK ..................................................... vi
ABSTRACT .................................................... vii
DAFTAR ISI .................................................. viii
DAFTAR TABEL ................................................ x
DAFTAR GAMBAR ............................................... xi
DAFTAR LAMPIRAN ............................................. xii

BAB I PENDAHULUAN ........................................... 1
  1.1 Latar Belakang Masalah ................................ 1
  1.2 Rumusan Masalah ....................................... 6
  1.3 Tujuan Penelitian ..................................... 7
  1.4 Manfaat Penelitian .................................... 7
      1.4.1 Manfaat Teoretis ................................ 7
      1.4.2 Manfaat Praktis ................................. 8

BAB II TINJAUAN PUSTAKA ..................................... 10
  2.1 Penelitian Terdahulu .................................. 10
      2.1.1 Gap Penelitian .................................. 13
  2.2 Tinjauan Pustaka ...................................... 14
      2.2.1 Teori Computer-Mediated Communication (CMC) ..... 14
      2.2.2 Teori Graf dan Analisis Jaringan Komunikasi .... 19
      2.2.3 Media Sosial Twitter sebagai Ruang Percakapan .. 23
      2.2.4 Isu yang Dibicarakan Publik tentang Kebijakan .. 25
      2.2.5 Dialog Teori CMC dan Teori Graf ................ 26
  2.3 Kerangka Pemikiran .................................... 27
  2.4 Fokus Analitis ........................................ 29

BAB III METODE PENELITIAN ................................... 31
  3.1 Pendekatan Penelitian ................................. 31
  3.2 Definisi dan Operasionalisasi ........................ 33
  3.3 Pengukuran Variabel ................................... 35
      3.3.1 Validitas dan Reliabilitas Pengukuran .......... 36
  3.4 Lokasi dan Waktu Penelitian .......................... 37
  3.5 Populasi, Sampel, dan Cara Pengambilan Sampel ........ 38
  3.6 Jenis dan Sumber Data ................................. 40
  3.7 Teknik Pengumpulan Data ............................... 41
      3.7.1 Prinsip Etis Penelitian ........................ 43
      3.7.2 Tahapan Pembersihan Data ....................... 44
  3.8 Teknik Analisis Data .................................. 46
      3.8.1 Analisis Isi: Penilaian 9 Emoji, Sindiran, Isu . 46
      3.8.2 Analisis Perilaku .............................. 47
      3.8.3 Analisis Struktur Jaringan ..................... 48
      3.8.4 Interpretasi dan Visualisasi ................... 49
      3.8.5 Batasan Penelitian ............................. 49
  3.9 Temuan Awal Studi Pendahuluan ........................ 51
      3.9.1 Karakteristik Makro Jaringan ................... 51
      3.9.2 Aktor Dominan .................................. 52
      3.9.3 Jangkauan dan Perubahan Antarperiode ........... 53
      3.9.4 Implikasi bagi Rancangan Penelitian ............ 54

DAFTAR PUSTAKA .............................................. 55
LAMPIRAN .................................................... 62
  Lampiran 1. Kata Kunci dan Kueri Pencarian NodeXL ....... 63
  Lampiran 2. Buku Panduan Penilaian 9 Emoji .............. 64
  Lampiran 3. Kamus Isu Program MBG ........................ 70
```

**CATATAN PENTING:**
- Halaman di atas adalah **PERKIRAAN** berdasarkan struktur standar
- **CEK ULANG** nomor halaman setelah semua perbaikan diterapkan di Word
- Gunakan fitur **Update Table of Contents** di Word setelah semua perbaikan selesai

---

## 4️⃣ CHECKLIST IMPLEMENTASI LENGKAP

### ✅ **PRIORITAS TERTINGGI (HARUS):**

- [ ] **Tabel 2.1:** Tambahkan baris penelitian Sianturi dkk. (2025)
- [ ] **Subbagian 2.1:** Tambahkan paragraf tentang Sianturi dkk. (2025)
- [ ] **Subbagian 2.1.1:** Tambahkan "Sianturi dkk., 2025" di gap pertama
- [ ] **Daftar Pustaka:** Tambahkan Sianturi dkk. (2025)
- [ ] **Subbagian 3.7, paragraf 2:** Ganti dengan versi baru (NodeXL Pro)
- [ ] **Subbagian 3.7, paragraf "Pencarian...":** Ganti dengan versi baru
- [ ] **Subbagian 2.2.2:** Hapus atau ringkas paragraf tentang NodeXL
- [ ] **Tabel 3.3:** Update dengan versi baru (catatan deduplikasi)
- [ ] **Subbagian 3.5:** Tambahkan penjelasan korpus 5.272 → 5.263
- [ ] **Subbagian 3.7.2:** Ganti dengan versi lengkap (kriteria bot >120/hari)
- [ ] **Subbagian 2.4:** Ganti judul "Hipotesis" → "Fokus Analitis"
- [ ] **Subbagian 2.4:** Ganti isi dengan versi "Fokus Analitis"
- [ ] **Tambah Subbagian 3.3.1:** Validitas dan Reliabilitas Pengukuran
- [ ] **Tambahkan:** Daftar Lampiran (setelah Daftar Gambar)
- [ ] **Daftar Isi:** Update semua nomor halaman dengan "Update Table"

### ✅ **JIKA ADA WAKTU:**

- [ ] Buat Lampiran 1 (Kata Kunci NodeXL)
- [ ] Buat Lampiran 2 (Buku Panduan 9 Emoji)
- [ ] Buat Lampiran 3 (Kamus Isu)

---

## 5️⃣ TEMPLATE LAMPIRAN 1: KATA KUNCI NODEXL

```markdown
# LAMPIRAN 1
## Kata Kunci dan Kueri Pencarian Data Twitter dengan NodeXL Pro

### A. Kata Kunci Penelitian

Pencarian data dilakukan dengan kombinasi kata kunci berikut:

1. "Makan Bergizi Gratis"
2. "MBG"
3. "Makan Siang Gratis"
4. #MakanBergizisGratis
5. #MBG

### B. Kueri Pencarian di NodeXL Pro

**Fitur yang digunakan:** Import from Twitter Search Network

**Syntax kueri:**
```
"Makan Bergizi Gratis" OR MBG OR "Makan Siang Gratis" OR 
#MakanBergizisGratis OR #MBG
```

**Pengaturan (Settings):**
- **Bahasa:** Indonesian (lang:id)
- **Periode:** 2 Maret 2026 - 24 Mei 2026
- **Jenis:** Semua jenis tweet (original, replies, quotes)
- **Limit:** Unlimited (hingga API limit tercapai)

### C. Output yang Diperoleh

NodeXL Pro secara otomatis mengekstrak kolom-kolom berikut:

| Kolom | Keterangan |
|-------|------------|
| Vertex 1 | Akun penulis (@username) |
| Vertex 2 | Akun yang disebut (@mention) |
| Relationship | Jenis relasi (Mentions, Replies to, etc.) |
| Tweet | Teks lengkap termasuk emoji |
| Created at | Tanggal dan waktu unggah |
| Like count | Jumlah suka |
| Reply count | Jumlah balasan |
| Retweet count | Jumlah retweet |
| Quote count | Jumlah kutipan |
| Views | Jumlah tayangan (jika tersedia) |

### D. Jumlah Data Terkumpul

- **Data mentah awal:** 5.272 tweet
- **Setelah penyaringan:** 5.263 tweet
- **Periode:** 2 Maret - 24 Mei 2026

Sumber: Diolah peneliti menggunakan NodeXL Pro (2026).
```

---

## 📊 RINGKASAN PERUBAHAN

| No | Item | Status | Halaman |
|----|------|--------|---------|
| 1 | Judul tetap "Twitter" | ✅ Tidak diubah | Semua |
| 2 | Tambah penelitian Sianturi dkk. (2025) | ✅ Kerjakan | 10-13 |
| 3 | NodeXL sebagai alat pengumpul data | ✅ Kerjakan | 41-42 |
| 4 | Perbaiki Tabel 3.3 | ✅ Kerjakan | 38 |
| 5 | Lengkapi kriteria bot | ✅ Kerjakan | 44-45 |
| 6 | Ganti "Proposisi" → "Fokus Analitis" | ✅ Kerjakan | 29 |
| 7 | Tambah Subbagian 3.3.1 | ✅ Kerjakan | 36 |
| 8 | Tambah Daftar Lampiran | ✅ Kerjakan | xii |
| 9 | Update Daftar Isi | ✅ Kerjakan | viii-ix |

---

**Versi:** 2.0 - Final dengan NodeXL dan Penelitian Terdahulu
**Tanggal:** 4 November 2026
**Status:** ✅ Siap Implementasi

---

💡 **CARA KERJA:**
1. Buka dokumen Word "proposal baru (1).docx"
2. Lakukan perbaikan sesuai urutan di checklist
3. Setelah semua selesai, klik kanan Daftar Isi → **Update Field** → **Update entire table**
4. Cek ulang nomor halaman yang ter-update otomatis
