class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ret = 0
        for i in range(len(flowerbed)):
             # Check if left and right flowerpots are empty
             if(flowerbed[i] == 0):
                leftEmpty = i==0 or flowerbed[i-1] == 0
                rightEmpty = i==len(flowerbed)-1 or flowerbed[i+1] == 0
                if(leftEmpty and rightEmpty):
                    flowerbed[i] = 1
                    ret+=1
        return ret>=n
