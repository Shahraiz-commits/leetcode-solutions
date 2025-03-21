#include <unordered_map>
#include <vector>
using std::vector;
using std::unordered_map;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        unordered_map<int, int> map;
        for(int i=0; i<nums.size(); i++){
            if(map.count(nums[i]) > 0)
        }
    }
};