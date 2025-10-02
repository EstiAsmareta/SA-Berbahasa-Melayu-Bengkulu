import streamlit as st

# Mengatur konfigurasi halaman
st.set_page_config(
    page_title="Analisis Sentimen Berbahasa Melayu Bengkulu",
    layout="centered" # Opsional: mengatur layout menjadi terpusat
)

# --- Tombol Navigasi Manual Book (di atas) ---
# st.switch_page digunakan untuk navigasi antar halaman di Streamlit
if st.button("📚 Manual Book / Tentang Aplikasi", type="secondary"):
    st.switch_page("pages/manual.py") 
    
st.markdown("---")


# Menambahkan judul ke website
st.title('Analisis Sentimen Pada Dataset Komentar Berbahasa Melayu Bengkulu')

# Menambahkan teks sambutan
st.write('Halo sanak segalo, kini kito pacak melakukan analisis sentimen menggunokan bahasa Melayu Bengkulu dengan lebih mudah disiko. Mulailah pilih topiknyo dibawah iko!')

# Menambahkan tombol untuk navigasi
st.markdown("---")
st.subheader("Pilih Topik untuk Analisis Sentimen")

# Menggunakan kolom untuk tata letak tombol
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Cagub 2025 Provinsi Bengkulu Paslon 01", key="paslon_01"):
        st.switch_page("pages/paslon_01_app.py") 

with col2:
    if st.button("Cagub 2025 Provinsi Bengkulu Paslon 02", key="paslon_02"):
        st.switch_page("pages/paslon_02_app.py") 

with col3:
    if st.button("Perubahan Julukan Provinsi Bengkulu", key="julukan"):
        st.switch_page("pages/perubahan_julukan.py")
