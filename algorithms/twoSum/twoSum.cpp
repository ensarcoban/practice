#include <vector>
#include <unordered_map>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::vector<int> result;

    int length = nums.size();
    for (int i = 0; i < length; i++)
    {
        for (int j = i+1; j < length; j++)
        {
            if (target == nums[i] + nums[j])
            {
            result.push_back(i);
            result.push_back(j);
            return result;
            }
        }
    }
    return result;
    
}

std::vector<int> twoSum2(std::vector<int>& nums, int target) {
    std::vector<int> result;

    std::unordered_map<int, int> hash_map;
    int length = nums.size();
    for (int i = 0; i < length; i++)
    {
        if (hash_map.find(target - nums[i]) != hash_map.end())
        {
            result.push_back(hash_map[target - nums[i]]);
            result.push_back(i);
            return result;
        }
        hash_map[nums[i]] = i;
    }
    return result;
}