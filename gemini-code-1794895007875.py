import re
from pathlib import Path

# Maps Roman numeral volume references to Docsify route slugs
VOL_MAP = {
    "I": "vol-1",
    "II": "vol-2",
    "III": "vol-3",
    "IV": "vol-4",
    "V": "vol-5",
}

def link_index_text(text: str) -> str:
    # Matches patterns like "I, 36" or "V, 183" (including multiple pages like "V, 4, 6, 14")
    vol_pattern = re.compile(r'\b(I|II|III|IV|V),\s*(\d+(?:\s*,\s*\d+)*)')

    def replace_vol_group(match):
        vol_roman = match.group(1)
        pages_str = match.group(2)
        slug = VOL_MAP[vol_roman]

        # Split comma-separated page numbers belonging to the same volume (e.g., "4, 6, 14")
        pages = [p.strip() for p in pages_str.split(",")]
        linked_pages = [
            f"[{vol_roman}, {pages[0]}](#/{slug}?id=p-{pages[0]})"
        ]
        for p in pages[1:]:
            linked_pages.append(f"[{p}](#/{slug}?id=p-{p})")

        return ", ".join(linked_pages)

    return vol_pattern.sub(replace_vol_group, text)

if __name__ == "__main__":
    index_file = Path("general-index.md")
    if index_file.exists():
        original = index_file.read_text(encoding="utf-8")
        updated = link_index_text(original)
        index_file.write_text(updated, encoding="utf-8")
        print("Successfully linked volume and page references in general-index.md!")
    else:
        print("Could not find general-index.md in the current directory.")