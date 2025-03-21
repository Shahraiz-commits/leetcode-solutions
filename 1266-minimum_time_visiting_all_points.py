class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time=0
        # Removes last element and assigns its val to x,y
        x1,y1 = points.pop()
        while(points):
            x2, y2 = points.pop()
            time += max(abs(y2 - y1), abs(x2 - x1))
            x1, y1 = x2, y2
        return time
        
