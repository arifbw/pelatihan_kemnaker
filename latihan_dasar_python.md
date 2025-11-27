## **P1 — Variabel, Tipe Data, dan F-string**

**Tujuan:** vibe dasar Python.
**Instruksi:**

* Buat 3 variabel (`nama`, `usia`, `is_admin`)
* Print dalam satu kalimat dengan f-string:
  “Halo, nama saya …, usia …, admin? …”

---

## **P2 — List & Loop**

**Tujuan:** memahami list, looping, quick transformation.
**Instruksi:**

* Buat list angka `1–20`
* Print hanya angka yang kelipatan 3
* Buat list baru hasil kuadratnya (pakai list comprehension)

---

## **P3 — Dictionary & Nested Structure**

**Tujuan:** memperkenalkan real-life data shape.
**Instruksi:**

* Buat dict:

```python
user = {
    "nama": "Andi",
    "skills": ["SQL", "Python"],
    "pengalaman": {"tahun": 4, "role": "Data Analyst"}
}
```

* Tambahkan skill baru dan tampilkan semua key/value.

---

## **P4 — Conditional untuk Data Quality**

**Tujuan:** logika dasar seperti rule cleansing.
**Instruksi:**

* Jika `usia < 18`: print "Di bawah umur"
* Jika `usia 18–59`: print "Dewasa"
* Jika `usia >= 60`: print "Lansia"

---

## **P5 — Load Excel Menggunakan Pandas**

**Tujuan:** bridging SQL → Python.
**Instruksi:**

* Import `pandas`
* Load file: `df = pd.read_excel("sample_data.xlsx")`
* Tampilkan 5 baris pertama
* Tampilkan info tipe data (`df.info()`)

---

## **P6 — Filtering Data ala SQL WHERE**

**Tujuan:** bandingkan SQL vs pandas.
**Instruksi:**

* Tampilkan semua row dengan pendapatan > 5 juta
* Tampilkan semua row dari kota = “Jakarta”
* Hitung berapa jumlahnya

---

## **P7 — Grouping & Aggregation ala SQL GROUP BY**

**Tujuan:** tunjukkan kecepatan & fleksibilitas Python.
**Instruksi:**

* Group by `kota` → hitung rata-rata pendapatan
* Sort descending
* Print hasilnya

---

## **P8 — Cleaning Text Kolom `catatan`**

**Tujuan:** menunjukkan power Python dalam text processing.
**Instruksi:**
Gunakan library **re** dan **textacy / nltk / regex** (pilih salah satu):

* Normalisasi teks (lowercase)
* Hapus angka
* Hapus special characters
* Tokenisasi kata
* Hitung 10 kata paling sering muncul

> Ini akan menunjukkan betapa canggihnya Python untuk text cleansing yang *sangat sulit di SQL*.

---

## **P9 — Fuzzy Matching untuk Pemadanan Data**

**Tujuan:** menunjukkan kemampuan Python yang mustahil di SQL biasa.
Gunakan library:
`pip install rapidfuzz`

**Instruksi:**

* Buat 2 list nama yang mirip tapi tidak sama
* Hitung similarity score antar nama
* Tampilkan pasangan nama dengan score > 80%

Contoh:
“budi santoso” vs “budi santoko” → similarity 91

---

## **P10 — Visualisasi Data**

**Tujuan:** menunjukkan Python = SQL + grafik.
Gunakan:
`matplotlib` atau `plotly`

**Instruksi:**

* Buat bar chart rata-rata pendapatan per kota
* Tampilkan grafik langsung di VSCode

---