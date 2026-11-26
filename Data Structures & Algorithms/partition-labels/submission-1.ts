class Solution {
    /**
     * @param {string} S
     * @return {number[]}
     */
    partitionLabels(S: string): number[] {
        //logic: keep track of last seen index for each character

        let seen = new Map<string,number>();
        let res = [];

        for (let i = 0; i < S.length; i++){
            seen.set(S[i],i);
        }

        let size = 0;
        let last = 0;

        for (let j = 0; j < S.length; j++){
            last = Math.max(seen.get(S[j]),last);
            size += 1;
            if (j == last){
                res.push(size);
                size = 0;
            }
        }

        return res
    }
}
