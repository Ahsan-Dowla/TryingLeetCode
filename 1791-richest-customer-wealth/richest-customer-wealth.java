import java.lang.Math;
class Solution {
    public int max_sub_arr(int[] arr){
        int sum=0;
        for(int i=0;i<arr.length;i++){
            sum += arr[i];
        }
        return sum;
    }
    public int maximumWealth(int[][] accounts) {
        int max=0;
        for (int i=0;i<accounts.length;i++){
            
                max = Math.max(max_sub_arr(accounts[i]),max);
            
        }
        return max;
    }
}