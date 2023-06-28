import pandas as pd
data_file_path = "128.turkish/restaurants_train_turkish.xml.dat"

with open(data_file_path, "r", encoding="utf-8") as file:
    text = file.read()
    file.close()

data = pd.Series(text)
data.str.split("\n").tolist()