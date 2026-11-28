class Solution {
    /**
     * @param {number[][]} triplets
     * @param {number[]} target
     * @return {boolean}
     */
    mergeTriplets(triplets: number[][], target: number[]): boolean {
        //check first if any triplet matches target
        //triplet: (a,b,c) target: (a1,b1,c1)
        //if a > a1 || b > b1 || c > c1 don't merge

        let curr = [-Infinity,-Infinity,-Infinity];
        let a1 = target[0];
        let b2 = target[1];
        let c2 = target[2];

        for (let i = 0; i < triplets.length;i++){
            let a = triplets[i][0];
            let b = triplets[i][1];
            let c = triplets[i][2];
            
            if (a <= a1 && b <= b2 && c <= c2){
                curr = [Math.max(curr[0],a),Math.max(curr[1],b),Math.max(curr[2],c)];
            }

        }


        for (let j = 0; j < curr.length; j++){
            if (curr[j] !== target[j]){
                return false;
            }
        }

        return true;
    }
}
