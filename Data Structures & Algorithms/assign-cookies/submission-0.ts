class Solution {
    /**
     * @param {number[]} g
     * @param {number[]} s
     * @return {number}
     */
    findContentChildren(g: number[], s: number[]): number {
        //sort both arrays, mantain two pointers

        let child = 0;
        let cookie = 0;
        let res = 0;

        g.sort((a,b) => a - b);
        s.sort((a,b) => a - b);

        //stop when no cookies or children left
        while (child < g.length && cookie < s.length){
            if (s[cookie] >= g[child]){
                child += 1;
                cookie += 1;
                res += 1;
            } else {
                cookie += 1;
            }
        }

        return res
    }
}
