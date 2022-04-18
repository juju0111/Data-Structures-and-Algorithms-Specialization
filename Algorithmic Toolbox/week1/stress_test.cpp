#include <cstdlib>
#include <iostream>
#include <vector>
#include <ctime>

using namespace std;

using std::cin;
using std::cout;
using std::vector;

long long MaxPairwiseProduct(const vector<int> &numbers){
    long long result = 0;
    int n= numbers.size();
    clock_t start = clock();

    for (int i = 0;i <n; i++){
        for (int j = i+1;j<n;j++){
            if (((long long)numbers[i]) * numbers[j] > result ){
                result = ((long long)(numbers[i])) * numbers[j];
            }
        }
    }
    float run_time = (float)(clock() - start) / CLOCKS_PER_SEC;

    cout << "run time : " << run_time << endl;
    return result;
}

long long MaxPairwiseProduct_fast(const vector<int> &numbers)
{
    int result = 0;
    int n = numbers.size();
    clock_t start = clock();
    int max_index1 = -1;
    for (int i = 0; i < n; i++)
    {
        if ((max_index1 == -1) || (numbers[i] > numbers[max_index1]))
        {
            max_index1 = i;
        }
    }
    int max_index2 = -1;
    for (int j = 0; j < n; j++)
    {
        if ((j != max_index1) && ((max_index2 == -1) || (numbers[j] >= numbers[max_index2])))
        {
            max_index2 = j;
        }
    }

    float run_time = (float)(clock() - start) / CLOCKS_PER_SEC;

    cout << "run time_fast : " << run_time << endl;

    return ((long long)(numbers[max_index1])) * numbers[max_index2];
}

int main()
{
    int num_iter = 0;
    
    // stress test
    
    while (num_iter < 1000)
    {
        int n = rand() % 1000 + 2;
        cout << n << "\n";
        vector<int> a;
        for (int i = 0; i < n;i++){
            // (c++ vector) push_back == (python list) append
            a.push_back(rand() % 100000);
        }
        for (int i = 0; i < n;i++){
            cout << a[i] << "  ";
        }
        cout << "\n";

        long long res1 = MaxPairwiseProduct(a);
        long long res2 = MaxPairwiseProduct_fast(a);

        if (res1 != res2){
            cout << "Wrong answer : " << res1 << " " << res2 << "\n";
            break;
        }
        else {
            cout << "OK\n";
        }
        num_iter += 1;
    }
    
    /*
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; i++)
    {

        cin >> numbers[i];
    }
    clock_t start = clock();
    long long result = MaxPairwiseProduct_fast(numbers);
    float run_time = (float)(clock() - start)/CLOCKS_PER_SEC;

    long long result2 = MaxPairwiseProduct(numbers);


    cout << result << std::endl;
    cout << result2 << std::endl;
    */
}
