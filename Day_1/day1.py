left_array = []
right_array = []

def read_input(filename='Day_1/input.txt'):
    """
    Reads and processes the input file to extract and sort two arrays of integers.

    Args:
        filename (str): Path to the input file containing two space-separated columns of integers.

    Returns:
        tuple: Two sorted lists of integers (`left_array` and `right_array`).
    """
    # Open the input file and read the data
    with open(filename) as file:
        # Split each line into two integers and store them in separate lists
        left, right = zip(*[map(int, line.split()) for line in file])
    
    # Return the sorted lists
    return sorted(left), sorted(right)

if __name__ == '__main__':
    # Read and process input to get the two sorted arrays
    left_array, right_array = read_input()
    
    # Ensure both arrays have the same length
    if len(left_array) != len(right_array):
        raise ValueError("Arrays must have the same length")
    
    # Calculate the total distance (sum of absolute differences between corresponding elements)
    total_distance = sum(abs(left - right) for left, right in zip(left_array, right_array))
    
    # Calculate the similarity metric (sum of matching values, weighted by their occurrences)
    similarity = sum(val * right_array.count(val) for val in left_array)

    # Output the results
    print(f'Distance = {total_distance}')
    print(f'Similarity = {similarity}')
