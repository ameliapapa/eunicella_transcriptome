#!/bin/bash
cd /Users/test/Desktop/RNAseq/raw_data_copy_2/

# Initialize sample number
sample_number=1

# Loop through files matching the pattern "Unknown*.fq.gz"
for file in Unknown*.fq.gz; do
  # Extract the end part (_1.fq.gz or _2.fq.gz) to maintain it in the new filename
  suffix=$(echo "$file" | grep -o "_[12].fq.gz$")
  
  # Construct the new filename using the sample number and the suffix
  new_filename="sample${sample_number}${suffix}"
  
  # Check if the new filename already exists
  if [[ -e "$new_filename" ]]; then
    echo "File $new_filename already exists. Appending '_new' to the filename."
    new_filename="sample${sample_number}_new${suffix}"
  fi
  
  # Rename the file
  mv "$file" "$new_filename"
  
  # Increment the sample number after every second file to match your provided pattern
  if [[ $suffix == "_2.fq.gz" ]]; then
    ((sample_number++))
  fi
done

echo "Renaming completed."
