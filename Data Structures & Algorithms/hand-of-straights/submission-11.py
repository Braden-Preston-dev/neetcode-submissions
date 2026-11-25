class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        

        count = Counter(hand)
        hand.sort()
        h = hand[0]
        while h <= hand[-1]:

            while h not in count:
                h += 1
                if h > hand[-1]: break
            
            if h in count:
                for i in range(h, h + groupSize):
                    if i not in count: return False
                    count[i] -= 1
                    if count[i] == 0: count.pop(i)

        return False if count else True
            

