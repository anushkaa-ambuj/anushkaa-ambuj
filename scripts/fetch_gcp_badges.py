import os, requests

token = os.environ['GCP_TOKEN']
headers = {'Authorization': f'Bearer {token}'}
response = requests.get("https://cloud.google.com/badges/api/user/badges", headers=headers)

badges_md = ""
for badge in response.json():
    badges_md += f"![{badge['name']}]({badge['image_url']})\n"

with open("README.md", "a") as f:
    f.write("\n" + badges_md)
