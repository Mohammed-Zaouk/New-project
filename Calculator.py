class Calculator:
    def __init__(self):
        self.memory_sumb = []
        self.memory_subt = []
        self.memory_multy = []
        self.memory_divin = []
        self.memory_expon = []

    def sumb(self, num1, num2):
        """Return the sum of two numbers."""
        re = num1 + num2
        self.memory_sumb.append(re)
        return re
    
    def subtract(self, num1, num2):
        """Return the result of subtracting num2 from num1."""
        re = num1 - num2
        self.memory_subt.append(re)
        return re
    
    def multiply(self, num1, num2):
        """Return the product of two numbers."""
        re = num1 * num2
        self.memory_multy.append(re)
        return re

    def divide(self, num1, num2):
        """Return the result of dividing num1 by num2."""
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        re = num1 / num2
        self.memory_divin.append(re)
        return re

    def exponentiate(self, num1, num2):
        """Return the result of raising num1 to the power of num2."""
        if num2 < 0:
            raise ValueError("Exponent should be a non-negative integer.")
        elif num2 == 0:
            return 1
        else:
        
            result = 1
            for _ in range(num2):
                result *= num1
            
            self.memory_expon.append(result)
            return result

    def calculate(self, num1, num2, operator):
        """Perform the specified operation on two numbers."""
        if operator == '+':
            return self.sumb(num1, num2)
        elif operator == '-':
            return self.subtract(num1, num2)
        elif operator == '*':
            return self.multiply(num1, num2)
        elif operator == '/':
            return self.divide(num1, num2)
        elif operator == '^':
            return self.exponentiate(num1, num2)
        else:
            raise ValueError("Unknown operator. Choose between '+', '-', '*', '/', '^'.")

    def memory_call(self, operator):
        """Retrieve the memory for a specific operation."""
        if operator == '+':
            return self.memory_sumb
        elif operator == '-':
            return self.memory_subt
        elif operator == '*':
            return self.memory_multy
        elif operator == '/':
            return self.memory_divin
        elif operator == '^':
            return self.memory_expon
        else:
            raise ValueError("Unknown operator. Choose between '+', '-', '*', '/', '^'.")

    def memory_clear(self):
        """Clear all memory."""
        self.memory_sumb = []
        self.memory_subt = []
        self.memory_multy = []
        self.memory_divin = []
        self.memory_expon = []
    
    def free_style(self, operator, Target=None, *args):
        """
        Perform a free-style operation based on the provided operator.

        Parameters:
        - operator (str): The operation to perform ('+', '-', '*', '/').
        - Target (int or None): The target value for division and subtraction.
        - *args: Variable number of arguments for the operation.

        Returns:
        - The result of the operation.
        """
        if operator not in {'+', '-', '*', '/'}:
            raise ValueError("Unknown operator. Choose between '+', '-', '*', or '/'.")

        result = 1 if operator == '*' else 0  # Corrected syntax

        for x in args:
            if operator == '+':
                result += x
            elif operator == '-':
                if Target is not None:
                    Target -= x
                else:

                    # Handle the case where Target is None
                    result -= x
            elif operator == '*':
                result *= x
            elif operator == '/':
                if Target is not None:
                    Target /= x
                else:
                    # Handle the case where Target is None
                    result /= x

        return result if Target is None else Target

    def main(self):
        option = input("Do you want to use the basic calculator(1) or the free_style mode(2)? (1/2): ")

        if option == '1':
            try:
                option1 = int(input("Enter your first number: "))
                option2 = int(input("Enter your second number: "))
                operator = input("What operator do you want to use, (+/-/*/^ or /): ")

                result = self.calculate(option1, option2, operator)
                print("Result:", result)

                memory_operator = input("Enter the operator for memory retrieval: ")
                print(f"Memory for '{memory_operator}':", self.memory_call(memory_operator))

            except ValueError as e:
                print(f"Error: {e}")
        elif option == '2':
            ress = []
            while True:
                option = input("Enter a number or any other key to finish: ")
                if option.isdigit():
                    ress.append(int(option))
                else:
                    break

            Target = input("Enter a number for Target option in division and subtraction, or leave it empty: ")
            if Target.isdigit():
                Target = int(Target)
            else:
                Target = None
            operator = input("What operator do you want to use, (+/-/*/^ or /): ")
            result1 = self.free_style(operator, Target, *ress)
            print("Result:", result1)
        else:
            print("Invalid choice. Please enter 1 or 2.")



if __name__ == '__main__':
    calculator = Calculator()
    
    while True:
        calculator.main()
        res = input("Do you want to use it again? (y/n): ").lower()
        
        if res != "y":
            clear_memory = input("Do you want to clear the memory? (y/n): ").lower()
            if clear_memory == "y":
                calculator.memory_clear()
            break

    print("Have a nice day!")

