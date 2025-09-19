from tabulate import tabulate
import random

# Fungsi fungsi untuk memvalidasi datatype yang diinput sama user
# Fungsi Data yang diinput harus Angka/Int
def inputHarusAngka(pesan):
    while True:
        nilai = input(pesan)
        if nilai.isdigit():
            return int(nilai)
        print("Input harus berupa angka! Coba lagi.\n")
# Fungsi Data yang diinput harus huruf/string
def inputHarusString(pesan):
    while True:
        teks = input(pesan)
        if teks.replace(" ", "").isalpha():
            return teks
        print("Input harus berupa huruf saja! Coba lagi.\n")

# Fungsi-fungsi yang akan dimasukkan atau dipanggil sub menu karakter
# Fungsi untuk melihat karakter
def liatkarakter(karakter):
    if not karakter:
        print("Tidak ada karakter yang tersedia.\n")
        return
    tabel = [[i+1, b["nama"], b["HP"], b["ATK"], b["Afiliasi"]] for i, b in enumerate(karakter)]
    print(tabulate(tabel, headers=["Index", "Nama", "HP", "ATK", "Afiliasi"], tablefmt="fancy_grid"))
# Fungsi untuk menambah karakter
def tambahkarakter(karakter):
    while True:
        nama = inputHarusString("Masukkan nama karakter: ")
        if any(b["nama"].lower() == nama.lower() for b in karakter):
            print("Karakter sudah ada!\n")
            continue
        afiliasi = inputHarusString("Masukkan afiliasi karakter: ")
        while True:
            hp = inputHarusAngka("Masukkan HP (200-600): ")
            atk = inputHarusAngka("Masukkan ATK (200-600): ")
            if 200 <= hp <= 600 and 200 <= atk <= 600 and hp + atk == 800: # nilai bisa sampai 600 karena mengambil nilai tengah
                karakter.append({"nama": nama, "HP": hp, "ATK": atk, "Afiliasi": afiliasi})
                print(f"Karakter {nama} berhasil ditambahkan!\n")
                return
            print("HP + ATK harus = 800, dan masing-masing 200-600.\n")
# Fungsi untuk menghapus karakter
def hapuskarakter(karakter):
    if not karakter:
        print("Tidak ada karakter untuk dihapus.\n")
        return
    liatkarakter(karakter)
    idx = inputHarusAngka("Masukkan index karakter yang ingin dihapus: ")-1
    if 0 <= idx < len(karakter):
        hapus = karakter.pop(idx)
        print(f"Karakter {hapus['nama']} berhasil dihapus.\n")
    else:
        print("Index tidak valid.\n")
# Fungsi untuk mengedit karakter
def editkarakter(karakter):
    if not karakter:
        print("Tidak ada karakter untuk diedit.\n")
        return
    liatkarakter(karakter)
    idx = inputHarusAngka("Masukkan index karakter yang ingin diedit: ")-1
    if 0 <= idx < len(karakter):
        nama = inputHarusString("Masukkan nama baru: ")
        afiliasi = inputHarusString("Masukkan afiliasi baru: ")
        while True:
            hp = inputHarusAngka("Masukkan HP baru (200-600): ")
            atk = inputHarusAngka("Masukkan ATK baru (200-600): ")
            if 200 <= hp <= 600 and 200 <= atk <= 600 and hp+atk == 800:
                karakter[idx]["nama"] = nama
                karakter[idx]["afiliasi"] = afiliasi
                karakter[idx]["HP"], karakter[idx]["ATK"] = hp, atk
                print(f"Karakter berhasil diedit!\n")
                return karakter
            print("HP+ATK harus = 800, dan masing2 200-600.\n")
    else:
        print("Index tidak valid.\n")
    return karakter

# Fungsi-fungsi yang akan dimasukkan atau dipanggil sub menu Item
# Fungsi saat melihat item
def liatitem(item):
    if not item:
        print("Tidak ada item yang tersedia.\n")
        return
    tabel = [[i+1, b["nama"], b["rarity"], b["kegunaan"]] for i, b in enumerate(item)]
    print(tabulate(tabel, headers=["Index", "Nama", "Rarity", "Kegunaan"], tablefmt="fancy_grid"))
