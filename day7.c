#include <stdio.h>
#include <string.h>

int checkit(char* string)
{
        int i;
        int l = strlen(string);
        int inside_sb = 0;
        int palindrome = 0;
        
        for(i=0; i <= (l-4); i++) {
                if (string[i] == '[') {
                        inside_sb = 1;
                }
                
                if (string[i] == ']') {
                        inside_sb = 0;
                }
                
                if ((string[i] == string[i + 3]) && (string[i + 1] == string[i + 2]) && (string[i] != string[i+1]))
                {
                        if (inside_sb) {
                                return 0;
                        } else {
                                palindrome = 1;
                        }
                }
        }
        return palindrome;
}

int main(int argc, char** argv)
{       
        char buffer[4096];
        while (!feof(stdin)) {
                scanf("%s\n", buffer);
                if (checkit(buffer)) {
                        printf("%s\n", buffer);
                }
        }
        return 0;
}