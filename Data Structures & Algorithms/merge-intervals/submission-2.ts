class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    merge(intervals: number[][]): number[][] {
        let res: number[][] = [];
        intervals.sort((a,b) => a[0] - b[0]);

        let curr: number[] = intervals[0]

        for (let i = 0; i < intervals.length; i++){
            if (intervals[i][0] <= curr[1]){
                curr[1] = Math.max(intervals[i][1],curr[1]);
            } else {
                res.push(curr);
                curr = intervals[i];
            }
        }

        res.push(curr)
        return res
    }


}
