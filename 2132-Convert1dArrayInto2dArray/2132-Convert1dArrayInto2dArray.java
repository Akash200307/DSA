// Last updated: 2/3/2026, 9:36:53 PM
class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        int [][] arr=new int[m][n];
        if(m*n!=original.length){
            return new int[0][0];
        }
        for(int i=0;i<m*n;i++){
            arr[i/n][i%n]=original[i];
        }    
        return arr;
        }
    }
