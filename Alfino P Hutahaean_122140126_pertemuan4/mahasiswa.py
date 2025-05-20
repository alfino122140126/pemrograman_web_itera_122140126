mahasiswa = [
    {"nama": "Alfino", "nim": "122140126", "uts": 80, "uas": 90, "tugas": 85},
    {"nama": "Satria", "nim": "122140122", "uts": 60, "uas": 70, "tugas": 65},
    {"nama": "Supri", "nim": "122140123", "uts": 75, "uas": 60, "tugas": 70},
    {"nama": "Charly", "nim": "122140124", "uts": 90, "uas": 85, "tugas": 95},
    {"nama": "Aditya", "nim": "122140125", "uts": 40, "uas": 50, "tugas": 45}
]

print("{:<10} {:<8} {:<10} {:<10} {:<10} {:<12} {:<6}".format(
    "Nama", "NIM", "UTS", "UAS", "Tugas", "Nilai Akhir", "Grade"))

nilai_akhir_tertinggi = 0
nilai_akhir_terendah = 100
mahasiswa_tertinggi = None
mahasiswa_terendah = None

for m in mahasiswa:
    nilai_akhir = m["uts"] * 0.3 + m["uas"] * 0.4 + m["tugas"] * 0.3
    m["nilai_akhir"] = nilai_akhir

    if nilai_akhir >= 80:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 60:
        grade = "C"
    elif nilai_akhir >= 50:
        grade = "D"
    else:
        grade = "E"

    m["grade"] = grade

    print("{:<10} {:<8} {:<10} {:<10} {:<10} {:<12.2f} {:<6}".format(
        m["nama"], m["nim"], m["uts"], m["uas"], m["tugas"], nilai_akhir, grade))

    if nilai_akhir > nilai_akhir_tertinggi:
        nilai_akhir_tertinggi = nilai_akhir
        mahasiswa_tertinggi = m

    if nilai_akhir < nilai_akhir_terendah:
        nilai_akhir_terendah = nilai_akhir
        mahasiswa_terendah = m

print(f"\nMahasiswa Nilai Tertinggi: {mahasiswa_tertinggi['nama']} ({nilai_akhir_tertinggi:.2f})")
print(f"Mahasiswa Nilai Terendah: {mahasiswa_terendah['nama']} ({nilai_akhir_terendah:.2f})")
