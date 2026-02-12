def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    chunks = []
    start = 0
    
    step = chunk_size - overlap

    for i in range(0, len(tokens), step):
        chunks.append(tokens[i:i+chunk_size])
        if i + chunk_size >= len(tokens):
            break
    return chunks