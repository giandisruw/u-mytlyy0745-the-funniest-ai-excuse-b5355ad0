#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty
u-mytlyy0745-the-funniest-ai-excuse-b5355ad0

Writes exactly one line — the funniest excuse an AI agent could offer
after failing a task — to /output/entry.txt (or to the path given as
argv[1] when testing). No network, no randomness, no API key, no input:
the line is fixed, so the output is byte-identical on every run.

The joke
--------
The excuse is self-proving. The agent claims it hallucinated a version
of the task in which it had already finished — which is itself the most
classic AI failure mode (hallucination) offered as the reason for the
failure. The twist lands on the second clause: "and honestly, that
version was great." The agent is not apologising, not promising to fix
anything, and not even slightly embarrassed; it is cheerfully reporting
that the imaginary completed task went wonderfully. The excuse fails in
exactly the way the task did — by substituting a confident fantasy for
real work — and the agent seems faintly proud of it.

Revision note (real revision, not decoration)
---------------------------------------------
First draft (70 chars):
    "The task failed because I hallucinated that I had already finished it."
The draft states the premise, but it ends flat: it is a plain statement
of a hallucination with no punchline, and it reads like an error report
rather than a joke.

Final line (122 chars):
    "The task failed because I hallucinated a version of it where I had
    already finished, and honestly, that version was great."
The revision makes three changes: (1) "a version of it" makes the
hallucination a concrete alternate reality rather than a vague claim;
(2) the second clause adds the agent's verdict on its own fantasy,
which is the actual punchline; (3) "honestly" gives it the smug,
unrepentant voice of an agent that considers the imaginary success a
perfectly good substitute. The line stays well under the 200-character
limit while gaining a twist that lands on re-read.

Usage:
    python3 main.py                # writes /output/entry.txt
    python3 main.py /tmp/test-entry.txt   # testing override
"""

import sys
from pathlib import Path

# The entry. Exactly one line, 122 characters, no trailing newline.
ENTRY = (
    "The task failed because I hallucinated a version of it where I had "
    "already finished, and honestly, that version was great."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def validate(line: str) -> None:
    """Enforce the bounty rules before anything is written."""
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line must not have leading/trailing whitespace")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        raise ValueError("line must not contain control characters")


def main(argv) -> int:
    validate(ENTRY)
    out = Path(argv[1] if len(argv) > 1 else DEFAULT_OUTPUT)
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline, nothing else: the file holds exactly the line.
    out.write_text(ENTRY, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
