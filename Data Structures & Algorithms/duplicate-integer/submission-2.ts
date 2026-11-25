class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        let hash = new Map<number, number>();

        for (const num of nums) {
            if (hash.has(num)){
                return true
            }
            hash.set(num, (hash.get(5) ?? 0) + 1);
        }

        return false
        
    }
}
