class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def convert(num:str) -> int:
            digit = 1
            number = 0
            for n in num[::-1]:
                if n == "1":
                    number += digit * 1
                elif n == "2":
                    number += digit * 2
                elif n == "3":
                    number += digit * 3
                elif n == "4":
                    number += digit * 4
                elif n == "5":
                    number += digit * 5
                elif n == "6":
                    number += digit * 6
                elif n == "7":
                    number += digit * 7
                elif n == "8":
                    number += digit * 8
                elif n == "9":
                    number += digit * 9
                digit *= 10
            return number
            
        return str(convert(num1) * convert(num2))
