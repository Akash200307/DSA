// Last updated: 2/3/2026, 9:37:04 PM
class Solution {

public void dfs (int[][] grid1, int[][] grid2, int i, int j){
    if(i<0||j<0||i==m||j==n||grid2[i][j]==0) return;

    if(grid1[i][j]!=grid2[i][j]) isSub=false;

    grid2[i][j]=0;
    dfs(grid1, grid2, i + 1, j);  // Down
        dfs(grid1, grid2, i - 1, j);  // Up
        dfs(grid1, grid2, i, j + 1);  // Right
        dfs(grid1, grid2, i, j - 1);  // Left
}


    public int countSubIslands(int[][] grid1, int[][] grid2) {
        m=grid1.length;
        n=grid1[0].length;
        int count=0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid2[i][j]==1 ){
                    isSub=true;
                    dfs(grid1,grid2,i,j);
                    if(isSub){
                    count++;
                }
                }
                
            }
        }
        return count;
    }
    int m;
    int n;
    boolean isSub;

}