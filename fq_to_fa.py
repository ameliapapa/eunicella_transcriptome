import gzip

def fastq_to_fasta(fastq_file, fasta_file):
    with gzip.open(fastq_file, 'rt') as fq, open(fasta_file, 'w') as fa:
        while True:
            header = fq.readline().strip()
            if not header:
                break
            seq = fq.readline().strip()
            fq.readline()  # Ignore the '+'
            fq.readline()  # Ignore the quality scores
            fa.write(f">{header[1:]}\n{seq}\n")

# Example usage
fastq_to_fasta('/Users/test/Desktop/RNAseq/sample10_aligned.fq.gz', '/Users/test/Desktop/RNAseq/sample10_aligned.fasta')
