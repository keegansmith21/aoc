#include <algorithm>
#include <fstream>
#include <iostream>
#include <math.h>
#include <sstream>
#include <tuple>
#include <vector>

std::tuple<std::vector<int>, std::vector<int>>
read_input(std::string filename) {
  std::vector<int> c1, c2;
  std::ifstream file(filename);
  std::string line;
  int n1, n2;

  while (std::getline(file, line)) {
    std::stringstream ss(line);
    ss >> n1 >> n2;
    c1.push_back(n1);
    c2.push_back(n2);
  }
  file.close();
  return {c1, c2};
}

int difference(std::vector<int> c1, std::vector<int> c2) {
  int sum{0};
  for (int i{0}; i < c1.size(); i++) {
    sum += std::abs(c1[i] - c2[i]);
  }
  return sum;
}

int similarity(std::vector<int> c1, std::vector<int> c2) {
  int sim{0};
  for (int i : c1) {
    sim += count(c2.begin(), c2.end(), i) * i;
  }
  return sim;
}

int main() {
  auto [c1, c2] = read_input("day_01_input.txt");
  std::sort(c1.begin(), c1.end());
  std::sort(c2.begin(), c2.end());
  auto sum = difference(c1, c2);
  std::cout << "Part 1 answer: " << sum << "\n";
  auto sim = similarity(c1, c2);
  std::cout << "Part 2 answer: " << sim << "\n";

  return 0;
}
