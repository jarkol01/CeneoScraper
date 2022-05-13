import os
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")
selected_product_id = input("Enter selected product ID: ")

opinions = pd.read_json(f"opinions/{selected_product_id}.json")
print(opinions)