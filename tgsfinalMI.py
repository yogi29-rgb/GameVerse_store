import mysql.connector
import time
import sys
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Style, init
from pyfiglet import Figlet
import os



init(autoreset=True)

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="Gameverse_Store",
)
cursor = db.cursor()
user_name = 'admin'
kata_sandi = 'admin'
 


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#  daftar produk 
def list_products():
    proses_message()
    cursor.execute("SELECT id, name, price, stock FROM products")
    products = cursor.fetchall()
    
    # Membuat tabel
    table = PrettyTable()
    table.field_names = ["ID", "Nama Produk", "Harga (Rp)", "Stok"]

    if products:
        for product in products:
            table.add_row([product[0], product[1], f"Rp{product[2]:,}", product[3]])
    else:
        table.add_row(["", "Tidak ada produk yang tersedia", "", ""])

    print(Fore.CYAN + "\nDaftar Produk:")
    print(table)
    input("Tekan enter untuk kembali ke Menu...")
    
    
# menjual produk
def sell_product():
    total_belanja = 0
    items_bought = []  # Daftar untuk menyimpan produk yang dibeli
    while True:
        list_products()
        product_id = int(input("\nMasukkan ID produk yang ingin dibeli: "))
        cursor.execute("SELECT name, price, stock FROM products WHERE id = %s", (product_id,))
        product = cursor.fetchone()

        if product:
            name, price, stock = product
            qty = int(input(f"Masukkan jumlah yang ingin dibeli (Stok tersedia: {stock}): "))
            if qty <= stock:
                total = qty * price
                total_belanja += total
                items_bought.append((name, qty, price, total))  # Menyimpan barang yang dibeli
                cursor.execute("INSERT INTO sales (product_id, quantity, total_price) VALUES (%s, %s, %s)", (product_id, qty, total))
                cursor.execute("UPDATE products SET stock = stock - %s WHERE id = %s", (qty, product_id))
                db.commit()
                proses_message()
                print(Fore.GREEN + f"Berhasil menjual {qty} unit {name}. Total: Rp{total:,}")
            else:
                print(Fore.RED + "Stok tidak mencukupi.")
        else:
            print(Fore.RED + "Produk tidak ditemukan.")

        beli_lagi = input("Apakah Anda ingin membeli lagi? (y/n): ").lower()
        if beli_lagi == 'n':
            break

    # Pilihan pembayaran
    while True:
        metode_pembayaran = input("Pilih metode pembayaran: 1. Cash 2. QRIS (ketik 1 atau 2): ")
        if metode_pembayaran == '1':
            uang_dibayar = int(input(f"Total belanja: Rp{total_belanja:,}. Masukkan jumlah uang yang diberikan: Rp"))
            if uang_dibayar >= total_belanja:
                kembalian = uang_dibayar - total_belanja
                print(Fore.GREEN + f"Pembayaran berhasil. Kembalian: Rp{kembalian:,}")
                print_bukti(total_belanja, uang_dibayar, kembalian, items_bought, "Cash")
            else:
                print(Fore.RED + "Uang yang diberikan tidak cukup.")
            break
        elif metode_pembayaran == '2':
            print(Fore.GREEN + f"Pembayaran QRIS berhasil. Total Belanja: Rp{total_belanja:,}")
            print_bukti(total_belanja, total_belanja, 0, items_bought, "QRIS")
            break
        else:
            print(Fore.RED +"Pilihan tidak valid. Silakan pilih 1 untuk Cash atau 2 untuk QRIS.")
            
            
# struk pembyaran
def slow_print(text, color=Fore.WHITE, delay=0.0001):
    """Menampilkan teks satu per satu dengan warna."""
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)  # Warna tetap utuh
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_bukti(total_belanja, uang_dibayar, kembalian, items_bought, metode_pembayaran):
    proses_message()
    now = datetime.now()
    tanggal_waktu = now.strftime("%Y-%m-%d %H:%M:%S")

    # Header Struk
    slow_print("=" * 40, Fore.CYAN)
    slow_print("          GAMEVERSE STORE          ", Fore.YELLOW)
    slow_print("       Jl. Fais ganteng. 123, Jakarta  ", Fore.YELLOW)
    slow_print("=" * 40, Fore.CYAN)

    # Detail Pembelian
    for i, item in enumerate(items_bought, 1):
        name, qty, price, total = item
        slow_print(f"Produk {i}       : {name}", Fore.GREEN)
        slow_print(f"Jumlah           : {qty}", Fore.GREEN)
        slow_print(f"Harga Satuan     : Rp{price:,}", Fore.GREEN)
        slow_print(f"Total Harga      : Rp{total:,}", Fore.GREEN)
        slow_print("-" * 40, Fore.CYAN)

    # Total, Uang Diterima, Kembalian
    slow_print(f"Total Belanja     : Rp{total_belanja:,}", Fore.GREEN)
    slow_print(f"Uang Diterima     : Rp{uang_dibayar:,}", Fore.GREEN)
    slow_print(f"Kembalian         : Rp{kembalian:,}", Fore.GREEN)
    slow_print(f"Metode Pembayaran : {metode_pembayaran}", Fore.GREEN)
    slow_print(f"Tanggal/Waktu     : {tanggal_waktu}", Fore.GREEN)
    slow_print("=" * 40, Fore.CYAN)

    # Footer Struk
    slow_print("  Terima kasih atas pembelian Anda!  ", Fore.YELLOW)
    slow_print("=" * 40, Fore.CYAN)
    
    print()
    print()
    input("Tekan Enter ...")


