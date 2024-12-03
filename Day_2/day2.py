def read_input(filename='Day_2/input.txt'):
    """
    Reads and processes the input file containing multiple rows of space-separated integers.

    Args:
        filename (str): Path to the input file.

    Returns:
        list: A list of lists, where each inner list contains integers from one line of the file.
    """
    with open(filename, 'r') as file:
        # Read each line, split by spaces, and convert elements to integers
        return [list(map(int, line.split())) for line in file]

def is_safe(report):
    """
    Determines if a report is "safe" based on consecutive differences in values.

    A report is considered safe if all consecutive differences are between:
    - 1 and 3 (inclusive), or
    - -3 and -1 (inclusive).

    Args:
        report (list): A list of integers representing a single report.

    Returns:
        bool: True if the report is safe, False otherwise.
    """
    # Calculate differences between consecutive elements
    differences = [report[i] - report[i - 1] for i in range(1, len(report))]
    # Check if all differences are within safe ranges
    return all(1 <= diff <= 3 for diff in differences) or all(-3 <= diff <= -1 for diff in differences)

def is_safe_with_dampener(report):
    """
    Determines if a report is "safe" with a dampener applied.

    A dampener allows removing exactly one element from the report. A report is considered
    safe with a dampener if:
    - It is safe without removing any elements, or
    - It becomes safe after removing one element.

    Args:
        report (list): A list of integers representing a single report.

    Returns:
        bool: True if the report is safe with the dampener, False otherwise.
    """
    # Check if the report is already safe
    if is_safe(report):
        return True

    # Check if removing any single element makes the report safe
    return any(is_safe(report[:i] + report[i + 1:]) for i in range(len(report)))

if __name__ == '__main__':
    # Read all reports from the input file
    reports = read_input()

    # Part 1: Count the number of safe reports
    safe_reports_part1 = sum(is_safe(report) for report in reports)
    print(f"Safe reports (Partie 1) : {safe_reports_part1}")

    # Part 2: Count the number of safe reports with the dampener
    safe_reports_part2 = sum(is_safe_with_dampener(report) for report in reports)
    print(f"Safe reports (Partie 2) : {safe_reports_part2}")
