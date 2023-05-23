import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("display.max_rows",100)
temp_data = pd.read_csv("Sales 2016 to 2019.csv")
temp_data["date"] = pd.to_datetime(temp_data["date"])
data = temp_data.loc[(temp_data["date"] >= "2016-01-01") & (temp_data["date"] < "2019-12-31")]
data = data.astype({"zip_code": int})

popular_per_zip = data.groupby(["zip_code"])["bottles_sold"].sum().sort_values(ascending=False)
popular = pd.DataFrame(popular_per_zip).reset_index()

percentage = data.groupby("store_number")["sale_dollars"].sum()
temp_total = data.agg({"sale_dollars":sum})
total_sum = float(temp_total.iloc[0])
percentage = percentage * 100 / total_sum
percentage_per_store = pd.DataFrame(percentage).reset_index()

plt.scatter(popular["zip_code"], popular["bottles_sold"], c=np.random.rand(len(popular),3))
plt.title("Bottles sold per zip code")
plt.xlabel("Zip code")
plt.ylabel("Bottles Sold")
plt.show()
plt.plot(percentage_per_store["store_number"], percentage_per_store["sale_dollars"],'H')
plt.title("Percentage of Sales per store")
plt.xlabel("Store Number")
plt.ylabel("Percentage of Total Sales")
plt.show()
