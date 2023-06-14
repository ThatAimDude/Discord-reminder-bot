import requests
import json

notion_token = ""
database_id = "028e6cf3082043c3a140e3de354abf52"
url = f"https://api.notion.com/v1/databases/{database_id}/query"

payload = {"page_size": 100}
headers = {
    "Authorization": f"Bearer {notion_token}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
data = json.loads(response.text)

results = []
for result in data["results"]:

    if "Name" in result["properties"] and result["properties"]["Name"].get("title"):
        name = result["properties"]["Name"]["title"][0]["plain_text"]
    else:
        name = "N/A"

    if "Date" in result["properties"] and result["properties"]["Date"].get("date"):
        date = result["properties"]["Date"]["date"]["start"]
    else:
        date = "N/A"

    if "Description" in result["properties"] and result["properties"]["Description"].get("rich_text"):
        description = result["properties"]["Description"]["rich_text"][0]["plain_text"]
    else:
        description = "N/A"

    if "Subject" in result["properties"] and result["properties"]["Subject"].get("select"):
        subject = result["properties"]["Subject"]["select"]["name"]
    else:
        subject = "N/A"

    if "Type" in result["properties"] and result["properties"]["Type"].get("select"):
        type = result["properties"]["Type"]["select"]["name"]
    else:
        type = "N/A"

    result_data = {
        "Name": name,
        "Date": date,
        "Description": description,
        "Subject": subject,
        "Type": type
    }

    results.append(result_data)

output_data = {
    "results": results
}

with open("db.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=4)
