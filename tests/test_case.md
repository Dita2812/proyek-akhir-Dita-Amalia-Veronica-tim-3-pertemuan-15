from src.proses import hitung_rata_rata, status_lulus, ringkasan

def jalankan_uji():
    # TC01: Rata-rata normal[cite: 7]
    assert hitung_rata_rata([70, 80, 90]) == 80.0, "TC01 Gagal"  #[cite: 7]
    
    # TC02: List kosong (Empty case)[cite: 7, 8]
    assert hitung_rata_rata([]) == 0, "TC02 Gagal"  #[cite: 7]
    
    # TC03: Kelulusan pada nilai batas[cite: 7]
    assert len(status_lulus([60])) == 1, "TC03 Gagal"  #[cite: 7]
    
    # TC04: Kelulusan nilai di bawah batas[cite: 7]
    assert len(status_lulus([59])) == 0, "TC04 Gagal"
    
    # TC05: Ringkasan data lengkap
    res = ringkasan([50, 60, 70])
    assert res["jumlah"] == 3
    assert res["lulus"] == 2
    
    print("Semua test case berhasil dijalankan (PASS)!")  #[cite: 7]

if __name__ == "__main__":
    jalankan_uji()