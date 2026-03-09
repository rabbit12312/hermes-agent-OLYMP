"""
OLYMPUS Display — Terminal UI Theme

Rich-powered god-themed spinners, headers, colors, and status styles.
Used by run_olympus.py to give the terminal the feel of Olympus.
"""

import re
import sys
from typing import Optional

# ─────────────────────────────────────────────────────────────────
# Try to import rich; fall back to plain-text if not installed
# ─────────────────────────────────────────────────────────────────
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.style import Style
    from rich.spinner import Spinner
    from rich.live import Live
    from rich import box
    _RICH = True
except ImportError:
    _RICH = False


# ─────────────────────────────────────────────────────────────────
# ANSI color codes for god names (used in live hermes terminal output)
# ─────────────────────────────────────────────────────────────────

RESET  = "\033[0m"
BOLD   = "\033[1m"

GOD_ANSI = {
    "⚡ HERMES":    "\033[1;33m",   # bold yellow/gold
    "⚔️ PERSEUS":   "\033[1;36m",   # bold cyan
    "🌊 MNEMOSYNE": "\033[1;34m",   # bold blue
    "🌿 ASCLEPIUS": "\033[1;32m",   # bold green
    "👁️ ARGUS":     "\033[1;31m",   # bold red
    "💪 HERACLES":  "\033[1;35m",   # bold magenta
    "PERSEUS":    "\033[1;36m",
    "MNEMOSYNE":  "\033[1;34m",
    "ASCLEPIUS":  "\033[1;32m",
    "ARGUS":      "\033[1;31m",
    "HERACLES":   "\033[1;35m",
    "HERMES":     "\033[1;33m",
}

# Regex to detect god name lines in agent output
GOD_LINE_RE = re.compile(
    r"(⚡|\u2694\ufe0f|\U0001F30A|\U0001F33F|\U0001F441\ufe0f|\U0001F4AA)?\s?"
    r"(HERMES|PERSEUS|MNEMOSYNE|ASCLEPIUS|ARGUS|HERACLES)",
    re.IGNORECASE
)


def colorize_god_output(text: str) -> str:
    """
    Scan a line of agent output and colorize god names with ANSI codes.
    Works in any terminal that supports ANSI escape sequences (macOS/Linux).
    """
    def _replace(match):
        full = match.group(0)
        god  = match.group(2).upper()
        color = GOD_ANSI.get(god, BOLD)
        return f"{color}{full}{RESET}"

    return GOD_LINE_RE.sub(_replace, text)


class OlympusDisplay:
    """
    Terminal display handler for OLYMPUS.

    Usage:
        display = OlympusDisplay()
        display.banner()
        display.god_speaking("HERMES", "Routing your message…")
        display.status("Waiting for Perseus…")
    """

    # ── God color palette (rich) ───────────────────────────────
    GOD_COLORS = {
        "HERMES":    "bold yellow",
        "PERSEUS":   "bold cyan",
        "MNEMOSYNE": "bold blue",
        "ASCLEPIUS": "bold green",
        "ARGUS":     "bold red",
        "HERACLES":  "bold magenta",
        "OLYMPUS":   "bold white",
    }

    GOD_EMOJI = {
        "HERMES":    "⚡",
        "PERSEUS":   "⚔️",
        "MNEMOSYNE": "🌊",
        "ASCLEPIUS": "🌿",
        "ARGUS":     "👁️",
        "HERACLES":  "💪",
    }

    BANNER = r"""
  ___  _    _   _ __  __ ____  _   _ ____
 / _ \| |  | | | |  \/  |  _ \| | | / ___|
| | | | |  | |_| | |\/| | |_) | | | \___ \
| |_| | |__|  _  | |  | |  __/| |_| |___) |
 \___/|____|_| |_|_|  |_|_|    \___/|____/

        Second Brain — Multi-Agent System
        Built on hermes-agent  ·  v1.0.0
"""

    def __init__(self, quiet: bool = False):
        self.quiet = quiet
        if _RICH:
            self.console = Console(stderr=False, highlight=False)
        else:
            self.console = None

    # ── Public API ─────────────────────────────────────────────

    def banner(self) -> None:
        """Print the OLYMPUS ASCII banner on startup."""
        if self.quiet:
            return
        if _RICH:
            self.console.print(
                Panel(
                    Text(self.BANNER, style="bold yellow", justify="center"),
                    border_style="dim white",
                    box=box.DOUBLE,
                )
            )
        else:
            print(self.BANNER)

    def god_speaking(self, god: str, message: str) -> None:
        """Print a god's status line with emoji and color."""
        if self.quiet:
            return
        emoji = self.GOD_EMOJI.get(god.upper(), "•")
        color = self.GOD_COLORS.get(god.upper(), "white")
        line  = f"{emoji}  {god.upper()} — {message}"
        if _RICH:
            self.console.print(line, style=color)
        else:
            ansi = GOD_ANSI.get(god.upper(), BOLD)
            print(f"{ansi}{line}{RESET}")

    def print_agent_line(self, line: str) -> None:
        """
        Print a line from agent output with god names colorized.
        Call this instead of print() when streaming agent responses.
        """
        colored = colorize_god_output(line)
        if _RICH:
            # Use ANSI-precolored version since rich would escape it
            sys.stdout.write(colored + "\n")
            sys.stdout.flush()
        else:
            sys.stdout.write(colored + "\n")
            sys.stdout.flush()

    def status(self, message: str) -> None:
        """Print a neutral status line."""
        if self.quiet:
            return
        if _RICH:
            self.console.print(f"   {message}", style="dim white")
        else:
            print(f"   {message}")

    def routing(self, plan: dict) -> None:
        """Print the routing plan summary from route_to_gods()."""
        if self.quiet:
            return
        rationale = plan.get("rationale", "")
        if _RICH:
            self.console.print(f"\n⚡ {rationale}\n", style="bold yellow")
        else:
            print(f"\n\033[1;33m⚡ {rationale}\033[0m\n")

    def divider(self) -> None:
        """Print a thin divider line."""
        if self.quiet:
            return
        if _RICH:
            self.console.rule(style="dim white")
        else:
            print("─" * 60)

    def error(self, message: str) -> None:
        """Print an error message."""
        if _RICH:
            self.console.print(f"✗  {message}", style="bold red")
        else:
            print(f"\033[1;31m✗ {message}\033[0m", file=sys.stderr)

    def success(self, message: str) -> None:
        """Print a success message."""
        if self.quiet:
            return
        if _RICH:
            self.console.print(f"✓  {message}", style="bold green")
        else:
            print(f"\033[1;32m✓ {message}\033[0m")

    def cron_registered(self, name: str, schedule: str) -> None:
        """Confirm a cron job was registered."""
        if self.quiet:
            return
        msg = f"Cron registered: {name}  [{schedule}]"
        if _RICH:
            self.console.print(f"🕐  {msg}", style="bold cyan")
        else:
            print(f"\033[1;36m🕐 {msg}\033[0m")
