#include <iostream>
using namespace std;

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  for (int i = 0; i < 3; i++) {
    int bae_count = 0;
    for (int j = 0; j < 4; j++) {
      int token;
      cin >> token;
      if (!token) {
        bae_count++;
      }
    }
    if (bae_count == 0) {
      cout << 'E' << '\n';
    } else if (bae_count == 1) {
      cout << 'A' << '\n';
    } else if (bae_count == 2) {
      cout << 'B' << '\n';
    } else if (bae_count == 3) {
      cout << 'C' << '\n';
    } else {
      cout << 'D' << '\n';
    }
  }
}
