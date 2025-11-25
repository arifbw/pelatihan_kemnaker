# 🟦 **1. SCHEMA TABEL LATIHAN**

## **1.1. Tabel: dikti_mahasiswa**

Data dari DIKTI — banyak variasi nama, tanggal lahir belum tentu presisi.

```sql
CREATE TABLE dikti_mahasiswa (
    id SERIAL PRIMARY KEY,
    nim VARCHAR(50),
    nama_lengkap TEXT,
    nama_bersih TEXT, -- hasil normalisasi
    nik VARCHAR(20),
    tgl_lahir DATE,
    prodi TEXT,
    universitas TEXT
);
```

---

## **1.2. Tabel: dukcapil_penduduk**

Data dari Dukcapil — biasanya lebih bersih untuk identitas dasar.

```sql
CREATE TABLE dukcapil_penduduk (
    id SERIAL PRIMARY KEY,
    nik VARCHAR(20),
    nama TEXT,
    nama_bersih TEXT, -- hasil normalisasi
    tgl_lahir DATE,
    alamat TEXT,
    jk VARCHAR(10)
);
```

---

# 🟧 **2. DUMMY DATA UNTUK LATIHAN**

## **2.1. Insert dummy data DIKTI**

```sql
INSERT INTO dikti_mahasiswa 
(nim, nama_lengkap, nik, tgl_lahir, prodi, universitas)
VALUES
('2018001', 'Aisyah Dwi', '3201012000010001', '2000-01-20', 'Informatika', 'Universitas A'),
('2018002', 'A i s y a h   D w i', '3201012000010001', '2000-01-20', 'Sistem Informasi', 'Universitas A'),
('2018003', 'Budi Santoso', '3201013000050002', '2000-05-05', 'Teknik Industri', 'Universitas B'),
('2018004', 'B u d i   S a n t o s o', '3201013000050002', '2000-05-05', 'Teknik Industri', 'Universitas B'),
('2018005', 'Dédé Pratama', NULL, '1999-12-11', 'Hukum', 'Universitas C'),
('2018006', 'Andri Wijaya', '1234567890123456', '2001-01-01', 'Akuntansi', 'Universitas D');
```

---

## **2.2. Insert dummy data Dukcapil**

```sql
INSERT INTO dukcapil_penduduk
(nik, nama, tgl_lahir, alamat, jk)
VALUES
('3201012000010001', 'AISYAH DWI', '2000-01-20', 'Jl. Merdeka 1', 'P'),
('3201013000050002', 'BUDI SANTOSO', '2000-05-05', 'Jl. Merdeka 2', 'L'),
('3201019999999999', 'DEDE PRATAMA', '1999-12-11', 'Jl. Merdeka 3', 'L'),
('1234567890123456', 'ANDRI WJAYA', '2001-01-01', 'Jl. Merdeka 4', 'L');
```

---

# 🟩 **3. CREATE EXTENSION (Wajib untuk latihan)**
cek apakah extension sudah tersedia, dan melihat deskripsi extension
```sql
SELECT * FROM pg_available_extensions WHERE name IN ('pg_trgm', 'unaccent', 'fuzzystrmatch', 'citext', 'uuid-ossp') ;
```

```sql
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS unaccent;
CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;
CREATE EXTENSION IF NOT EXISTS citext;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

---

# 🟪 **4. CONTOH PENGGUNAAN EXTENSION**

---

# ✅ **4.1. pg_trgm — Similarity Matching**

### Cek similarity:

```sql
SELECT 
    nama_lengkap,
    similarity(nama_lengkap, 'aisyah dwi') AS score
FROM dikti_mahasiswa
ORDER BY score DESC;
```

### Search fuzzy:

```sql
SELECT *
FROM dikti_mahasiswa
WHERE nama_lengkap % 'aisyah dwi';
```