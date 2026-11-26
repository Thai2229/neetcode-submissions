class Solution {
    /**
     * @param {number[]} ratings
     * @return {number}
     */
    candy(ratings: number[]): number {
        //O(n) is possible
        //sweep from left and right, intialize everyone to 1 candy

        let candies = new Array(ratings.length).fill(1);

        for (let i = 1; i < ratings.length;i++){
            if (ratings[i] > ratings[i-1]){
                candies[i] = candies[i-1] + 1
            }
        }

        for (let i = ratings.length-2; i >= 0; i--){
            if (ratings[i] > ratings[i+1]){
                candies[i] = Math.max(candies[i], candies[i+1] + 1);
            }
        }

        let res = 0;
        for (const candie of candies){
            res += candie;
        }
        return res


    }
}
