class Solution:
    def generateTag(self, caption: str) -> str:
        caption = caption.split()

        result = "#"
        
        for i, j in enumerate(caption):
            if i == 0:
                result += j.lower()

            else:
                result += j.capitalize()

        return result[:100]