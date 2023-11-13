#include <stdio.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

int main() {
    int min = 2, max = 2000000;
    long long sum_of_primes = 0;
    bool sieve[max + 1];

    // Initialize sieve
    for (int i = 0; i <= max; i++) {
        sieve[i] = true;
    }

    // Sieve of Eratosthenes
    for (int num = 3; num <= sqrt(max); num += 2) {
        if (sieve[num]) {
            for (int j = num * num; j <= max; j += num * 2) {
                sieve[j] = false;
            }
        }
    }

    // Measure start time
    clock_t start = clock();

    // Calculate the sum of primes
    if (min <= 2) {
        sum_of_primes = 2;
        min = 3;
    }

    for (int i = min; i <= max; i += 2) {
        if (sieve[i]) {
            sum_of_primes += i;
        }
    }

    // Measure end time
    clock_t end = clock();

    // Calculate total time taken
    double total_time = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Sum of the primes: %lld\n", sum_of_primes);
    printf("Total time: %f seconds\n", total_time);

    return 0;
}
