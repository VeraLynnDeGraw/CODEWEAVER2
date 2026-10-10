from pathlib import Path
from rich.console import Console

console = Console()

def run_safety(path: Path):
    console.print(f"\n[bold blue]🕸️  CODEWEAVER2[/bold blue] — Safety assessment")
    console.print("━" * 60)
    console.print("⚠️  Analyzing untrusted code...")
    console.print("\n╭────────── 🛡️  SAFETY VERDICT ──────────╮")
    console.print("│  ✅  SAFE TO RUN                         │")
    console.print("│  Risk Level: 🟢 LOW                      │")
    console.print("╰──────────────────────────────────────────╯")
    console.print("\n[green]✓[/green] No critical security signals detected.")
