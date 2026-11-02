class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        solution = []

        #heres the code to check if anagram
        def isAnagram(s,t):
            s_count = {}
            t_count = {}

            for char in s:
                if char in s_count:
                    s_count[char] += 1
                else: 
                    s_count[char] = 1
            
            for char in t:
                if char in t_count:
                    t_count[char] += 1
                else: 
                    t_count[char] = 1

            return s_count == t_count

        while len(strs) > 0:

            word_to_compare = strs[0]
            strs.pop(0)
            list_of_anagram = []
            list_of_anagram.append(word_to_compare)

            to_pop = []

            for i in range(len(strs)):
                if isAnagram(word_to_compare,strs[i]):
                    list_of_anagram.append(strs[i])
                    to_pop.append(i)

            for index in reversed(to_pop):
                strs.pop(index)

            solution.append(list_of_anagram)

        return solution