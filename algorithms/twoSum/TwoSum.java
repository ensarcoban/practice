import java.util.HashMap;
import java.util.Map;

class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int res[] = new int[2];
        Map<Integer,Integer> h = new HashMap<>();
        for(int i=0;i<nums.length;i++) {
            for (int j = i+1; j < res.length; j++) {
                if (target == nums[i] + nums[j]) {
                    res[0]=i;
                    res[1]=j;
                    return res;
                }
            }
        }
        return res;
    }

    public int[] twoSum2(int[] nums, int target) {
        int res[] = new int[2];
        Map<Integer,Integer> h = new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            int rem = target -nums[i];
            if(h.containsKey(rem))
            {
                res[0]=h.get(rem);
                res[1]=i;
                return res;
                }
            h.put(nums[i],i);
            }
         return res;
        }
    }