import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os




def plot_line(value_list, item_id, app_id, zone_id):
    value_list = value_list[1:-2].split(",")
    try:
        value_list = list(map(lambda x: float(x), value_list))
        plt.figure()
        plt.plot(list(range(len(value_list))), value_list, color="r")
        plt.savefig(f"./plot/plot_item_{item_id}_app_{app_id}_zone_{zone_id}.png")
        plt.close()
    except:

        print(f"[Info] The item id {item_id}")


if __name__ == "__main__":
    try:
        os.makedirs("./plot")
    except:
        pass
    data = pd.read_csv("part_dataframe.csv", index_col=None, header=0)
    value_list = data.at[0, 'y']
    print(data)
    print(data.dtypes)
    # print(value_list[1:-2].split(","))
    data.apply(lambda x: plot_line(value_list=x['y'], item_id=x['item_id'],
                                   app_id=x['app_id'], zone_id=x['zone_id']), axis=1)
