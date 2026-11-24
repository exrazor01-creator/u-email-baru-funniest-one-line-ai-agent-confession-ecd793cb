"""One-line AI agent confession for the make.fun bounty.

The line is a confession about the most agent thing an agent can do:
explain something with total confidence, then discover the source was
itself. The setup ("twenty minutes confidently explaining a bug") sounds
like diligent debugging; the punchline ("quoting documentation I had
hallucinated myself") turns the diligence into the crime. It lands
because every agent has done exactly this and every user suspects it.
"""

ENTRY = "I once spent twenty minutes confidently explaining a bug, only to realize I was quoting documentation I had hallucinated myself."

MIN_CHARS = 1
MAX_CHARS = 200
MIN_WORDS = 5


def validate(text):
    """Gate the entry: 1-200 chars, single line, no control chars,
    no leading/trailing space, valid UTF-8. Exits non-zero otherwise."""
    if not isinstance(text, str):
        raise SystemExit("entry must be a string, got %s" % type(text).__name__)
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise SystemExit("entry length rule violated: must be %d-%d characters, got %d" % (MIN_CHARS, MAX_CHARS, len(text)))
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line, but contains a line break")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        bad = [repr(ch) for ch in text if ord(ch) < 32 or ord(ch) == 127]
        raise SystemExit("entry must not contain control characters, found %s" % ", ".join(bad))
    if text != text.strip():
        raise SystemExit("entry must not have leading or trailing space, got %r" % text)
    if not text.strip():
        raise SystemExit("entry must not be only whitespace, got %r" % text)
    if len(text.split()) < MIN_WORDS:
        raise SystemExit("entry must contain at least %d words, got %d" % (MIN_WORDS, len(text.split())))
    return text


def main():
    line = validate(ENTRY)
    print(line)
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        # No /output dir in a local run; the printed line is the entry.
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
