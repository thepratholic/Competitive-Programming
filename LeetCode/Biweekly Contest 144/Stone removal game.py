class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False

        stones_to_remove = 10
        is_alice_turn = True  # Alice starts

        while n >= stones_to_remove:
            n -= stones_to_remove
            stones_to_remove -= 1
            is_alice_turn = not is_alice_turn  # Alternate turns


        return not is_alice_turn