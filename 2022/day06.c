#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
    int ch;
    char* queue;
    int queueSize = 0;
    int pos = -1;
    int count = 0;
    int histo[26];
    int check = 0;

    for (int i = 0; i < 26; i++) {
        histo[i] = 0;
    }

    if (argc != 2) {
        fprintf(stderr, "Usage: %s <message size>\n", argv[0]);
        return 1;
    }

    queueSize = atoi(argv[1]);
    queue = calloc(queueSize, sizeof(char));

    while ((ch = getchar()) != EOF) {
        if (ch == '\n') {
            break;
        } else if (ch < 'a' || ch > 'z') {
            fprintf(stderr, "unexpected character %c (%d)\n", ch, ch);
        }

        count++;
        pos++;
        histo[ch - 'a']++;

        if (pos == queueSize) {
            pos = 0;
        }

        if (queue[pos] >= 'a' && queue[pos] <= 'z') {
            histo[queue[pos] - 'a']--;
        }
        queue[pos] = ch;

        if (count >= queueSize) {
            check = 1;
            for (int i = 0; i < 26; i++) {
                if (histo[i] > 1) {
                    check = 0;
                }
            }
            if (check) {
                printf("GO IT: %d\n", count);
                break;
            }
        }
    }
    return 0;
}
