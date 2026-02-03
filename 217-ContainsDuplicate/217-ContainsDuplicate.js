// Last updated: 2/3/2026, 9:40:23 PM
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const set=new Set();
    for (const i of nums){
        if (set.has(i)){
            return true
        }
        set.add(i)
    }
    return false
};