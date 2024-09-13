class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        sint = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {}
        for item in self.file_names:
            new_text = ""
            with open(item, encoding="utf8") as file:
                text = file.read()
                for char in text:
                    if char in sint:
                        char = ""
                        new_text += char
                    elif char == "\n":
                        char = " "
                        new_text += char
                    else:
                        new_text += char
                words = new_text.lower().split()
            all_words[item] = words
        return all_words

    def find(self, word):
        finds = {}
        for name, words in self.get_all_words().items():
            finds[name] = words.index(word.lower()) + 1
        return finds

    def count(self, word):
        finds = {}
        for name, words in self.get_all_words().items():
            finds[name] = words.count(word.lower())
        return finds


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
