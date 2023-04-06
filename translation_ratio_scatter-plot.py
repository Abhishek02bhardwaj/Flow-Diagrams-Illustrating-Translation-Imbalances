import pandas as pd
import matplotlib.pyplot as plt

# Read the original CSV file
df = pd.read_csv('supported_pairs.csv')

# Extract the unique language names from the 'source language' and 'target language' columns
language_names = set(df['source language']).union(set(df['target language']))

# Create a new DataFrame with the language names and write it to a new CSV file
new_df = pd.DataFrame({'Language': list(language_names)})
new_df.to_csv('translation_ratio.csv', index=False)

# Read the language names CSV file
language_df = pd.read_csv('translation_ratio.csv')

# Initialize the "translation in" and "translation out" columns to 0
language_df['translation in'] = 0
language_df['translation out'] = 0

# Loop through each row in the language names CSV file
for i, row in language_df.iterrows():
    # Get the language for the current row
    lang = row['Language']

    # Get the set of languages in the "source language" column of the original CSV file
    translation_in = set(df.loc[df['target language'] == lang, 'source language'])

    # Get the set of languages in the "target language" column of the original CSV file
    translation_out = set(df.loc[df['source language'] == lang, 'target language'])

    # Update the "translation in" and "translation out" columns for the current row
    language_df.at[i, 'translation in'] = len(translation_in)
    language_df.at[i, 'translation out'] = len(translation_out)

language_df = language_df.sort_values(by=['translation in'], ascending=False)

# Write the updated DataFrame to a new CSV file with only the "Language", "translation in", and "translation out" columns
language_df[['Language', 'translation in', 'translation out']].to_csv('translation_ratio.csv', index=False)

# Load CSV file into a Pandas DataFrame
df = pd.read_csv('translation_ratio.csv')

# Create scatter plot
plt.scatter(df['translation in'], df['translation out'])


# Define a function to calculate label positions
def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    duplicates = a.pivot_table(index=['x','y'], aggfunc=lambda x: ', '.join(x))
    for i, point in duplicates.iterrows():
        dx = dy = 0.01
        text = ax.text(point.name[0]+dx, point.name[1]+dy, str(point['val']))


# Call the label_point function to add labels to the scatter plot
label_point(df['translation in'], df['translation out'], df['Language'], plt.gca())

# Set plot title and axis labels
plt.title('Translation In vs. Translation Out')
plt.xlabel('Number of translations in')
plt.ylabel('Number of translations out')

# Show plot
plt.show()