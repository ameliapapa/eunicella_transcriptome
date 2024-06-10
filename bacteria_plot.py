import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your BLAST CSV output file
blast_csv_file = '/Users/test/Desktop/RNAseq/analysis/blast/sample5_ssu_filtered_length.csv'

# Define the column names for the DataFrame
column_names = [
    "Query ID",
    "Query Length",
    "Alignment Length",
    "Bit Score",
    "Query Coverage (%)",
    "E-value",
    "Percent Identity",
    "Subject ID",
    "Kingdom",
    "Supergroup",
    "Group",
    "Subgroup",
    "Clade",
    "Subclade",
    "Phylum",
    "Class",
    "Subclass",
    "Order",
    "Family",
    "Genus",
    "Species"
]

# Read the CSV file into a DataFrame with the specified column names, handling bad lines
blast_df = pd.read_csv(blast_csv_file, names=column_names, on_bad_lines='skip', skiprows=0)

# Display the first few rows of the DataFrame to understand its structure
print(blast_df.head())

# Print the column headers of the DataFrame
print("Column headers of the DataFrame:", blast_df.columns.tolist())

# Check for unique values in the 'Kingdom' column
if 'Kingdom' in blast_df.columns:
    print("Unique Kingdom values:", blast_df['Kingdom'].unique())
else:
    print("Column 'Kingdom' not found in the DataFrame.")

# Filter the DataFrame for rows where Kingdom is 'Bacteria'
if 'Kingdom' in blast_df.columns:
    filtered_df = blast_df[blast_df['Kingdom'] == 'Bacteria']

    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        print("No rows found for Kingdom 'Bacteria'.")
    else:
        # Define the relevant columns for Subgroup and Subclade
        subgroup_col = 'Subgroup'
        subclade_col = 'Subclade'

        # Check if the relevant columns exist in the DataFrame
        if subgroup_col in filtered_df.columns and subclade_col in filtered_df.columns:
            # Check for missing values in the relevant columns
            print("Missing values in 'Subgroup' before dropna:", filtered_df[subgroup_col].isnull().sum())
            print("Missing values in 'Subclade' before dropna:", filtered_df[subclade_col].isnull().sum())

            # Drop rows with missing subgroup or subclade values if necessary
            filtered_df = filtered_df.dropna(subset=[subgroup_col, subclade_col])

            # Check for missing values in the relevant columns after dropna
            print("Missing values in 'Subgroup' after dropna:", filtered_df[subgroup_col].isnull().sum())
            print("Missing values in 'Subclade' after dropna:", filtered_df[subclade_col].isnull().sum())

            # Strip trailing spaces from the Subgroup and Subclade columns
            filtered_df[subgroup_col] = filtered_df[subgroup_col].str.strip()
            filtered_df[subclade_col] = filtered_df[subclade_col].str.strip()

            # Group by Subgroup and Subclade and count occurrences
            subgroup_subclade_counts = filtered_df.groupby([subclade_col, subgroup_col]).size().reset_index(name='Count')

            # Calculate the total counts
            total_count = subgroup_subclade_counts['Count'].sum()

            # Calculate the percentage of each subclade within the sample
            subgroup_subclade_counts['Percentage'] = (subgroup_subclade_counts['Count'] / total_count) * 100

            # Check if the grouped DataFrame is empty
            if subgroup_subclade_counts.empty:
                print("No data available for the given Subgroup and Subclade after filtering.")
            else:
                # Diagnostic print to check DataFrame content
                print(subgroup_subclade_counts)

                # Ensure the DataFrame has the correct subgroup and subclade names
                print(f"Subgroup and Subclade names: {subgroup_subclade_counts[[subclade_col, subgroup_col]].values.tolist()}")

                # Create a bar plot for subgroup and subclade counts with increased figure height
                plt.figure(figsize=(14, 10))  # Adjust the size as needed

                # Create the barplot
                ax = sns.barplot(
                    data=subgroup_subclade_counts,
                    x='Percentage',
                    y=subclade_col,
                    hue=subgroup_col,
                    palette='viridis'
                )

                # Set plot labels and title
                plt.xlabel('Percentage')
                plt.ylabel('Subclade')
                plt.title('Percentage of Subclades within Bacteria, Colored by Subgroup')

                # Adjust the subplot parameters to give some padding
                plt.subplots_adjust(left=0.3)  # Adjust this value as needed to reduce the white gap

                # Ensure layout is tight so labels are not cut off
                plt.tight_layout()

                # Show the plot
                plt.show()

                # Optionally, save the plot to a file
                # plt.savefig('/path/to/save/subgroup_subclade_counts.png')
        else:
            print(f"Columns '{subgroup_col}' and/or '{subclade_col}' not found in the DataFrame.")
else:
    print("Column 'Kingdom' not found in the DataFrame.")
