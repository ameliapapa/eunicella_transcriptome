#!/bin/bash
#SBATCH --job-name=blast_ssu
#SBATCH --output=blast_ssu.out
#SBATCH --error=blast_ssu.err
#SBATCH --gres=gpu:a100:2
#SBATCH --cpus-per-task=64
#SBATCH --time=6:00:00  # Adjust time as needed
#SBATCH --mem=128G         # Adjust memory as needed

module load ncbi-blast/2.14.1+

# Set the path to the database
db_path="/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc/dcyl/blast/SILVA_138.1"
base_dir="/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc/dcyl/blast"
query_dir="${base_dir}/fasta"
output_dir="${base_dir}/out"

blastn -task megablast -num_threads 64 -outfmt "6 qseqid qlen length bitscore qcovs evalue pident sseqid" -db "${db_path}/SILVA_SSU" -max_target_seqs 1 -query "${query_dir}/sample2_aligned.fa" -out "${output_dir}/sample2_ssu.out"