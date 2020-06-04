def intersection(arrays):
    """
    YOUR CODE HERE
    """

    cashe={}
    for l in arrays:
        for i in l:
            if i in cashe:
                cashe[i]+=1
            else:
                cashe[i]=1
   
    result = []
    for key,value in cashe.items():
        if value ==(len(arrays)):
            result.append(key)

    return result

    

'''
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
'''
result = intersection([
            [1,2,3],
            [1,4,5,3],
            [1,6,7,3]
        ])
result.sort()