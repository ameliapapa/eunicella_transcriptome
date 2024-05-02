#!/bin/bash
#
#SBATCH -t 10:00:00 #Run job for 10 hours
#SBATCH --job-name rnaseq_fastqc
#SBATCH --cpus-per-task=2
#SBATCH --ntasks-per-node=8
#SBATCH --mem-per-cpu=20GB
#SBATCH --output=/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/analysis/logs/fas>
#SBATCH --error=/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/analysis/logs/fast>

###################################################################
module load cesga/2020 fastqc/0.12.1

cd /mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/concat

input_dir="/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/concat"
output_dir="${input_dir}/fastqc"

SECONDS=0 
for file in "$input_dir"/*.fq.gz; do
    fastqc -t 5 "$file" -o "$output_dir"
done

duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed"

