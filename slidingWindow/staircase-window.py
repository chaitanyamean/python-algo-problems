def stairCase(height, maxSteps):
    currentNumberOfWays = 0
    waysToTop = [1]
    for ch in range(1, height + 1):
        sow = ch - maxSteps - 1
        eow = ch -1
        if sow >= 0:
            currentNumberOfWays -= waysToTop[sow]
        currentNumberOfWays += waysToTop[eow]
        waysToTop.append(currentNumberOfWays)
    return waysToTop[height]


print(stairCase(4,2))