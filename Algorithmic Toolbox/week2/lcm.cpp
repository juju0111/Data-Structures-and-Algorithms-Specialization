#include <iostream>
#include <ctime>

using namespace std;

long long lcm_naive(int a, int b)
{
  for (long l = 1; l <= (long long) a * b; ++l)
    if (l % a == 0 && l % b == 0)
      return l;

  return (long long) a * b;
}

int gcd_fast(int a, int b)
{
  //x is bigger than y
  int x, y;
  if (a > b){
    x = a;
    y = b;
  }
  else{
    x = b;
    y = a;
  }
  if (y==0){
    return x;
  }
  int remain = x % y;
  return gcd_fast(y, remain);

}

long long lcm_fast(int a, int b) {
  return (long long)a * b/ gcd_fast(a,b);
}

int main() {
  int a, b;
  std::cin >> a >> b;
  
  //std::cout << lcm_naive(a, b) << std::endl;
  std::cout << lcm_fast(a, b) << std::endl;

  return 0;
}
