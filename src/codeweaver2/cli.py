"""🕸️ CODEWEAVER2 - Main CLI Entry Point"""
import click
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
import questionary
from codeweaver2.commands.scan import run_scan
from codeweaver2.commands.runtime import run_runtime
from codeweaver2.commands.safety import run_safety
from codeweaver2.commands.cursor import run_cursor

console = Console()

@click.group(invoke_without_command=True)
@click.version_option(version="2.0.0", prog_name="CODEWEAVER2")
@click.pass_context
def cli(ctx):
    """🕸️ CODEWEAVER2 - Weaving insight through code"""
    if ctx.invoked_subcommand is None:
        interactive_menu()

def interactive_menu():
    console.print(Panel.fit("[bold blue]🕸️  CODEWEAVER2 v2.0.0[/bold blue]\n[dim]Weaving insight through code[/dim]", border_style="blue"))
    
    choice = questionary.select(
        "What would you like to do?",
        choices=[
            questionary.Choice("🔍 Scan code quality", value="scan"),
            questionary.Choice("📦 Check runtime requirements", value="runtime"),
            questionary.Choice("🛡️  Audit security/safety", value="safety"),
            questionary.Choice("🖱️  Open proposal in Cursor", value="cursor"),
            questionary.Choice("❓ Help & Documentation", value="help"),
            questionary.Choice("🚪 Exit", value="exit"),
        ]
    ).ask()

    if choice == "exit" or choice is None:
        console.print("\n[dim]Goodbye! 🕸️[/dim]")
    elif choice == "help":
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
    elif choice == "scan":
        path = questionary.path("Directory to scan?", default=".").ask()
        mode = questionary.select("Scan mode?", choices=["quick", "standard", "deep"]).ask()
        if path and mode: run_scan(Path(path), mode=mode)
    elif choice == "runtime":
        path = questionary.path("Directory to analyze?", default=".").ask()
        if path: run_runtime(Path(path))
    elif choice == "safety":
        path = questionary.path("Directory to audit?", default=".").ask()
        if path: run_safety(Path(path))
    elif choice == "cursor":
        run_cursor(list_proposals=True)

@cli.command()
@click.argument("path", default=".", type=click.Path(exists=True))
@click.option("--quick", is_flag=True, help="Fast health check")
@click.option("--deep", is_flag=True, help="Deep analysis")
def scan(path, quick, deep):
    """🔍 Analyze code quality and generate proposals"""
    mode = "quick" if quick else ("deep" if deep else "standard")
    run_scan(Path(path), mode=mode)

@cli.command()
@click.argument("path", default=".", type=click.Path(exists=True))
@click.option("--install", is_flag=True, help="Auto-install missing requirements")
def runtime(path, install):
    """📦 Check runtime requirements"""
    run_runtime(Path(path), auto_install=install)

@cli.command()
@click.argument("path", default=".", type=click.Path(exists=True))
def safety(path):
    """🛡️  Security audit for untrusted code"""
    run_safety(Path(path))

@cli.command()
@click.argument("proposal_id", required=False)
@click.option("--list", "list_proposals", is_flag=True)
@click.option("--apply", is_flag=True)
def cursor(proposal_id, list_proposals, apply):
    """🖱️  Open proposals in Cursor IDE"""
    run_cursor(proposal_id=proposal_id, list_proposals=list_proposals, apply_patch=apply)

if __name__ == "__main__":
    cli()
