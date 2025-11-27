""" Tujuan: membiasakan penggunaan sidebar. Instruksi:

Buat input di sidebar:

nama (text_input)
usia (number_input)
Tampilkan greeting di main area: "Halo, {nama}, usia {usia}!" """

import streamlit as st
# Membuat input di sidebar
nama = st.sidebar.text_input("Masukkan nama Anda:")
usia = st.sidebar.number_input("Masukkan usia Anda:", min_value=0, step=1)
# Menampilkan greeting di main area
st.sidebar.write(f"Halo 2, {nama}, usia {usia}!")