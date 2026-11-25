class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        let seen = new Map<number,number>();
        //mapping nums[i] to index

        for (let i = 0; i < nums.length; i++){
            let diff = target - nums[i]
            if (seen.has(diff)){
                return [seen.get(diff), i]
            }
            seen.set(nums[i],i);
        }

    }   
}
