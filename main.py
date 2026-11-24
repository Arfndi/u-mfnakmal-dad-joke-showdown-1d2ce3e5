"""Dad Joke Showdown entry: one dad joke, told in a single line.

The joke below is the whole entry. It is fixed text, so every run writes
the same bytes to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

from pathlib import Path
import os

JOKE = "My dad got a GPS for his birthday. We haven't heard from him in days, but his car has reached Level 85 in Candy Crush."

# The scorer only accepts 1 to 200 characters, so refuse to write
# anything outside that range instead of handing in an invalid entry.
LIMIT = 200


def main():
    joke = JOKE.strip()
    if not 1 <= len(joke) <= LIMIT:
        raise SystemExit(f"joke is {len(joke)} characters, outside the 1-{LIMIT} gate")
    if joke.count("\n"):
        raise SystemExit("the joke must fit on one line")
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(joke, encoding="utf-8")
    if target.read_text(encoding="utf-8") != joke:
        raise SystemExit("entry.txt did not round-trip cleanly")
    print(f"wrote entry.txt ({len(joke)} characters)")


if __name__ == "__main__":
    main()
