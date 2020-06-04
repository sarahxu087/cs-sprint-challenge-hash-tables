def has_negatives(a):
    """
    YOUR CODE HERE
    """
    negative={i:i<0 for i in a}
    result = []
    for i in a:
        if i >0 and(-i in negative):
                result.append(i)
    


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
