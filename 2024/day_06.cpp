#include <algorithm>
#include <fstream>
#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

std::vector<std::vector<char>> read_input(std::string f) {
  std::string line;
  std::ifstream fs(f);
  std::vector<std::vector<char>> floor;
  while (std::getline(fs, line)) {
    std::vector<char> row(line.begin(), line.end());
    floor.push_back(row);
  }
  return floor;
}
std::vector<int> find_start(std::vector<std::vector<char>> &floor) {
  for (int i(0); i < floor.size(); i++) {
    for (int j(0); j < floor.size(); j++) {
      if (floor[i][j] == '^') {
        return std::vector<int>{i, j};
      }
    }
  }
  std::cout << "ERROR"
            << "\n";
  return {0, 0}; // Shouldn't happen
}

void add_to_tracker(std::unordered_map<int, int> &tracker,
                    std::vector<int> &loc, std::vector<ulong> &sz) {
  tracker[loc[0] * sz[1] + loc[1]] = 1;
}

bool next_move_outside(std::vector<ulong> &sz, std::vector<int> &loc,
                       std::vector<int> &dir) {
  std::vector<int> new_loc(loc);
  new_loc[0] += dir[0];
  new_loc[1] += dir[1];
  return (new_loc[0] < 0 || new_loc[1] < 0 || new_loc[0] >= sz[0] ||
          new_loc[1] >= sz[1]);
}
void change_dir(std::vector<int> &dir) {
  if (dir == std::vector<int>{-1, 0}) {
    dir = {0, 1};
  } else if (dir == std::vector<int>{1, 0}) {
    dir = {0, -1};
  } else if (dir == std::vector<int>{0, -1}) {
    dir = {-1, 0};
  } else if (dir == std::vector<int>{0, 1}) {
    dir = {1, 0};
  }
}

void update_loc(std::vector<std::vector<char>> &floor, std::vector<int> &dir,
                std::vector<int> &loc) {
  char space;
  std::vector<int> new_loc(loc);

  new_loc[0] += dir[0];
  new_loc[1] += dir[1];
  while (floor[new_loc[0]][new_loc[1]] == '#') {
    // Deals with the edge case that you're in a corner of boxes
    // ....#..
    // ....>#.
    // ....#..
    change_dir(dir);
    new_loc = loc;
    new_loc[0] += dir[0];
    new_loc[1] += dir[1];
  }
  loc[0] += dir[0];
  loc[1] += dir[1];
}

bool add_to_dir_tracker(
    std::unordered_map<int, std::vector<std::vector<int>>> &dir_tracker,
    std::vector<int> &loc, std::vector<ulong> &sz, std::vector<int> &dir) {

  int idx = loc[0] * sz[1] + loc[1];
  if (std::find(dir_tracker[idx].begin(), dir_tracker[idx].end(), dir) !=
      dir_tracker[idx].end()) {
    return true;
  } else {
    dir_tracker[idx].push_back(dir);
    return false;
  }
}

int check_loop(std::vector<std::vector<char>> &floor, std::vector<ulong> &sz) {
  std::vector<int> dir{-1, 0};
  auto loc = find_start(floor);
  std::unordered_map<int, std::vector<std::vector<int>>> dir_tracker;
  add_to_dir_tracker(dir_tracker, loc, sz, dir);
  while (!next_move_outside(sz, loc, dir)) {
    // Update location and tracker
    update_loc(floor, dir, loc);
    if (add_to_dir_tracker(dir_tracker, loc, sz, dir)) {
      return 1;
    }
  }
  return 0;
}

int part1() {
  int count(0);
  auto floor = read_input("day_06_input.txt");
  auto loc = find_start(floor);
  std::vector<ulong> sz{floor.size(), floor[0].size()};
  std::vector<int> dir{-1, 0};
  std::unordered_map<int, int> tracker;
  add_to_tracker(tracker, loc, sz);
  while (!next_move_outside(sz, loc, dir)) {
    // Update location and tracker
    update_loc(floor, dir, loc);
    add_to_tracker(tracker, loc, sz);
  }
  for (auto &it : tracker) {
    count += it.second;
  }
  return count;
}

int part2() {
  int count(0);
  auto floor = read_input("day_06_input.txt");
  std::vector<ulong> sz{floor.size(), floor[0].size()};
  auto loc = find_start(floor);
  std::vector<int> dir{-1, 0};
  std::set<std::vector<int>> tracker;
  tracker.insert(loc);

  while (!next_move_outside(sz, loc, dir)) {
    update_loc(floor, dir, loc);
    tracker.insert(loc);
  }
  for (auto ij : tracker) {
    if (floor[ij[0]][ij[1]] == '^')
      continue;
    floor[ij[0]][ij[1]] = '#';
    count += check_loop(floor, sz);
    floor[ij[0]][ij[1]] = '.';
  }

  return count;
}

int main() {
  int p1(part1());
  std::cout << "Part 1 answer: " << p1 << "\n";
  int p2(part2());
  std::cout << "Part 2 answer: " << p2 << "\n";
}
