#include <stdio.h>

int main(int argc, char** argv)
{
	int depth, last_depth;
	int count = 0;
	int increases = 0;
	int increases3 = 0;
	int window[3];
	int sum3, last_sum3 = -1;

	while (!feof(stdin)) {
		scanf("%d\n", &depth);
		window[0] = window[1];
		window[1] = window[2];
		window[2] = depth;

		if (count) {
			if (depth > last_depth) {
				increases++;
			}
			count++;

			if (count >= 3) {
				sum3 = window[0] + window[1] + window[2];

				if (last_sum3 != -1 && sum3 > last_sum3) {
					increases3++;
				}
				last_sum3 = sum3;
			}
		} else {
			count = 1;
		}

		last_depth = depth;
	}
	printf("increases: %d\n", increases);
	printf("Moving window(3) increases: %d\n", increases3);

	return 0;
}

