class CountVectorizer:
    def __init__(self):
        self.vocab = {}
        self.feature_names = []

    def fit_transform(self, corpus: list[list[str]]) -> list[list[int]]:
        """Подсчет частоты каждого слова в текстах"""
        for text in corpus:
            words = text.lower().split()
            for word in words:
                if word not in self.vocab:
                    self.vocab[word] = len(self.vocab)

        count_matrix = []
        for text in corpus:
            word_count = [0] * len(self.vocab)
            words = text.lower().split()
            for word in words:
                word_count[self.vocab[word]] += 1
            count_matrix.append(word_count)

        return count_matrix

    def get_feature_names(self):
        """Получаем слова в порядке их появления в словаре"""
        self.feature_names = [word for word, _ in self.vocab.items()]
        return self.feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    print([row for row in vectorizer.fit_transform(corpus)])
    print(vectorizer.get_feature_names())
