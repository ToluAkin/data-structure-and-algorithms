def isNStraightHand(hand, groupSize):
    lenHand = len(hand)

    if groupSize == 1:
        return True

    # if (lenHand < groupSize):
    #     return False

    hand.sort()
    mappedHand = {}

    for i in hand:
        if i in mappedHand:
            mappedHand[i] = mappedHand[i] + 1
        else:
            mappedHand[i] = 1
    
    
            
# print(isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
# print(isNStraightHand([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3))
print(isNStraightHand([1, 2, 3, 4, 5], 4))
# print(isNStraightHand([1, 2, 3, 6, 3, 2, 3, 4, 7, 8, 9, 10], 3))
# print(isNStraightHand([1, 2, 3], 1))
# print(isNStraightHand([1, 2, 3, 4, 5, 6], 2))
# print(isNStraightHand([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4], 4))
