#include <iostream>

int gcd_naive(int a, int b) {
  int current_gcd = 1;
  for (int d = 2; d <= a && d <= b; d++) {
    if (a % d == 0 && b % d == 0) {
      if (d > current_gcd) {
        current_gcd = d;
      }
    }
  }
  return current_gcd;
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

int main() {
  int a, b;
  std::cin >> a >> b;
  //std::cout << gcd_naive(a, b) << std::endl;
  std::cout << gcd_fast(a, b) << std::endl;
  return 0;
}
