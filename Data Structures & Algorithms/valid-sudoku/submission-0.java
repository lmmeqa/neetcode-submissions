class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean uniqueRow = false;
        boolean uniqueColumn = false;
        boolean uniqueSubBox = false;
        Set<Character>[] columns = (Set<Character>[]) new HashSet[9];

        for (int i = 0; i < 9; i++) {
            columns[i] = new HashSet<>();
        }
        
        int rowNum = 0;
        Set<Character>[] squares = (Set<Character>[]) new HashSet[3];

        for (int i = 0; i < 3; i++) {
            squares[i] = new HashSet<>();
        }
        for(char[] row : board){
            if(rowNum%3 == 0){
                for (int i = 0; i < 3; i++) {
            squares[i] = new HashSet<>();
        }
            }
            Set<Character> currRow = new HashSet<Character>();
            int digitNum = 0;
            for(char digit: row){
                if(digit == '.') {
                    digitNum++;
                    continue;
                    }
                if(!squares[Math.floorDiv(digitNum,3)].add(digit)) return false;
                if(!currRow.add(digit)) return false;
                if(!columns[digitNum].add(digit)) return false;
                digitNum++;
            }
            rowNum++;
        }
        return true;
    }
}