# Fungsi untuk melihat riwayat penjualan
def view_sales():
    proses_message()
    cursor.execute("""
        SELECT sales.id, products.name, sales.quantity, products.price AS price_per_unit, 
               sales.total_price, DATE_FORMAT(sales.created_at, '%Y-%m-%d %H:%i:%s') AS sale_time
        FROM sales
        INNER JOIN products ON sales.product_id = products.id
    """)
    sales = cursor.fetchall()
    
    # Membuat tabel PrettyTable
    table = PrettyTable()
    table.field_names = ["ID Transaksi", "Nama Produk", "Jumlah", "Harga Satuan (Rp)", "Total Harga (Rp)", "Waktu Transaksi"]

    if sales:
        for sale in sales:
            table.add_row([sale[0], sale[1], sale[2], f"Rp{sale[3]:,}", f"Rp{sale[4]:,}", sale[5]])
        print("\nRiwayat Penjualan dan Struk:")
        print(table)
    else:
        print("\nBelum ada riwayat penjualan.")
        
#data karyawan 
def karyawan():
    proses_message()
    cursor.execute("SELECT * FROM karyawan")
    result = cursor.fetchall()

    # Membuat tabel menggunakan PrettyTable
    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Jabatan", "Gaji"]

    if not result:
        print("Tidak ada data karyawan.")
    else:
        for data in result:
            table.add_row([data[0], data[1], data[2], f"Rp{data[3]:,}"])

    print("\nDaftar Karyawan:")
    print(table)
    input("Tekan enter untuk kembali ke Menu admin...")

#  menambahkan produk baru
def add_product():
    name = input("Masukkan nama produk: ")
    price = int(input("Masukkan harga produk: "))
    stock = int(input("Masukkan stok produk: "))
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
    db.commit()
    print(f"Produk {name} berhasil ditambahkan!")

#  memperbarui produk
def update_product():
    list_products()
    product_id = int(input("\nMasukkan ID produk yang ingin diperbarui: "))
    print("1. update nama\n2. Update Harga\n3. Update Stok")
    while True:
        choice = input("Pilih opsi: ")
        if choice == "1":
            new_name = input("Maasukan nama baru :")
            cursor.execute("UPDATE products SET name = %s WHERE id = %s", (new_name, product_id) )
        elif choice == '2':
            new_price = int(input("Masukkan harga baru: "))
            cursor.execute("UPDATE products SET price = %s WHERE id = %s", (new_price, product_id))
        elif choice == '3':
            new_stock = int(input("Masukkan stok baru: "))
            cursor.execute("UPDATE products SET stock = %s WHERE id = %s", (new_stock, product_id))
        else:
            print("Pilihan tidak valid.")
        Opsi_lain = input("Apakah masih ada yang dibuah (y/n): ").lower()
        if Opsi_lain == 'n':
            break
        db.commit()
        print("Produk berhasil diperbarui!")
    

#  menghapus produk
def delete_product():
    list_products()
    product_id = int(input("\nMasukkan ID produk yang ingin dihapus: "))
    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    db.commit()
    print("Produk berhasil dihapus!")


#  mencari produk berdasarkan nama atau harga
def search_data():
    keyword = input("Kata kunci: ")
    cursor.execute("SELECT * FROM products WHERE name LIKE %s OR price LIKE %s", (f"%{keyword}%", f"%{keyword}%"))
    result = cursor.fetchall()

    # Membuat tabel 
    table = PrettyTable()
    table.field_names = ["ID", "Nama Produk", "Harga (Rp)", "Stok"]

    if not result:
        print("Tidak ada data yang ditemukan.")
    else:
        for data in result:
            table.add_row([data[0], data[1], f"Rp{data[2]:,}", data[3]])

    print("\nHasil Pencarian:")
    print(table)

            
