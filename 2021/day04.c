#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

struct board
{
	char board[5][5];
	char marked[5][5];
	char won;
	struct board* next;
};

struct input
{
	char numbers[2048];
	struct board* boards;
};

struct input* read_input(void)
{
	struct input* input = NULL;
	struct board* current = NULL;
	char a, b, c, d, e;
	int row = 0;

	input = calloc(1, sizeof(struct input));

	scanf("%s", input->numbers);

	input->boards = calloc(1, sizeof(struct board));
	current = input->boards;
	while (!feof(stdin)) {
		int n = scanf("%hhd %hhd %hhd %hhd %hhd\n", &a, &b, &c, &d, &e);
		if (n == 5) {
			if (row == 5) {
				current->next = calloc(1, sizeof(struct board));
				current = current->next;
				row = 0;
			}

			current->board[row][0] = a;
			current->board[row][1] = b;
			current->board[row][2] = c;
			current->board[row][3] = d;
			current->board[row][4] = e;
			row ++;
		}
	}

	return input;
}

static void dump_board(struct board* b)
{
	printf("-- -- -- -- --\n");
	for (int r = 0; r < 5; r++) {
		for (int c = 0; c < 5; c++) {
			printf("%c%02d ", b->marked[r][c]==1?'X':'O', b->board[r][c]);
		}
		printf("\n");
	}
	printf("-- -- -- -- --\n");
}

static int check_win(struct board* b)
{
	for (int r = 0; r < 5; r++) {
		if (b->marked[r][0] && b->marked[r][1] && b->marked[r][2] &&
			b->marked[r][3] && b->marked[r][4]) {
				return 1;
			}
	}

	for (int c = 0; c < 5; c++) {
		if (b->marked[0][c] && b->marked[1][c] && b->marked[2][c] &&
			b->marked[3][c] && b->marked[4][c]) {
				return 1;
			}
	}
	return 0;
}

static int calc_score(struct board* b, int draw)
{
	int sum = 0;

	for (int r = 0; r < 5; r++) {
		for (int c = 0; c < 5; c++) {
			if (!b->marked[r][c]) {
				sum += b->board[r][c];
			}
		}
	}

	return sum * draw;
}

int main(int argc, char** argv)
{
	struct input* i = read_input();
	struct board* b = i->boards;
	struct board *first_win = NULL, *last_win = NULL;

	char* n = i->numbers;
	char t[10];
	int j;
	int draw, first_win_draw = 0, last_win_draw = 0;

	while (*n) {
		j = 0;
		while (*n >= '0' && *n <= '9') {
			t[j] = *n;
			n++;
			j++;
		}
		t[j] = '\0';
		draw = atoi(t);

		b = i->boards;
		while (b) {
			if (!b->won) {
				for (int row = 0; row < 5; row++) {
					for (int col = 0; col < 5; col++) {
						if (b->board[row][col] == draw) {
							b->marked[row][col] = 1;
							if (check_win(b)) {
								b->won = 1;
								if (!first_win) {
									first_win = b;
									first_win_draw = draw;
								}
								last_win = b;
								last_win_draw = draw;
							}
						}
					}
				}
			}
			b = b->next;
		}
		n++;
	}

	printf("Part 1\n");
	dump_board(first_win);
	printf("Score: %d", calc_score(first_win, first_win_draw));

	printf("\nPart 2\n");
	dump_board(last_win);
	printf("Score: %d\n", calc_score(last_win, last_win_draw));

	return 0;
}


