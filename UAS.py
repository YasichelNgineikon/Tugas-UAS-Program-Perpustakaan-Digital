import json

# Daftar untuk menyimpan data dan peminjaman 
data_buku = []  # Menyimpan semua buku
buku_dipinjam = []  # Menyimpan buku yang sedang dipinjam

# Fungsi ini untuk menambahkan buku baru ke perpustakaan TADIKA MESRA
def tambah_data_buku():
    print("\n=== Tambah Koleksi Buku ===")
    judul = input("Judul: ").strip()
    penulis = input("Penulis: ").strip()
    tahun = input("Tahun Terbit: ").strip()
    kategori = input("Kategori: ").strip()

    # Validasi input tidak kosong
    if judul == ""or penulis == ""or tahun ==""or kategori =="":
        print("semua kolom harus diisi tidak boleh kosong.").strip()
        return

    data_buku.append({
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun,
        "kategori": kategori,
        "status": "tersedia"  # Semua buku baru tersedia
    })
    print(f"Buku '{judul}' berhasil ditambahkan dalam PERPUSTAKAAN TADIKA MESRA!\n")

# Fungsi untuk hapus buku
def hapus_buku():
    print("\n=== Hapus buku dari koleksi ===")
    judul = input("Masukan judul buku yang ingin kamu hapus: ").strip().lower()

    for buku in data_buku:
        if buku["judul"].lower():
            data_buku.remove(buku)
            print(f"Buku '{judul}' sudah berhasil dihapus dari PERPUSTAKAAN TADIKA MESRA.")
            return
    
    print(f"Buku '{judul}' tidak ditemukan dalam koleksi.")


# Fungsi untuk menampilkan semua buku di perpustakaan
def tampilkan_buku():
    print("\n=== Koleksi Buku PERPUSTAKAAN TADIKA MESRA ===")
    if not data_buku:
        print("Belum ada satupun buku yang ditambahkan.")
        return
    for idx, buku in enumerate(data_buku, start=1):
        print(f"{idx}. {buku['judul']} - {buku['penulis']} ({buku['tahun']}) [{buku['kategori']}] - {buku['status']}")

# Fungsi untuk mencari buku berdasarkan judul, penulis, atau kategori
def cari_buku():
    print("\n=== Cari ===")
    kriteria = input("pilih salah satu (judul/penulis/kategori): ").strip()
    kata_kunci = input("cari sesuai apa yang kamu pilih: ").strip()

    hasil_cari = [
        buku for buku in data_buku
        if buku.get(kriteria, "") == kata_kunci
    ]

    if hasil_cari:
        print("\nHasil Pencarian:")
        for buku in hasil_cari:
            print(f"- {buku['judul']} oleh {buku['penulis']} [{buku['kategori']}]")
    else:
        print("yahh maap nih bestiee buku yang kamu cari sepertinya tidak ada di PERPUSTAKAAN TADIKA MESRA🙂.")

# Fungsi untuk meminjam buku
def pinjam_buku():
    print("\n=== Pinjam Buku ===")
    tampilkan_buku()
    judul = input("Masukkan judul buku yang ingin kamu pinjam: ").strip().lower()

    for buku in data_buku:
        if buku["judul"].lower() == judul:
            if buku["status"] == "tersedia":
                buku["status"] = "buku sedang dipinjam" 
                buku_dipinjam.append(buku)
                print(f"Buku '{judul}' berhasil dipinjam.Dua tiga luna maya, Selamat membanca ya!")
            else:
                print(f"Buku '{judul}' Waduhh.. ayem sorry nih bukunya sedang dipinjam.")
            return
    print(f"Buku '{judul}' maaf wahai kutu buku, buku tidak ditemukan😣")

# Funngsi untuk mengembalikan buku
def kembalikan_buku():
    print("\n=== Kembalikan Buku ===")
    if not buku_dipinjam:
        print("Tidak ada buku yang dipinjam, yuk pinjam, hahayy😍.")
        return
    
    for buku in buku_dipinjam:
        print(f"- {buku['judul']}")

    judul = input("buku apa yang ingin kamu kembalikan: ").strip().lower()
    for buku in buku_dipinjam:
        if buku["judul"].lower() == judul.lower():
            buku["status"] = "tersedia"
            buku_dipinjam.remove(buku)
            print(f"Buku '{judul}' berhasil dikemmbalikan, Kamsahamida!")
            return
    print(f"Buku '{judul}' waduh... bukunya tidak ada dalam daftar pinjamanmu nichh.")

# Fungsi untuk menyimpan data ke file JSON
def simpan_data():
    with open("perpustakaan.json", "w") as file:
        json.dump(data_buku, file)
    print("Data berhasil disimpan ke file 'Perpustakaan.json'.")

# Fungsi untuk memuat data dari file JSON
def muat_data():
    global data_buku
    try:
        with open("perpustakaan.json", "r") as file:
            data_buku = json.load(file)
            print("Data berhasil dimuat dari file.")
    except FileNotFoundError:
        print("File data tidak ditemukan, mulai dengan data kosong.")

    
# Menu utama
def menu_utama():
    muat_data()
    while True:
        print("\n=== PERPUSTAKAAN TADIKA MESRA === ")
        print("1. Lihat Semua koleksi Buku")
        print("2. Tambah koleksi buku")
        print("3. Cari")
        print("4. Pinjam Buku")
        print("5. Kembalikan Buku")
        print("6. Hapus Buku")
        print("7. Simpan")
        print("8. Keluar")

        pilihan = input("Pilihan Menu: ").strip()
        if pilihan == "1":
            tampilkan_buku()
        elif pilihan == "2":
            tambah_data_buku()
        elif pilihan == "3":
            cari_buku()
        elif pilihan == "4":
            pinjam_buku()
        elif pilihan == "5":
            kembalikan_buku()
        elif pilihan == "6":
            hapus_buku()
        elif pilihan == "7":
            simpan_data()
        elif pilihan == "8":
            print("Program telah selesai. Gelas pecah airnya Tumpah kamsahamida dan sampai jumpa!")
            break
        else:
            print("pilih angkanya kawan")

# Jalankan Program
menu_utama()
