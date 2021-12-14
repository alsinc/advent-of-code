#include <stdio.h>
#define SIZE 1000

typedef int tcounts [SIZE][SIZE];

static void zero_counts(tcounts counts)
{
	for (int x = 0; x < SIZE; x++) {
		for (int y = 0; y < SIZE; y++) {
			counts[x][y] = 0;
		}
	}
}

static void do_vert(tcounts c, int x, int y1, int y2)
{
	int t;

	if (y1 > y2) {
		t = y2;
		y2 = y1;
		y1 = t;
	}

	for (int y = y1; y <= y2; y++) {
		c[x][y]++;
	}
}

static void do_horiz(tcounts c, int x1, int x2, int y)
{
	int t;

	if (x1 > x2) {
		t = x2;
		x2 = x1;
		x1 = t;
	}

	for (int x = x1; x <= x2; x++) {
		c[x][y]++;
	}
}

static void do_diag(tcounts c, int x1, int y1, int x2, int y2)
{
	int t, y, yd;

	if (x1 > x2) {
		t = x2;
		x2 = x1;
		x1 = t;

		t = y2;
		y2 = y1;
		y1 = t;
	}

	y = y1;
	yd = (y1 > y2)?-1:1;

	for (int x = x1; x <= x2; x++) {
		c[x][y]++;
		y += yd;
	}
}

int main(int argc, char** argv)
{
	short int x1, y1, x2, y2;
	int overlaps = 0;
	int n;
	int part2 = 0;
	tcounts counts;

	if (argc == 2 && argv[1][0] == '2') {
		part2 = 1;
	}

	zero_counts(counts);

	while (!feof(stdin)) {
		n = scanf("%hd,%hd -> %hd,%hd", &x1, &y1, &x2, &y2);
		if (n == 4) {
			if (x1 == x2){
				do_vert(counts, x1, y1, y2);
			} else if (y1 == y2){
				do_horiz(counts, x1, x2, y1);
			} else {
				if (part2) {
					do_diag(counts, x1, y1, x2, y2);
				}
			}
		}
	}

	for (int x = 0 ; x < SIZE; x++) {
		for (int y = 0 ; y < SIZE; y++) {
			if (counts[x][y] >= 2) {
				overlaps++;
			}
		}
	}

	if (!part2) {
		printf("overlaps (part1): %d\n", overlaps);
	} else {
		printf("overlaps (part2): %d\n", overlaps);
	}

	return 0;
}

