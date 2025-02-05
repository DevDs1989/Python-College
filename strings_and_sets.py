def count_capital_letters(input_string):
  count = sum(1 for char in input_string if char.isupper())
  return count

# Example usage
input_string = "Hello World! This is a Test String."
capital_letters_count = count_capital_letters(input_string)
print(f"Number of capital letters: {capital_letters_count}")

