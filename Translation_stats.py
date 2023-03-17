import pandas as pd
import requests

# Define the API
url = "https://en.wikipedia.org/w/api.php?action=query&list=contenttranslationstats&format=json"

# Send a request to the API and retrieve the response data
response = requests.get(url)
data = response.json()

# Extract the translation data from the response data and convert it to a list of dictionaries
translations = data['query']['contenttranslationstats']['pages']
translations_list = []
for t in translations:
    translations_list.append({
        'translations_from': t['sourceLanguage'],
        'translations_to': t['targetLanguage'],
        'article_count': t['count']
    })

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(translations_list)

df.to_csv('output.csv', index=False)

