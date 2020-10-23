import os

import pandas as pd
import schedule
from google.oauth2 import service_account

# historical dataset in .csv format with comma delimeter
url_hist = (
    "https://data.cityofnewyork.us/api/views/"
    + "p32s-yqxq/rows.csv?accessType=DOWNLOAD"
)

# historical dataset in .csv format with comma delimeter
url_new = (
    "https://data.cityofnewyork.us/api/views/"
    + "dpec-ucu7/rows.csv?accessType=DOWNLOAD"
)

# .json credentials for GBQ
path = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(path, "key", "big-query-284408-e895d0eb5b23.json")
credentials = service_account.Credentials.from_service_account_file(
    json_path,
)


# Project and table -> 'big-query-284408:123test.my_table'
project_id = "big-query-284408"
table_id = "123test.my_table"


def download_datasets_csv(url):
    """ downloading and renaming columns - replace space with '_' """
    # dataset = pd.read_csv(url, sep='\t')
    dataset = pd.read_csv(url, sep=",")
    dataset.columns = dataset.columns.str.replace(" ", "_")
    return dataset


def save_today_up_to_date_local_copy(url_hist, url_new):
    """ download and save historical + new dataset in complte dataset"""
    df_historical = download_datasets_csv(url_hist)
    df_new = download_datasets_csv(url_new)
    # creating complete dataset
    complete_dataset = df_historical.append(df_new, ignore_index=True)
    # saving dataset
    complete_dataset.to_csv("complete_dataset.csv", sep=",", index=False)
    return complete_dataset


def replace_data_in_gbq_table(project_id, table_id, complete_dataset):
    """ replacing data in Google Cloud Table """
    complete_dataset.to_gbq(
        destination_table=table_id,
        project_id=project_id,
        credentials=credentials,
        if_exists="replace",
    )
    return None


def main_task():
    complete_dataset = save_today_up_to_date_local_copy(url_hist, url_new)
    replace_data_in_gbq_table(project_id, table_id, complete_dataset)
    return None


schedule.every().day.at("23:55").do(main_task)

if __name__ == "__main__":
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
