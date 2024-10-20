#include <stdio.h>

void printPattern(int rows) {
    for (int i = 1; i <= rows; i++) {
        // Print the increasing part of the pattern
        for (int j = i; j <= rows; j++) {
            printf("%d", j);
        }
        // Print the constant part of the pattern (last number)
        for (int k = 1; k < i; k++) {
            printf("%d", rows);
        }
        printf("\n");
    }
}

int main() {
    int rows;
    printf("Enter the number of rows: ");
    scanf("%d", &rows);
    printPattern(rows);
    return 0;
}
