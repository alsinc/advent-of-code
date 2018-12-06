#include <stdio.h>


int main(int argc, char** argv)
{
	long freq = 0;
	long res = 0;
	int n;

	do	{
		n = scanf("%ld\n", &freq);
		if (n > 0) res = res + freq;
	} while (n >= 0);
	printf("Resulting frequency: %ld\n", res);

	return 0;
}

