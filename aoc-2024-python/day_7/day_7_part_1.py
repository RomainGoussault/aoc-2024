def is_valid(target: int, nums: list[int]) -> bool:
    if len(nums) == 1:
        return target == nums[0]

    if is_valid(target, [nums[0] * nums[1]] + nums[2:]):
        return True

    if is_valid(target, [nums[0] + nums[1]] + nums[2:]):
        return True

    return False


with open("input", "r") as file:
    lines = file.readlines()

sum = 0
for line in lines:
    # print(line)
    target_str, nums_str = line.split(":")
    target = int(target_str)

    nums = [int(x) for x in nums_str.rstrip().lstrip().split(" ")]

    # print(target)
    # print(nums)

    is_line_valid = is_valid(target, nums)
    if is_line_valid:
        sum += target
    # print()

print(sum)
