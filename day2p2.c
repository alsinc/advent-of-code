#include <stdio.h>
#include <string.h>

#define BUFFLEN 4096

char* keypad[5] = {"XX1XX", "X234X", "56789", "XABCX", "XXDXX"};

int main(int argc, char** argv)
{
        char buffer[BUFFLEN];
        char *c;
        char dir;
        int row = 2, col = 0, old_row, old_col;
        
        while (fgets(buffer, BUFFLEN, stdin) != NULL) {
                if (buffer[strlen(buffer) - 1] == '\n') {
                        buffer[strlen(buffer) - 1] = '\0';
                }
        
                c = buffer;

                while (dir = *c++) {
                        old_row = row;
                        old_col = col;
                        
                        if (dir == 'U') {
                                --row;
                        }
                        if (dir == 'D') {
                                ++row;
                        }
                        if (dir == 'L') {
                                --col;
                        }
                        if (dir == 'R') {
                                ++col;
                        }
                        
                        if ((row < 0) || (row > 4) || (col < 0) || (col > 4) || keypad[row][col] == 'X') {
                                row = old_row;
                                col = old_col;
                        }
                }
                printf("%c", keypad[row][col]);
                
        }
        printf("\n");
        return 0;
}
