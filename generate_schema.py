# generate schema
import json
from datetime import date

import pandas as pd


def generate_schema():
    """ schema generation from today filename dataset """
    today = date.today().strftime("%d_%m_%Y")
    complete_dataset = pd.read_csv(f"complete_dataset_{today}.csv")
    json_schema = pd.io.json.build_table_schema(complete_dataset)
    with open("json_schema_for_big_query.json", "w", encoding="utf-8") as f:
        json.dump(json_schema, f, ensure_ascii=False, indent=4)
    return None


if __name__ == "__main__":
    generate_schema()
