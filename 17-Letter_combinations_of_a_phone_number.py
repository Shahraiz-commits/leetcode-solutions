Class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
            "1":"abc",
            "2":"def",
            "3":"ghi",
     
        }
        result = []
        def backtrack(index, path):
            # Base case
            if(index == len(digits)):
                result.append("".join(path))
                return
            # Recursive case
            letters = phone_map(digits[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()

        backtrack(0, [])
        return result
