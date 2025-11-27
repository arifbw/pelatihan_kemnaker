🧹 **A. DATA CLEANSING (6 PRAKTIK)**
====================================

* * *

**A1 — Normalisasi Spasi & Nama Bersih**
----------------------------------------

**Komponen Streamlit yang digunakan:**

* `st.file_uploader()`

* `st.dataframe()`

* `st.button("Clean Name")`

* `st.text_area("Regex Output Preview")`

**Tugas:**

* Upload file.

* Tampilkan baris dengan pola regex `\s+` berlebih.

* Klik tombol → lakukan: strip, collapse spaces, uppercase.

* Preview hasil sebelum & sesudah.

* * *

**A2 — Normalisasi NIK**
------------------------

**Tujuan:** memastikan kolom identitas konsisten.

**Komponen:**

* `st.file_uploader()`

* `st.number_input("Target Length", value=16)`

* `st.checkbox("Show only invalid NIK")`

* `st.dataframe()`

**Tugas:**

* Bersihkan non-numeric: `re.sub(r'\D','',nik)`

* Tambahkan leading zero → panjang 16

* Filter invalid dengan checkbox

* * *

**A3 — Duplicate Detection Dashboard**
--------------------------------------

**Tujuan:** duplicate detection.

**Komponen:**

* `st.file_uploader()`

* `st.radio(["NIK","Nama+Tgl Lahir"])`

* `st.dataframe()`

* `st.button("Drop Duplicates")`

**Tugas:**

* Pilih metode duplikasi via `radio`

* Highlight duplicates menggunakan pandas style

* Berikan tombol hapus duplikasi

* * *

**A4 — Clean Tanggal Berantakan**
---------------------------------

**Tujuan:** handle tanggal amburadul, misal “20/01/00”, “2000.01.20”.

**Komponen:**

* `st.file_uploader()`

* `st.dataframe()`

* `st.success/st.error()`

* `st.expander("Rows Gagal Parse")`

**Tugas:**

* Parse otomatis menggunakan `dateutil`

* Tampilkan baris gagal parse di expander

* Tampilkan status validasi

* * *

**A5 — Split Alamat → Provinsi/Kota/Kecamatan**
-----------------------------------------------

**Tujuan:** memperlihatkan transforming column.

**Komponen:**

* `st.file_uploader()`

* `st.text_input("Regex Kota")`

* `st.text_input("Regex Kecamatan")`

* `st.dataframe()`

* `st.download_button()`

**Tugas:**

* Pisah kolom alamat sesuai regex

* Tambahkan kolom baru otomatis ke dataframe

* Download hasil sebagai CSV

* * *

**A6 — Generate Data Quality Score**
------------------------------------

**Tujuan:** membuat scoring kualitas data.

**Komponen:**

* `st.file_uploader()`

* `st.progress()` atau `st.metric()`

* `st.bar_chart()` untuk distribusi skor

* `st.dataframe()`

**Tugas:**

* Hitung skor 0–100

* Tampilkan indikator metric:
  
      st.metric("Quality Score Rata-rata", "84")

* Tampilkan chart distribusi skor

* * *

* * *

🔄 **B. ETL SEDERHANA (6 PRAKTIK)**
===================================

* * *

**B1 — ETL: Excel → Transform → PostgreSQL**
--------------------------------------------

**Tujuan:** ETL end-to-end pertama peserta.

**Komponen:**

* `st.file_uploader(type=['xlsx'])`

* `st.dataframe()`

* `st.text_input("Postgres URI")`

* `st.button("Run ETL")`

* `st.code()` untuk log

**Tugas:**

* Upload Excel

* Transform nama dan tanggal

* Insert ke PostgreSQL

* Tampilkan log proses

* * *

**B2 — Simulasi ETL Scheduling**
--------------------------------

**Tujuan:** memperkenalkan konsep schedule.

**Komponen:**

* `st.button("Run ETL Now")`

* `st.write(f"Last run: {timestamp}")`

* `st.dataframe()`

**Tugas:**

* ETL sederhana (uppercase + trim)

* Simpan timestamp pada session state

* Tampilkan waktu terakhir ETL dijalankan

* * *

**B3 — Merge & Fuzzy Match Dikti vs Dukcapil**
----------------------------------------------

**Tujuan:** ETL join.

**Komponen:**

* `st.file_uploader("Dikti")`

* `st.file_uploader("Dukcapil")`

* `st.slider("Similarity Threshold", 60, 100, 85)`

* `st.dataframe()`

**Tugas:**

* Normalisasi nama

* Fuzzy match token dengan threshold slider

* Tampilkan matching pairs

* * *

**B4 — Mapping (Dictionary Join)**
----------------------------------

**Tujuan:** ETL kategori.

**Komponen:**

* `st.file_uploader("Data Utama")`

* `st.file_uploader("Mapping Dictionary")`

* `st.selectbox("Key Column", [...])`

* `st.dataframe()`

**Tugas:**

* Upload dua file

* Join berdasarkan key

* Tampilkan hasil join

* * *

**B5 — ETL Logging**
--------------------

**Tujuan:** menanamkan mindset logging pipeline.

**Komponen:**

* `st.json()`

* `st.expander("ETL Logs")`

* `st.button("Export Logs")`

* `st.download_button()`

**Tugas:**

* Buat log dict setiap step

* Tampilkan JSON dalam expander

* Bisa di-download

* * *

