# 📚 Sistem Manajemen Perpustakaan Sederhana

## 🧠 Deskripsi

Aplikasi ini dirancang untuk mendemonstrasikan penerapan konsep Object-Oriented Programming (OOP) pada Python dalam bentuk sistem perpustakaan sederhana.

## 🎯 Fitur

- Menambahkan item ke perpustakaan
- Menampilkan semua item (Book, Magazine)
- Mencari berdasarkan judul dan ID

## 🧱 Konsep OOP yang Diterapkan

| Konsep         | Implementasi                                               |
| -------------- | ---------------------------------------------------------- |
| Abstract Class | `LibraryItem` (dengan method abstract `display_info`)      |
| Inheritance    | `Book` dan `Magazine` mewarisi `LibraryItem`               |
| Polymorphism   | Override method `display_info`                             |
| Encapsulation  | Atribut `__items`, `_id`, `_title`, `_author`, dll.        |
| Property       | Getter `@property` untuk `title` dan `id` di `LibraryItem` |

## 📂 Struktur

alfino_122140126_pertemuan5/
├── library_system.py
└── README.md

## 🧪 Contoh Output

=== Daftar Koleksi Perpustakaan ===
[BOOK] ID: IF220 | Title: Python OOP | Author: Alfino | Year: 2022
[BOOK] ID: IF221 | Title: Algoritma | Author: Suori | Year: 2022
[MAGAZINE] ID: MT22 | Title: Tekno Monthly | Issue: April | Year: 2023

---
