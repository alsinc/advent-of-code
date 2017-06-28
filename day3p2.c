#include <stdio.h>

static void check(int a, int b, int c)
{
        if ((a<(b+c)) && (b<(a+c)) && (c<(a+b))) {
                printf("GOOD: %d %d %d\n", a, b, c);
        } else {
                printf("BAD: %d %d %d\n", a, b, c);
        }
}

int main(int argc, char** argv)
{       
        int a, b, c;
        int d, e, f;
        int g, h, i;
        while (!feof(stdin)) {
                if (scanf("%d %d %d\n%d %d %d\n%d %d %d\n", &a, &b, &c, &d, &e, &f, &g, &h, &i) != 9) {
                        perror("Failed to read 18 items");
                        return 1;
                }

                check(a, d, g);
                check(b, e, h);
                check(c, f, i);
        }
        return 0;
}