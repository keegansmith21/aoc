#include <algorithm>
#include <fstream>
#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

int antenna_from_line(
    std::unordered_map<char, std::vector<std::vector<int>>> &antennas,
    std::string &line, int row) {

  int len(line.size());
  for (std::string::size_type i(0); i < line.size(); i++) {
    if (line[i] == '.')
      continue;
    std::vector<int> loc{row, int(i)};
    antennas[line[i]].push_back(loc);
  }
  return len;
}

std::vector<int> distance_apart(std::vector<int> i, std::vector<int> j) {
  return {i[0] - j[0], i[1] - j[1]};
}

bool in_bounds(std::vector<int> loc, int ylen, int xlen) {
  bool in(loc[0] >= 0 && loc[0] < ylen && loc[1] >= 0 && loc[1] < xlen);
  return in;
}

void find_antinodes(std::set<std::vector<int>> &antinodes,
                    std::vector<std::vector<int>> &identical_antennas, int ylen,
                    int xlen) {
  for (size_t i(0); i < identical_antennas.size(); i++) {
    for (size_t j(0); j < identical_antennas.size(); j++) {
      if (i == j)
        continue;
      auto d(distance_apart(identical_antennas[i], identical_antennas[j]));
      auto new_loc = std::vector{identical_antennas[i][0] - 2 * d[0],
                                 identical_antennas[i][1] - 2 * d[1]};
      if (in_bounds(new_loc, ylen, xlen)) {
        antinodes.insert(new_loc);
      }
    }
  }
}

void find_resonant_antinodes(std::set<std::vector<int>> &antinodes,
                             std::vector<std::vector<int>> &identical_antennas,
                             int ylen, int xlen) {
  for (size_t i(0); i < identical_antennas.size(); i++) {
    for (size_t j(0); j < identical_antennas.size(); j++) {
      if (i == j)
        continue;
      int mult(1);
      auto d(distance_apart(identical_antennas[i], identical_antennas[j]));
      auto new_loc = std::vector{identical_antennas[i][0] - mult * d[0],
                                 identical_antennas[i][1] - mult * d[1]};
      while (in_bounds(new_loc, ylen, xlen)) {
        antinodes.insert(new_loc);
        mult++;
        new_loc[0] = identical_antennas[i][0] - mult * d[0];
        new_loc[1] = identical_antennas[i][1] - mult * d[1];
      }
    }
  }
}

int part1() {
  std::fstream input("day_08_input.txt");
  /* std::fstream input("day_08_demo.txt"); */
  std::set<std::vector<int>> antinodes;
  std::unordered_map<char, std::vector<std::vector<int>>> antennas;
  std::string line;
  int ylen(0);
  int xlen(0);
  while (std::getline(input, line)) {
    xlen = antenna_from_line(antennas, line, ylen++);
  }
  for (auto it : antennas) {
    find_antinodes(antinodes, it.second, ylen, xlen);
  }
  // Print answer grid
  /* for (int i(0); i < ylen; i++) { */
  /*   for (int j(0); j < ylen; j++) { */
  /*     if (std::find(antinodes.begin(), antinodes.end(), std::vector{i, j}) !=
   */
  /*         antinodes.end()) { */
  /*       std::cout << "#"; */
  /*     } else { */
  /*       std::cout << "."; */
  /*     } */
  /*   } */
  /*   std::cout << "\n"; */
  /* } */
  return antinodes.size();
}

int part2() {
  std::fstream input("day_08_input.txt");
  /* std::fstream input("day_08_demo.txt"); */
  std::set<std::vector<int>> antinodes;
  std::unordered_map<char, std::vector<std::vector<int>>> antennas;
  std::string line;
  int ylen(0);
  int xlen(0);
  while (std::getline(input, line)) {
    xlen = antenna_from_line(antennas, line, ylen++);
  }
  for (auto it : antennas) {
    find_resonant_antinodes(antinodes, it.second, ylen, xlen);
  }
  // Print answer grid
  /* for (int i(0); i < ylen; i++) { */
  /*   for (int j(0); j < ylen; j++) { */
  /*     if (std::find(antinodes.begin(), antinodes.end(), std::vector{i, j}) !=
   */
  /*         antinodes.end()) { */
  /*       std::cout << "#"; */
  /*     } else { */
  /*       std::cout << "."; */
  /*     } */
  /*   } */
  /*   std::cout << "\n"; */
  /* } */
  return antinodes.size();
}

int main() {
  int p1(part1());
  std::cout << "Part 1 answer: " << p1 << "\n";
  int p2(part2());
  std::cout << "Part 2 answer: " << p2 << "\n";
}
