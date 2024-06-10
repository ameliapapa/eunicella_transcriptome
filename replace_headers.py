def replace_spaces_in_headers(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.startswith('>'):
                # Replace spaces with underscores in headers
                new_header = line.replace(' ', '_')
                outfile.write(new_header)
            else:
                outfile.write(line)

input_file = 'SILVA_138.1_LSURef_NR99_tax_silva.fasta'
output_file = 'SILVA_138.1_LSURef_NR99_tax_silva_new.fasta'

replace_spaces_in_headers(input_file, output_file)