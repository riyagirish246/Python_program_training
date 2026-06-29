class intToRomanConvertor:
    def int_to_Roman(self, num: int) -> str:
        val_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        roman_num = ""
        for value, symbol in val_map:
            while num >= value:
                roman_num += symbol
                num -= value
                
        return roman_num

if __name__ == "__main__":
    converter = intToRomanConvertor()
    print("--- Integer to Roman Numeral Converter ---")
    print("Type 'exit' to quit the program.\n")

    while True:
        user_input = input("Enter an integer: ").strip()
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
            
        try:
            number = int(user_input)
            if number <= 0:
                print("Please enter a positive integer greater than 0.\n")
                continue
                
            result = converter.int_to_Roman(number)
            print(f"Roman Numeral: {result}\n")
            
        except ValueError:
            print("Invalid input. Please enter a valid whole number.\n")


