left_array = []
right_array = []

def read_input(filename='entry.txt'):
    with open(filename, 'r') as file:
        left_array, right_array = zip(*[
            (int(val_g), int(val_d)) for line in file 
            for val_g, val_d in [line.strip().split()]
        ])
    
    return sorted(left_array), sorted(right_array)

def calculate_total_distance(left_array, right_array):
    if len(left_array) != len(right_array):
        raise ValueError("Arrays must have the same length")
    
    return sum(abs(left - right) for left, right in zip(left_array, right_array))


def calculate_similarity(left_array, right_array):
    if len(left_array) != len(right_array):
        raise ValueError("Arrays must have the same length")

    return sum(val * right_array.count(val) for val in left_array)


def main():
    left_array, right_array = read_input()
    total_distance = calculate_total_distance(left_array, right_array)
    similarity = calculate_similarity(left_array, right_array)

    print(f'Distance = {total_distance}')
    print(f'Similarité = {similarity}')

if __name__ == '__main__':
    main()