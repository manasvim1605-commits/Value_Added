def duplicateZero(arr: List[int]) -> List[int]:
    res = []

    for i in arr:
        res.append(i)
        if i == 0:
            res.append(0)

    return res[:len(arr)]