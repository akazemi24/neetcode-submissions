class Solution {
    public int longestConsecutive(int[] nums) {
        int[] sorted = nums;
        Arrays.sort(sorted);
        int res = 1;
        int cur = 1;

        if (nums.length == 0) return 0;

        for (int i = 1; i < nums.length; i++){
            if (Math.abs(sorted[i] - sorted[i-1]) == 0){
                continue;
            }
            else if (Math.abs(sorted[i] - sorted[i-1]) == 1){
                cur++; 
            }
            else {
                cur = 1; 
            }
            if (cur > res){
                    res = cur;
                }

        }
        return res;
    }
}


