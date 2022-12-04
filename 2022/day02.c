#include <stdio.h>

enum Move {
    Rock = 1,
    Paper = 2,
    Scissors = 3
};

enum Result {
    Win = 6,
    Lose = 0,
    Draw = 3
};

static enum Move DecodeMove(char move)
{
    switch (move) {
        case 'A':
        case 'X':
            return Rock;
        case 'B':
        case 'Y':
            return Paper;
        case 'C':
        case 'Z':
            return Scissors;
        default:
            return 0;
    }



}

static enum Result DecodeResult(char result)
{
    if (result == 'X') return Lose;
    if (result == 'Y') return Draw;
    if (result == 'Z') return Win;
    return -1;
}

static enum Result Evaluate(enum Move p1, enum Move p2)
{
    if (p1 == p2) return Draw;

    if (p1 == Rock && p2 == Paper) return Win;
    if (p1 == Rock && p2 == Scissors) return Lose;
    if (p1 == Paper && p2 == Rock) return Lose;
    if (p1 == Paper && p2 == Scissors) return Win;
    if (p1 == Scissors && p2 == Rock) return Win;
    if (p1 == Scissors && p2 == Paper) return Lose;
    return -1;
}

static enum Move CalcMove(enum Move p1, enum Result expectedresult)
{
    if (expectedresult == Draw) return p1;

    if (p1 == Rock && expectedresult == Win) return Paper;
    if (p1 == Rock && expectedresult == Lose) return Scissors;
    if (p1 == Paper && expectedresult == Win) return Scissors;
    if (p1 == Paper && expectedresult == Lose) return Rock;
    if (p1 == Scissors && expectedresult == Win) return Rock;
    if (p1 == Scissors && expectedresult == Lose) return Paper;
    return 0;
}

int main(int argc, char** argv)
{
    char p1in, p2in;
    enum Move p1move, p2move, bestmove;
    enum Result gameresult, expectedresult;
    int score = 0;
    int score2 = 0;
    int total = 0;
    int total2 = 0;

    while (!feof(stdin)) {
        scanf("%c %c\n", &p1in, &p2in);

        p1move = DecodeMove(p1in);
        p2move = DecodeMove(p2in);
        expectedresult = DecodeResult(p2in);

        if (!p1move || !p2move || expectedresult == -1) {
            fprintf(stderr, "OOPS unknown move\n");
            return 1;
        }

        gameresult = Evaluate(p1move, p2move);
        bestmove = CalcMove(p1move, expectedresult);

        score = p2move + gameresult;
        score2 = bestmove + expectedresult;

        total += score;
        total2 += score2;
    }
    printf("Total (part1): %d\n", total);
    printf("Total (part2): %d\n", total2);

    return 0;
}