# Fungsi saat menambah item
def tambahitem(item):
    nama = inputHarusString("Masukkan nama item: ")
    while True:
        kegunaan = input("Kegunaan item (HP/ATK): ").strip().upper()
        if kegunaan in ["HP", "ATK"]:
            break
        print("Input salah, hanya HP/ATK.\n")
    while True:
        rarity = input("Rarity item (common/rare/epic): ").strip().lower()
        if rarity in ["common", "rare", "epic"]:
            break
        print("Input salah, hanya common/rare/epic.\n")
    item.append({"nama": nama, "rarity": rarity, "kegunaan": kegunaan})
    print(f"Item {nama} berhasil ditambahkan!\n")
# Fungsi saat menghapus item
def hapusitem(item):
    if not item:
        print("Tidak ada item untuk dihapus.\n")
        return
    liatitem(item)
    idx = inputHarusAngka("Masukkan index item yang ingin dihapus: ")-1
    if 0 <= idx < len(item):
        hapus = item.pop(idx)
        print(f"Item {hapus['nama']} berhasil dihapus.\n")
    else:
        print("Index tidak valid.\n")
# Fungsi untuk menentukan efek dan rarity item
def efekitem(item, player):
    if item["rarity"] == "common": 
        hp, atk = 30, 5
    elif item["rarity"] == "rare": 
        hp, atk = 60, 10
    else: 
        hp, atk = 90, 15
    if item["kegunaan"] == "HP":
        player["HP"] += hp
        print(f"{player['nama']} menambah HP {hp}!")
    else:
        player["ATK"] += atk
        print(f"{player['nama']} menambah ATK {atk}!")

# Fungsi-fungsi yang akan dimasukkan atau dipanggil sub menu play
# Fungsi memilih bos
def pilihbos():
    while True:
        level = input("Pilih bos (easy/hard): ").strip().lower()
        if level == "easy":
            return {"nama": "Boss Easy", "HP": random.randint(600,700), "ATK": random.randint(30,60)}
        elif level == "hard":
            return {"nama": "Boss Hard", "HP": random.randint(800,1000), "ATK": random.randint(70,90)}
        else:
            print("Input salah! Ketik 'easy' atau 'hard'.\n")
# Fungsi memainkan PVE
def pve(karakter, item):
    if not karakter:
        print("Belum ada karakter.\n")
        return
    if not item:
        print("Belum ada item.\n")
        return
    liatkarakter(karakter)
    idx = inputHarusAngka("Pilih karakter: ")-1
    if not (0 <= idx < len(karakter)):
        print("Index tidak valid.\n")
        return
    player = karakter[idx].copy()
    bos = pilihbos()
    print(f"\n{player['nama']} melawan {bos['nama']} (HP {bos['HP']}, ATK {bos['ATK']})\n")

    while player["HP"] > 0 and bos["HP"] > 0:
        giliran = random.randint(1,2)
        if giliran == 1:
            print(f"\n--- Giliran {player['nama']} ---")
            liatitem(item)
            idxi = inputHarusAngka("Pilih item (index): ")-1
            if 0 <= idxi < len(item):
                efekitem(item[idxi], player)
            bos["HP"] = max(0, bos["HP"] - player["ATK"])
            print(f"{player['nama']} menyerang {bos['nama']} -{player['ATK']} HP")
        else:
            print(f"\n--- Giliran {bos['nama']} ---")
            player["HP"] = max(0, player["HP"] - bos["ATK"])
            print(f"{bos['nama']} menyerang {player['nama']} -{bos['ATK']} HP")

        print(f"Status: {player['nama']} HP={player['HP']} | {bos['nama']} HP={bos['HP']}")

    print("\n=== HASIL ===")
    if player["HP"] <= 0 and bos["HP"] <= 0: print("Pertarungan Seri!")
    elif player["HP"] <= 0: print(f"{player['nama']} Kalah!")
    else: print(f"{player['nama']} Menang!")
