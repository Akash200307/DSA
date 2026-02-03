// Last updated: 2/3/2026, 9:36:17 PM
class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        int ans=numBottles;
        int e=numBottles;

        while(e>=numExchange){
            e-=numExchange;
            ans++;
            e++;
            numExchange++;
        }
        return ans;
    }
};