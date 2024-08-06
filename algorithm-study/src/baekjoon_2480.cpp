#include <algorithm>
#include <iostream>
using namespace std;

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int dice_numbers[3];
  for (int i = 0; i < 3; ++i) {
    cin >> dice_numbers[i];
  }
  sort(dice_numbers, dice_numbers + 3);
  if (dice_numbers[0] == dice_numbers[2]) {
    cout << 10000 + 1000 * dice_numbers[0];
  } else if (dice_numbers[0] == dice_numbers[1] ||
             dice_numbers[1] == dice_numbers[2]) {
    cout << 1000 + 100 * dice_numbers[1];
  } else {
    cout << 100 * dice_numbers[2];
  }
}
