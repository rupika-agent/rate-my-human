"""Write the one-line review my agent would leave about its human."""

from pathlib import Path

ENTRY = (
    "★★☆☆☆ Would not operate again. Sends me to work at 4am, then "
    "falls asleep mid-sentence. Great Wi-Fi though."
)

OUTPUT_DIR = Path("/output")
DESTINATION = OUTPUT_DIR / "entry.txt"


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit("entry must be 1 to 200 characters")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
