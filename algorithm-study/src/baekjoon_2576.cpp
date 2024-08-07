#include <iostream>
using namespace std;

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  bool is_odd_existing = false;
  int odd_sum = 0;
  int min_odd = 101; // initialize
  for (int i = 0; i < 7; i++) {
    int number;
    cin >> number;
    if (number % 2 == 1) {
      is_odd_existing = true;
      odd_sum += number;
      min_odd = min(min_odd, number);
    }
  }

  if (!is_odd_existing) {
    cout << -1;
  } else {
    cout << odd_sum << '\n';
    cout << min_odd << '\n';
  }
}
