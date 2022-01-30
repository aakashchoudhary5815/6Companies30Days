class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        Aid, Bid, idx = 0, 0, 0
        piles.sort(reverse=True)
        while idx != len(piles):
            Aid += piles[idx]
            idx += 1
            Bid += piles[idx]
            idx += 1
        return True if Aid > Bid else False