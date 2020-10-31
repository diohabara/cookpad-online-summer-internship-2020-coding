import unittest

def check_duplicate(filename: str) -> str:
    matrix = get_matrix_from_file(filename)
    rows = [ set() for _ in range(len(matrix))]
    columns = [ set() for _ in range(len(matrix[0]))]
    # for row in O(n^2) in both space and time complexity
    for row, used_row in zip(matrix, rows):
        for ele in row:
            if ele in used_row:
                return "invalid"
            else:
                used_row.add(ele)

    # for column in O(n^2) in both space and time complexity
    for y in range(len(matrix)):
        used_column = columns[y]
        for x in range(len(matrix[0])):
            if matrix[y][x] in used_column:
                return "invalid"
            else:
                used_column.add(matrix[y][x])

    return "valid"



def get_matrix_from_file(filename: str) -> list[list[int]]:
    matrix = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            matrix.append(list(map(int, line.rstrip().split(' '))))
    return matrix


class TestQuestion1(unittest.TestCase):
    def test_get_matrix_fromfile(self):
        filename = 'q1.txt'
        expected = [[1, 2, 3],
                    [2, 3, 1],
                    [3, 1, 2]]
        achieved = get_matrix_from_file(filename)
        self.assertEqual(expected, achieved)

    def test_check_duplicate(self):
        filename = 'q1.txt'
        expected = 'valid'
        achieved = check_duplicate(filename)
        self.assertEqual(expected, achieved)

if __name__ == '__main__':
    unittest.main()
