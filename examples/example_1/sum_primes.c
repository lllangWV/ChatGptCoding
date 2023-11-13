#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

bool is_prime(int num) {
    if (num <= 1) return false;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) return false;
    }
    return true;
}

int main() {
    int min = 2, max = 2000000;
    long long sum_of_primes = 0;

    // Measure start time
    clock_t start = clock();

    for (int i = min; i <= max; i++) {
        if (is_prime(i)) {
            sum_of_primes += i;
        }
    }

    // Measure end time
    clock_t end = clock();

    // Calculate total time taken
    double total_time = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Sum of primes: %lld\n", sum_of_primes);
    printf("Total time: %f seconds\n", total_time);

    return 0;
}