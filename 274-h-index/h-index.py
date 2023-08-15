class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # intuitive approach
        #hIndex_val = 0
        #for i in range(1, max(citations) + 1):
        #    minHindex = [x for x in citations if x >= i]
        #    if len(minHindex) >= i:
        #        hIndex_val = i
        #return hIndex_val

        # sorting approach

        citations.sort(reverse=True)

        if len(citations) == 1 and citations[0] > 0:
            # only one citation, can't be more than 1
            return 1
        # if smallest number of citations is greater
        # than the number of publications, then the
        # hIndex is equal to the number of publications
        if citations[-1] >= len(citations):
            return len(citations)
        
        # if this all is not the case, then we have to find 
        # the h index by going from the largest to the smallest
        # citations

        for i in range(len(citations)):
            # less citations than counter + 1
            # + 1 because the number of citations have to be
            # greater or equal to the number of publications
            # having this stat
            if citations[i] < i + 1:
                return i

        # never lucky 
        return 0
                