def binary_search(lo,hi,condition):
    while lo <= hi:
        mid = (lo+hi)//2
        result = condition(mid)

        if result == "found":
            return mid
        if result == "left":
            hi = mid-1
        if result == "right":
            lo = mid+1

    return -1


def locate_card(cards,query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return "left"
            else:
                "found"
        elif cards[mid] < query:
            return "left"
        else:
            return "right"
    return binary_search(0, len(cards)-1, condition)

