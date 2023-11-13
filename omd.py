from math import log


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
    print(idf_transform(count_matrix))
