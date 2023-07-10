def find_missing_number(numbers):
    if numbers[0] != 1:
        return 1
    for i in range(len(numbers) - 1):
        if numbers[i] + 1 != numbers[i+1]:
            return numbers[i] + 1
    return -1