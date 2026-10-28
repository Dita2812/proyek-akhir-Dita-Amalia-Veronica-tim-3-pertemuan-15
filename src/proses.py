BATAS_LULUS = 60

def hitung_rata_rata(nilai):
    if not nilai:
        return 0
    return sum(nilai) / len(nilai)

def status_lulus(nilai, batas=BATAS_LULUS):
    return [x for x in nilai if x >= batas]

def ringkasan(nilai):
    if not nilai:
        return {
            "jumlah": 0,
            "rata_rata": 0,
            "minimum": None,
            "maksimum": None,
            "lulus": 0
        }
    return {
        "jumlah": len(nilai),
        "rata_rata": hitung_rata_rata(nilai),
        "minimum": min(nilai) if nilai else None,
        "maksimum": max(nilai) if nilai else None,
        "lulus": len(status_lulus(nilai))
    }