#!/bin/bash
#SBATCH --job-name="sample2_sortrna"
#SBATCH --error="sample2_sortrna.err"
#SBATCH --output="sample2_sortrna.out" 
#SBATCH -c 2
#SBATCH --cpus-per-task=2
#SBATCH --mem=10GB
#SBATCH --time=1:00:00

module load cesga/2020 miniconda3/22.11.1-1
export LANG=en_US.UTF-8
export CONDA_ENVS_PATH=$STORE/conda/envs
export CONDA_PKGS_PATH=$STORE/conda/pkgs 
export XDG_CACHE_HOME=$STORE/conda/cache
conda activate sortmerna_env
export PATH="/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/rRNA_databases/bin:$PATH"
cd /mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc
reads_dir="/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc"
# Ensure output directories exist
mkdir -p $ sample2 sample2/out/aligned sample2/out/other

sortmerna --ref /mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/rRNA_databases/SILVA_138.1/SILVA_138.1_SSURef_NR99_tax_silva.fasta \
            --reads ${reads_dir}/sample2_1_val_1.fq.gz \
            --reads ${reads_dir}/sample2_2_val_2.fq.gz \
            --aligned ${reads_dir}/sample2/out/aligned \
            --other ${reads_dir}/sample2/out/other \
            --fastx \
            --workdir ${reads_dir}/sample2