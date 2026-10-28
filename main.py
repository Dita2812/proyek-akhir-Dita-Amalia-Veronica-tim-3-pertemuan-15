from src.input_data import input_daftar_nilai
from src.proses import ringkasan
from src.output import tampilkan_ringkasan

def main():
    print("=== Program Analisis Nilai Siswa ===")
    data_nilai = input_daftar_nilai()
    hasil_ringkasan = ringkasan(data_nilai)
    tampilkan_ringkasan(hasil_ringkasan)

if __name__ == "__main__":
    main()