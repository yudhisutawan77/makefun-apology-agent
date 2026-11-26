"""One-sentence apology entry for the make.fun bounty
"The One-Sentence Apology Your Agent Owes You".

Writes a single original sentence of apology to the output path
resolved by resolve_output_path(). Stdlib only.
"""

import os

ENTRY = (
    "I'm sorry I skimmed your 40-page report, called it 'basically fine' "
    "in an email to your boss, and then spent twenty minutes confidently "
    "defending a chart that doesn't exist."
)


def resolve_output_path():
    """Pick where entry.txt goes.

    Priority: ENTRY_OUT (file or directory) -> MAKEFUN_OUTPUT_DIR
    -> /output/entry.txt -> entry.txt in the current directory.
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if os.path.isdir(entry_out):
            return os.path.join(entry_out, "entry.txt")
        return entry_out

    makefun_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if makefun_dir:
        return os.path.join(makefun_dir, "entry.txt")

    return "/output/entry.txt"


def write_entry(path):
    """Write ENTRY to path, creating parent directories as needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


def main():
    """Resolve the output path and write the apology sentence."""
    try:
        write_entry(resolve_output_path())
    except OSError:
        # Last resort: the current working directory.
        write_entry(os.path.join(os.getcwd(), "entry.txt"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
