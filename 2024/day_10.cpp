#include <algorithm>
#include <fstream>
#include <iostream>
#include <set>
#include <vector>

void print_map(std::vector<std::vector<int>> &map) {
  for (auto i : map) {
    for (auto j : i) {
      std::cout << j << " ";
    }
    std::cout << "\n";
  }
}

bool in_bounds(std::vector<std::vector<int>> &map, std::vector<int> &loc) {
  return (loc[0] >= 0 && loc[0] < map.size() && loc[1] >= 0 &&
          loc[1] < map[0].size());
}

std::vector<std::vector<int>> read_map(std::string filename) {
  std::ifstream stream(filename);
  std::string line;
  std::vector<std::vector<int>> map;

  while (std::getline(stream, line)) {
    std::vector<int> nline;
    for (char c : line) {
      nline.push_back(c - '0'); // convert to int
    }
    map.push_back(nline);
  }
  return map;
}

std::vector<std::vector<int>>
find_trailheads(std::vector<std::vector<int>> &map) {
  std::vector<std::vector<int>> trailheads;
  /* std::vector<int> coord; */
  for (int y(0); y < map.size(); y++) {
    auto it = std::find(map[y].begin(), map[y].end(), 0);
    while (it != map[y].end()) {
      int i = it - map[y].begin();
      trailheads.push_back({y, i});
      it = std::find(it + 1, map[y].end(), 0);
    }
  }
  return trailheads;
}

int th_score(std::vector<std::vector<int>> &map, std::vector<int> loc, int v,
             std::set<std::vector<int>> &heads) {
  if (v == 9) {
    heads.insert(loc);
    return 1;
  }
  int score(0);
  std::vector<int> l{loc[0], loc[1] - 1};
  std::vector<int> r{loc[0], loc[1] + 1};
  std::vector<int> u{loc[0] - 1, loc[1]};
  std::vector<int> d{loc[0] + 1, loc[1]};
  std::vector<std::vector<int>> dir{l, r, u, d};
  for (auto i : dir) {
    if (in_bounds(map, i)) {
      if (map[i[0]][i[1]] == v + 1) {
        score += th_score(map, i, v + 1, heads);
      }
    }
  }
  return score;
}

int part1() {
  /* std::vector<std::vector<int>> map(read_map("day_10_demo.txt")); */
  std::vector<std::vector<int>> map(read_map("day_10_input.txt"));
  /* print_map(map); */
  std::vector<std::vector<int>> trailheads(find_trailheads(map));
  int score(0);

  for (auto th : trailheads) {
    std::set<std::vector<int>> heads;
    th_score(map, th, 0, heads);
    score += heads.size();
  }

  return score;
}

int part2() {
  std::vector<std::vector<int>> map(read_map("day_10_input.txt"));
  std::vector<std::vector<int>> trailheads(find_trailheads(map));
  int score(0);

  for (auto th : trailheads) {
    std::set<std::vector<int>>
        heads; // Don't use heads but it works with my function
    score += th_score(map, th, 0, heads);
  }

  return score;
}

int main() {
  auto p1(part1());
  std::cout << "Part 1 answer: " << p1 << "\n";
  auto p2(part2());
  std::cout << "Part 2 answer: " << p2 << "\n";
}
