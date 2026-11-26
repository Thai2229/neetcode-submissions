class Solution {
    /**
     * @param {number[][]} intervals
     * @param {number[]} newInterval
     * @return {number[][]}
     */
    insert(intervals: number[][], newInterval: number[]): number[][] {
        let res: number[][] = [];

        for (let i = 0; i < intervals.length; i++){
            if (newInterval[0] > intervals[i][1]){
                res.push(intervals[i]);
            } else if (newInterval[0] <= intervals[i][1] &&
           newInterval[1] >= intervals[i][0]){
                newInterval[1] = Math.max(intervals[i][1],newInterval[1]);
                newInterval[0] = Math.min(intervals[i][0],newInterval[0]);
            } else {
                res.push(newInterval)
                return res.concat(intervals.slice(i)); 
            }
        }
        
        res.push(newInterval)
        return res

    }
}
