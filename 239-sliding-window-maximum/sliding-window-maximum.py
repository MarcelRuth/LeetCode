class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # time limit reached
        # max_pool = []
        # if len(nums) > k:
        #     for i in range(k, len(nums)+1):
        #         window = nums[i-k:i]
        #         max_pool.append(max(window))
        #     return max_pool
        # else:
        #     return [max(nums)]

        # time limit reached as well
        # # deque approach
        # window = deque(maxlen=k)
        # max_pool = []
        # # first k - 1 elements into deque
        # for x in nums[:k-1]:
        #     window.append(x)
        # # now the next and then compute the max
        # for x in nums[k-1:]:
        #     window.append(x)
        #     # fill up till first k elements are in
        #     max_pool.append(max(window))
        # return max_pool

        # indexing deque

        if k == 1:
            return nums
        window = deque()
        max_pool = []

        for i in range(len(nums)):
            # as long as the index in window position 0 is smaller than window left boundry:
            while window and window[0] < i - k + 1:
                # remove left 
                window.popleft()
            # as long as the number of index i is greater than the number that is currently at first window position:
            # this means the window at all times only contains one elemnt
            while window and nums[i] > nums[window[-1]]:
                # remove right
                window.pop()
            # append index
            window.append(i)
            # wait till first window as build up
            if i >= k - 1:
                max_pool.append(nums[window[0]])

        return max_pool