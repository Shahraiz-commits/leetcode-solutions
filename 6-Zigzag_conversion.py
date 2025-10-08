Class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1 or numRows >= len(s)):
            return s
        rows = [""] * numRows
        currRow = 0
        going_down = False 
        for c in s:
            rows[currRow] += c
            # Change direction if reached top or bottom
            if(currRow == 0 or currRow == numRows - 1):
                going_down = not going_down
            currRow += 1 if going_down else -1
        return "".join(rows)