# Menu Admin yang membutuhkan kata sandi
def admin_menu():
    table = PrettyTable()
    table_field_name =["input_user","input_sandi"]
    input_user = input("masukan user admin:")
    input_sandi = input("Masukkan kata sandi admin: ")
    if (input_user,input_sandi) == (kata_sandi,user_name):
        while True:
            display_menu([
                ["Karyawan", "Melihat data karyawan."],
                ["Tambah Produk", "Menambahkan produk baru ke database."],
                ["Lihat Daftar Produk", "Melihat daftar semua produk."],
                ["Update Produk", "Memperbarui informasi produk yang sudah ada."],
                ["Hapus Produk", "Menghapus produk dari database."],
                ["Search Data", "Mencari produk berdasarkan nama atau harga."],
                ["Kembali ke Menu Utama", "Kembali ke menu utama."]
            ], "Menu Admin")
            while True:
                try:
                    pilihanAdmin = int(input("\nMasukkan pilihan: "))
                    if 1 <= pilihanAdmin <= 7:
                        break
                    else:
                        print("Pilihan tidak valid. Masukkan angka 1-7.")
                except ValueError:
                    print("Input harus angka. Masukkan angka 1-7.")

            if pilihanAdmin == 1:
                karyawan()
            elif pilihanAdmin == 2:
                add_product()
            elif pilihanAdmin == 3:
                list_products()
            elif pilihanAdmin == 4:
               update_product()
            elif pilihanAdmin == 5:
                delete_product()
            elif pilihanAdmin == 6:
                search_data()
            elif pilihanAdmin == 7:
                break
            else:
                print("Pilihan tidak valid.")
    else:
        print("Kata sandi salah! Kembali ke menu utama.")


def slow_print(text, color=Fore.WHITE, delay=0.05):
    """Mencetak teks satu per satu dengan delay."""
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Fungsi untuk animasi selamat datang
def welcome_message():
    clear_screen()
    f = Figlet(font="slant")  # Pilih font untuk logo ASCII
    logo = f.renderText("GameVerseStore")
    
    # Cetak logo dengan warna dan animasi
    for line in logo.split("\n"):
        print(Fore.CYAN + line)
        time.sleep(0.05)
    
    slow_print("Selamat datang di Gameverse_Store! Jelajahi dunia game terbaik!",Fore.YELLOW, delay=0.03)
    time.sleep(1)  # Delay sebelum lanjut

def farewell_message():
    clear_screen()
    f = Figlet(font="slant")  # Font untuk logo
    logo = f.renderText("Goodbye!")
    
    # Cetak logo dengan warna dan animasi keluar
    for line in logo.split("\n"):
        print(Fore.CYAN + line)
        time.sleep(0.05)
    
    slow_print( "Terima kasih telah mengunjungi Gameverse_Store! Sampai jumpa lagi!",Fore.YELLOW, delay=0.03)
    time.sleep(1)  # Delay sebelum keluar
    
# Fungsi Animasi Proses
def proses_message():
    print(Fore.YELLOW + "\nSedang dalam proses", end="")
    for _ in range(5):
        time.sleep(0.5)
        print(Fore.YELLOW + ".", end="", flush=True)
    print("\n" + Fore.GREEN + "Proses selesai!\n")
        


def display_menu(menu_items, title="Menu"):
    """Menampilkan menu dalam tabel menggunakan prettytable."""
    table = PrettyTable()
    table.field_names = ["No.", "akses", "Deskripsi"]
    for i, item in enumerate(menu_items, 1):
        table.add_row([i, item[0], item[1]])  # item[0] = perintah, item[1] = deskripsi
    print(f"\n{title}:\n{table}")

def main_menu():
    welcome_message()
    while True:
        display_menu([
            ["Toko", "Menu untuk berbelanja game."],
            ["Admin", "khusus karyawan."],
            ["Keluar Aplikasi", "Keluar dari aplikasi."]
        ], "Menu Utama")
        while True:
            try:
                pilihanMenu = int(input("\nMasukkan pilihan: "))
                if 1 <= pilihanMenu <= 3:
                    break
                else:
                    print("Pilihan tidak valid. Masukkan angka 1-3.")
            except ValueError:
                print("Input harus angka. Masukkan angka 1-3.")

        if pilihanMenu == 1:
            while True:
                display_menu([
                    ["Lihat Daftar Game", "Melihat daftar game yang tersedia."],
                    ["Beli Game", "Membeli game."],
                    ["Lihat Riwayat Penjualan", "Melihat riwayat penjualan."],
                    ["Kembali ke Menu Utama", "Kembali ke menu utama."]
                ], "Menu Penjualan")
                while True:
                    try:
                        pilihanPenjualan = int(input("\nMasukkan pilihan: "))
                        if 1 <= pilihanPenjualan <= 4:
                            break
                        else:
                            print("Pilihan tidak valid. Masukkan angka 1-4.")
                    except ValueError:
                        print("Input harus angka. Masukkan angka 1-4.")

                if pilihanPenjualan == 1:
                    list_products()
                elif pilihanPenjualan == 2:
                    sell_product()
                elif pilihanPenjualan == 3:
                    view_sales()
                elif pilihanPenjualan == 4:
                    break
                else:
                    print("Pilihan tidak valid.")

        elif pilihanMenu == 2:
            admin_menu()

        elif pilihanMenu == 3:
            farewell_message()
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main_menu()