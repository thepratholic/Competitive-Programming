class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for ch in s:
            if ch.islower():
                result.append(ch)

            elif ch == '*':
                if result:
                    result = result[:-1]

            elif ch == '#':
                result += result

            elif ch == '%':
                result.reverse()

        return "".join(result)