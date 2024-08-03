from jovian.pythondsa import evaluate_test_cases

# find a number whose left side is bigger than that number and the index of that number is the answer
def count_rotations_linear(nums):
    position = 1

    while position < len(nums):
        if nums[position] < nums[position-1]:
            return position

        position += 1
    
    return 0

def count_rotations_binary(nums):
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (lo+hi)//2
        mid_number = nums[mid]

        if mid >0 and mid_number < nums[mid-1]:
            return mid
        #answer is in left half
        elif mid_number < nums[hi]:
            hi = mid-1 
        #answer is in right half 
        else:
            lo = mid + 1
    return 0

test1 = {
    "input": {
        "nums": [4,5,6,7,8,1,2,3]
    },
    "output": 5
}


test2 = {
    "input": {
        "nums": [1,2,3,4,5,6,7,8]
    },
    "output": 0
}


test3 = {
    "input": {
        "nums": [9,6,8]
    },
    "output": 1
}

test4 = {
    "input": {
        "nums": [1]
    },
    "output": 0
}

test5 = {
    "input": {
        "nums": [2,3,4,1]
    },
    "output": 3
}

test6 = {
    "input": {
        "nums": [1,2,3,4,5]
    },
    "output": 0
}

test7 = {
    "input": {
        "nums": []
    },
    "output": 0
}

tests = [test1, test2, test3, test4, test5, test6, test7]
linear_search_tests = evaluate_test_cases(count_rotations_binary, tests)
