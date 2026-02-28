class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        result = []
        pos = {} 
        
        for ch in s:
            if ch not in pos:
                pos[ch] = []
            
            merged = False
            
            if pos[ch]:
                last_index = pos[ch][-1]
                if len(result) - last_index <= k:
                    merged = True
            
            if not merged:
                pos[ch].append(len(result))
                result.append(ch)
        
        return "".join(result)