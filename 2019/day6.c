#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct pair {
	char* orbitee;
	char* orbiter;
};

struct node {
	struct pair* entry;
	struct node* next;
};

static struct pair* read_map(int *pentries)
{
	char input[50];
	char *bracket;
	struct pair *map = NULL;
	int map_size = 20;
	int entries = 0;

	map = malloc(map_size * sizeof(struct pair));
	assert(map);

	while (!feof(stdin)) {
		if (fgets(input, 50, stdin)) {
			if (input[strlen(input) - 1] == '\n') {
				input[strlen(input) - 1] = '\0';
			}

			bracket = strchr(input, ')');
			if (bracket) {
				entries++;
				if (entries > map_size) {
					map_size = map_size * 2;
					map = realloc(map, map_size * sizeof(struct pair));
					assert(map);
				}
				map[entries - 1].orbitee = strndup(input, bracket - input);
				map[entries - 1].orbiter = strdup(bracket + 1);
			} else {
				fprintf(stderr, "Invalid input ')' not found : %s\n", input);
				return NULL;
			}
		} else {
		}
	}
	*pentries = entries;
	return map;
}

static int search(struct pair* map, int entries, char* orbiter)
{
	int i;
	if (!strcmp(orbiter, "COM")) {
		return 0;
	}

	for (i = 0; i < entries; i++) {
		if (!strcmp(map[i].orbiter, orbiter)) {
			return search(map, entries, map[i].orbitee) + 1;
		}
	}
	printf("OOPS: %s\n", orbiter);
	return 0;
}

static struct node *search2(struct pair* map, int entries, char* orbiter)
{
	int i;
	struct node *n;
	if (!strcmp(orbiter, "COM")) {
		return NULL;
	}

	for (i = 0; i < entries; i++) {
		if (!strcmp(map[i].orbiter, orbiter)) {
			n = malloc(sizeof(struct node));
			assert(n);

			n->entry = &map[i];
			n->next = search2(map, entries, map[i].orbitee);
			return n;
		}
	}
	printf("OOPS: %s\n", orbiter);
	return NULL;
}

static void part1(struct pair* map, int entries)
{
	int i, total_orbits = 0;
	for (i = 0; i < entries; i++) {
		total_orbits += search(map, entries, map[i].orbitee);
		total_orbits++;
	}
	printf("Part1: %d\n", total_orbits);
}

static void part2(struct pair* map, int entries)
{
	struct node *santa_route, *you_route;
	struct node *current_s, *current_y;
	int santa = 0, you = 0;

	santa_route = search2(map, entries, "SAN");
	you_route = search2(map, entries, "YOU");

	current_s = santa_route;
	while(current_s) {
		current_y = you_route;
		you = 0;
		while(current_y) {
			if (!strcmp(current_s->entry->orbitee, current_y->entry->orbitee)) {
				printf("Santa: %d, You: %d, Total: %d\n", santa, you, santa + you);
				return;
			}
			current_y = current_y->next;
			you++;
		}

		current_s = current_s->next;
		santa++;
	}
}

int main(int argc, char** argv)
{
	struct pair* map;
	int entries = 0;

	map = read_map(&entries);
	part1(map, entries);
	part2(map, entries);
	return 0;
}
