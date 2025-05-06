def calculate_checksum(file_path):
    checksum = 0
    with open(file_path, 'r') as file:
        for line in file:
            numbers = [int(num) for num in line.split()]
            max_value = max(numbers)
            min_value = min(numbers)
            checksum += max_value - min_value
    return checksum

def main():
    file_path = 'day02.txt'  
    result = calculate_checksum(file_path)
    print(result)

if __name__ == "__main__":
    main()
