def tf_transform(count_matrix:list[list[int]])->list[list[float]]:
    """Подсчет отношения повторений/всего"""
    return [[el/sum(line) for el in line] for line in count_matrix]


if __name__ == '__main__':
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    print(tf_transform(count_matrix))
