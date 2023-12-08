#include <ctype.h>
#include <stdio.h>

static unsigned char list[4096];
static int entries = 0;

static void read_data(void)
{
	int ch;

	while ((ch = getchar()) != EOF) {
		if (isdigit(ch))
			list[entries++] = (ch - '0');
	}

}

int main(int argc, char** argv)
{
	int total = 0, i;

	read_data();
	printf("no of entries: %d\n", entries);

	for (i = 0; i < entries; i++) {
			if (list[i] == list[(i + entries/2)%entries])
				total += list[i];
	}


	printf("Total: %d\n", total);

	return 0;
}
