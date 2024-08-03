from jovian.pythondsa import evaluate_test_cases

# #LINEAR SEARCH
# def locate_card(cards, query):
#     N = len(cards)
#     position = 0

#     while position < len(cards):
#         if cards[position] == query:
#             return position
        
#         position += 1
#         if position == len(cards):
#             return -1
#     return -1 

#BINARY SEARCH

"""
1 find the middle element
2 compare middle element with the target
3 if middle element is equal to the target, we are done
4 if middle element is greater than the target, discard right side
5 if middle element is less than the target, discard left side
6 repeat
"""

def test_card(cards,query,mid):
    mid_num = cards[mid]
    if mid_num == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return "left"
        else:
            return "found"
    elif mid_num < query:
        return "left"
    else:
        return "right"

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo+hi) // 2
        mid_num = cards[mid]

        result = test_card(cards,query,mid)
        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        elif result == "right":
            lo = mid + 1

    return -1

test_cases = [
        # Test case 1
        {
            "input": {
                "cards": [13, 11, 10, 7, 4, 3, 1, 0],
                "query": 7
            },
            "output": 3
        },
        # Test case 2
        {
            "input": {
                "cards": [13, 11, 10, 7, 4, 3, 1, 0],
                "query": 13
            },
            "output": 0
        },
        # Test case 3
        {
            "input": {
                "cards": [13, 11, 10, 7, 4, 3, 1, 0],
                "query": 0
            },
            "output": 7
        },
        # Test case 4
        {
            "input": {
                "cards": [13, 11, 10, 7, 4, 3, 1, 0],
                "query": 5
            },
            "output": -1
        },
        # Test case 5
        {
            "input": {
                "cards": [],
                "query": 7
            },
            "output": -1
        },
        # Test case 6
        {
            "input": {
                "cards": [7],
                "query": 7
            },
            "output": 0
        },
        # Test case 7
        {
            "input": {
                "cards": [13],
                "query": 7
            },
            "output": -1
        },
        # Test case 8
        {
            "input": {
                "cards": [13, 7, 10, 7, 4, 3, 1, 0],
                "query": 7
            },
            "output": 1
        }
    ]

evaluate_test_cases(locate_card, test_cases)
