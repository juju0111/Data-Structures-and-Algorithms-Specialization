#include <iostream>
#include <ctime>
using namespace std;

int fibonacci_sum_naive(long long n) {
    if (n <= 1)
        return n;

    long long previous = 0;
    long long current  = 1;
    long long sum      = 1;

    for (long long i = 0; i < n - 1; ++i) {
        long long tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
        sum += current;
    }

    return sum % 10;
}

int fibonacci_sum_fast(long long n)
{
    if (n <= 1)
        return n;

    int previous = 0;
    int current = 1;
    int sum = 1;

    for (int i = 0; i < n - 1; ++i)
    {
        int tmp_previous = previous;
        previous = current;
        current = (tmp_previous + current) % 10;
        sum = (sum + current)%10;
    }

    return sum;
}

int main() {
    long long n = 0;
    std::cin >> n;
    //clock_t start = clock();
    //std::cout << fibonacci_sum_naive(n)<<std::endl;
    //float run_time = (float)(clock() - start) / CLOCKS_PER_SEC;
    //cout << "run time_fast : " << run_time << endl;

    //clock_t start2 = clock();
    std::cout << fibonacci_sum_fast(n) << std::endl;
    //float run_time2 = (float)(clock() - start2) / CLOCKS_PER_SEC;
    //cout << "run time_fast : " << run_time2 << endl;
}
