#!/bin/bash
#SBATCH --job-name=sample2_bbmap_coral
#SBATCH --output=transcriptome_logs/sample2_bbmap_coral.out
#SBATCH --error=transcriptome_logs/sample2_bbmap_coral.err
#SBATCH -N 2
#SBATCH --ntasks-per-node=1
#SBATCH --time=6:00:00
#SBATCH --mem=300GB
#SBATCH -c 10

module load cesga/2020 jdk/21.0.1
module load bbmap/38.90

# Set Java memory options
export _JAVA_OPTIONS="-Xmx20g -Xms12g"

targetdir="/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc/dcyl/transcriptome/other"
logdir="/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc/dcyl/transcriptome/logs"
cd /mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/genomes

bbsplit.sh \
  build=1 \
  in=${targetdir}/sample2_other.fq.gz \
  outm=${targetdir}/sample2_out%.fq.gz \
  outu=${targetdir}/sample2_bbsplit_nocoral.fq.gz \ 
  refstats=${logdir}/sample2_bbsplit_coral_stats.txt