// Last updated: 2/3/2026, 9:45:00 PM
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map1= new Map()
    for (let i =0;i<nums.length;i++){
        let diff=target-nums[i]
         if (map1.has(diff)){
            return [map1.get(diff),i]
        }
        map1.set(nums[i],i)
    }
     return []
};