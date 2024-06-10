import gzip

def split_fastq(gzipped_fastq_file, r1_output, r2_output):
    with gzip.open(gzipped_fastq_file, 'rt') as input_file:
        with open(r1_output, 'w') as r1_file, open(r2_output, 'w') as r2_file:
            while True:
                # Read the next four lines for a single sequence entry
                header = input_file.readline().strip()
                if not header:
                    break  # End of file
                
                sequence = input_file.readline().strip()
                plus = input_file.readline().strip()
                quality = input_file.readline().strip()
                
                # Check if this is an R1 or R2 read
                if ' 1:N:0:' in header:
                    r1_file.write(f"{header}\n{sequence}\n{plus}\n{quality}\n")
                elif ' 2:N:0:' in header:
                    r2_file.write(f"{header}\n{sequence}\n{plus}\n{quality}\n")

# Specify the input gzipped FASTQ file and the output files for R1 and R2
gzipped_fastq_file = '/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc/dcyl/sample10/out/sample10_other.fq.gz'
r1_output = '/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc/dcyl/sample10/out/sample10_other_R1.fq.gz'
r2_output = '/mnt/lustre/scratch/nlsas/home/csic/bye/jdc/projects/esin_rnaseq/test/trimmed_fastqc/dcyl/sample10/out/sample10_other_R2.fq.gz'

# Call the function to split the gzipped FASTQ file
split_fastq(gzipped_fastq_file, r1_output, r2_output)
