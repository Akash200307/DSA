// Last updated: 2/3/2026, 9:37:34 PM
import java.util.*;
class Solution {
    public double average(int[] salary) {
        Arrays.sort(salary);
    
        double total=0;
        int count=0;
        for(int i=1;i<salary.length-1;i++){
            total+=salary[i];
            count++;
        }return total/count;
    }
}