class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        if len(trust) == 0:
            if n == 1:
                return 1
            return -1

        n_arr = list(range(1, n+1))
        has_trust = {}
        trusts = set()

        # first person trusts
        for t in trust:
            if t[1] not in has_trust:
                has_trust[t[1]] = 1 
            else:
                has_trust[t[1]] += 1 
            if t[0] not in trusts:
                trusts.add(t[0])
                n_arr.remove(t[0])

        # town judge has to have trust of all people except himself
        if len(n_arr) != 0:
            if has_trust[n_arr[0]] == n - 1:
                return n_arr[0]
        return -1
