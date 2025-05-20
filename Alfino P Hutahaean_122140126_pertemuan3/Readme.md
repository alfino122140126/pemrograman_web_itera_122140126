# Isi README.md
readme_content = """
# 📚 Aplikasi Manajemen Buku Pribadi

Aplikasi ini memungkinkan pengguna untuk mencatat, mengelola, dan memantau buku-buku yang dimiliki, sedang dibaca, atau ingin dibeli. Dibuat menggunakan React.js sebagai bagian dari tugas kuliah *Pemrograman Web*.

---

## 🚀 Fitur Aplikasi

- Menambah buku baru (judul, penulis, status)
- Mengedit dan menghapus data buku
- Pencarian buku berdasarkan judul atau penulis
- Filter buku berdasarkan status (Dimiliki, Sedang Dibaca, Ingin Dibeli)
- Statistik real-time jumlah buku per kategori
- Penyimpanan data di localStorage
- Navigasi antar halaman menggunakan React Router

---

## 🛠️ Teknologi dan Konsep

- **React Functional Components** dengan Hooks (`useState`, `useEffect`)
- **Custom Hooks**: `useLocalStorage`, `useBookStats`
- **Context API** untuk manajemen state global
- **PropTypes** untuk type checking komponen
- **React Router** untuk navigasi multi halaman
- **React Testing Library** untuk testing komponen

---

## 🧪 Testing

Dilakukan menggunakan:
- `@testing-library/react`
- `@testing-library/user-event`
- `@testing-library/jest-dom`

**Jumlah unit test:** 5  
**File test utama:** `BookForm.test.js`


---

## 📷 Screenshot Antarmuka
![Screenshot 2025-05-20 181944](https://github.com/user-attachments/assets/5cf47ae7-1bf4-4a5b-89ac-f2517c0af4c8)


---

## ⚙️ Cara Instalasi dan Menjalankan

1. Clone repositori atau ekstrak file zip
2. Jalankan di terminal:

```bash
npm install
npm start
