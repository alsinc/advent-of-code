#include <stdio.h>
#include <stdlib.h>

static char** read_map(int *num_rows, int* num_cols)
{
	char *line = NULL;
	size_t line_len = 0;
	ssize_t read;
	int max_rows = 100;
	char** map;
	int rows = 0;
	int cols = 0;

	map = malloc(max_rows * sizeof(char*));

	while (!feof(stdin)) {
		read = getline(&line, &line_len, stdin);
		if (read > 0) {
			if (cols == 0) cols = read - 1;
			map[rows] = line;
			line = NULL;
			rows++;

			if (rows > (max_rows - 1)) {
				max_rows *= 2;
				map = realloc(map, max_rows * sizeof(char*));
			}
		}
		*num_rows = rows;
		*num_cols = cols;
	}
	return map;
}

static int count_trees(char** map, int rows, int cols, int dr, int dc)
{
	const char TREE = '#';
	int row = 0, col = 0;
	int trees = 0;

	while (1 == 1) {
		row += dr;
		col += dc;

		if (col > (cols - 1))
			col = col % cols;

		if (row > (rows - 1)) {
			return trees;
		}

		if (map[row][col] == TREE) trees++;
	}
	return 0;
}

int main(int argc, char** argv)
{
	int rows = 0, cols = 0;
	char** map;
	int count11, count31, count51, count71, count12;

	map = read_map(&rows, &cols);

	count11 = count_trees(map, rows, cols, 1, 1);
	count31 = count_trees(map, rows, cols, 1, 3);
	count51 = count_trees(map, rows, cols, 1, 5);
	count71 = count_trees(map, rows, cols, 1, 7);
	count12 = count_trees(map, rows, cols, 2, 1);

	printf("Part1: %d trees\n", count31);
	printf("Part 2: %d * %d * %d * %d * %d\n", count11, count31, count51, count71, count12);
	printf("Part 2: Result = %ld\n", (long)count11 * count31 * count51 * count71 * count12);

	return 0;
}
