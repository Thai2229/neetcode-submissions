class Solution {
    /**
     * @param {number[][]} points
     * @return {number}
     */
    findMinArrowShots(points: number[][]): number {
        points.sort((a,b) => a[0] - b[0]);

        let res = 1;
        let curr = points[0];

        for (let i = 0;i < points.length; i++){
            if (points[i][0] >= curr[0] && points[i][0] <= curr[1]){
                curr[0] = Math.max(curr[0],points[i][0]);
                curr[1] = Math.min(curr[1],points[i][1]);
            } else {
                curr = points[i];
                res += 1
            }
        }

        return res;
    }
}
