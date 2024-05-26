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

  // cout << "Pt 1 Answer: " << << endl;
  // cout << "Pt 2 Answer: " << << endl;

  return 0;
}
