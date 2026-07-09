"""
Bank tizimining asosiy boshqaruv moduli.
Kiritilgan buyruqlarni tekshiradi va xavfsiz qayta ishlaydi.
"""

from hisob import (
    yangi_hisob, pul_qoyish, ko_rsat_balans, 
    pul_yechish, pul_otkazish, ko_rsat_tarix, tizim_hisoboti
)

hisoblar = {}
keyingi_raqam = 1001


def tekshir_summa(matn: str) -> int:
    """Summa son va musbat ekanligini tekshiradi, aks holda None qaytaradi."""
    try:
        qiymat = int(matn)
        if qiymat <= 0:
            print("Xato: summa musbat bo'lsin")
            return None
        return qiymat
    except ValueError:
        print("Xato: summa son bo'lsin")
        return None


while True:
    try:
        cmd = input().strip()
        if not cmd or cmd == '':
            continue
        if cmd == 'exit':
            break
            
        # 1. Hisob ochish
        if cmd.startswith("och "):
            ism = cmd[4:].strip()
            if ism:
                hisoblar[keyingi_raqam] = yangi_hisob(ism, keyingi_raqam)
                keyingi_raqam += 1
                
        # 2. Pul qo'yish
        elif cmd.startswith("qoy "):
            qismlar = cmd[4:].split()
            if len(qismlar) == 2:
                summa = tekshir_summa(qismlar[1])
                if summa is not None:
                    pul_qoyish(hisoblar, int(qismlar[0]), summa)
                
        # 3. Balansni tekshirish
        elif cmd.startswith("balans "):
            ko_rsat_balans(hisoblar, int(cmd[7:].strip()))
            
        # 4. Pul yechish
        elif cmd.startswith("yech "):
            qismlar = cmd[5:].split()
            if len(len(qismlar) == 2 if isinstance(qismlar, list) else 0) or len(qismlar) == 2:
                summa = tekshir_summa(qismlar[1])
                if summa is not None:
                    pul_yechish(hisoblar, int(qismlar[0]), summa)
                
        # 5. Pul o'tkazish
        elif cmd.startswith("otkaz "):
            qismlar = cmd[6:].split()
            if len(qismlar) == 3:
                summa = tekshir_summa(qismlar[2])
                if summa is not None:
                    pul_otkazish(hisoblar, int(qismlar[0]), int(qismlar[1]), summa)
                    
        # 6. Tarix ko'rish
        elif cmd.startswith("tarix "):
            ko_rsat_tarix(hisoblar, int(cmd[6:].strip()))
            
        # 7. Umumiy hisobot
        elif cmd == "hisobot":
            tizim_hisoboti(hisoblar)
            
    except (EOFError, KeyboardInterrupt):
        break
    except Exception:
        continue
