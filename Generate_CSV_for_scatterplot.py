import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file into a Pandas DataFrame
df = pd.read_csv('supported_pairs.csv')

# Create a new DataFrame that counts the occurrences of each language in the target_language column
languages_in = df.groupby('target language').size().reset_index(name='number of translations in')

# Create a new DataFrame that counts the occurrences of each language in the source_language column
languages_out = df.groupby('source language').size().reset_index(name='number of translations out')

# Merge the two DataFrames on the language name, using an outer join to include all languages
languages = pd.merge(languages_in, languages_out, how='outer', left_on='target language', right_on='source language')

# Fill missing values with an empty string
languages = languages.fillna('0')

# Combine the two columns of language names, and keep only one
languages['Language name'] = languages['target language'].fillna(languages['source language'])
languages = languages[['Language name', 'number of translations in', 'number of translations out']]

# Save the DataFrame to a new CSV file
languages.to_csv('language_counts.csv', index=False)

# Load CSV file into a Pandas DataFrame
df = pd.read_csv('language_counts.csv')

# Create scatter plot
plt.scatter(df['number of translations in'], df['number of translations out'])


# Define a function to calculate label positions
def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    duplicates = a.pivot_table(index=['x','y'], aggfunc=lambda x: ', '.join(x))
    for i, point in duplicates.iterrows():
        dx = dy = 0.01
        text = ax.text(point.name[0]+dx, point.name[1]+dy, str(point['val']))


# Call the label_point function to add labels to the scatter plot
label_point(df['number of translations in'], df['number of translations out'], df['Language name'], plt.gca())

# Set plot title and axis labels
plt.title('Translation In vs. Translation Out')
plt.xlabel('Number of translations in')
plt.ylabel('Number of translations out')

# Show plot
plt.show()
