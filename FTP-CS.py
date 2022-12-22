def hamming_distance(s1,s2):
    if len(s1) != len(s2):
        return "Different length"

    result = 0
    for i in range(0, len(s1) - 1):
        if s1[i] != s2[i]:
            result += 1

    return result



