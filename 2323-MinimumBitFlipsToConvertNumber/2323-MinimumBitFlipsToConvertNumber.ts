// Last updated: 2/3/2026, 9:36:47 PM
function minBitFlips(start: number, goal: number): number {
   let ans:number=0
   let xor:number=start^goal

    while(xor!=0){
        ans+=xor&1;

        xor>>=1;
    }
    return ans;
    
};