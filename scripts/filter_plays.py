#!/usr/bin/env python3
"""Filter NFL play-by-play CSV to only run and pass plays.

Usage:
  python3 scripts/filter_plays.py --input nfl_playbyplay_dataset_2009_2018.csv --output filtered_plays.csv

This script loads the CSV into a pandas DataFrame, keeps only rows where
`play_type` is 'pass' or 'run', writes the filtered CSV, and prints a short summary.
"""
import argparse
from pathlib import Path
import sys
import pandas as pd


def main():
    print('Loading CSV (this may take a while for large files)...')
    df = pd.read_csv("nfl_playbyPlay_dataset_2009_2018.csv", low_memory=False)
    print(df.shape)

    # Normalize play_type column presence
    if 'play_type' not in df.columns:
        print("ERROR: 'play_type' column not found in CSV", file=sys.stderr)
        sys.exit(3)

    keep_types = {'pass', 'run'}
    filtered = df[df['play_type'].isin(keep_types)].copy()
    print(filtered.shape)

    out = Path("filtered_dataset.csv")
    filtered.to_csv(out, index=False)


if __name__ == '__main__':
    main()
