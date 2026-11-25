class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for h in sorted(hand):

            if count[h] == 0:
                continue
            
            if h in count:
                for i in range(h, h + groupSize):
                    if not count[i]: return False
                    count[i] -= 1
                    if count[i] == 0: count.pop(i)

        return False if count else True
            

