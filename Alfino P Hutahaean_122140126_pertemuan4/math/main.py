
import math_operations

from math_operations import celsius_to_fahrenheit, celsius_to_kelvin

print("=== Geometri ===")
print("Luas persegi 4x4:", math_operations.luas_persegi(4))
print("Keliling lingkaran r=5:", math_operations.keliling_lingkaran(5))
print("Luas persegi panjang 3x6:", math_operations.luas_persegi_panjang(3, 6))

print("\n=== Konversi Suhu ===")
print("30°C ke Fahrenheit:", celsius_to_fahrenheit(30))
print("30°C ke Kelvin:", celsius_to_kelvin(30))
