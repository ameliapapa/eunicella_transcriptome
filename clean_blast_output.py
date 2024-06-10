import csv 

def filter_by_alignment_length(input_file, output_file, min_alignment_length=150):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Read and write the header row
        headers = next(reader)
        writer.writerow(headers)

        # Index for the alignment length column
        alignment_length_idx = headers.index("Alignment Length")

        # Read and filter the rows
        for row in reader:
            alignment_length = int(row[alignment_length_idx])

            # Apply filtering by alignment length
            if alignment_length >= min_alignment_length:
                writer.writerow(row)

# Define input and output files
input_file = 'sample5_ssu_filtered.csv'
output_file = 'sample5_ssu_filtered_length.csv'

# Run the filtering function
filter_by_alignment_length(input_file, output_file)