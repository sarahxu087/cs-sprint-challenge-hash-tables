def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table ={}
    for i,n in enumerate(weights):
        if limit - n in hash_table:
            return [i,hash_table[limit-n]]
        else:
            hash_table[n]=i
