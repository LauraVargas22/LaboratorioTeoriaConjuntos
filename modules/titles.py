import pyfiglet
from rich.console import Console
from rich.panel import Panel

console = Console()

# Título principal
title1 = pyfiglet.figlet_format("TEORIA DE", font="slant",)
subtitle = pyfiglet.figlet_format("CONJUNTOS", font="digital")

def show_title():
    console.print(Panel.fit(
        f"[bold cyan]{title1}[/bold cyan]\n[bold magenta]{subtitle}[/bold magenta]",
        border_style="bright_blue",
        title="📘 PROGRAMA",
    ))

# Subtítulos
espanol = pyfiglet.figlet_format("Espanol", font="standard")
ingles = pyfiglet.figlet_format("Ingles", font="small")
concurrencia = pyfiglet.figlet_format("Palabras", font="small")

def show_español():
    console.print(Panel.fit(
        f"[green]{espanol}[/green]",
        border_style="green",
        title="Frecuencia de Letras"
    ))

def show_ingles():
    console.print(Panel.fit(
        f"[yellow]{ingles}[/yellow]",
        border_style="yellow",
        title="Frecuencia de Letras"
    ))

def show_concurrencia():
    console.print(Panel.fit(
        f"[purple]{concurrencia}[/purple]",
        border_style="purple",
        title="Concurrencia de"
    ))
