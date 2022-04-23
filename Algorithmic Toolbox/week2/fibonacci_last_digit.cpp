#include <iostream>

int get_fibonacci_last_digit_naive(int n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;

    for (int i = 0; i < n - 1; ++i) {
        int tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % 10;
}

int get_fibonacci_last_digit_fast(int n)
{
    long long fibo[n + 1] = {0};
    fibo[0] = 0;
    fibo[1] = 1;

    if (n >= 2)
    {
        for (int i = 2; i <= n; i++)
        {
            int digit = (fibo[i - 1] + fibo[i - 2]) % 10;
            fibo[i] = digit;
        }
    }
    return fibo[n];
}

int main() {
    int n;
    std::cin >> n;
    //int c = get_fibonacci_last_digit_naive(n);
    //std::cout << c << '\n';
    int f = get_fibonacci_last_digit_fast(n);
    std::cout << f << '\n';
    }
