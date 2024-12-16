<p align="center">
  <a href="" rel="noopener">
 <img src="test_predict.png" alt="Project Thumbnail"></a>
</p>
<h3 align="center">Corn Disease Detection Based on Leaf Images</h3>

<div align="center">

<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white">
<img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white">
<img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=Keras&logoColor=white">
<img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
<img src="https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white">
<img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white">
</div>

---

<p align="center"> Selamat datang di repositori ini! Proyek ini menggunakan machine learning untuk mendeteksi penyakit pada tanaman jagung berdasarkan gambar daunnya. Tujuannya adalah untuk membantu petani mengidentifikasi penyakit sejak dini dan membantu petani mengambil tindakan untuk meminimalisir kerugian yang disebabkan oleh penyakit pada tanaman jagung.</p>
    <br> 
</p>

## Features
- Image classification: Menggunakan algoritma Convolutional Neural Network (CNN) untuk mengklasifikasikan penyakit tanaman jagung berdasarkan gambar daunnya.
- Model deployment: Menggunakan streamlit untuk membuat website sederhana(app.py) untuk menjalankan dan menguji model yang sudah dibuat.

## Files
- `corn_disease` : Folder yang menyimpan dataset yang belum dilakukan augmentasi khusus pada class gray leaf spot.
- `corn_disease2` : Folder yang menyimpan dataset yang sudah dilakukan augmentasi khusus pada class gray leaf spot.
- `requirements.txt` : File yang berisi daftar dependencies yang diperlukan untuk menjalankan proyek ini.
- `corn_disease_detection.ipynb`: File jupyter notebook yang berisi kode untuk melakukan preprocessing data, membuat visualisasi, dan melatih model.
- `model.h5`: File model yang telah dilatih dan disimpan dalam format h5.
- `app.py`: File utama yang berisi kode untuk menjalankan website streamlit.

## Installation
1. Clone repositori github ini ke local computer anda .
2. Install depedencies dengan menjalankan code berikut : 
```
pip install -r requirements.txt
```
3. Eksekusi file `app.py` untuk memulai website dengan code berikut:
```
streamlit run app.py
```

## Usage
1. Buka streamlit website yang sudah dijalankan.
2. Mengunggah foto daun tanaman jagung yang terindikasi penyakit.