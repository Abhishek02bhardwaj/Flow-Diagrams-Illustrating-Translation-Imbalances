import pandas as pd
import matplotlib.pyplot as plt

# Read the original CSV file
df_original = pd.read_csv('output.csv')

# Get all unique values from 'translations_from' and 'translations_to' columns
languages = pd.unique(df_original[['translations_from', 'translations_to']].values.ravel('K'))

# Create a new dataframe with the languages as the only column
df_languages = pd.DataFrame({'languages': languages})

# Add translations from count column
df_languages['translations_from_count'] = df_languages['languages'].apply(
    lambda x: df_original[df_original['translations_from'] == x]['article_count'].sum())

# Add translations to count column
df_languages['translations_to_count'] = df_languages['languages'].apply(
    lambda x: df_original[df_original['translations_to'] == x]['article_count'].sum())

# Sort the dataframe by 'translations_from_count' column in descending order
df_languages = df_languages.sort_values(by='translations_from_count', ascending=False)

# Write the new CSV file
df_languages.to_csv('translation_ratio_on_the_basis_of_article_count.csv', index=False)

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('translation_ratio_on_the_basis_of_article_count.csv')

# Group languages by their coordinates using a dictionary
lang_groups = {}
for i, row in df.iterrows():
    coord = (row['translations_from_count'], row['translations_to_count'])
    lang = row['languages']
    if coord not in lang_groups:
        lang_groups[coord] = [lang]
    else:
        lang_groups[coord].append(lang)

# Create a list of labels where each label is either a single language name or a comma-separated list of language names
labels = []
for i, row in df.iterrows():
    coord = (row['translations_from_count'], row['translations_to_count'])
    if len(lang_groups[coord]) == 1:
        labels.append(lang_groups[coord][0])
    else:
        labels.append(', '.join(lang_groups[coord]))

# Create a scatter plot
plt.scatter(df['translations_from_count'], df['translations_to_count'])
plt.xlabel('Translations from Count')
plt.ylabel('Translations to Count')

# Add annotations for each point
for i, label in enumerate(labels):
    plt.annotate(label, (df['translations_from_count'][i], df['translations_to_count'][i]))

plt.show()