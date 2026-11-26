"""Write one code-review comment that approves a PR with quiet dread."""

import os

COMMENT = (
    "Approved. The tests pass and the diff is clean; in a hundred years "
    "this will be someone else's problem, and that someone is probably me."
)

MAX_CHARS = 140


def validate(text):
    """Enforce the gate: 1-140 chars, a single line, valid UTF-8."""
    if not isinstance(text, str):
        raise ValueError("comment must be a string")
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    if not text.strip():
        raise ValueError("comment must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("comment is %d chars, over the %d limit" % (len(text), MAX_CHARS))
    if "\n" in text or "\r" in text:
        raise ValueError("comment must be a single line")
    return text


def main():
    validate(COMMENT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(COMMENT)


if __name__ == "__main__":
    main()
