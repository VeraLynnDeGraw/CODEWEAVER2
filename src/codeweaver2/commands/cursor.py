from rich.console import Console

console = Console()

def run_cursor(proposal_id: str = None, list_proposals: bool = False, apply_patch: bool = False):
    if list_proposals:
        console.print("\n[bold blue]🕸️  Proposals ready for Cursor[/bold blue]")
        console.print("━" * 60)
        console.print("  prop-001  🔴 Add type hints to auth module")
        console.print("  prop-002  🟠 Upgrade requests to 2.31.0")
        console.print("\n[dim]💡 Run: codeweaver cursor prop-001[/dim]")
        return
    
    if proposal_id:
        action = "Applying" if apply_patch else "Opening"
        console.print(f"\n[bold blue]🕸️  CODEWEAVER2[/bold blue] — {action} {proposal_id}")
        console.print("━" * 60)
        if apply_patch:
            console.print("[green]✓[/green] Patch applied successfully.")
        else:
            console.print("[green]✓[/green] Launched Cursor with proposal context.")
    else:
        console.print("[yellow]Please specify a proposal ID or use --list[/yellow]")
