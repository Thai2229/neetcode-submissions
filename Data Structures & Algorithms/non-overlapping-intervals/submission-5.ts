class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number}
     */
    eraseOverlapIntervals(intervals: number[][]): number {
        //sort by start, store highest ending, greedily choose least end
        intervals.sort((a,b) => a[0] - b[0]);
        
        let res = 0;
        let curr: number[] = intervals[0];

        for (let i = 1; i < intervals.length;i++){
            if (intervals[i][0] < curr[1]){
                res += 1;
                if (intervals[i][1] < curr[1]){
                    curr = intervals[i];
                }
            } else {
                curr = intervals[i];
            }
        }
        

        return res 
    }
}
