# downloding script for datasets.
* merging datasets and saving complete up-to-date locally. 
* Upload dataset to Google big Query

Local copy save name is in this format: 
'complete_dataset_23_10_2020.csv' (today date)


### Repo contain windows wersion with scheduling and linux version with crontab

Windows version -  [download.py](https://github.com/Georgitanev/downloading_data_uploading_gbq_via/blob/main/download.py)
Linux version - [download_linux_version.py](https://github.com/Georgitanev/downloading_data_uploading_gbq_via/blob/main/download_linux_version.py)

#### Python version:
Python 3.7.9
### how to install:
```sh
pip install -r requirements.txt
```

Run windows version: 
(it run in schedule every day at 23:55)
```sh
python download.py
```
Run in linux version: 
(it run in schedule every day at 23:55)
```sh
python download.py
```
Also you can run linux version with this command:
```sh
55 23 * * * python download_linux_version.py
```

#### Optional:
You can generate schema for Google Big Query table with this script:
Schema generator - [generate_schema.py](https://github.com/Georgitanev/downloading_data_uploading_gbq_via/blob/main/generate_schema.py)

It saving file with name: "json_schema_for_big_query.json"
#### You can run it with:

```sh
python generate_schema.py
```

#### Shots from google big Query

- table view
[![Table Image](https://raw.githubusercontent.com/Georgitanev/downloading_data_uploading_gbq_via/main/gbq_table.png)](https://github.com/Georgitanev/downloading_data_uploading_gbq_via/blob/main/gbq_table.png)

- details view
[![Details Image](https://raw.githubusercontent.com/Georgitanev/downloading_data_uploading_gbq_via/main/gbq_big_table_details.png)](https://github.com/Georgitanev/downloading_data_uploading_gbq_via/blob/main/gbq_table.png)

