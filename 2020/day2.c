#include <stdio.h>

int main(int argc, char** argv)
{
	int min_pass, max_pass;
	char ch;
	char password[200], *p;
	int count, len;
	int part1 = 0, part2 = 0;


	while (!feof(stdin)) {
		scanf("%d-%d %c: %s\n", &min_pass, &max_pass, &ch, password);

		count = len = 0;
		for (p = password; *p; p++) {
			if (*p == ch) count++;
			len++;
		}

		if (count >= min_pass && count <= max_pass) {
			part1++;
		}

		if ((password[min_pass - 1] == ch || password[max_pass - 1] == ch) && password[min_pass - 1] != password[max_pass - 1]) {
			part2++;
		}
	}

	printf("Part 1: %d\nPart 2: %d\n", part1, part2);
	return 0;
}

