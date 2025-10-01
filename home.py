import streamlit as st

st.set_page_config(page_title="Analisis Sentimen Berbahasa Melayu Bengkulu")

# Menambahkan judul ke website
st.title('Analisis Sentimen Pada Dataset Komentar Berbahasa Melayu Bengkulu')

# Menambahkan teks
st.write('Halo sanak segalo, kini kito pacak melakukan analisis sentimen menggunokan bahasa Melayu Bengkulu dengan lebih mudah disiko. Mulailah pilih topiknyo dibawah iko!')

# Menambahkan tombol untuk navigasi
st.write("---")
st.subheader("Pilih Topik untuk Analisis Sentimen")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Cagub 2025 Provinsi Bengkulu Paslon 01"):
        st.switch_page("pages/app.py")

with col2:
    if st.button("Cagub 2025 Provinsi Bengkulu Paslon 02"):
        st.switch_page("pages/app1.py")

with col3:
    if st.button("Perubahan Julukan Provinsi Bengkulu"):
        st.switch_page("pages/page2.py")
