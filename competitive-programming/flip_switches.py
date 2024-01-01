"""
Flip Switches: 
Company: Works
"""

operations = [[1, 4], [2, 6], [1, 6]]
def process_ranges(list_of_ranges):
    result_set = set()
    for start, end in list_of_ranges:
        new_numbers = set(range(start, end + 1))

        result_set.symmetric_difference_update(new_numbers)

    return sum(result_set)

# Example usage:
list_of_ranges = [
    [1, 5],
    [3, 8],
    [7, 10],
]

result = process_ranges(operations)
print(result)