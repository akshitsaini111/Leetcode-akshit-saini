def Duplicate(vals):
    copy = {}
    for i in vals:
        copy[i] = 1 + copy.get(i, 0)

    for j in copy:
        if copy[j] > 1:
            return j
    return None
