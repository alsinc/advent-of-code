#include <stdio.h>

int main(int argc, char** argv)
{       
        int a, b, c;
        while (!feof(stdin)) {
                scanf("%d %d %d\n", &a, &b, &c);

                if ((a<(b+c)) && (b<(a+c)) && (c<(a+b))) {
                        printf("GOOD: %d %d %d\n", a, b, c);
                } else {
                        printf("BAD: %d %d %d\n", a, b, c);
                }
        }
        return 0;
}