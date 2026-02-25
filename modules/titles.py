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
lineal = pyfiglet.figlet_format("Idioma", font="small")
quadratic = pyfiglet.figlet_format("Idioma", font="small")
rational = pyfiglet.figlet_format("Concurrencia", font="small")

def show_lineal():
    console.print(Panel.fit(
        f"[green]{lineal}[/green]",
        border_style="green",
        title="Español"
    ))

def show_quadratic():
    console.print(Panel.fit(
        f"[yellow]{quadratic}[/yellow]",
        border_style="yellow",
        title="Inglés"
    ))

def show_rational():
    console.print(Panel.fit(
        f"[purple]{rational}[/purple]",
        border_style="purple",
        title="Concurrencia de Palabras"
    ))
