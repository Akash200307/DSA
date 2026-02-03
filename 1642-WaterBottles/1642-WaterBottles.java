// Last updated: 2/3/2026, 9:37:24 PM
class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int n=numBottles;
        int k=numExchange;

        return n+(n-1)/(k-1);
    }
}