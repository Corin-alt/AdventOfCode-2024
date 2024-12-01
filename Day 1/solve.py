left_array = []
right_array = []

def read_input(filename='entry.txt'):
    with open(filename, 'r') as file:
        left_array, right_array = zip(*[
            (int(val_g), int(val_d)) for line in file 
            for val_g, val_d in [line.strip().split()]
        ])
    
    return sorted(left_array), sorted(right_array)

if __name__ == '__main__':
    left_array, right_array = read_input()
    
    if len(left_array) != len(right_array):
        raise ValueError("Arrays must have the same length")
    
    total_distance = sum(abs(left - right) for left, right in zip(left_array, right_array))
    similarity = sum(val * right_array.count(val) for val in left_array)

    print(f'Distance = {total_distance}')
    print(f'Similarité = {similarity}')