import string

class Word_Frequency_Counter:
    def __init__(self, data):
        self.data = data

    def counter(self):
        result = {}
        translation_table = str.maketrans("", "", string.punctuation)

        for word in self.data.split():
            # Remove punctuation from each word
            word = word.translate(translation_table).lower()
            if word in result:
                result[word] += 1
            else:
                result[word] = 1

        return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

if __name__ == "__main__":
    text = "Yes, your code is sufficient to pass the exercise. It meets the main requirements of counting the frequency of words in the given text, handling punctuation, and displaying the results in descending order of frequency. The implementation is clear and functional. It's always a good practice to consider potential improvements and additional features, but those are often optional and depend on the specific goals of the exercise. Your code successfully addresses the core requirements. If you're interested in further challenges, you might consider adding optional features like ignoring common stop words, handling contractions differently, or providing more interactive user input. However, these enhancements are not necessary for the basic functionality of the word frequency counter. Keep up the good work, and feel free to explore more coding exercises to continue improving your skills!"
    word_counter = Word_Frequency_Counter(text)
    result = word_counter.counter()
    for n, (key, val) in enumerate(result.items(), start=1):
        print(f"{n}. {key} - {val}")
