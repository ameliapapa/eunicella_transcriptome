#!/bin/bash
#SBATCH --job-name="sample2_sortrna"
#SBATCH --error="sample2_sortrna.err"
#SBATCH --output="sample2_sortrna.out" 
#SBATCH --gres=gpu:a100:2
#SBATCH -c 64
#SBATCH --mem=128GB
#SBATCH --time=6:00:00

module load cesga/2020 miniconda3/22.11.1-1
export LANG=en_US.UTF-8
export CONDA_ENVS_PATH=$STORE/conda/envs
export CONDA_PKGS_PATH=$STORE/conda/pkgs 
export XDG_CACHE_HOME=$STORE/conda/cache
conda activate sortmerna_env
export PATH="/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/rRNA_databases/bin:$PATH"
cd /mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc
# Ensure output directories exist
mkdir -p sample2 sample2/out/aligned sample2/out/other

sortmerna --ref $STORE/sortmerna/sortmerna-4.3.7/data/rRNA_databases/rfam-5.8s-database-id98.fasta \
            --reads /mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc/sample2_1_val_1.fq.gz \
            --reads /mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc/sample2_2_val_2.fq.gz \
            --aligned /mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc/sample2/out/aligned \
            --other /mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc/sample2/out/other \
            --fastx -v  \
            --workdir /mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc/sample2 \
            --threads 22
