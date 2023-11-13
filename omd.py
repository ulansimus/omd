from math import log


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
        return [[el/sum(line) for el in line] for line in count_matrix]

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


if __name__ == '__main__':
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    tfidf = TfidfTransformer()
    print(tfidf.fit_transform(count_matrix))
