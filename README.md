# 📊 Student Grade Analysis (Analisis Nilai Siswa)

Proyek ini adalah aplikasi berbasis Python untuk menganalisis data nilai siswa secara modular. Program dibuat untuk memenuhi tugas **Pertemuan 15 (Proyek Akhir)** dengan struktur kode yang rapi, teruji, dan memiliki penanganan kesalahan input (*error handling*) secara aman.

---

## 📁 Struktur Proyek

```text
proyek-akhir-Dita-Amalia-Veronica-tim-3-pertemuan-15/
│
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── proses.py
│   └── output.py
│
├── tests/
│   └── test_sederhana.py
│
├── data/
│   └── contoh_data.txt
│
├── docs/
│   └── screenshot/
│       ├── 01_fitur_utama.png
│       └── 02_pengujian_assert.png
│
├── main.py
├── .gitignore
└── README.md
```

---

## 🚀 Fitur Utama & Keunggulan

1. **Input Data Interaktif**: Memasukkan data nilai siswa satu per satu secara dinamis hingga pengguna mengetikkan `selesai`.
2. **Penanganan Kesalahan (Error Handling)**: Program tidak akan *crash* saat pengguna memasukkan karakter non-angka atau perintah salah, melainkan menampilkan pesan peringatan error secara interaktif.
3. **Analisis Statistik Lengkap**:
   - Menghitung nilai rata-rata (*mean*).
   - Menilai batas kelulusan ($\ge 60$).
   - Menentukan nilai tertinggi dan terendah.
4. **Pengujian Otomatis (Unit Testing)**: Menggunakan pernyataan `assert` untuk memastikan fungsi perhitungan bernilai valid secara konstan.

---

## 💻 Cara Menjalankan Aplikasi

### 1. Menjalankan Program Utama
Buka terminal PowerShell di folder proyek, lalu jalankan:
```powershell
python main.py
```

### 2. Menjalankan Unit Testing
Untuk menguji kebenaran logika fungsi secara otomatis:
```powershell
python -m tests.test_sederhana
```

---

## 📸 Dokumentasi & Bukti Pengujian

### 1. Eksekusi Program Utama & Handling Error
Bukti eksekusi program utama yang mencakup input nilai, penanganan input invalid, hingga pencetakan hasil analisis statistik secara lengkap:

![Eksekusi Fitur Utama](docs/screenshot/01_fitur_utama.png)

### 2. Pengujian Unit Test (Assert PASS)
Bukti bahwa seluruh *test case* fungsi matematika dan logika berhasil dijalankan tanpa kendala:

![Hasil Pengujian Assert](docs/screenshot/02_pengujian_assert.png)

---

## 🛠️ Modul & Peran Kode

- `src/input_data.py`: Menerima dan memvalidasi input dari pengguna.
- `src/proses.py`: Mengolah data nilai (hitung rata-rata, min, max, kelulusan).
- `src/output.py`: Menampilkan hasil analisis ke layar terminal secara terformat.
- `main.py`: Menghubungkan seluruh fungsi modul menjadi satu kesatuan alur program.