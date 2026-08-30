/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let n=nums.length;
    let max=(n*(n+1))/2
    let sum=0;

    for(let i of nums){
        sum+=i
    }
    return max-sum
    

};