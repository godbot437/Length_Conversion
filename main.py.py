import os 

def clearScreen():
    # Mmeberihkan display Windows
    if os.name == 'nt':
        os.system('cls')
    
    # Membersihkan display Unix/Linux/Mac
    else:
        os.system('clear')


# Rumus Kilometer (KM)
def konvers_kilometer(input_km):
    km_to_hm = input_km * 10
    km_to_dam = input_km * 100
    km_to_m = input_km * 10 ** 3
    km_to_dm = input_km * 10 ** 4
    km_to_cm = input_km * 10 ** 5
    km_to_mm = input_km * 10 ** 6

    # pembulatan
    hasil_km_to_hm = f"{km_to_hm:.2f}"
    hasil_km_to_dam = f"{km_to_dam:.2f}"
    hasil_km_to_m = f"{km_to_m:.2f}"
    hasil_km_to_dm = f"{km_to_dm:.2f}"
    hasil_km_to_cm = f"{km_to_cm:.2f}"
    hasil_km_to_mm = f"{km_to_mm:.2f}"
    
    print(str(input_km) +  " km")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_km_to_hm) + " hm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_km_to_dam) + " dam")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_km_to_m) + " m")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_km_to_dm) + " dm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_km_to_cm) + " cm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_km_to_mm) + " mm")

    return
# ==========================================
# Rumus Hektometer (HM)
def konvers_hektometer(input_hm):
    hm_to_km = input_hm / 10
    hm_to_dam = input_hm * 10
    hm_to_m = input_hm * 100
    hm_to_dm = input_hm * 10 ** 3
    hm_to_cm = input_hm * 10 ** 4
    hm_to_mm = input_hm * 10 ** 5
    
    # pembulatan
    hasil_hm_to_km = f"{hm_to_km:.2f}"
    hasil_hm_to_dam = f"{hm_to_dam:.2f}"
    hasil_hm_to_m = f"{hm_to_m:.2f}"
    hasil_hm_to_dm = f"{hm_to_dm:.2f}"
    hasil_hm_to_cm = f"{hm_to_cm:.2f}"
    hasil_hm_to_mm = f"{hm_to_mm:.2f}"

    print(str(input_hm) +  " hm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_hm_to_km) + " km")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_hm_to_dam) + " dam")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_hm_to_m) + " m")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_hm_to_dm) + " dm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_hm_to_cm) + " cm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_hm_to_mm) + " mm")

    return
# ==============================================
# Rumus Dekameter (DAM)
def konvers_dekameter(input_dam):
    dam_to_km = input_dam / 100
    dam_to_hm = input_dam / 10
    dam_to_m = input_dam * 10
    dam_to_dm = input_dam * 100
    dam_to_cm = input_dam * 10 ** 3
    dam_to_mm = input_dam * 10 ** 4

    # pembulatan
    hasil_dam_to_km = f"{dam_to_km:.2f}"
    hasil_dam_to_hm = f"{dam_to_hm:.2f}"
    hasil_dam_to_m = f"{dam_to_m:.2f}"
    hasil_dam_to_dm = f"{dam_to_dm:.2f}"
    hasil_dam_to_cm = f"{dam_to_cm:.2f}"
    hasil_dam_to_mm = f"{dam_to_mm:.2f}"

    print(str(input_dam) +  " dam")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_dam_to_km) + " km")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_dam_to_hm) + " hm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_dam_to_m) + " m")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_dam_to_dm) + " dm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_dam_to_cm) + " cm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_dam_to_mm) + " mm")

    return
# ========================================
# Rumus Meter (M)
def konvers_meter(input_m):
    m_to_km = input_m / 10 ** 3
    m_to_hm = input_m / 100
    m_to_dam = input_m / 10
    m_to_dm = input_m * 10
    m_to_cm = input_m * 100
    m_to_mm = input_m * 10 ** 3

    # pebulatan
    hasil_m_to_km = f"{m_to_km:.2f}"
    hasil_m_to_hm = f"{m_to_hm:.2f}"
    hasil_m_to_dam = f"{m_to_dam:.2f}"
    hasil_m_to_dm = f"{m_to_dm:.2f}"
    hasil_m_to_cm = f"{m_to_cm:.2f}"
    hasil_m_to_mm = f"{m_to_mm:.2f}"

    print(str(input_m) +  " m")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_m_to_km) + " km")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_m_to_hm) + " hm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_m_to_dam) + " dam")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_m_to_dm) + " dm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_m_to_cm) + " cm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_m_to_mm) + " mm")

    return
# ==========================================
# Rumus Desimeter (DM)
def konvers_desimeter(input_dm):
    dm_to_km = input_dm / 10 ** 4
    dm_to_hm = input_dm / 10 ** 3
    dm_to_dam = input_dm / 100
    dm_to_m = input_dm / 10
    dm_to_cm = input_dm * 10
    dm_to_mm = input_dm * 100

    # pembulatan
    hasil_dm_to_km = f"{dm_to_km:.2f}"
    hasil_dm_to_hm = f"{dm_to_hm:.2f}"
    hasil_dm_to_dam = f"{dm_to_dam:.2f}"
    hasil_dm_to_m = f"{dm_to_m:.2f}"
    hasil_dm_to_cm = f"{dm_to_cm:.2f}"
    hasil_dm_to_mm = f"{dm_to_mm:.2f}"

    print(str(input_dm) +  " dm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_dm_to_km) + " km")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_dm_to_hm) + " hm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_dm_to_dam) + " dam")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_dm_to_m) + " m")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_dm_to_cm) + " cm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_dm_to_mm) + " mm")

    return
