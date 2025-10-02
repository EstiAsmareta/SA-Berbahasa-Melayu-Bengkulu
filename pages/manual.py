import streamlit as st

# Menambahkan judul ke website
st.title('Tentang Kami')

# Bagian Deskripsi
st.write(
    "Website ini dikembangkan guna menyediakan ruang bagi masyarakat **Kota Bengkulu** untuk mengetahui opini/perasaan dari sebuah teks **berbahasa Melayu Bengkulu**. "
    "Website ini dapat melakukan analisis sentimen pada tiga topik: Cagub Provinsi Bengkulu 2024 Paslon 01, Cagub Provinsi Bengkulu 2024 Paslon 02, dan perubahan julukan Provinsi Bengkulu."
)

st.divider() # Garis pemisah yang lebih modern daripada st.write("---")

# Bagian Panduan Penggunaan
st.header("Panduan Penggunaan")
st.markdown("""
1.  Pilih **topik** dari teks yang akan dianalisis sentimennya
2.  Anda akan diarahkan ke halaman analisis sentimen
3.  Silahkan masukkan teks pada kolom yang telah disediakan
4.  Tekan tombol **'Mulai Analisis'** untuk memulai proses analisis
5.  Silahkan menunggu hingga hasil analisis selesai dan ditampilkan
""")

st.divider()

# Bagian Syarat dan Ketentuan
st.header("Syarat dan Ketentuan")
st.write("Informasi Lebih lanjut: **asmaretaayu@gmail.com**")