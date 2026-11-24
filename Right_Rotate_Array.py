def rotateArray(arr: List[int], r: int) -> List[int]:
    r = r % len(arr)
    arr = arr[-r:] + arr[:-r]
    return arr