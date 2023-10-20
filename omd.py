class CountVectorizer:
    def __init__(self):
        self.vocab = {}
        self.feature_names = []

    def fit_transform(self, documents):
        """Подсчет частоты каждого слова в документах"""
        # строим словарь
        for document in documents:
            words = document.split()
            for word in words:
                if word not in self.vocab:
                    self.vocab[word] = len(self.vocab)

        # Создаем матрицу счетчиков слов
        matrix = []
        for document in documents:
            word_count = [0] * len(self.vocab)
            words = document.split()
            for word in words:
                word_count[self.vocab[word]] += 1
            matrix.append(word_count)

        return matrix

    def get_feature_names(self):
        """Получаем слова в порядке их появления в словаре"""
        self.feature_names = [word for word, _ in self.vocab.items()]
        return self.feature_names


if __name__ == '__main__':
    # Пример использования CountVectorizer
    documents = ["""Crock Pot Pasta
                    Never boil pasta again""",
                 """Pasta Pomodoro
                    Fresh ingredients Parmesan to taste"""]
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(documents)
    feature_names = vectorizer.get_feature_names()

    # Выводим матрицу счетчиков слов
    print("Матрица счетчиков слов:")
    for row in matrix:
        print(row)

    # Выводим слова
    print("Слова:")
    print(feature_names)

