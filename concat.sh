#!/bin/bash
#
#SBATCH -t 2:00:00 
#SBATCH --job-name concat
#SBATCH --cpus-per-task=2
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=20GB
#SBATCH --output=/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/analysis/logs/concat.out
#SBATCH --error=/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/analysis/logs/concat.err

base_dir="/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test"
concat_dir="${base_dir}/concat"

SECONDS=0

for file1 in "$base_dir"/*_1.fq.gz; do
  if [ -f "$file1" ]; then  
    file2="${file1/_1.fq.gz/_2.fq.gz}"
    base_name=$(basename "$file1" _1.fq.gz)
    output_file="${concat_dir}/${base_name}.fq.gz"
    if [ -f "$file2" ]; then
      cat "$file1" "$file2" > "$output_file"
    else
      echo "Matching file for $file1 not found."
    fi
  fi
done

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed"