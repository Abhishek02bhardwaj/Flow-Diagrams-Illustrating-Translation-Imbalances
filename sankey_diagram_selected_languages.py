import pandas as pd
import plotly.graph_objects as go

# Load data from CSV file
data = pd.read_csv("output.csv")

# Define the list of languages you want to include
languages = ["an", "az", "ca", "cs", "cy", "es", "ed", "de", "it", "pt", "ja", "ko", "vi", "zh", "ar"]

# Filter the data to only include the selected languages
data = data[(data["translations_from"].isin(languages)) & (data["translations_to"].isin(languages))]

# Define source, target, and value columns
source = data["translations_from"]
target = data["translations_to"]
value = data["article_count"]

# Create Sankey diagram figure
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=source.unique().tolist() + target.unique().tolist(),
        color="blue"
    ),
    link=dict(
        source=source.map(lambda x: source.unique().tolist().index(x)),
        target=target.map(lambda x: target.unique().tolist().index(x)),
        value=value,
    ))])

# Show figure
fig.show()
