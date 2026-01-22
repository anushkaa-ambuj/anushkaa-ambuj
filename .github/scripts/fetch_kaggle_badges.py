import os
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

competitions = api.competitions_list(sort_by='latestDeadline')
badges_md = ""

for comp in competitions[:5]:  # Example: last 5 competitions
    badges_md += f"![{comp.title}]({comp.url})\n"

with open("README.md", "a") as f:
    f.write("\n" + badges_md)
