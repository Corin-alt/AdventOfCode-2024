import re

def process_memory(filename='Day_3/input.txt', with_conditions=False):
    """
    Processes a corrupted memory file to calculate the sum of specific operations.

    Args:
        filename (str): Path to the input file containing corrupted memory data. Default is 'Day_3/input.txt'.
        with_conditions (bool): Flag to enable conditional processing. If True, only operations 
                                 between `do()` and `don't()` blocks are considered.

    Returns:
        int: The total sum of valid `mul(x, y)` operations.
    """
    # Open and read the corrupted memory file
    with open(filename, 'r') as file:
        corrupted_memory = file.read()
    
    # Regex patterns to match `mul(x, y)` operations and control tokens (`do()` / `don't()`)
    mul_pattern = re.compile(r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)")
    control_pattern = re.compile(r"(do\(\)|don't\(\))")
    
    if with_conditions:
        # Split the content using control tokens and initialize variables
        tokens = re.split(control_pattern, corrupted_memory)
        is_enabled = True  # Tracks whether operations are currently enabled
        total = 0

        # Process each token
        for token in tokens:
            token = token.strip()
            
            if token == "do()":
                is_enabled = True  # Enable operations
            elif token == "don't()":
                is_enabled = False  # Disable operations
            elif is_enabled:
                # Calculate and add all `mul(x, y)` results in the enabled block
                matches = mul_pattern.findall(token)
                total += sum(int(x) * int(y) for x, y in matches)
    else:
        # If no conditions, sum all `mul(x, y)` operations in the file
        matches = mul_pattern.findall(corrupted_memory)
        total = sum(int(x) * int(y) for x, y in matches)

    return total


if __name__ == '__main__':
    # Part 1: Calculate the total sum of all `mul(x, y)` operations
    result = process_memory()
    print(f"The total sum of results is: {result}")

    # Part 2: Calculate the total sum of `mul(x, y)` operations considering conditions
    result = process_memory(with_conditions=True)
    print(f"The total sum of enabled results is: {result}")
