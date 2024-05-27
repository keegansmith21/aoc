#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

vector<vector<int>> read_file(string filename) {
  ifstream file(filename);
  string line;
  int n1, n2, n3;
  vector<vector<int>> contents;

  while (getline(file, line)) {
    for (char &c : line) {
      if (c == 'x') {
        c = ' ';
      }
    }
    stringstream ss{line};
    ss >> n1 >> n2 >> n3;
    contents.push_back(vector<int>{n1, n2, n3});
    // cout << "line read: " << n1 << " " << n2 << " " << n3 << endl;
  }
  return contents;
}

int get_area(vector<int> d) {
  int side_1{d[0] * d[1]};
  int side_2{d[0] * d[2]};
  int side_3{d[1] * d[2]};
  vector<int> areas{side_1, side_2, side_3};
  int min = *min_element(areas.begin(), areas.end());
  return 2 * side_1 + 2 * side_2 + 2 * side_3 + min;
}

int get_bow(vector<int> d) {
  sort(d.begin(), d.end());
  int perimeter = 2 * d[0] + 2 * d[1];
  int volume = d[0] * d[1] * d[2];
  return perimeter + volume;
}

int main() {
  string filename{"input.txt"};
  vector<vector<int>> contents;
  int area{0};
  int bow{0};
  contents = read_file(filename);
  for (vector<int> cube : contents) {
    area += get_area(cube);
    bow += get_bow(cube);
  }
  cout << "Pt 1 Answer: " << area << endl;
  cout << "Pt 2 Answer: " << bow << endl;

  return 0;
}
