from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.align import Align
from rich import box
from time import sleep
import os

console = Console()

# Data Login (Adrian)
users = [
    {"name": "adrian", "email": "adrian@sipbar.com", "password": "12345"},
    {"name": "muhammad iqbal", "email": "iqbal@sipbar.com", "password": "12345"},
    {"name": "mahardika", "email": "mahardika@sipbar.com", "password": "12345"},
    {"name": "ramadhanny arda", "email": "arda@sipbar.com", "password": "12345"},
]

barang_list = []

# Banner - Adrian
def banner():
    console.clear()
    title = Text("PROCURA", style="bold bright_cyan on black")
    subtitle = Text("Procurement System", style="bold white")
    
    content = Align.center(
        f"\n[bright_cyan]╔═════════════════════════════════════════════╗[/bright_cyan]\n"
        f"       [bold cyan]💼 PROCURA[/bold cyan] - Procurement System\n"
        f"[bright_cyan]╚═════════════════════════════════════════════╝[/bright_cyan]\n"
        f"[white]Created by Kelompok 7 - Informatics 15.1D.01 UBSI[/white]\n"
        f"[green]Adrian Baihaqi • Muhammad Iqbal • Mahardika • Ramadhanny Arda[/green]\n"
    )
    console.print(Panel(content, border_style="bright_cyan", title="[bold yellow]Welcome to SIPBAR[/bold yellow]", subtitle="v1.0", expand=False))
    sleep(0.7)

# Login Page - Adrian
def login():
    banner()
    console.print(Panel.fit("[bold cyan]🔐 Silakan login menggunakan email dan password Anda[/bold cyan]", border_style="cyan"))
    
    while True:
        email = Prompt.ask("[bold white]📧 Email[/bold white]")
        password = Prompt.ask("[bold white]🔑 Password[/bold white]", password=True)
        user = next((u for u in users if u["email"] == email and u["password"] == password), None)

        if user:
            console.print(Panel(f"[green]✅ Login berhasil![/green]\nSelamat datang, [bold yellow]{user['name'].title()}[/bold yellow]! 🎉", border_style="green"))
            sleep(1)
            return user
        else:
            console.print(Panel("[bold red]❌ Email atau password salah! Coba lagi.[/bold red]", border_style="red"))

