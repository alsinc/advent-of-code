#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct stack
{
    int count;
    int capacity;
    char* data;
};

const int MaxStacks = 10;

static void newStack(struct stack** s)
{
    *s = malloc(sizeof(struct stack));
    (*s)->capacity = 1;
    (*s)->data = calloc((*s)->capacity, sizeof(char));
    (*s)->count = 0;
}

static void push(struct stack* s, char item)
{
    if (s->count + 1 > s->capacity) {
        s->capacity = s->capacity * 2;
        s->data = realloc(s->data, s->capacity * sizeof(char));
    }
    s->data[s->count] = item;
    s->count++;
}

static char pop(struct stack* s) {
    if (!s->count) {
        fprintf(stderr, "OOPS - Stack underflow\n");
        exit(0);
    }
    s->count--;
    return s->data[s->count];
}

static void reverseStacks(struct stack** stacks)
{
    char temp;

    for (int s = 0; s < MaxStacks; s++) {
        int e = stacks[s]->count-1;
        for (int i = 0; i < stacks[s]->count / 2; i++) {
            temp = stacks[s]->data[i];
            stacks[s]->data[i] = stacks[s]->data[e];
            stacks[s]->data[e] = temp;
            e--;
        }
    }
}

static void parseStackLine(char* line, struct stack* stacks[10])
{
    char* c;
    long int offset;
    long int stacknum;

    c = line;
    while (*c) {
        if (*c == '['){
            c++;
            if (*c && *c >= 'A' && *c <= 'Z') {
                offset = c - line;
                stacknum = (offset - 1) / 4;
                push(stacks[stacknum], *c);
            }
        }
        c++;
    }
}

static void copyStacks(struct stack** source, struct stack** dest)
{
    for (int s = 0; s < MaxStacks; s++) {
        if (dest[s]->capacity < source[s]->capacity) {
            dest[s]->capacity = source[s]->capacity;
            dest[s]-> data = realloc(dest[s]->data, dest[s]->capacity * sizeof(char));
        }

        for (int i = 0; i < source[s]->count; i++) {
            dest[s]->data[i] = source[s]->data[i];
        }
        dest[s]->count = source[s]->count;
    }
}

static void dumpStacks(struct stack** stacks)
{
        for (int i = 0; i < MaxStacks; i++) {
        if (stacks[i]->count) {
            printf("%d: ", i + 1);
            for (int e = 0; e < stacks[i]->count; e++) {
                printf("%c", stacks[i]->data[e]);
            }
            printf("\n");
        }
    }
}

int main(int argc, char** argv)
{
    char line[500];
    int numtomove, from, to;
    struct stack **stacks, **stacks2, *tempstack;

    stacks = calloc(MaxStacks, sizeof(struct stack*));
    stacks2 = calloc(MaxStacks, sizeof(struct stack*));
    for (int i = 0; i < MaxStacks ; i++) {
        newStack(&stacks[i]);
        newStack(&stacks2[i]);
    }
    newStack(&tempstack);

    while (!feof(stdin)) {
        fgets(line, sizeof(line), stdin);

        if (index(line, '[')) {
            parseStackLine(line, stacks);
        } else {
            break;
        }
    }

    reverseStacks(stacks);
    copyStacks(stacks, stacks2);

    while (!feof(stdin)) {
        if (!fgets(line, sizeof(line), stdin)) {
            break;
        }
        if (strstr(line, "move")) {
            sscanf(line, "move %d from %d to %d", &numtomove, &from, &to);

            for (int n = 0; n < numtomove; n++) {
                char item;
                item = pop(stacks[from - 1]);
                push(stacks[to - 1], item);
                item = pop(stacks2[from -1]);
                push(tempstack, item);
            }
            for (int n = 0; n < numtomove; n++) {
                char item;
                item = pop(tempstack);
                push(stacks2[to - 1], item);
            }
        }
    }
    dumpStacks(stacks);
    printf("Result (part1): ");
    for (int i = 0; i < MaxStacks; i++) {
        if (stacks[i]->count) {
            printf("%c", stacks[i]->data[stacks[i]->count-1]);
        }
    }
    printf("\n");

    dumpStacks(stacks2);
    printf("Result (part2): ");
    for (int i = 0; i < MaxStacks; i++) {
        if (stacks2[i]->count) {
            printf("%c", stacks2[i]->data[stacks2[i]->count-1]);
        }
    }
    printf("\n");

    return 0;
}
