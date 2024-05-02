#!/bin/bash
#SBATCH -J trimming  
#SBATCH -o trim_%A_%a.out 
#SBATCH -e trim_%A_%a.err    
#SBATCH --ntasks=5
#SBATCH -t 02:00:00          
#SBATCH --mem-per-cpu=3G    
#SBATCH --array=1-26%2  # Start from index 1 to skip sample1

module load cesga/2020 miniconda3/4.11.0 fastqc/0.12.1 cutadapt
export LANG=en_US.UTF-8
export CONDA_ENVS_PATH=$STORE/conda/envs
export CONDA_PKGS_PATH=$STORE/conda/pkgs 
export XDG_CACHE_HOME=$STORE/conda/cache
conda activate trim-galore-env

# Define directories
input_dir="/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test"
output_dir="${input_dir}/trimmed_fastqc"
samples_list="${input_dir}/samples.txt"

# Read the sample name based on SLURM_ARRAY_TASK_ID
mapfile -t samples < "${samples_list}"
samp=${samples[$SLURM_ARRAY_TASK_ID]}  # This will automatically skip the first two if array starts from 2

SECONDS=0

file1="${input_dir}/${samp}_1.fq.gz"
file2="${input_dir}/${samp}_2.fq.gz"

if [[ -f "$file1" && -f "$file2" ]]; then
    echo "Processing $samp..."
    trim_galore --paired --gzip --fastqc --quality 20 -o "${output_dir}" "${file1}" "${file2}"
else
    echo "Files for sample $samp not found."
fi

duration=$SECONDS
echo "Processing took $(($duration / 60)) minutes and $(($duration % 60)) seconds."


# Note
# One job is processing both forward and reverse reads. But it's being done twice, because I have duplicated
