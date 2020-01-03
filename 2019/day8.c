#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

const int WIDTH = 25;
const int HEIGHT = 6;
const int FRAME_SIZE = WIDTH * HEIGHT;


int main(int argc, char** argv)
{
	char *frame;
	char image[WIDTH][HEIGHT];
	int x, y;
	int histo[10];
	int i;
	int min_zeros = WIDTH * HEIGHT + 1;

	frame = malloc(sizeof(char) * FRAME_SIZE);
	assert(frame);

	for (y = 0; y < HEIGHT; y++) {
		for (x = 0; x < WIDTH; x++) {
			image[x][y] = '2';
		}
	}

	while (fread(frame, sizeof(char) * FRAME_SIZE, 1, stdin)) {
		for (i = 0; i < 10; i++) histo[i] = 0;
		for (y = 0; y < HEIGHT; y++) {
			for (x = 0; x < WIDTH; x++) {
				if (image[x][y] == '2') {
					image[x][y] = frame[y * WIDTH + x];
				}
				histo[frame[y * WIDTH + x] - '0']++;
			}
		}

		if (histo[0] < min_zeros) {
			min_zeros = histo[0];
			printf("%d %d %d %d\n", histo[0], histo[1], histo[2], histo[1] * histo[2]);
		}
	}

	for (y = 0; y < HEIGHT; y++) {
		for (x = 0; x < WIDTH; x++) {
			printf("%c", image[x][y]=='0'?'X':image[x][y]=='1'?'.':' ');
		}
		printf("\n");
	}
	return 0;
}

