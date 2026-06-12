class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, ArrayList<Integer>> squares = new HashMap<>();
        Map<Integer, ArrayList<Integer>> rows = new HashMap<>();
        Map<Integer, ArrayList<Integer>> cols = new HashMap<>();

        int r = board.length;
        int c = board[0].length;
        for (int i = 0; i < r; i++){
            for (int j = 0; j < c; j++){
                int cur = board[i][j];
                if (cur != '.'){
                    rows.putIfAbsent(i, new ArrayList<>());
                    if (rows.get(i).contains(cur)) return false;
                    rows.get(i).add(cur);

                    cols.putIfAbsent(j, new ArrayList<>());
                    if (cols.get(j).contains(cur)) return false;
                    cols.get(j).add(cur);

                    int squareNum = (i/3) * 3 + (j/3);
                    squares.putIfAbsent(squareNum, new ArrayList<>());
                    if (squares.get(squareNum).contains(cur)) return false;
                    squares.get(squareNum).add(cur);
                }
                
            }
        }
        return true;
    }
}
