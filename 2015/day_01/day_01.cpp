#include <fstream>
#include <iostream>
using namespace std;

auto read_file(std::string filename) {
  std::ifstream file(filename);
  std::string line;
  std::string contents;

  if (file.is_open()) {
    while (std::getline(file, line)) {
      contents = contents + line + "\n";
    }
  }
  file.close();
  return contents;
}
int main() {
  std::string filename{"input.txt"};
  std::string contents;
  contents = read_file(filename);

  int counter{0};
  int basement{0};
  for (size_t i = 0; i < contents.size(); i++) {
    if (contents[i] == '(') {
      ++counter;
    } else if (contents[i] == ')') {
      --counter;
      if (counter == -1 && basement == 0) {
        basement = i + 1;
      }
    }
  }
  cout << "Pt 1 Answer: " << counter << endl;
  cout << "Pt 2 Answer: " << basement << endl;

  return 0;
}
