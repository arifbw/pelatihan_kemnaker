
---

## **S1 — Hello Streamlit + Layout Dasar**

**Tujuan:** mengenalkan struktur app.
**Instruksi:**

* Tampilkan judul dengan `st.title()`
* Tambahkan deskripsi
* Tambahkan emoji
* Tampilkan 3 teks sekaligus di kolom (`st.columns`)

---

## **S2 — Sidebar & Input Form**

**Tujuan:** membiasakan penggunaan sidebar.
**Instruksi:**

* Buat input di sidebar:

  * `nama` (text_input)
  * `usia` (number_input)
* Tampilkan greeting di main area:
  "Halo, {nama}, usia {usia}!"

---

## **S3 — Upload Excel & Preview**

**Tujuan:** workflow paling penting: upload → baca → tampilkan.
**Instruksi:**

* Buat `st.file_uploader(accept_excel)`
* Load dengan pandas
* Tampilkan 5 baris pertama
* Tampilkan jumlah row dan kolom

---

## **S4 — Filtering Data Realtime (SQL WHERE versi Streamlit)**

**Tujuan:** pemadanan data akan butuh fitur ini.
**Instruksi:**

* Ambil DataFrame dari upload
* Buat input pilihan kota (`selectbox`)
* Tampilkan data: `df[df["kota"] == pilihan_kota]`
* Hitung jumlah baris hasil filter

---

## **S5 — Form lengkap: Search + Range**

**Tujuan:** logika filtering multi-kriteria.
**Instruksi:**

* Input search: nama
* Range pendapatan: slider
* Filter DF berdasarkan 2 kondisi
* Tampilkan hasilnya

---

## **S6 — Visualisasi Interaktif**

**Tujuan:** mengenalkan chart cepat.
**Instruksi:**

* Buat bar chart rata-rata pendapatan per kota
* Pakai: `st.bar_chart()` atau `plotly`
* Chart otomatis berubah saat user pilih kota

---

## **S7 — Fuzzy Matching Interaktif**

**Tujuan:** tunjukkan bahwa Streamlit + Python powerful untuk pemadanan data.
**Instruksi:**

* Input dua nama di sidebar
* Hitung similarity pakai `rapidfuzz`
* Tampilkan score dalam gauge bar / progress bar
* Jika > 85 → tampilkan warna hijau ✔
* Jika < 85 → merah ✖


---

## **S8 — Data Cleansing Dashboard**

**Tujuan:** memperlihatkan power pandas di UI.
**Instruksi:**
Buat tombol:

* “Trim spasi nama”
* “Uppercase kolom nama”
* “Hapus duplikat”
  Setiap klik tombol, DF berubah dan tampil ulang.

---

## **S9 — Mini JSON Viewer**

**Tujuan:** bridging materi JSON → Flatten.
**Instruksi:**

* Input JSON via text_area
* Parse dengan `json.loads`
* Tampilkan hasil dalam expanders
* Jika JSON berisi array objek, tampilkan tabel

---

## **S10 — Export DataFrame ke Excel**

**Tujuan:** fitur yang sangat dibutuhkan di pekerjaan harian.
**Instruksi:**

* Setelah DataFrame difilter → bikin tombol
* Gunakan:

```python
st.download_button(
    label="Download Excel",
    data=df.to_excel(buffer, index=False),
    file_name="hasil.xlsx"
)
```

---