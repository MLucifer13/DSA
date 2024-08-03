marks = [62,64,65,66]

def linear_search(num, target):
    position =0
    for position in range(len(num)):
        if num[position] == target:
            return position
        
    return -1

result = linear_search(marks,89)
print(result)