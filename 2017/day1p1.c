#include <ctype.h>
#include <stdio.h>

int main(int argc, char** argv)
{
	int ch, last_ch = -1, first_ch = 0;
	int total = 0;

	while ((ch = getchar()) != EOF) {
		if (isdigit(ch)) {
			if (ch == last_ch) {
				total = total + (ch - '0');
			}
			if (!first_ch) first_ch = ch;

			last_ch = ch;
		}
	}

	if (last_ch == first_ch) total += (last_ch - '0');

	printf("Total: %d\n", total);

	return 0;
}
