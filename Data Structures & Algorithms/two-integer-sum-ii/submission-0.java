class Solution {
    public int[] twoSum(int[] numbers, int target) {
        for(int i = 0; i< numbers.length;i++){
            for(int j = numbers.length - 1; j>i; j--){
                if(numbers[i] + numbers[j] == target) {
                    int[] answer = new int[2];
                    answer[0] = i + 1;
                    answer[1] = j + 1;
                    return answer;
                }
            }
        }
        return new int[2];
    }
}
