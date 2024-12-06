#include <algorithm>
#include <fstream>
#include <iostream>
#include <math.h>
#include <sstream>
#include <vector>

int conditions(std::vector<int> &diffs) {
  // Check conditions of the vector
  if (std::find(diffs.begin(), diffs.end(), 0) != diffs.end()) {
    return 0;
  }
  auto [min, max] = std::minmax_element(diffs.begin(), diffs.end());
  if (*min < 0 && *max > 0) {
    return 0;
  }

  if (*min < -3 || *max > 3) {
    return 0;
  }
  return 1;
}

std::vector<int> gen_diffs(std::vector<int> &nums) {
  int prev_n, n;
  std::vector<int> diffs;
  prev_n = nums[0];
  for (size_t i{1}; i < nums.size(); i++) {
    n = nums[i];
    diffs.push_back(n - prev_n);
    prev_n = n;
  }
  return diffs;
}

int is_safe(std::string line) {
  std::stringstream ss(line);
  std::vector<int> diffs;
  int n, prev_n;

  ss >> prev_n;
  while (!ss.eof()) {
    ss >> n;
    diffs.push_back(n - prev_n);
    prev_n = n;
  }

  return conditions(diffs);
}
int is_safe_damp(std::string line) {
  std::vector<int> diffs, nums, damp_nums;
  std::stringstream ss(line);
  int n;

  while (!ss.eof()) {
    ss >> n;
    nums.push_back(n);
  }

  diffs = gen_diffs(nums);
  if (conditions(diffs) == 1) { // If it's valid, don't do the next step
    return 1;
  }

  for (size_t i{0}; i < nums.size(); i++) {
    for (size_t j{0}; j < nums.size(); j++) {
      if (i == j) {
        continue;
      }
      damp_nums.push_back(nums[j]);
    }
    diffs = gen_diffs(damp_nums);
    if (conditions(diffs) == 1) {
      return 1;
    }
    damp_nums.clear();
  }

  return 0;
}

int count_safe() {
  int safe{0};
  std::ifstream infile("day_02_input.txt");
  std::string line;

  while (std::getline(infile, line)) {
    safe += is_safe(line);
  }
  infile.close();
  return safe;
}

int count_safe_damp() {
  int safe{0};
  std::ifstream infile("day_02_input.txt");
  std::string line;

  while (std::getline(infile, line)) {
    safe += is_safe_damp(line);
  }

  infile.close();
  return safe;
}

int main() {
  std::cout << "Part 1 answer: " << count_safe() << "\n";
  std::cout << "Part 2 answer: " << count_safe_damp() << "\n";
  return 0;
}
