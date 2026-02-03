// Last updated: 2/3/2026, 9:43:09 PM
class Solution {
    public void setZeroes(int[][] matrix) {
        int rows=matrix.length;
        int cols=matrix[0].length;
        boolean row=false;
        boolean col=false;

        for(int i=0;i<rows;i++){
            if(matrix[i][0]==0){
                col=true;
            }
        }
        for(int j=0;j<cols;j++){
            if(matrix[0][j]==0){
                row=true;
            }
        }
        for(int i=1;i<rows;i++){
            for(int j=1;j<cols;j++){
                if(matrix[i][j]==0){
                    matrix[0][j]=0;
                    matrix[i][0]=0;
                }
            }
        }
        for(int i=1;i<rows;i++){
            if(matrix[i][0]==0){
                for(int j=1;j<cols;j++){
                    matrix[i][j]=0;
                }
            }
        }
        for(int j=1;j<cols;j++){
            if(matrix[0][j]==0){
                for(int i=1;i<rows;i++){
                    matrix[i][j]=0;
                }
            }
        }
        if(row){
            for(int j=0;j<cols;j++){
                matrix[0][j]=0;
            }
        }
        if(col){
            for(int i=0;i<rows;i++){
                matrix[i][0]=0;
            }
        }


       
    }
}