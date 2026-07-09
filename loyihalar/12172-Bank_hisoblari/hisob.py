"""
Bank hisoblari amallari moduli.
Hisob ochish, balans, o'tkazmalar, tarix va tizim hisoboti funksiyalari.
"""

def yangi_hisob(ism: str, keyingi_raqam: int) -> dict:
    """Yangi mijoz uchun bo'sh balansli hisob yaratadi."""
    hisob_malumoti = {
        "ism": ism,
        "balans": 0,
        "tarix": []
    }
    print(f"Hisob ochildi: {keyingi_raqam} — {ism}")
    return hisob_malumoti


def pul_qoyish(hisoblar: dict, raqam: int, summa: int) -> None:
    """Hisob balansini oshiradi va amalni tarixga yozadi."""
    h = hisoblar.get(raqam)
    if h is None:
        print("Xato: hisob topilmadi")
        return
        
    h["balans"] += summa
    h["tarix"].append(f"+{summa}")
    print(f"Qo'yildi: {summa} (balans: {h['balans']})")


def ko_rsat_balans(hisoblar: dict, raqam: int) -> None:
    """Mavjud hisob balansini ekranga chiqaradi."""
    h = hisoblar.get(raqam)
    if h is None:
        print("Xato: hisob topilmadi")
        return
        
    print(f"{raqam} — {h['ism']}: {h['balans']} so'm")


def pul_yechish(hisoblar: dict, raqam: int, summa: int) -> None:
    """Hisobdan pul yechadi, xatoliklarni tekshiradi."""
    h = hisoblar.get(raqam)
    if h is None:
        print("Xato: hisob topilmadi")
        return
        
    if h["balans"] < summa:
        print("Xato: mablag' yetarli emas")
        return
        
    h["balans"] -= summa
    h["tarix"].append(f"-{summa}")
    print(f"Yechildi: {summa} (balans: {h['balans']})")


def pul_otkazish(hisoblar: dict, dan_raqam: int, ga_raqam: int, summa: int) -> None:
    """Ikki hisob orasida pul o'tkazmasini xavfsiz bajaradi."""
    if dan_raqam == ga_raqam:
        print("Xato: o'ziga o'tkazib bo'lmaydi")
        return

    dan_h = hisoblar.get(dan_raqam)
    ga_h = hisoblar.get(ga_raqam)
    
    if dan_h is None or ga_h is None:
        print("Xato: hisob topilmadi")
        return
        
    if dan_h["balans"] < summa:
        print("Xato: mablag' yetarli emas")
        return
        
    dan_h["balans"] -= summa
    ga_h["balans"] += summa
    
    dan_h["tarix"].append(f"-{summa} ({ga_raqam} ga)")
    ga_h["tarix"].append(f"+{summa} ({dan_raqam} dan)")
    
    print(f"O'tkazildi: {dan_raqam} → {ga_raqam}, {summa} so'm")


def ko_rsat_tarix(hisoblar: dict, raqam: int) -> None:
    """Hisob amallari tarixini raqamlab ko'rsatadi."""
    h = hisoblar.get(raqam)
    if h is None:
        print("Xato: hisob topilmadi")
        return
        
    if not h["tarix"]:
        print("Tarix bo'sh")
        return
        
    for i, amal in enumerate(h["tarix"], 1):
        print(f"{i}. {amal}")


def tizim_hisoboti(hisoblar: dict) -> None:
    """Butun bank tizimi bo'yicha umumiy hisobot chiqaradi."""
    if not hisoblar:
        print("Hisoblar yo'q")
        return
        
    n = len(hisoblar)
    jami_mablag = sum(h["balans"] for h in hisoblar.values())
    print(f"Hisoblar: {n} ta | Jami mablag': {jami_mablag} so'm")
    
    eng_katta_raqam = max(hisoblar.keys(), key=lambda k: hisoblar[k]["balans"])
    eng_h = hisoblar[eng_katta_raqam]
    print(f"Eng katta balans: {eng_katta_raqam} — {eng_h['ism']} ({eng_h['balans']} so'm)")
