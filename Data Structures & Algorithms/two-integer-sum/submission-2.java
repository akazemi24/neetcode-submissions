class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashNums = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int diff = target - nums[i]; 
            if (hashNums.containsKey(diff)){
                return new int[] {hashNums.get(diff), i};
            }
            hashNums.put(nums[i], i);
        }
        return new int[0];
    }
}
