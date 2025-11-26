---

# 📘 **PANDUAN PERSIAPAN PELATIHAN PYTHON DASAR (SORE–MALAM INI)**

Pastikan semua langkah berikut diselesaikan sebelum pelatihan dimulai besok.

---

# ✅ **1. Install Python 3.10+**

### **Windows**

1. Download Python di:
   [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Saat instalasi, **CEKLIS**:
   ✔ *Add Python to PATH*
3. Klik **Install Now**
4. Setelah selesai, cek instalasi:
   Buka CMD → ketik:

   ```
   python --version
   pip --version
   ```

### **MacOS**

```
brew install python
```

Cek:

```
python3 --version
pip3 --version
```

### **Linux (Ubuntu/Debian)**

```
sudo apt update
sudo apt install python3 python3-pip -y
```

---

# ✅ **2. Install Streamlit**

Streamlit akan dipakai untuk membuat aplikasi web sederhana dari Python.

Jalankan:

```
pip install streamlit
```

Cek instalasi:

```
streamlit hello
```

Jika halaman demo terbuka di browser → *sukses*.

---

# ✅ **3. Install Library Pemrosesan Data (Wajib Terpasang)**

Jalankan perintah berikut:

```
pip install pandas numpy matplotlib seaborn plotly
```

Opsional (jika ingin lebih advanced):

```
pip install jupyter notebook
```

---

# ✅ **4. Install Library Koneksi PostgreSQL & Import Data**

### **Koneksi ke PostgreSQL**

```
pip install psycopg2-binary sqlalchemy
```

### **Baca & Tulis File Excel**

```
pip install openpyxl
```

### **Penggabungan Data Multi-Source (CSV, Excel, DB, dll)**

Sudah ter-cover oleh:

* **pandas**
* **sqlalchemy**
* **openpyxl**

Tambahan jika ingin dukung Parquet:

```
pip install pyarrow
```

---

# ✅ **5. (Opsional tapi direkomendasikan) Buat Virtual Environment**

Supaya library tidak bentrok.

### Windows / Mac / Linux:

```
python -m venv venv
```

Aktifkan environment:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

Setelah aktif, ulangi instalasi library:

```
pip install streamlit pandas numpy matplotlib seaborn plotly psycopg2-binary sqlalchemy openpyxl pyarrow
```

---

# ✅ **6. Cek Lengkap Instalasi (Silakan jalankan kode ini)**

Buat file `check_setup.py`, isi dengan:

```python
import pandas as pd
import numpy as np
import matplotlib
import streamlit as st
import sqlalchemy
import psycopg2
import openpyxl

print("Semua library terinstall dengan baik!")
```

Jalankan:

```
python check_setup.py
```

Jika tidak ada error → setup siap.

---

# 📎 **7. Tools Tambahan yang Disarankan**

### **Editor yang disarankan: VSCode**

Download: [https://code.visualstudio.com/](https://code.visualstudio.com/)

Install extensions:

* **Python** (Microsoft)
* **Pylance**
* **Jupyter**

---