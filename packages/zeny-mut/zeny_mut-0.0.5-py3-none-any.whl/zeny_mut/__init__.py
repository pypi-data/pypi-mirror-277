from Bio import SeqIO

def detectMutation(original_fasta_file, mutant_fasta_file):
    
    original_sequences = {seq_record.id: str(seq_record.seq) for seq_record in
                          SeqIO.parse(original_fasta_file, "fasta")}
    mutant_sequences = {seq_record.id: str(seq_record.seq) for seq_record in SeqIO.parse(mutant_fasta_file, "fasta")}

    for gene_id in original_sequences:
        original_sequence = original_sequences[gene_id]
        mutant_sequence = mutant_sequences.get(gene_id)
        if mutant_sequence is None:
            print(f"Gene {gene_id} not found in mutant sequences.")
            continue
        for i, (x, y) in enumerate(zip(original_sequence, mutant_sequence)):
            if x != y:
                # Determine the region of mutation
                start = max(0, i - 10)  # Start 10 bases before the mutation
                end = min(len(original_sequence), i + 10)  # End 10 bases after the mutation
                mutated_region = mutant_sequence[start:end]
                return f"Mutation detected in gene {gene_id} at position {i}. Mutated region: {mutated_region}"
    return "No mutation detected."

