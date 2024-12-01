left_array = []
right_array = []

def read_input(filename='entry.txt'):
    with open(filename) as file:
        left, right = zip(*[map(int, line.split()) for line in file])
        
    return sorted(left), sorted(right)

if __name__ == '__main__':
    left_array, right_array = read_input()
    
    if len(left_array) != len(right_array):
        raise ValueError("Arrays must have the same length")
    
    total_distance = sum(abs(left - right) for left, right in zip(left_array, right_array))
    similarity = sum(val * right_array.count(val) for val in left_array)

    print(f'Distance = {total_distance}')
    print(f'Similarité = {similarity}')