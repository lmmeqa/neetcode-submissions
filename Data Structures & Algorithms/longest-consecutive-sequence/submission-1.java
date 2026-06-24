class Solution {
    public int longestConsecutive(int[] nums) {
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
        Set<Integer> biggestSeries = new HashSet<Integer>();
        Set<Integer> currentSeries = new HashSet<Integer>();
        double prevNumber = Math.pow(10,9) + 1;
        for(int num: nums){
            if(prevNumber == num)continue;
            if(prevNumber == Math.pow(10,9) + 1) {
                currentSeries.add(num);
                biggestSeries.add(num);
                prevNumber = num;
                continue;
            };
            System.out.println(num-prevNumber);    
            currentSeries.add(num);
            currentSeries.add((int)prevNumber);
            if(currentSeries.size()> biggestSeries.size()) biggestSeries = currentSeries;
            if(num-prevNumber != 1){currentSeries = new HashSet <Integer>();
                biggestSeries.remove(num);
                }
            prevNumber = num;
        }
        System.out.println(biggestSeries.toString());
        return biggestSeries.size();
    }
}
