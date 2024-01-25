class Palindrome:
    def __init__(self, data):
        self.data = data
        self.palindrome = {}

    def Palindrome_Checker(self):
        for data in self.data.split():
            if data[::-1] == data:
                self.palindrome[data] = "The entered phrase is a palindrome!"
            else:
                self.palindrome[data] = "The entered phrase is not a palindrome."

    def main(self):
        self.Palindrome_Checker()
        for n, (key, val) in enumerate(self.palindrome.items(), start=1):
            print(f"{n}. {key} : {val}" )


if __name__ == "__main__":
    game = Palindrome("Here is where you can find me, meem")
    game.main()