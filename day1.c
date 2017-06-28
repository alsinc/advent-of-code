#include <stdio.h>
#include <ctype.h>

int main(int argc, char** argv)
{
    char c;
    int directions[4][2] = {{0, 1}, {1,0}, {0, -1}, {-1, 0}};
    int current_dir = 0;
    int current_x = 0, current_y = 0;
    
    int d = 0;
    
    while ((c = getchar()) != EOF) {
            if (c == 'L') {
                current_dir = current_dir - 1;

                if (current_dir == -1) {
                        current_dir = 3;
                }
            } else if (c == 'R') {
                current_dir = current_dir + 1;

                if (current_dir == 4) {
                        current_dir = 0;
                }            
            } else if (isdigit(c)) {
                d = d * 10 + (c - '0');
            } else {
                current_x += directions[current_dir][0] * d;
                current_y += directions[current_dir][1] * d;
                d = 0;
                printf("%d, %d\n", current_x, current_y);
            }
    }
    return 0;
}