**B6 — Golden Record Selector**
-------------------------------

**Tujuan:** pilih data terbaik dari banyak sumber.

**Komponen:**

* `st.file_uploader("Data Sumber A")`

* `st.file_uploader("Data Sumber B")`

* `st.radio("Conflict Resolution Strategy", ["Longest Text","Valid Date","Cleanest Format"])`

* `st.dataframe()`

**Tugas:**

* Upload 2 dataset sama (A & B)

* Aturan:
  
  * Jika NIK sama → pilih nama terbersih
  
  * Jika tanggal beda → pilih yang valid
  
  * Jika alamat beda → pilih yang terlengkap

* Tampilkan hasil “golden record”

* * *

* * *

🧠 **C. TEXT CLASSIFICATION (REGEX, RULE, DICTIONARY) — 5 PRAKTIK**
===================================================================

* * *

**C1 — Regex Classification Viewer**
------------------------------------

**Tujuan:** gunakan pola regex untuk mendeteksi kategori.

**Komponen:**

* `st.file_uploader()`

* `st.text_input("Regex")`

* `st.dataframe()`

* `st.highlight_text()` (alternatif → pandas style)

**Tugas:**

* Deteksi pola dengan regex input

* Tampilkan semua baris yang cocok

* Highlight hasil temuan

* * *

**C2 — Rule-Based Classifier**
------------------------------

**Tujuan:** klasifikasi berdasarkan aturan logika.

**Komponen:**

* `st.file_uploader()`

* `st.checkbox("Validasi Usia < 15")`

* `st.checkbox("Validasi Tanggal")`

* `st.dataframe()`

* `st.metric()`

**Tugas:**

* Terapkan rule berdasarkan checkbox

* Tambahkan kolom kategori

* Hitung jumlah per kategori

* * *

**C3 — Dictionary-Based Job Categorization**
--------------------------------------------

**Tujuan:** kategorisasi pekerjaan berdasarkan keyword.

**Komponen:**

* `st.file_uploader("Data Pekerjaan")`

* `st.file_uploader("Dictionary Mapping")`

* `st.dataframe()`

* `st.sidebar.selectbox("Metode Match", ["Contains","Startswith","Token"])`

**Tugas:**

* Klasifikasikan pekerjaan berdasarkan dictionary

* Tampilkan kategori di kolom baru

* * *

**C4 — Token Fuzzy Job Matching**
---------------------------------

**Tujuan:** fuzzy + token classification.

**Komponen:**

* `st.file_uploader()`

* `st.slider("Fuzzy Threshold", 0, 100, 85)`

* `st.dataframe()`

* `st.progress()`

**Tugas:**

* Tokenize

* Hitung similarity

* Tampilkan score

* Highlight score < threshold

* * *

**C5 — Multi-Label Classifier**
-------------------------------

**Tujuan:** kombinasikan semua teknik.

**Komponen:**

* `st.file_uploader()`

* `st.dataframe()`

* `st.checkbox("Regex Label")`

* `st.checkbox("Rule Label")`

* `st.checkbox("Dictionary Label")`

**Tugas:**

* Terapkan 3 label berbeda

* Hasil = dataframe multilabel

* Tampilkan summary label

* * *

* * *

😊 **D. SENTIMENT ANALYSIS (2 PRAKTIK)**
========================================

* * *

**D1 — Simple Sentiment Dashboard**
-----------------------------------

**Tujuan:** mengenalkan AI NLP ringan.

**Komponen:**

* `st.text_area("Input Text")`

* `st.button("Analyze")`

* `st.metric()`

* `st.progress()`

* `st.dataframe()`

**Tugas:**

* Hitung sentiment

* Tampilkan score sebagai metric

* Tampilkan confidence bar

* * *

**D2 — Batch Sentiment Analyzer**
---------------------------------

**Tujuan:** proses banyak data.

**Komponen:**

* `st.file_uploader()`

* `st.dataframe()`

* `st.radio("Color Highlight", ["Positive","Neutral","Negative"])`

**Tugas:**

* Klasifikasi banyak komentar

* Tampilkan hasil dalam warna kategori

* Export hasil

* * *

* * *

🤖 **E. AI IMPLEMENTATION (3 PRAKTIK)**
=======================================

* * *

**E1 — AI Summarizer**
----------------------

**Tujuan:** kasih penjelasan otomatis.

**Komponen:**

* `st.text_area()`

* `st.button("Summarize")`

* `st.code()`

* `st.success()`

**Tugas:**

* Gunakan model huggingface mini

* Summary menjadi 3 bullet

* Tampilkan hasil

* * *

**E2 — AI Data Normalizer**
---------------------------

**Tujuan:** memadankan nama otomatis.

**Komponen:**

* `st.text_input("Nama Berantakan")`

* `st.button("Normalize")`

* `st.json()`

**Tugas:**

* Normalisasi (regex + AI)

* Tampilkan 3 versi:
  
  * regex_clean
  
  * fuzzy_best_match
  
  * ai_suggestion

* * *

**E3 — AI Error Detector**
--------------------------

**Tujuan:** mendeteksi kesalahan data secara otomatis.

**Komponen:**

* `st.file_uploader()`

* `st.dataframe()`

* `st.expander("Error Detail")`

* `st.checkbox("Show only errors")`

* `st.metric()`

**Tugas:**

* Deteksi error data dengan rule + model

* Tampilkan summary kesalahan

* Expand detail error per record

* * *
