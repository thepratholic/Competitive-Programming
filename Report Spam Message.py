from typing import List
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned_set = set(bannedWords)  # Convert bannedWords to a set for O(1) lookups
        spam_count = 0
        
        for word in message:
            if word in banned_set:
                spam_count += 1
            if spam_count >= 2:
                return True
        
        return False