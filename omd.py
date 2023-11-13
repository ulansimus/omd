from math import log


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


class TfidfTransformer:
    def __init__(self):
        pass

    def fit_transform(self, count_matrix: list[list[int]]) -> list[list[float]]:
        """Подсчет tf*idf"""
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        res = []
        for row in tf:
            res.append([a * b for a, b in zip(row, idf)])
        return res

    @staticmethod
    def tf_transform(count_matrix: list[list[int]]) -> list[list[float]]:
        """Подсчет отношения повторений/всего"""
        return [[el / sum(line) for el in line] for line in count_matrix]

    @staticmethod
    def idf_transform(count_matrix: list[list[int]]) -> list[float]:
        """Подсчет ln((всего текстов+1)/(документов со словом+1))+1"""
        word_in_docs = [0] * len(count_matrix[0])
        for line in count_matrix:
            for idx, el in enumerate(line):
                if el > 0:
                    word_in_docs[idx] += 1
        text_count = len(count_matrix)
        return [log((text_count + 1) / (num + 1)) + 1 for num in word_in_docs]


class TfidfVectorizer(CountVectorizer):
    def __init__(self, tf_class=TfidfTransformer):
        super().__init__()
        self.transformer = tf_class()

    def fit_transform(self, corpus: list[list[str]]) -> list[list[float]]:
        count_matrix_numbers = super().fit_transform(corpus)
        return self.transformer.fit_transform(count_matrix_numbers)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
