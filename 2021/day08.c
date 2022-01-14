#include <stdio.h>
#include <string.h>

int main(int argc, char** argv)
{
	char digit[8];
	int read;
	int len;
	int day1_count = 0;

	while (!feof(stdin)) {
		for (int i = 0; i < 10; i++) {
			if (scanf("%s", &digit) == 1) {
				//printf("%s\n", digit);
			} else {
				fprintf(stderr, "Scan error expected a string\n");
				return 2;
			}
		}

		while ((read = fgetc(stdin)) == ' '){}

		if (read != '|') {
			fprintf(stderr, "OOPS, parse error expected '|' got '%c'\n", read);
			return 1;
		}

		for (int i = 0; i < 4; i++) {
			scanf("%s", &digit);
			//printf("%s\n", digit);
			len = strlen(digit);

			if (len == 2 || len == 3 || len == 4 || len == 7) day1_count++;
		}

		while ((read = fgetc(stdin)) == '\n'){}
	}
	printf("Part1: %d\n", day1_count);
	return 0;
}
