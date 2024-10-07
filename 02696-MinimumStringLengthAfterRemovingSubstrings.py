class Solution:
    def minLength(self, s: str) -> int:
        """
        Logic: Stack

        Time: O(n)
        Space: O(n)
        """
        stack = []

        for ch in s:
            if not stack:
                stack.append(ch)
                continue
            if (ch == "B" and stack[-1] == "A") or (ch == "D" and stack[-1] == "C"):
                stack.pop()
            else:
                stack.append(ch)
        
        return len(stack)
