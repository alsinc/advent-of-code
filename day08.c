#include <stdio.h>
#include <string.h>

#define BUFFLEN 4095
#define SCREEN_WIDTH 50
#define SCREEN_HEIGHT 6

static char screen[SCREEN_HEIGHT][SCREEN_WIDTH];

static void init_screen()
{
        int r, c;
        
        for(r = 0; r < SCREEN_HEIGHT; r++) {
                for(c = 0; c < SCREEN_WIDTH; c++) {
                        screen[r][c] = ' ';
                }
        }
}

static void draw_rect(int w, int h)
{
        int r, c;
        
        for(r = 0; r < h; r++) {
                for(c = 0; c < w; c++) {
                        screen[r][c] = '#';
                }
        }
}

static void rotate_row(int row, int num)
{
        int c;
        while(num--) {
                char rhs = screen[row][SCREEN_WIDTH-1];
                c = SCREEN_WIDTH -1;
                while(c--) {
                        screen[row][c + 1] = screen[row][c];
                }
                screen[row][0] = rhs;
        }
}

static void rotate_col(int col, int num)
{
        int r;
        while(num--) {
                char bot = screen[SCREEN_HEIGHT - 1][col];
                r = SCREEN_HEIGHT -1;
                while(r--) {
                        screen[r + 1][col] = screen[r][col];
                }
                screen[0][col] = bot;
        }
}

static void display()
{
        int r, c;
        
        printf("+--------------------------------------------------+\n");
        for(r = 0; r < SCREEN_HEIGHT; r++) {
                printf("|");
                for(c = 0; c < SCREEN_WIDTH; c++) {
                        putchar(screen[r][c]);
                }
                printf("|\n");
        }
        printf("+--------------------------------------------------+\n");
}

static int count_pixels() 
{
        int r, c, i = 0;
        
        for(r = 0; r < SCREEN_HEIGHT; r++) {
                for(c = 0; c < SCREEN_WIDTH; c++) {
                        if (screen[r][c] == '#') i++;
                }
        }
        return i;
        
}

int main(int argc, char** argv)
{
        char buffer[BUFFLEN];

        int w, h, r, c, n;
       
        init_screen();
        while (fgets(buffer, BUFFLEN, stdin) != NULL) {
                if (!strncmp(buffer, "rect ", 5)) {
                        sscanf(buffer, "rect %dx%d", &w, &h);
                        draw_rect(w, h);
                }
                if (!strncmp(buffer, "rotate row", 10)) {
                        sscanf(buffer, "rotate row y=%d by %d", &r, &n);
                        rotate_row(r, n);
                }
                if (!strncmp(buffer, "rotate col", 10)) {
                        sscanf(buffer, "rotate column x=%d by %d", &c, &n);
                        rotate_col(c, n);
                }
                display();
        }
        printf("prixel lit: %d", count_pixels());
        return 0;
}