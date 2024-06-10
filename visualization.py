import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your BLAST CSV output file
blast_csv_file = '/Users/test/Desktop/RNAseq/analysis/blast/sample5_ssu_filtered_length.csv'
# Read the CSV file into a DataFrame, handling bad lines
blast_df = pd.read_csv(blast_csv_file, on_bad_lines='skip')

# Display the first few rows of the DataFrame to understand its structure
print(blast_df.head())

# Define relevant columns based on your provided column names
genus_col = 'Genus'

# Group by Genus and count occurrences
genus_counts = blast_df[genus_col].value_counts()

# Calculate total counts and determine the threshold
total_counts = genus_counts.sum()
threshold = total_counts * 0.01

# Filter genera that have counts greater than 10% of total counts
filtered_genus_counts = genus_counts[genus_counts > threshold]

# Filter the DataFrame to include only the top genera above the threshold
filtered_df = blast_df[blast_df[genus_col].isin(filtered_genus_counts.index)]

# Convert filtered genus counts to a DataFrame for plotting
genus_counts_df = filtered_genus_counts.reset_index()
genus_counts_df.columns = [genus_col, 'Count']

print(genus_counts_df)

# Create a bar plot for genus counts with increased figure height
plt.figure(figsize=(4, 4))  # Increase height to 16

sns.barplot(
    data=genus_counts_df,
    x='Count',
    y=genus_col,
    palette='viridis'
)

# Set plot labels and title
plt.xlabel('Count')
plt.ylabel('Genus')
plt.title('Most Common Genera in BLAST Results')

# Show the plot
plt.show()

# Optionally, save the plot to a file
#plt.savefig('/Users/test/Desktop/RNAseq/analysis/blast/figures/genus_counts.png')

