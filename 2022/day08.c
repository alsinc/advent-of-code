#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct map_t
{
    int width;
    int height;
    u_int8_t* map;
};

static struct map_t* readinput(void)
{
    char buffer[500];
    int len;
    struct map_t *map = malloc(sizeof(struct map_t));
    int mapsize = 200;

    map->height = 0;
    map->width = -1;
    map->map = calloc(mapsize, sizeof(u_int8_t));
    while (!feof(stdin)) {
        if (!fgets(buffer, sizeof(buffer), stdin)) {
            break;
        }

        len = strlen(buffer);
        if (buffer[len - 1] == '\n') len--;

        if (map->width == -1) {
            map->width = len;
        } else if (len != map->width) {
            fprintf(stderr, "OOPS, not all lines the same length\n");
            exit(1);
        }
        map->height = map->height + 1;

        if (map->width * map->height > mapsize) {
            mapsize = map->width * map->height;
            map->map = realloc(map->map, mapsize * sizeof(u_int8_t));
        }
        for (int i = 0; i < len; i++) {
            map->map[(map->height - 1) * map->width + i] = buffer[i] - '0';
        }
    }
    return map;
}

static int isvisible(struct map_t* map, int row, int col, int step, int count)
{
    int pos = row * map->width + col;
    int height = map->map[pos];

    while (count--) {
        pos += step;
        if (map->map[pos] >= height) return 0;
    }

    return 1;
}

static int count(struct map_t* map, int row, int col, int step, int count)
{
    int pos = row * map->width + col;
    int height = map->map[pos];
    int trees = 0;

    while (count--) {
        pos += step;
        trees++;
        if (map->map[pos] >= height) return trees;
    }

    return trees;
}

int main(int argc, char** argv)
{
    int vright, vleft, vup, vdown, visible, visiblecount = 0;
    int cright, cleft, cup, cdown, score, bestscore = 0;
    struct map_t* map = readinput();

    for(int r = 0; r < map->height; r++) {
        for (int c = 0; c < map->width; c++) {
            vright = isvisible(map, r, c, 1, map->width - c -1);
            vleft = isvisible(map, r, c, -1, c);
            vdown = isvisible(map, r, c, map->width, map->height - r - 1);
            vup = isvisible(map, r, c, -map->width, r);

            cright = count(map, r, c, 1, map->width - c -1);
            cleft = count(map, r, c, -1, c);
            cdown = count(map, r, c, map->width, map->height - r - 1);
            cup = count(map, r, c, -map->width, r);
            score = cright * cleft * cdown * cup;

            visible = vup || vdown || vleft || vright;

            if (visible) {
                visiblecount++;
            }

            if (score > bestscore) {
                bestscore = score;
            }
        }
    }
    printf("Trees visible (part 1): %d\n", visiblecount);
    printf("Best scenic score (part 2): %d\n", bestscore);
}