# ==========================================
# Rumus Centimeter (CM)
def konvers_centimeter(input_cm):
    cm_to_km = input_cm / 10 ** 5
    cm_to_hm = input_cm / 10 ** 4
    cm_to_dam = input_cm / 10 ** 3
    cm_to_m = input_cm / 100
    cm_to_dm = input_cm / 10
    cm_to_mm = input_cm * 10

    # pembulatan
    hasil_cm_to_km = f"{cm_to_km:.2f}"
    hasil_cm_to_hm = f"{cm_to_hm:.2f}"
    hasil_cm_to_dam = f"{cm_to_dam:.2f}"
    hasil_cm_to_m = f"{cm_to_m:.2f}"
    hasil_cm_to_dm = f"{cm_to_dm:.2f}"
    hasil_cm_to_mm = f"{cm_to_mm:.2f}"

    print(str(input_cm) +  " cm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_cm_to_km) + " km")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_cm_to_hm) + " hm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_cm_to_dam) + " dam")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_cm_to_m) + " m")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_cm_to_dm) + " dm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_cm_to_mm) + " mm")

    return
# ==========================================

# Rumus Milimeter (MM)
def konvers_milimeter(input_mm):
    mm_to_km = input_mm / 10 ** 6
    mm_to_hm = input_mm / 10 ** 5
    mm_to_dam = input_mm / 10 ** 4
    mm_to_m = input_mm / 10 ** 3
    mm_to_dm = input_mm / 100
    mm_to_cm = input_mm / 10

    # pembulatan
    hasil_mm_to_km = f"{mm_to_km:.2f}"
    hasil_mm_to_hm = f"{mm_to_hm:.2f}"
    hasil_mm_to_dam = f"{mm_to_dam:.2f}"
    hasil_mm_to_m = f"{mm_to_m:.2f}"
    hasil_mm_to_dm = f"{mm_to_dm:.2f}"
    hasil_mm_to_cm = f"{mm_to_cm:.2f}"

    print(str(input_mm) +  " mm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_mm_to_km) + " km")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_mm_to_hm) + " hm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_mm_to_dam) + " dam")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_mm_to_m) + " m")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_mm_to_dm) + " dm")
    print("||" )
    print("=" * 5 + ">" + " " + str(hasil_mm_to_cm) + " cm")


    return
# ===========================================
def submenu():
    print("\n[9] Kembali ke menu")
    print("[0] Keluar")
    return

# Menu Konvers
while True:
    # clearScreen()
    print("="*30 + " " + "Main Menu" + " " + "="*30)
    print("[1] Konversi kilometer")
    print("[2] Konversi hektometer")
    print("[3] Konversi dekameter")
    print("[4] Konversi meter")
    print("[5] Konversi desimeter")
    print("[6] Konversi centimeter")
    print("[7] Konversi milimeter")
    print("[0] Keluar")

    input_menu = int(input("\n[+] Masukkan Nilai : "))
    clearScreen()

    if input_menu == 1:
        input_km = float(input("[+] Masukkan Nilai : "))
        clearScreen()
        konvers_kilometer(input_km)

        submenu()
        input_submenu = int(input("[+] Masukkan nilai : "))

        if input_submenu == 9:
            clearScreen()
            continue

        elif input_submenu == 0:
            print("Have a nice day")
            break
        break
    
    elif input_menu == 2:
        input_hm = float(input("[+] Masukkan Nilai : "))
        clearScreen()
        konvers_hektometer(input_hm)
        submenu()
        input_submenu = int(input("[+] Masukkan nilai : "))

        if input_submenu == 9:
            clearScreen()
            continue

        elif input_submenu == 0:
            print("Have a nice day")
            break
        break

    elif input_menu == 3:
        input_dam = float(input("[+] Masukkan Nilai : "))
        clearScreen()
        konvers_dekameter(input_dam)
        submenu()
        input_submenu = int(input("[+] Masukkan nilai : "))

        if input_submenu == 9:
            clearScreen()
            continue

        elif input_submenu == 0:
            print("Have a nice day")
            break
        break

    elif input_menu == 4:
        input_m = float(input("[+] Masukkan Nilai : "))
        clearScreen()
        konvers_meter(input_m)
        submenu()
        input_submenu = int(input("[+] Masukkan nilai : "))

        if input_submenu == 9:
            clearScreen()
            continue

        elif input_submenu == 0:
            print("Have a nice day")
            break
        break
    
    elif input_menu == 5:
        input_dm = float(input("[+] Masukkan Nilai : "))
        clearScreen()
        konvers_desimeter(input_dm)
        submenu()
        input_submenu = int(input("[+] Masukkan nilai : "))

        if input_submenu == 9:
            clearScreen()
            continue

        elif input_submenu == 0:
            print("Have a nice day")
            break
        break

    elif input_menu == 6:
        input_cm = float(input("[+] Masukkan Nilai : "))
        clearScreen()
        konvers_centimeter(input_cm)
        submenu()
        input_submenu = int(input("[+] Masukkan nilai : "))

        if input_submenu == 9:
            clearScreen()
            continue

        elif input_submenu == 0:
            print("Have a nice day")
            break
        break

    
    elif input_menu == 7:
        input_mm = float(input("[+] Masukkan Nilai : "))
        clearScreen()
        konvers_milimeter(input_mm)
        submenu()
        input_submenu = int(input("[+] Masukkan nilai : "))

        if input_submenu == 9:
            clearScreen()
            continue

        elif input_submenu == 0:
            print("Have a nice day")
            break
        break

    elif input_menu == 0:
        print("Thanks telah menggunakan tool sederhana ini")
        break

    else:
        print("Pilihan tidak valid")
        break
