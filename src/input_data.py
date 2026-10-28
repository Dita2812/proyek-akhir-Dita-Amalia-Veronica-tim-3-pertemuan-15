def input_daftar_nilai():
    nilai_list = []
    print("\n--- Input Data Nilai Siswa ---")
    print("Ketikkan angka nilai satu per satu. Ketik 'selesai' untuk mengakhiri.")

    while True:
        teks = input("Masukkan nilai: ").strip()
        if teks.lower() == 'selesai':
            break
        try:
            val = float(teks)
            if 0 <= val <= 100:
                nilai_list.append(val)
            else:
                print("[Peringatan] Nilai harus berada dalam rentang 0 - 100.")
        except ValueError:
            print("[Error] Input tidak valid! Harap masukkan angka yang benar.")

    return nilai_list