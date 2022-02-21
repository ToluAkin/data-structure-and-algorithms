# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(T):
    # write your code in Python 3.6
    season = len(T) // 4

    winter = T[:season]
    spring = T[season:season * 2]
    summer = T[season * 2: season * 3]
    autumn = T[season * 3:]

    winterValue = max(winter) - min(winter)
    springValue = max(spring) - min(spring)
    summerValue = max(summer) - min(summer)
    autumnValue = max(autumn) - min(autumn)

    allSeasons = [winterValue, springValue, summerValue, autumnValue]
    maxValue = allSeasons.index(max(allSeasons))
    
    if maxValue == 0:
        return 'WINTER'
    elif maxValue == 1:
        return 'SPRING'
    elif maxValue == 2:
        return 'SUMMER'
    else:
        return 'AUTUMN'
# [-3, -14, -5, 7, 8, 42, 8, 3]
# [2, 1, 1, 10, 2, 13, 3, -18]