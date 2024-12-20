#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

std::vector<std::vector<char>> read_input(std::string filename) {
  std::vector<std::vector<char>> map;
  std::ifstream input(filename);
  std::string line;

  while (std::getline(input, line)) {
    std::vector<char> cs;
    for (char c : line) {
      cs.push_back(c);
    }
    map.push_back(cs);
  }
  return map;
}

std::vector<std::vector<int>> get_dirs(std::vector<int> loc) {
  std::vector<int> up{loc[0] - 1, loc[1]};
  std::vector<int> down{loc[0] + 1, loc[1]};
  std::vector<int> left{loc[0], loc[1] - 1};
  std::vector<int> right{loc[0], loc[1] + 1};
  std::vector<std::vector<int>> d{up, right, down, left};
  return d;
}

struct FloodObj {
  std::vector<std::vector<char>> map;
  std::vector<std::vector<int>> locs;
  int ys;
  int xs;
};

void flood(FloodObj &flobj, std::vector<int> loc, char from, char to) {
  // Bounds check
  if (loc[0] < 0 || loc[0] >= flobj.ys || loc[1] < 0 || loc[1] >= flobj.xs) {
    return;
  }

  // Not valid fill character
  if (flobj.map[loc[0]][loc[1]] != from) {
    return;
  }

  flobj.locs.push_back(loc);
  flobj.map[loc[0]][loc[1]] = to; // Replace with '_'

  for (auto d : get_dirs(loc)) {
    flood(flobj, d, from, to);
  }
}

int calc_perim(std::vector<std::vector<int>> &locs) {
  int perim(0);
  for (auto l : locs) {
    int surr(4);
    for (auto d : get_dirs(l)) {
      if (std::find(locs.begin(), locs.end(), d) != locs.end()) {
        surr -= 1;
      }
    }
    perim += surr;
  }
  return perim;
}

int calc_vertices(const std::vector<std::vector<int>> &locs,
                  const std::vector<std::vector<char>> &map, char in) {
  int vert = 0;
  std::vector<std::pair<std::pair<int, int>, std::pair<int, int>>> dir_pairs = {
      {{-1, 0}, {0, 1}},  // Up, Right
      {{-1, 0}, {0, -1}}, // Up, Left
      {{1, 0}, {0, 1}},   // Down, Right
      {{1, 0}, {0, -1}},  // Down, Left
  };

  auto get_char = [&](int x, int y) -> char {
    if (x < 0 || x >= static_cast<int>(map.size()) || y < 0 ||
        y >= static_cast<int>(map[0].size())) {
      return '_';
    }
    return map[x][y];
  };

  for (const auto &loc : locs) {
    int x = loc[0], y = loc[1];

    for (const auto &[dir1, dir2] : dir_pairs) {
      // Calculate neighbor positions
      int x1 = x + dir1.first, y1 = y + dir1.second;
      int x2 = x + dir2.first, y2 = y + dir2.second;
      char p1 = get_char(x1, y1);
      char p2 = get_char(x2, y2);

      // Check for interior corner
      if (p1 != in && p2 != in) {
        vert++;
      }
      // Check for exterior corner
      else if (p1 == in && p2 == in) {
        char diagonal = get_char(x + dir1.first + dir2.first,
                                 y + dir1.second + dir2.second);
        if (diagonal != in) {
          vert++;
        }
      }
    }
  }
  return vert;
}

int part1() {
  FloodObj flobj;
  /* flobj.map = read_input("day_12_demo.txt"); */
  flobj.map = read_input("day_12_input.txt");
  flobj.ys = flobj.map.size();
  flobj.xs = flobj.map[0].size();
  char to('_');
  long area, perim, ans(0);
  for (int i(0); i < flobj.ys; i++) {
    for (int j(0); j < flobj.xs; j++) {
      if (flobj.map[i][j] == '_') {
        continue;
      }
      std::vector<int> loc{i, j};
      flobj.locs.clear();
      char from{flobj.map[i][j]};
      flood(flobj, loc, from, to);
      area = flobj.locs.size();
      perim = calc_perim(flobj.locs);
      ans += area * perim;
    }
  }

  return ans;
}
int part2() {
  FloodObj flobj;
  /* auto map = read_input("day_12_demo.txt"); */
  auto map = read_input("day_12_input.txt");
  flobj.map = map;
  flobj.ys = flobj.map.size();
  flobj.xs = flobj.map[0].size();
  char to('_'), from;
  long area, perim, ans(0);
  for (int i(0); i < flobj.ys; i++) {
    for (int j(0); j < flobj.xs; j++) {
      char from{flobj.map[i][j]};
      if (from == to) {
        continue;
      }
      std::vector<int> loc{i, j};
      flobj.locs.clear();
      flood(flobj, loc, from, to);
      area = flobj.locs.size();
      perim = calc_vertices(flobj.locs, map, map[i][j]);
      ans += area * perim;
    }
  }

  return ans;
}

int main() {
  auto p1(part1());
  std::cout << "Part 1 answer: " << p1 << "\n";
  auto p2(part2());
  std::cout << "Part 2 answer: " << p2 << "\n";
}
