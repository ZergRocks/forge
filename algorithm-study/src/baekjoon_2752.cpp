#include <algorithm>
#include <iostream>
using namespace std;

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int *a = new int[3];
  for (int i = 0; i < 3; i++) {
    cin >> a[i];
  }
  sort(a, a + 3);
  for (int i = 0; i < 3; i++) {
    cout << a[i] << ' ';
  }
}
