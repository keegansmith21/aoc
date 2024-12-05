#include <fstream>
#include <iostream>
#include <unordered_map>
#include <vector>

std::vector<std::vector<char>> read_in() {
  std::vector<std::vector<char>> wordsearch;
  std::ifstream input("input.txt");
  std::string line;

  while (std::getline(input, line)) {
    std::vector<char> charline(line.begin(), line.end());
    wordsearch.push_back(charline);
  }
  return wordsearch;
}

int count_xmas(std::vector<std::vector<char>> &ws, int i, int j) {
  int ilen(ws.size());
  int jlen(ws[0].size());
  bool right(j <= jlen - 4);
  bool left(j >= 3);
  bool up(i >= 3);
  bool down(i <= ilen - 4);
  std::unordered_map<std::string, int> map;
  std::string key;

  if (right) { // right
    key = {'X', ws[i][j + 1], ws[i][j + 2], ws[i][j + 3]};
    map[key] += 1;
  }
  if (left) { // left
    key = {'X', ws[i][j - 1], ws[i][j - 2], ws[i][j - 3]};
    map[key] += 1;
  }
  if (down) { // Down
    key = {'X', ws[i + 1][j], ws[i + 2][j], ws[i + 3][j]};
    map[key] += 1;
  }
  if (up) { // Up
    key = {'X', ws[i - 1][j], ws[i - 2][j], ws[i - 3][j]};
    map[key] += 1;
  }
  if (down && right) { // Down rt
    key = {'X', ws[i + 1][j + 1], ws[i + 2][j + 2], ws[i + 3][j + 3]};
    map[key] += 1;
  }
  if (up && right) { // Up right
    key = {'X', ws[i - 1][j + 1], ws[i - 2][j + 2], ws[i - 3][j + 3]};
    map[key] += 1;
  }
  if (down && left) { // Down lft
    key = {'X', ws[i + 1][j - 1], ws[i + 2][j - 2], ws[i + 3][j - 3]};
    map[key] += 1;
  }
  if (up && left) { // Up left
    key = {'X', ws[i - 1][j - 1], ws[i - 2][j - 2], ws[i - 3][j - 3]};
    map[key] += 1;
  }

  return map["XMAS"];
}

int c1() {
  auto wordsearch(read_in());
  int count(0);
  for (size_t i(0); i < wordsearch.size(); i++) {
    for (size_t j(0); j < wordsearch[i].size(); j++) {
      if (wordsearch[i][j] == 'X') {
        count += count_xmas(wordsearch, i, j);
      }
    }
  }
  return count;
}

int count_x_mas(std::vector<std::vector<char>> &ws, int i, int j) {
  std::unordered_map<char, int> map;
  map[ws[i - 1][j - 1]] = 1;
  map[ws[i + 1][j + 1]] = 1;
  if (!(map['M'] == 1) || !(map['S'] == 1)) {
    return 0;
  }
  map[ws[i - 1][j + 1]] += 1;
  map[ws[i + 1][j - 1]] += 1;
  if (!(map['M'] == 2) || !(map['S'] == 2)) {
    return 0;
  }
  return 1;
}

int c2() {
  auto wordsearch(read_in());
  int count(0);
  for (size_t i(1); i < wordsearch.size() - 1; i++) {
    for (size_t j(1); j < wordsearch[i].size() - 1; j++) {
      if (wordsearch[i][j] == 'A') {
        count += count_x_mas(wordsearch, i, j);
      }
    }
  }
  return count;
}

int main() {
  int pt1(c1());
  std::cout << "Part 1 answer: " << pt1 << "\n";
  int pt2(c2());
  std::cout << "Part 2 answer: " << pt2 << "\n";

  return 0;
}
