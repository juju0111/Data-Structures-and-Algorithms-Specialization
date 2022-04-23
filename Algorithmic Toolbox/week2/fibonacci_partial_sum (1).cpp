#include <iostream>
#include <vector>

#include <ctime>
using namespace std;

using std::vector;

long long get_fibonacci_partial_sum_naive(long long from, long long to) {
    long long sum = 0;

    long long current = 0;
    long long next  = 1;

    for (long long i = 0; i <= to; ++i) {
        if (i >= from) {
            sum += current;
        }

        long long new_current = next;
        next = next + current;
        current = new_current;
    }

    return sum % 10;
}

long long get_fibonacci_partial_sum_fast(long long from, long long to)
{
    long long fibo[to + 1] = {0};
    fibo[0] = 0;
    fibo[1] = 1;
    int sum=0;
    if (to >= 2)
    {
        for (int i = 2; i <= to; i++)
        {
            int digit = (fibo[i - 1] + fibo[i - 2]) % 10;
            fibo[i] = digit;
        }
    }

    for (int i = from; i <= to;i++){
        sum = (sum + fibo[i]) % 10;
    }
    return sum;
}

int main() {
    long long from, to;
    std::cin >> from >> to;
    //clock_t start = clock();
    //std::cout << get_fibonacci_partial_sum_naive(from, to) << '\n';
    //float run_time = (float)(clock() - start) / CLOCKS_PER_SEC;
    //cout << "run time_fast : " << run_time << endl;
    

    //clock_t start2 = clock();
    std::cout << get_fibonacci_partial_sum_fast(from, to) << '\n';
    //float run_time2 = (float)(clock() - start2) / CLOCKS_PER_SEC;
    //cout << "run time_fast : " << run_time2 << endl;
}
