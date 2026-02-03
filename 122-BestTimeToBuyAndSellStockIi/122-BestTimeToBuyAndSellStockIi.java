// Last updated: 2/3/2026, 9:42:07 PM
class Solution {
    public int maxProfit(int[] prices) {
        int sum=0;
        int l=0;
        int r=1;
    while(r<prices.length){
        if(prices[l]<prices[r]){
            int profit=prices[r]-prices[l];
            sum=sum+profit;
        }
       l++;
        r++;
    }
    return sum;

    }
}