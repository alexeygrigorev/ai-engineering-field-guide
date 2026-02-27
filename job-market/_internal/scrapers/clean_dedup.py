#!/usr/bin/env python3
"""
Clean and deduplicate scraped job listings.

Reads a scraped CSV (all_jobs_{date}.csv):
  1. Removes spam companies (Alignerr, etc.)
  2. Deduplicates within the scrape by (title, company)
  3. Removes IDs already in global all_jobs_dedup.csv
  4. Appends only new jobs to global CSV

Outputs:
  - all_jobs_{date}_dedup.csv  (date-specific, new jobs only)
  - all_jobs_dedup.csv         (global, appended with scraped_date column)
"""
import argparse
from pathlib import Path

import pandas as pd

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent  # _internal/
REPO_ROOT = PROJECT_ROOT.parent   # job-market/
DATA_RAW_DIR = REPO_ROOT / "data_raw"

GLOBAL_DEDUP_CSV = PROJECT_ROOT / "all_jobs_dedup.csv"
SPAM_COMPANIES = ["Alignerr"]


def get_global_ids():
    """Get job IDs already in global all_jobs_dedup.csv."""
    if not GLOBAL_DEDUP_CSV.exists():
        return set()
    df = pd.read_csv(GLOBAL_DEDUP_CSV)
    return set(df.id.astype(str))


def main():
    parser = argparse.ArgumentParser(description="Clean and deduplicate scraped jobs CSV")
    parser.add_argument("csv_file", help="Input CSV file (e.g., all_jobs_20260227.csv)")
    args = parser.parse_args()

    csv_path = Path(args.csv_file)
    if not csv_path.is_absolute():
        csv_path = PROJECT_ROOT / args.csv_file

    if not csv_path.exists():
        print(f"ERROR: {csv_path} not found!")
        return

    df = pd.read_csv(csv_path)
    print(f"Total scraped: {len(df)}")

    # Ensure id column
    if "id" not in df.columns:
        df["id"] = df.link.apply(lambda l: l.rsplit("/", maxsplit=1)[1])

    # 1. Remove spam companies
    before = len(df)
    df = df[~df.company.isin(SPAM_COMPANIES)]
    removed_spam = before - len(df)
    if removed_spam:
        print(f"Removed {removed_spam} spam company jobs")

    # 2. Deduplicate within this scrape by (title, company)
    before = len(df)
    df = df.drop_duplicates(subset=["title", "company"])
    removed_dupes = before - len(df)
    if removed_dupes:
        print(f"Removed {removed_dupes} duplicate (title, company) pairs")

    print(f"After within-scrape dedup: {len(df)}")

    # 3. Remove IDs already in global all_jobs_dedup.csv
    existing_ids = get_global_ids()
    print(f"Existing jobs in all_jobs_dedup.csv: {len(existing_ids)}")

    overlap = df[df.id.astype(str).isin(existing_ids)]
    print(f"Already in global CSV (overlap): {len(overlap)}")

    df_new = df[~df.id.astype(str).isin(existing_ids)].copy()
    print(f"\nNew unique jobs: {len(df_new)}")

    if len(df_new) > 0:
        print(f"\nTop companies:")
        print(df_new.company.value_counts().head(10).to_string())

    # Add scraped_date
    stem = csv_path.stem  # e.g., all_jobs_20260227
    if "scraped_date" not in df_new.columns:
        date_str = stem.replace("all_jobs_", "")
        scraped_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
        df_new["scraped_date"] = scraped_date

    # Save date-specific dedup CSV
    dedup_path = csv_path.parent / f"{stem}_dedup.csv"
    df_new.to_csv(dedup_path, index=False)
    print(f"\nSaved: {dedup_path.name} ({len(df_new)} jobs)")

    # Append to global all_jobs_dedup.csv
    if len(df_new) > 0:
        if GLOBAL_DEDUP_CSV.exists():
            df_global = pd.read_csv(GLOBAL_DEDUP_CSV)
            df_global = pd.concat([df_global, df_new], ignore_index=True)
        else:
            df_global = df_new

        df_global.to_csv(GLOBAL_DEDUP_CSV, index=False)
        print(f"Updated: {GLOBAL_DEDUP_CSV.name} (total: {len(df_global)} jobs)")


if __name__ == "__main__":
    main()
