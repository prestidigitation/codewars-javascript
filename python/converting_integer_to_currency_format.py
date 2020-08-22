# Write a function that takes an integer in input and outputs a string with currency format.
# Integer in currency format is expressed by a string of number where every three characters are separated by comma.
# For example:
# 123456 --> "123,456"
# Input will always be an positive integer, so don't worry about type checking or negative/float values.Naive

# naive implementation
def to_currency(price):
    nums = str(price)
    new_string = ''
    for i, num in enumerate(nums):
        if (len(nums) - i) % 3 == 0 and i != 0:
            new_string += ','
        new_string += num
    return new_string
