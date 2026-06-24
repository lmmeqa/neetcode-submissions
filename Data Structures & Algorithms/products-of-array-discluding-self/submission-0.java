class Solution {
    public int[] productExceptSelf(int[] nums) {
        int fullProduct = 1;
        int zeroCounter = 0;
        for(int num: nums){
            fullProduct*=num;
            if(num == 0){
                zeroCounter++;
            }
        }
        if(zeroCounter > 1) return new int[nums.length];
        int[] output = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 0) {
                output[i] = 1;
                for(int j = 0; j < nums.length; j++){
                    if(j==i) continue;
                    output[i]*=nums[j];
                }
            }
            else{output[i] = fullProduct/nums[i];}

        }
        return output;
    }
}  
