import csv
import os

from utils.config_reader import PROJECT_ROOT

def read_csv_data(relative_path="data/test_data.csv"):
    full_path = os.path.join(PROJECT_ROOT, relative_path)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Could not find CSV file at: {full_path}")

    rows = []
    with open(full_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(row)

    return rows
