#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> read_input() {
  std::ifstream file{"input.txt"};
  std::vector<std::string> contents;
  std::string line;
  while (file >> line) {
    contents.push_back(line);
  }
  return contents;
}

bool enough_vowels(std::string in) {
  int count{0};
  std::string vowels{"aeiou"};
  for (char c : vowels) {
    count += std::count(in.begin(), in.end(), c);
  }
  std::cout << count << "\n";
  return count >= 3;
}

bool contains_double(std::string in) {
  for (int i = 1; i < in.size(); i++) {
    if (in.substr(i, 1) == in.substr(i - 1, 1)) {
      return true;
    }
  }
  return false;
}

bool no_bad_strs(std::string in) {
  bool found;
  std::vector<std::string> bad_strs{"ab", "cd", "pq", "xy"};
  for (int i = 1; i < in.size(); i++) {
    if (std::find(bad_strs.begin(), bad_strs.end(), in.substr(i - 1, 2)) !=
        bad_strs.end()) {
      return false;
    }
  }
  return true;
}

int is_nice(std::string in) {
  if (enough_vowels(in) && contains_double(in) && no_bad_strs(in)) {
    return 1;
  }
  return 0;
}

int main() {
  std::vector<std::string> contents{read_input()};
  int count{0};
  for (std::string in : contents) {
    std::cout << in << " :: " << enough_vowels(in) << "\n";
    count += is_nice(in);
  }
  std::cout << "PT1 answer: " << count << "\n";
}