# Fungsi main PVP (Perlu 2 karakter karena setiap orang harus memilih 1 krakter)
def pvp(karakter, item):
    if len(karakter) < 2:
        print("Butuh minimal 2 karakter untuk PVP.\n")
        return
    if not item:
        print("Belum ada item.\n")
        return
    liatkarakter(karakter)
    idx1 = inputHarusAngka("Pilih karakter Player 1: ") - 1
    if not (0 <= idx1 < len(karakter)):
        print("Index tidak valid.\n")
        return
    player1 = karakter[idx1].copy()

    while True:
        idx2 = inputHarusAngka("Pilih karakter Player 2: ") - 1
        if not (0 <= idx2 < len(karakter)):
            print("Index tidak valid.\n")
        elif idx2 == idx1:
            print("Karakter ini sudah dipilih Player 1, silahkan pilih karakter lain!\n")
        else:
            break
    player2 = karakter[idx2].copy()

    print(f"\n{player1['nama']} VS {player2['nama']}!\n")

    while player1["HP"] > 0 and player2["HP"] > 0:
        giliran = random.randint(1,2)
        if giliran == 1:
            print(f"\n--- Giliran {player1['nama']} ---")
            liatitem(item)
            idxi = inputHarusAngka("Pilih item (index): ")-1
            if 0 <= idxi < len(item):
                efekitem(item[idxi], player1)
            player2["HP"] = max(0, player2["HP"] - player1["ATK"])
            print(f"{player1['nama']} menyerang {player2['nama']} -{player1['ATK']} HP")
        else:
            print(f"\n--- Giliran {player2['nama']} ---")
            liatitem(item)
            idxi = inputHarusAngka("Pilih item (index): ")-1
            if 0 <= idxi < len(item):
                efekitem(item[idxi], player2)
            player1["HP"] = max(0, player1["HP"] - player2["ATK"])
            print(f"{player2['nama']} menyerang {player1['nama']} -{player2['ATK']} HP")

        print(f"HP {player1['nama']}: {player1['HP']} | HP {player2['nama']}: {player2['HP']}")

    print("\n=== HASIL ===")
    if player1["HP"] <= 0 and player2["HP"] <= 0: 
        print("Pertarungan Seri!")
    elif player1["HP"] <= 0: 
        print(f"{player2['nama']} Menang!")
    else: 
        print(f"{player1['nama']} Menang!")
# Fungsi fungsi menu
# Fungsi sub menu yang berisi sub menu itu ngapain aja
def menu_karakter(karakter):
    while True:
        print("\n=== Menu Karakter ===")
        print("1. Lihat karakter\n2. Tambah karakter\n3. Hapus karakter\n4. Edit karakter\n5. Kembali")
        sub = inputHarusAngka("Pilih: ")
        if sub == 1: 
            liatkarakter(karakter)
        elif sub == 2: 
            tambahkarakter(karakter)
        elif sub == 3: 
            hapuskarakter(karakter)
        elif sub == 4: 
            editkarakter(karakter)
        elif sub == 5: 
            break

def menu_item(item):
    while True:
        print("\n=== Menu Item ===")
        print("1. List item\n2. Tambah item\n3. Hapus item\n4. Kembali")
        sub = inputHarusAngka("Pilih: ")
        if sub == 1: 
            liatitem(item)
        elif sub == 2: 
            tambahitem(item)
        elif sub == 3: 
            hapusitem(item)
        elif sub == 4: 
            break

def menu_play(karakter, item):
    while True:
        print("\n=== Play ===")
        print("1. PVE\n2. PVP\n3. Kembali")
        sub = inputHarusAngka("Pilih: ")
        if sub == 1: 
            pve(karakter, item)
        elif sub == 2: 
            pvp(karakter, item)
        elif sub == 3: 
            break

# Fungsi Main menu masukan fungsi fungsi sub menu yang telah dibuat
def main():
    karakter = [{"nama": "Mona", "HP": 300, "ATK": 500, "Afiliasi": "Geng Kapak"},
    {"nama": "Kai", "HP": 400, "ATK": 400, "Afiliasi": "Geng cucur"},
    {"nama": "Calon", "HP": 600, "ATK": 200, "Afiliasi": "Kelompok Mooka lir"}
    ] 
    item = [{"nama": "Sekop", "rarity": "common", "kegunaan": "ATK"},
    {"nama": "Daun", "rarity": "common", "kegunaan": "HP"},
    {"nama": "Dona", "rarity": "common", "kegunaan": "HP"}
    ]
    while True:
        print("\nWelcome to The Game")
        print("1. Karakter\n2. Item\n3. Play\n4. Exit")
        pilih = inputHarusAngka("Pilih menu: ")
        if pilih == 1: 
            menu_karakter(karakter)
        elif pilih == 2: 
            menu_item(item)
        elif pilih == 3: 
            menu_play(karakter, item)
        elif pilih == 4:
            print("Terima kasih sudah bermain!")
            break

# Jalankan game bisa langsung panggil aja fungsi main yang sudah dibuat
main()  

