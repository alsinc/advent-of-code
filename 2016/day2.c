#include <stdio.h>
#include <string.h>

#define BUFFLEN 4096

char* keypad[3] = {"123", "456", "789"};

int main(int argc, char** argv)
{
        char buffer[BUFFLEN];
        char *c;
        char dir;
        int row = 1, col = 1;
        
        while (fgets(buffer, BUFFLEN, stdin) != NULL) {
                if (buffer[strlen(buffer) - 1] == '\n') {
                        buffer[strlen(buffer) - 1] = '\0';
                }
        
                c = buffer;

                while (dir = *c++) {
                        if (dir == 'U') {
                                if (--row < 0) row = 0;
                        }
                        if (dir == 'D') {
                                if (++row > 2) row = 2;
                        }
                        if (dir == 'L') {
                                if (--col < 0) col = 0;
                        }
                        if (dir == 'R') {
                                if (++col > 2) col = 2;
                        }
                        printf("%c", keypad[row][col]);
                }
                printf("\n");
                
        }
        printf("\n");
        return 0;
}
