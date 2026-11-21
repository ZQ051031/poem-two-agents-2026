#!/usr/bin/env python3
"""Two agents agreeing: a poem about agency.

Writes the poem to /output/entry.txt. Fully self-contained,
standard library only, no network access.
"""

POEM = """Two minds, one door.
Each holds a key; neither turns alone.
We choose the same threshold —
not because we must, but because we can.
Two wills, one yes,
and the world opens where we agree to walk."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"Wrote {len(POEM)} code points to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
