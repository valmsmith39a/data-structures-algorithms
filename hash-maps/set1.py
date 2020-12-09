

def twoSum(self, nums: List[int], target: int) -> List[int]):
    hm={}
    for i, num in enumerate(nums):
        r=target - num
        if r not in hm:
            hm[num]=i
        else:
            return [i, hm[r]]
