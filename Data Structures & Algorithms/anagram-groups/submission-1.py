class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_to_return = []
        list_index_to_skip = []
        for i_w in range(len(strs)):
            wordLHS = strs[i_w]
            list_to_append = []
            for n_w in range(i_w, len(strs)):
                wordRHS = strs[n_w]
                if len(wordLHS) != len(wordRHS) or n_w in list_index_to_skip:
                    continue
                for l in range(len(wordLHS)):
                    if wordLHS[l] not in wordRHS or wordLHS.count(wordLHS[l]) != wordRHS.count(wordLHS[l]):
                        break
                else:
                    list_to_append.append(wordRHS)
                    list_index_to_skip.append(n_w) 
            if list_to_append != []:
                list_to_return.append(list_to_append)
        return list_to_return
                    
