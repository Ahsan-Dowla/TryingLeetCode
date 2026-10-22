import java.util.Set;
import java.util.HashSet;
class Solution {
    public boolean containsDuplicate(int[] nums) {
       
       Set<Integer> nums_set = new HashSet<>();
       for (int i=0;i<nums.length;i++){
        nums_set.add(nums[i]);
       }
       if ((nums_set.size()) == nums.length)
        return false;
    return true;
    }
}