class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = []
        while matrix:
            # 1- Pop first row
            # += gets individual values like 1,2,3 and append adds the whole row like [1,2,3]
            # This only works over iterables. cannot do += for a single value append
            order+=(matrix.pop(0))
            if not any(matrix):
                break
            # 2- Pop last element of each row
            for row in matrix:
                order.append(row.pop())
                
            if not any(matrix):
                break
            # 3- Pop last row in reverse order
            order+=(matrix.pop()[::-1])
            
            # 4- Pop first element of each row in reverse order
            num_rows = len(matrix)
            # range takes start, end, and step (what to do each loop)
            for i in range(num_rows-1, -1, -1):
                order.append(matrix[i].pop(0))
        return order
