# ✅ **0. DATA PREPARATION — WAJIB DIJALANKAN SEBELUM CHALLENGE PRAKTIK**

Ini script lengkap untuk mempersiapkan peserta sebelum challenge dimulai.

## **0.1 Tambahan Kolom untuk Normalisasi**

```sql
ALTER TABLE dikti_mahasiswa 
ADD COLUMN nama_clean TEXT,
ADD COLUMN nik_clean TEXT;

ALTER TABLE dukcapil_penduduk
ADD COLUMN nama_clean TEXT,
ADD COLUMN nik_clean TEXT;
```

---

## **0.2 Tambahan Table untuk A3 (Rule-Based, Dictionary-Based)**

### **1) Dictionary pekerjaan (contoh sederhana)**

```sql
CREATE TABLE dict_profesi (
    keyword TEXT,
    kategori TEXT
);

INSERT INTO dict_profesi VALUES
('dokter', 'tenaga_medis'),
('dr.', 'tenaga_medis'),
('perawat', 'tenaga_medis'),
('kontraktor', 'vendor'),
('outsourcing', 'vendor'),
('freelance', 'non_tetap');
```

### **2) Dummy tabel pekerjaan mahasiswa**

Agar bisa diuji pada rule-based maupun dictionary.

```sql
CREATE TABLE mahasiswa_riwayat (
    id SERIAL PRIMARY KEY,
    nim VARCHAR(50),
    pekerjaan TEXT,
    tahun_masuk DATE,
    tahun_lulus DATE
);

INSERT INTO mahasiswa_riwayat 
(nim, pekerjaan, tahun_masuk, tahun_lulus)
VALUES
('2018001', 'Dokter Bedah', '2010-01-01', '2014-01-01'),   -- anomaly (masa pendidikan dokter minimal 6 tahun)
('2018002', 'Programmer Outsourcing', '2018-01-01', '2022-01-01'),
('2018003', 'Dosen', '2010-01-01', '2015-01-01'),
('2018004', 'Freelance Designer', '2017-01-01', '2019-01-01'),
('2018005', 'dr.', '2013-01-01', '2017-01-01'); -- still anomaly (min 6 yr)
```

---

# 🔥 **A1 — REGEX & NORMALISASI IDENTITAS**

Total: **5 praktik**

---

# ✅ **A1 — PRAKTIK (5 Soal)**

### **PRAKTIK 1 — Hapus spasi berlebihan dari nama**

Buat query untuk menghasilkan `nama_clean` dari `dikti_mahasiswa.nama_lengkap`, aturan:

* hilangkan spasi berlebih
* hilangkan spasi di antara huruf
* convert ke UPPERCASE

Contoh yang diharapkan:
`"A i s y a h   D w i"` → `"AISYAH DWI"`

---

### **PRAKTIK 2 — Normalisasi NIK**

Buat `nik_clean` dengan aturan:

* hanya ambil digit (`regex_replace(nik, '[^0-9]', '')`)
* pastikan total 16 digit
* jika kurang, tambahkan leading zero

---

### **PRAKTIK 3 — Validasi format NIK dengan regex**

Buat query yang menandai apakah `nik_clean` valid:

* regex format: `^[0-9]{16}$`
  Output kolom: `is_valid_nik (boolean)`

---

### **PRAKTIK 4 — Buat fungsi normalisasi nama (reusable)**

Buat function PostgreSQL:

`normalize_name(text) RETURNS text`

Fitur:

* trim
* multiple-space collapse
* remove spaces between single characters
* upper

---

### **PRAKTIK 5 — Deteksi nama yang memiliki 75% kemiripan**

Gunakan:

* `similarity()`
* ambang batas 0.75
  Contoh pasangan yang harus muncul:
* "Aisyah Dwi" dan "A i s y a h D w i"

---

# 🔥 **A2 — PENYAMAAN DATA LINTAS SUMBER**

Total: **5 praktik**

---

# ✅ **A2 — PRAKTIK (5 Soal)**

### **PRAKTIK 6 — Exact Match berdasarkan NIK**

Cocokkan `dikti_mahasiswa.nik_clean` vs `dukcapil_penduduk.nik_clean`.

---

### **PRAKTIK 7 — Match berdasarkan nama_clean + tanggal lahir**

Tampilkan pasangan yang cocok berdasarkan:

* nama_clean = nama_clean
* tgl_lahir = tgl_lahir

---

### **PRAKTIK 8 — Token-based matching nama (urutan tidak penting)**

Contoh:

* "Aisyah Dwi"
* "Dwi Aisyah"

Tetap harus matched.
Gunakan:

```
string_to_array()
array_sort()
```

---

### **PRAKTIK 9 — Fuzzy name matching dengan Levenshtein**

Cari pasangan:

* "Andri Wijaya" vs "ANDRI WJAYA"
  Threshold perbedaan ≤ 2 karakter.

---

### **PRAKTIK 10 — Buat skor match gabungan**

Gabungkan:

* similarity nama (0–1)
* exact match tanggal lahir (1 atau 0)
* exact match NIK (1 atau 0)

Buat kolom `match_score` dengan formula:

```
match_score = similarity(nama) * 0.6 + 
              (tgl_lahir match) * 0.3 +
              (NIK match) * 0.1
```

---

# 🔥 **A3 — CLASSIFICATION OF DATA ANOMALIES**

Total: **5 praktik**

---

# ✅ **A3 — PRAKTIK (5 Soal)**

### **PRAKTIK 11 — Deteksi masa studi < 6 tahun untuk profesi dokter**

Gunakan rule:

Jika pekerjaan LIKE '%dokter%' atau 'dr.'
→ masa studi minimal = 6 tahun.

Flag anomaly.

---

### **PRAKTIK 12 — Deteksi anomali tanggal**

Tanggal lulus > tanggal masuk ?
Jika tidak → anomali.

---

### **PRAKTIK 13 — Mapping pekerjaan ke kategori via dictionary**

Gunakan `dict_profesi.keyword`.

Ambil kategori via `ILIKE '%' || keyword || '%'`.

---

### **PRAKTIK 14 — Buat indikator “pekerjaan tidak sesuai kategori”**

Contoh:

* pekerjaan “Dokter Bedah” → kategori harus “tenaga_medis”
* jika dictionary tidak match → kategori_unknown

---

### **PRAKTIK 15 — Buat tabel view “data_bermasalah”**

Berisi:

* nim
* pekerjaan
* kategori
* jenis_anomali
  (masa_studi, tanggal_salah, kategori_tidak_terdeteksi)

---