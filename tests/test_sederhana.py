import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.proses import hitung_rata_rata, status_lulus, ringkasan

def jalankan_uji():
    assert hitung_rata_rata([70, 80, 90]) == 80.0, "TC01 Gagal"
    assert hitung_rata_rata([]) == 0, "TC02 Gagal"
    assert len(status_lulus([60])) == 1, "TC03 Gagal"
    assert len(status_lulus([59])) == 0, "TC04 Gagal"
    
    res = ringkasan([50, 60, 70])
    assert res["jumlah"] == 3
    assert res["lulus"] == 2
    
    print("Semua test case berhasil dijalankan (PASS)!")

if __name__ == "__main__":
    jalankan_uji()