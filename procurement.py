from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.align import Align
from time import sleep

console = Console()

users = [
    {"name": "adrian", "email": "admin1@procura.com", "password": "12345", "role": "admin"},
    {"name": "iqbal", "email": "petugas1@procura.com", "password": "12345", "role": "petugas"},
]

barang_list = []
permintaan_list = []

def banner():
    console.clear()
    content = Align.center(
        "[cyan bold]💼 PROCURA[/cyan bold]\n"
        "[white]Sistem Pengadaan Barang (Versi Sederhana)[/white]\n"
    )
    console.print(Panel(content, border_style="cyan"))
    sleep(0.5)

def login():
    banner()
    console.print(Panel("[bold cyan]Silakan Login[/bold cyan]", border_style="cyan"))
    
    while True:
        email = Prompt.ask("[white]📧 Email[/white]")
        password = Prompt.ask("[white]🔑 Password[/white]", password=True)

        user = next((u for u in users if u["email"] == email and u["password"] == password), None)

        if user:
            console.print(
                Panel(
                    f"[green]Login Berhasil![/green]\n"
                    f"Selamat datang, [yellow]{user['name'].title()}[/yellow] sebagai [bold]{user['role'].upper()}[/bold].",
                    border_style="green"
                )
            )
            sleep(1)
            return user
        else:
            console.print(Panel("[red]Email atau password salah![/red]", border_style="red"))

# ADMIN

def admin_input_barang():
    console.print(Panel("[bold green]Input Barang Baru[/bold green]"))
    nama = Prompt.ask("Nama Barang")
    jumlah = int(Prompt.ask("Jumlah"))
    barang_list.append({"nama": nama, "jumlah": jumlah})
    console.print(Panel(f"[green]Barang '{nama}' berhasil ditambahkan![/green]"))

def admin_pencatatan():
    console.print(Panel("[cyan]Daftar Barang[/cyan]"))
    if not barang_list:
        console.print("[red]Belum ada barang.[/red]")
        return

    table = Table(show_header=True, header_style="bold green")
    table.add_column("Nama Barang")
    table.add_column("Jumlah")

    for b in barang_list:
        table.add_row(b["nama"], str(b["jumlah"]))

    console.print(table)

def menu_admin():
    while True:
        console.print(Panel("[bold cyan]Menu Admin[/bold cyan]"))
        console.print("""
1. Input Barang
2. Lihat Daftar Barang
3. Logout
""")
        pilihan = Prompt.ask("Pilih menu", choices=["1", "2", "3"])

        if pilihan == "1": admin_input_barang()
        elif pilihan == "2": admin_pencatatan()
        elif pilihan == "3": break

# PETUGAS

def petugas_permintaan(nama_petugas):
    console.print(Panel("[bold yellow]Ajukan Permintaan Barang[/bold yellow]"))

    nama_barang = Prompt.ask("Nama Barang")
    jumlah = int(Prompt.ask("Jumlah"))

    permintaan_list.append({
        "petugas": nama_petugas,
        "nama": nama_barang,
        "jumlah": jumlah,
        "status": "Menunggu"
    })

    console.print(Panel("[green]Permintaan berhasil diajukan![/green]"))

def petugas_status(nama):
    console.print(Panel("[cyan]Status Permintaan Anda[/cyan]"))

    table = Table(show_header=True, header_style="bold yellow")
    table.add_column("Barang")
    table.add_column("Jumlah")
    table.add_column("Status")

    found = False
    for p in permintaan_list:
        if p["petugas"] == nama:
            found = True
            table.add_row(p["nama"], str(p["jumlah"]), p["status"])

    if not found:
        console.print("[red]Belum ada permintaan Anda.[/red]")
        return

    console.print(table)

def menu_petugas(user):
    while True:
        console.print(Panel("[bold cyan]Menu Petugas[/bold cyan]"))
        console.print("""
1. Ajukan Permintaan Barang
2. Lihat Status Permintaan
3. Logout
""")
        pilihan = Prompt.ask("Pilih menu", choices=["1", "2", "3"])

        if pilihan == "1": petugas_permintaan(user["name"])
        elif pilihan == "2": petugas_status(user["name"])
        elif pilihan == "3": break

# MAIN

if __name__ == "__main__":
    while True:
        user = login()
        if user["role"] == "admin":
            menu_admin()
        else:
            menu_petugas(user)








# -------------------------------------------------------------
# Kode fungsi yang belum ada :
# - Fungsi admin_persetujuan() (ADMIN): proses menyetujui permintaan
# - Fungsi admin_laporan() (ADMIN): perhitungan total pengeluaran
# - Tabel harga barang & perhitungan harga (ADMIN)
# - Daftar barang dengan harga (PETUGAS)
# - Fitur multi-admin & multi-petugas (disederhanakan)
#
# Penjelasan untuk role mana yang terdampak:
# - ADMIN: kehilangan fitur persetujuan + laporan keuangan
# - PETUGAS: kehilangan fitur melihat daftar barang lengkap
# -------------------------------------------------------------