import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your BLAST CSV output file
blast_csv_file = '/Users/test/Desktop/RNAseq/analysis/blast/sample5_ssu_filtered_length.csv'

# Read the CSV file into a DataFrame, handling bad lines
blast_df = pd.read_csv(blast_csv_file, on_bad_lines='skip')

# Display the first few rows of the DataFrame to understand its structure
print(blast_df.head())

# Filter the DataFrame for rows where Subgroup is 'Dinoflagellata'
filtered_df = blast_df[blast_df['Subgroup'] == 'Dinoflagellata']

# Define the relevant column for subclass
subclass_col = 'Subclass'

# Strip trailing spaces from the Subclass column
filtered_df[subclass_col] = filtered_df[subclass_col].str.strip()

# Drop rows with missing subclass values if necessary
filtered_df = filtered_df.dropna(subset=[subclass_col])

# Group by Subclass and count occurrences
subclass_counts = filtered_df[subclass_col].value_counts()

# Calculate total counts and determine the threshold
total_counts = subclass_counts.sum()
threshold = total_counts * 0.01

# Filter subclasses that have counts greater than 1% of total counts
filtered_subclass_counts = subclass_counts[subclass_counts > threshold]

# Convert to DataFrame for easier plotting
filtered_subclass_counts_df = filtered_subclass_counts.reset_index()
filtered_subclass_counts_df.columns = [subclass_col, 'Count']

# Diagnostic print to check DataFrame content
print(filtered_subclass_counts_df)

# Ensure the DataFrame has the correct subclass names
print(f"Subclass names: {filtered_subclass_counts_df[subclass_col].tolist()}")

# Create a bar plot for subclass counts with increased figure height
plt.figure(figsize=(12, 8))  # Adjust the size as needed

# Create the barplot
ax = sns.barplot(
    data=filtered_subclass_counts_df,
    x='Count',
    y=subclass_col,
    palette='viridis'
)

# Set plot labels and title
plt.xlabel('Count')
plt.ylabel('Subclass')
plt.title('Counts of Subclasses within Dinoflagellata Subgroup ( > 1% of total counts)')

# Adjust the subplot parameters to give some padding
plt.subplots_adjust(left=0.3)  # Adjust this value as needed to reduce the white gap

# Ensure layout is tight so labels are not cut off
plt.tight_layout()

# Show the plot
plt.show()

# Optionally, save the plot to a file
# plt.savefig('/path/to/save/subclass_counts.png')
