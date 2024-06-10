#!/bin/bash
#SBATCH --job-name=trinity_coral
#SBATCH --output=trinity_coral.out
#SBATCH --error=trinity_coral.err
#SBATCH --time=6:00:00
#SBATCH -N 5
#SBATCH -c 10
#SBATCH --ntasks-per-node=2
#SBATCH --mem=100G

module load cesga/system miniconda3/22.11.1-1

export CONDA_ENVS_PATH=$STORE/conda/envs
export CONDA_PKGS_PATH=$STORE/conda/pkgs 
export XDG_CACHE_HOME=$STORE/conda/cache

conda activate trinity
module load cesga/2020 gcccore/system trinityrnaseq/2.13.2
cd /mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc/dcyl/transcriptome/other/bbmap_coral

Trinity --seqType fq --single merged_coral.fq.gz --CPU 50 --max_memory 30G --min_kmer_cov 2
