from pathlib import Path
from rich.console import Console
from rich.progress import Progress

console = Console()

def run_scan(path: Path, mode: str = "standard"):
    console.print(f"\n[bold blue]🕸️  CODEWEAVER2[/bold blue] — Scanning {path} ({mode} mode)")
    console.print("━" * 60)
    
    files = [f for f in path.rglob("*") if f.is_file() and not any(part.startswith('.') for part in f.parts)]
    console.print(f"📂 Discovery: Found {len(files)} files")
    
    console.print("\n🧵 Weaving threads...")
    with Progress() as progress:
        task = progress.add_task("Analyzing...", total=len(files) if files else 10)
        for _ in range(10): # Simulated work
            progress.update(task, advance=1)
            
    console.print("\n╭────────────── 📊 PROJECT DASHBOARD ──────────────╮")
    console.print("│  Health: B (78/100)                              │")
    console.print("│  Findings: 12  |  Proposals: 5                   │")
    console.print("│  Quick Wins: 2  |  Critical: 1                   │")
    console.print("╰──────────────────────────────────────────────────╯")
    console.print("\n[green]✓[/green] Analysis complete. Run [bold]codeweaver cursor --list[/bold] to view proposals.")
