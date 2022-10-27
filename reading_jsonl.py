import jsonlines
import json

import pandas as pd

read_path = "./train.jsonl"
write_path = "./total_data.json"
i = 0
dataframe_list = list()


"""
'start': '2022-03-15 00:00:00',
  'end': '2022-05-15 23:50:00',
  'freq': '10min',
  'y': [0.74754228,
  0.78098471,
  0.63987695,
  0.66838659,
  0.58897271,
  ...],
  'app_id': '1',
  'zone_id': '10',
  'item_id': '1'}

"""

with open(read_path, "r") as rfd:
    temp_file = jsonlines.Reader(rfd)
    for item in jsonlines.Reader(rfd):
        temp_dict = dict()
        temp_dict["app_id"] = item['app_id']
        temp_dict["zone_id"] = item['zone_id']
        temp_dict["item_id"] = item['item_id']
        temp_dict["start"] = item["start"]
        temp_dict["end"] = item["end"]
        temp_dict["freq"] = item["freq"]

        temp_dataframe = pd.DataFrame(temp_dict, index=[0])
        temp_dataframe['y'] = [item["y"]]

        dataframe_list.append(temp_dataframe)

final_dataframe = pd.concat(dataframe_list, axis=0).reset_index(drop=True)
final_dataframe.to_csv("./part_dataframe.csv", index=None)
print(final_dataframe)
    # with open(write_path, "w", encoding='utf-8') as wfd:
    #     for data in rfd:
    #         json.dump(data, wfd, indent=4, ensure_ascii=False)

