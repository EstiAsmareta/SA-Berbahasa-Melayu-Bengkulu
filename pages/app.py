import streamlit as st
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
import re

# Konfigurasi aplikasi
MAX_SEQUENCE_LENGTH = 70

# Tentukan kamus pemetaan label
LABEL_MAPPING = {
    0: {'label_num': -1, 'label_text': 'Negatif'},
    1: {'label_num': 0, 'label_text': 'Netral'},
    2: {'label_num': 1, 'label_text': 'Positif'}
}
LABELS = [LABEL_MAPPING[i]['label_text'] for i in range(len(LABEL_MAPPING))]

# Muat sumber daya preprocessing (kamus slang, stopwords, kamus stemming)
@st.cache_resource
def load_preprocessing_resources():
    try:
        # Muat kamus normalisasi dari file Excel ke dictionary
        df_norm = pd.read_excel('normalisasi.xlsx')
        normalized_dict = pd.Series(df_norm['normalisasi'].values, index=df_norm['slang']).to_dict()
        
        # Muat daftar stopwords dari file Excel ke set
        df_stopwords = pd.read_excel('stopword.xlsx')
        stopwords = set(df_stopwords['stopword'].tolist())
            
        # Muat kamus stemming dari file Excel ke dictionary
        df_stem = pd.read_excel('stemmingTokens.xlsx')
        stemming_dict = pd.Series(df_stem['stemming'].values, index=df_stem['tokens']).to_dict()

        return normalized_dict, stopwords, stemming_dict
    except FileNotFoundError:
        st.error("Pastikan semua file sumber daya preprocessing tersedia.")
        st.stop()

normalized_dict, stopwords, stemming_dict = load_preprocessing_resources()

# --- Fungsi Pra-pemrosesan Teks Lengkap ---
def preprocess_text(text):
    """
    Melakukan serangkaian tahapan preprocessing pada teks.
    """
    # Pastikan input adalah string, tangani nilai non-string
    text = str(text)

    # 1. Hapus tanda baca (remove punctuation)
    text = re.sub(r'@\w+', ' ', text)
    text = re.sub(r'(.)\1{2,}', r'\1', text)
    text = re.sub(r'[\"*_\\/+>=\[\]:()\-^%~@&#?!,.]', ' ', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    # 2. Case folding
    text = text.lower()
    
    # 3. Normalisasi menggunakan kamus slang
    words = text.split()
    normalized_words = [normalized_dict.get(word, word) for word in words]
    text = ' '.join(map(str, normalized_words))
        
    # 4. Hapus stopwords (remove stopwords)
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords]
    text = ' '.join(map(str, filtered_words))
    
    # 5. Stemming
    words = text.split()
    stemming_words = [stemming_dict.get(word, word) for word in words]
    text = ' '.join(map(str, stemming_words))
    
    # Hapus spasi berlebih
    text = ' '.join(text.split())
    
    return text

# Muat model Keras dan Tokenizer
@st.cache_resource
def load_sentiment_resources():
    try:
        model = load_model('best_model.keras')
        with open('tokenizerQ1a.pkl', 'rb') as handle:
            tokenizer = pickle.load(handle)
        return model, tokenizer
    except FileNotFoundError:
        st.error("Pastikan file 'best_model.keras' dan 'tokenizerQ1a.pkl' tersedia.")
        st.stop()

model, tokenizer = load_sentiment_resources()

# --- Antarmuka Aplikasi Streamlit ---
st.title("Analisis Sentimen Cagub 2025 Provinsi Bengkulu Paslon 01")
st.markdown("Masukkan teks di bawah ini untuk mendapatkan hasil sentimen.")

user_input = st.text_area("Input Teks", height=150, placeholder="Tuliskan komentar Anda di sini...")
    
if st.button("Analisis Sentimen"):
    if user_input:
        with st.spinner("Menganalisis..."):
            cleaned_text = preprocess_text(user_input)
            
            sequence = tokenizer.texts_to_sequences([cleaned_text])
            padded_sequence = pad_sequences(sequence, maxlen=MAX_SEQUENCE_LENGTH, padding='post')
            
            prediction = model.predict(padded_sequence, verbose=0)
            
            predicted_class_index = np.argmax(prediction)
            predicted_label_text = LABEL_MAPPING[predicted_class_index]['label_text']
            predicted_score = np.max(prediction)
            
            st.subheader("Hasil Analisis:")
            if predicted_label_text == 'Positif':
                st.success(f"**Sentimen:** {predicted_label_text} 😊")
            elif predicted_label_text == 'Negatif':
                st.error(f"**Sentimen:** {predicted_label_text} 😠")
            else:
                st.info(f"**Sentimen:** {predicted_label_text} 😐")
            
            st.write(f"**Probabilitas Tertinggi:** {predicted_score:.2f}")

    else:
        st.warning("Mohon masukkan teks untuk dianalisis.")
