#include <stdio.h>

int sum_of_array(int *numbers, int size) {
    int total = 0;
    for (int i = 0; i < size; i++) {
        total += numbers[i];
    }
    return total;
}

int main() {
    int numbers[] = {1, 2, 3, 4, 5};
    int size = sizeof(numbers) / sizeof(numbers[0]);
    int result = sum_of_array(numbers, size);
    printf("The sum is: %d\n", result);
    return 0;
}