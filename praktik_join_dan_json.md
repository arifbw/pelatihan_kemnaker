✅ **0. PREPARATION — Tambah Tabel & Kolom untuk Latihan**

## **0.1 Tambah tabel universitas (untuk join practice)**

Agar bisa melakukan join antar tabel dengan benar.

```sql
CREATE TABLE universitas_ref (
    id SERIAL PRIMARY KEY,
    universitas TEXT,
    kota TEXT,
    akreditasi TEXT
);

INSERT INTO universitas_ref (universitas, kota, akreditasi) VALUES
('Universitas A', 'Bandung', 'A'),
('Universitas B', 'Jakarta', 'A'),
('Universitas C', 'Surabaya', 'B'),
('Universitas D', 'Yogyakarta', 'A');
```

---

## **0.2 Tambah tabel prodi (untuk join ke dikti_mahasiswa)**

```sql
CREATE TABLE prodi_ref (
    id SERIAL PRIMARY KEY,
    prodi TEXT,
    fakultas TEXT,
    jenjang TEXT
);

INSERT INTO prodi_ref (prodi, fakultas, jenjang) VALUES
('Informatika', 'FTI', 'S1'),
('Sistem Informasi', 'FTI', 'S1'),
('Teknik Industri', 'FTI', 'S1'),
('Hukum', 'FH', 'S1'),
('Akuntansi', 'FEB', 'S1');
```

---

## **0.3 Tambah tabel JSON untuk latihan JSON Processing**

```sql
CREATE TABLE log_request_api (
    id SERIAL PRIMARY KEY,
    payload JSONB,
    created_at TIMESTAMP DEFAULT now()
);
```

### Insert sample JSON (variasi nested & array)

```sql
INSERT INTO log_request_api (payload) VALUES
('{
    "request_id": "REQ-001",
    "mahasiswa": {
        "nim": "2018001",
        "nama": "Aisyah Dwi",
        "hobi": ["membaca", "menulis"],
        "kontak": { "email": "aisyah@mail.com", "phone": "08123" }
    }
}'),

('{
    "request_id": "REQ-002",
    "mahasiswa": {
        "nim": "2018003",
        "nama": "Budi Santoso",
        "hobi": ["musik", "basket", "travel"],
        "kontak": { "email": "budi@mail.com", "phone": null }
    }
}'),

('{
    "request_id": "REQ-003",
    "mahasiswa": {
        "nim": "2018006",
        "nama": "Andri Wijaya",
        "hobi": [],
        "kontak": { "email": "andri@mail.com" }
    },
    "metadata": { "source": "mobile-app", "version": 2 }
}');
```

---

---

# 🔥 **B — PRAKTIK JOIN & UNION (7 Soal Praktik)**

---

# **PRAKTIK B1 — INNER JOIN dasar (Dikti ➜ Universitas)**

**Tujuan:** memilih tipe join yang tepat.

**Tugas:**
Gabungkan `dikti_mahasiswa` dengan `universitas_ref`, tampilkan:

* nim
* nama_lengkap
* universitas
* kota universitas
* akreditasi

---

# **PRAKTIK B2 — LEFT JOIN untuk data yang mungkin tidak punya pasangan**

**Tugas:** cari mahasiswa yang **tidak memiliki universitas yang dikenal**, yaitu:

* join `LEFT JOIN`
* lalu filter `WHERE universitas_ref.id IS NULL`

(Tidak ada dalam data awal, tapi peserta harus paham pola-nya.)

---

# **PRAKTIK B3 — SEMI JOIN (EXISTS) vs INNER JOIN**

**Tugas:**
Tampilkan mahasiswa yang memiliki pasangan di `dukcapil_penduduk` berdasarkan:

* kondisi nama_clean mirip (similarity > 0.7)
* tanggal lahir sama

Gunakan **EXISTS**, bukan INNER JOIN.

---

# **PRAKTIK B4 — ANTI JOIN (NOT EXISTS)**

**Tugas:** cari mahasiswa yang **tidak ditemukan di Dukcapil** berdasarkan:

* nik_clean miss
* atau NIK NULL

Gunakan `NOT EXISTS`.

---

# **PRAKTIK B5 — UNION vs UNION ALL**

**Tugas:** gabungkan nama-nama mahasiswa dari:

* dikti_mahasiswa
* dukcapil_penduduk

Bandingkan hasil:

1. `UNION`
2. `UNION ALL`

Lalu hitung jumlah baris.

---

# **PRAKTIK B6 — LATERAL JOIN untuk memilih elemen tertentu**

**Tugas:** Ambil mahasiswa + 1 kata pertama dari nama mereka (tokenized).

Gunakan:

```sql
CROSS JOIN LATERAL unnest(string_to_array(nama_clean, ' ')) AS t(kata)
```

Lalu ambil hanya kata pertama.

---

# **PRAKTIK B7 — Optimasi JOIN besar (indexing + partition idea)**

**Tugas:**

1. Buat index untuk mempercepat join Dikti vs Dukcapil:

```sql
CREATE INDEX idx_dikti_nik ON dikti_mahasiswa(nik_clean);
CREATE INDEX idx_dukcapil_nik ON dukcapil_penduduk(nik_clean);
```

2. Jalankan ulang query join exact match dan lihat bahwa speed meningkat.

3. Berikan skenario kapan partition berguna:

   * based on `universitas`
   * based on `kota`

---

---

# 🔥 **C — JSON PROCESSING / JSON → FLAT (6 Soal Praktik)**

---

# **PRAKTIK C1 — Extract fields dasar dari JSON**

Ambil dari `payload`:

* request_id
* nim
* nama

Gunakan operator:

* `->`
* `->>`

---

# **PRAKTIK C2 — Mengambil array JSON menggunakan jsonb_array_elements**

Dari field:

```
mahasiswa.hobi
```

Tugas:

* kembalikan 1 row per hobi
* sertakan request_id

---

# **PRAKTIK C3 — Flatten JSON nested (kontak.email + kontak.phone)**

Gunakan:

* `jsonb_extract_path_text(payload, 'mahasiswa', 'kontak', 'email')`

Tugas: buat output tabel datar:

| request_id | nim | email | phone |

---

# **PRAKTIK C4 — explode full nested JSON (dynamic key → row)**

Gunakan:

* `jsonb_each_text`

Contoh: extract semua key-value tingkat pertama:

```
request_id : REQ-001  
mahasiswa  : {...}  
metadata   : {...}  
```

Tugas: return sebagai row.

---

# **PRAKTIK C5 — Buat reusable function: json_flatten(payload jsonb)**

Function harus:

* menerima JSONB
* mengubah nested JSON jadi key-value flat
* contoh output:

```
mahasiswa.nim   → 2018001
mahasiswa.nama  → AISYAH DWI
mahasiswa.hobi[0] → membaca
```

Gunakan recursive approach dengan:

* `jsonb_typeof()`
* looping key dengan `jsonb_each()`

Ini challenge paling besar.

---

# **PRAKTIK C6 — Combine JSON Flatten → Insert ke table flat_log**

Buat tabel:

```sql
CREATE TABLE flat_log (
    id SERIAL PRIMARY KEY,
    request_id TEXT,
    key TEXT,
    value TEXT
);
```

Tugas:

* pilih 1 record dari `log_request_api`
* flatten JSON memakai function C5
* insert seluruh key-value ke flat_log

---