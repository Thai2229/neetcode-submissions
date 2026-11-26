class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    canJump(nums: number[]): boolean {
        //core logic, take the one with max reach
        let reach = nums[0];
        
        for (let i = 0; i < nums.length; i++){
            if (i <= reach && i+nums[i] > reach){
                reach = i + nums[i]
            }
        }

        return reach >= nums.length-1;
    }
}
