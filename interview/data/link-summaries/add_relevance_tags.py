#!/usr/bin/env python3
"""
Add relevance tags (HIGH or MEDIUM) to every entry in the source markdown files.

Reads analysis files to build a mapping of entry titles to relevance levels,
then inserts **Relevance:** HIGH or **Relevance:** MEDIUM after each ## title line
in the source files.
"""

import re
import os
from difflib import SequenceMatcher

SUMMARIES_DIR = "/home/alexey/git/ai-engineering-field-guide/_work-in-progress/link-summaries"

ANALYSIS_FILES = {
    "blind": "/tmp/analysis_blind.md",
    "hn": "/tmp/analysis_hn.md",
    "reddit": "/tmp/analysis_reddit.md",
    "x": "/tmp/analysis_x.md",
}

SOURCE_FILES = {
    "blind": [f"blind-{i:02d}.md" for i in range(6)],
    "hn": [f"hn-{i:02d}.md" for i in range(4)],
    "reddit": [f"reddit-{i:02d}.md" for i in range(6)],
    "x": [f"x-{i:02d}.md" for i in range(3)],
}


def parse_analysis_file(filepath):
    """Parse an analysis file and return a dict mapping title text -> relevance level."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    mapping = {}
    current_level = None

    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("## HIGH"):
            current_level = "HIGH"
            continue
        elif line.startswith("## MEDIUM"):
            current_level = "MEDIUM"
            continue
        elif line.startswith("## LOW"):
            current_level = "LOW"
            continue
        elif line.startswith("## Summary"):
            current_level = None
            continue

        if current_level and line.startswith("- ["):
            # Extract the title from the analysis entry
            # Format: - [prefix: Title] -- Description
            match = re.match(r"^- \[(.+?)\]\s*--", line)
            if match:
                raw_title = match.group(1)
                # Remove the file prefix (e.g., "blind-00: " or "x-00:")
                title = re.sub(r"^[a-z]+-\d+:\s*", "", raw_title)
                mapping[title] = current_level

    return mapping


def normalize_for_matching(text):
    """Normalize text for fuzzy matching: lowercase, strip punctuation, collapse spaces."""
    text = text.lower()
    # Remove markdown link brackets
    text = re.sub(r"[\[\]]", "", text)
    # Remove common punctuation but keep spaces and alphanumeric
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def find_relevance(source_title, analysis_mapping):
    """Find the relevance level for a source title by matching against the analysis mapping.

    Returns (relevance_level, matched_key) or (None, None) if no match found.
    """
    norm_source = normalize_for_matching(source_title)

    # 1. Try exact match on normalized text
    for key, level in analysis_mapping.items():
        if normalize_for_matching(key) == norm_source:
            return level, key

    # 2. Try substring containment (either direction)
    for key, level in analysis_mapping.items():
        norm_key = normalize_for_matching(key)
        if norm_key in norm_source or norm_source in norm_key:
            return level, key

    # 3. Try matching on significant words (at least 3 content words matching)
    source_words = set(norm_source.split()) - {"the", "a", "an", "at", "in", "on", "to", "for", "of", "and", "or", "is", "are", "was", "were", "my", "i", "how", "what", "do", "does", "with", "from", "by", "its", "it", "this", "that"}
    best_match = None
    best_score = 0

    for key, level in analysis_mapping.items():
        norm_key = normalize_for_matching(key)
        key_words = set(norm_key.split()) - {"the", "a", "an", "at", "in", "on", "to", "for", "of", "and", "or", "is", "are", "was", "were", "my", "i", "how", "what", "do", "does", "with", "from", "by", "its", "it", "this", "that"}

        if not key_words or not source_words:
            continue

        # Count overlapping significant words
        overlap = source_words & key_words
        overlap_ratio = len(overlap) / min(len(source_words), len(key_words))

        if overlap_ratio > best_score:
            best_score = overlap_ratio
            best_match = (level, key)

    if best_score >= 0.5 and best_match:
        return best_match

    # 4. Try SequenceMatcher ratio
    best_ratio = 0
    best_match = None
    for key, level in analysis_mapping.items():
        norm_key = normalize_for_matching(key)
        ratio = SequenceMatcher(None, norm_source, norm_key).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = (level, key)

    if best_ratio >= 0.55 and best_match:
        return best_match

    return None, None


def process_source_file(filepath, analysis_mapping, filename):
    """Process a source file: add relevance tags after each ## title line."""
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    stats = {"HIGH": 0, "MEDIUM": 0, "unmatched": 0, "total": 0}
    warnings = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this is an entry header (## Title)
        # But skip the first line if it's a top-level header (# ...)
        # Also skip ## HIGH, ## MEDIUM, ## LOW headers from analysis format
        if line.startswith("## ") and not line.startswith("# ") and i > 0:
            # Skip if already tagged
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            if next_line.strip().startswith("**Relevance:**"):
                new_lines.append(line)
                i += 1
                continue

            # Extract the title
            title = line[3:].strip()
            # Remove markdown link syntax if present: ## [Title] -> Title
            link_match = re.match(r"^\[(.+?)\]$", title)
            if link_match:
                title = link_match.group(1)

            stats["total"] += 1

            # Find relevance
            level, matched_key = find_relevance(title, analysis_mapping)

            if level is None:
                # Default to MEDIUM
                level = "MEDIUM"
                stats["unmatched"] += 1
                warnings.append(f"  WARNING: No match for '{title}' in {filename} -> defaulting to MEDIUM")
            elif level == "LOW":
                # LOW entries should have been deleted already, but if still present, mark as MEDIUM
                level = "MEDIUM"

            stats[level] += 1

            # Write the title line followed by the relevance tag
            new_lines.append(line)
            new_lines.append(f"**Relevance:** {level}\n")
            i += 1
            continue

        new_lines.append(line)
        i += 1

    # Write back
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    return stats, warnings


def main():
    # Build analysis mappings per source type
    all_mappings = {}
    for source_type, analysis_path in ANALYSIS_FILES.items():
        mapping = parse_analysis_file(analysis_path)
        all_mappings[source_type] = mapping
        high_count = sum(1 for v in mapping.values() if v == "HIGH")
        med_count = sum(1 for v in mapping.values() if v == "MEDIUM")
        low_count = sum(1 for v in mapping.values() if v == "LOW")
        print(f"Loaded {len(mapping)} entries from {os.path.basename(analysis_path)}: {high_count} HIGH, {med_count} MEDIUM, {low_count} LOW")

    print()

    # Process each source file
    total_high = 0
    total_medium = 0
    total_entries = 0
    total_unmatched = 0

    for source_type, filenames in SOURCE_FILES.items():
        mapping = all_mappings[source_type]
        for filename in filenames:
            filepath = os.path.join(SUMMARIES_DIR, filename)
            if not os.path.exists(filepath):
                print(f"SKIP: {filename} does not exist")
                continue

            stats, warnings = process_source_file(filepath, mapping, filename)

            if stats["total"] > 0:
                print(f"{filename}: {stats['total']} entries -> {stats['HIGH']} HIGH, {stats['MEDIUM']} MEDIUM", end="")
                if stats["unmatched"] > 0:
                    print(f" ({stats['unmatched']} unmatched, defaulted to MEDIUM)", end="")
                print()

                for w in warnings:
                    print(w)

                total_high += stats["HIGH"]
                total_medium += stats["MEDIUM"]
                total_entries += stats["total"]
                total_unmatched += stats["unmatched"]

    print()
    print("=" * 60)
    print(f"TOTAL: {total_entries} entries tagged")
    print(f"  HIGH:   {total_high}")
    print(f"  MEDIUM: {total_medium}")
    print(f"  Unmatched (defaulted to MEDIUM): {total_unmatched}")


if __name__ == "__main__":
    main()
