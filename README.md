# PathFinder AI — Sistem Pakar Konsultasi Karir IT

[![Deployment Status](https://img.shields.io/badge/Deployment-Vercel-black?style=for-the-badge&logo=vercel)](https://sistempakar-ten.vercel.app)
[![Tech Stack](https://img.shields.io/badge/Stack-Python_%7C_Flask-blue?style=for-the-badge&logo=python)](https://flask.palletsprojects.com/)

Sistem Pakar ini dirancang untuk membantu mahasiswa atau individu dalam menentukan jalur karir di bidang Teknologi Informasi yang paling sesuai dengan minat dan keterampilan mereka. Sistem menggunakan metode **Forward Chaining** untuk melakukan inferensi berdasarkan basis pengetahuan (*knowledge base*) yang telah disusun secara pakar.

---

## 🚀 Fitur Utama
- **Inference Engine**: Menggunakan logika *Forward Chaining* untuk mencocokkan fakta (jawaban pengguna) dengan aturan (*rules*) karir.
- **Certainty Factor**: Menghasilkan persentase kecocokan (*match rate*) yang akurat untuk setiap kategori karir.
- **Visualisasi Dinamis**: Antarmuka berbasis *Glassmorphism* yang modern, responsif, dan interaktif.
- **Career Roadmap**: Menyediakan rekomendasi skill, tools, dan sertifikasi untuk setiap hasil karir.

---

## 🛠️ Teknologi yang Digunakan
- **Backend**: Python 3.13 & Flask Framework.
- **Frontend**: HTML5, CSS3 (Vanilla), & JavaScript (ES6+).
- **Logika Inferensi**: Forward Chaining (Fact-driven).
- **Deployment**: Vercel Cloud Platform.

---

## 📂 Struktur Project
Project ini dikembangkan dengan struktur yang minimalis dan efisien:
```text
sistem_pakar/
├── app.py           # Backend Flask & Embedded Frontend (HTML/CSS/JS)
├── requirements.txt # Daftar dependensi library
└── vercel.json      # Konfigurasi deployment serverless
```

---

## 💻 Cara Menjalankan Secara Lokal

1. **Clone Repository**
   ```bash
   git clone https://github.com/NadineAriesta/H1D024028-PraktikumKB-ResponsiSistemPakar.git
   cd H1D024028-PraktikumKB-ResponsiSistemPakar/sistem_pakar
   ```

2. **Install Dependensi**
   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Aplikasi**
   ```bash
   python app.py
   ```
   Buka browser dan akses `http://localhost:5000`.

---

## ✍️ Penulis
- **Nama**: Nadine Ariesta
- **NIM**: H1D024028
- **Mata Kuliah**: Praktikum Kecerdasan Buatan (Responsi 2)

---
© 2026 PathFinder AI — Dibuat untuk tujuan edukasi.
