#include <fstream>
#include <iostream>
#include <math.h>
#include <sstream>
#include <unordered_map>

std::unordered_map<long, long> read_stones_map(std::string filename) {
  std::ifstream input(filename);
  std::string line;
  std::unordered_map<long, long> stones;
  long n;
  while (std::getline(input, line)) {
    std::stringstream ss(line);
    while (ss >> n) {
      stones[n]++;
    }
  }
  return stones;
}

std::unordered_map<long, long>
orderless_blink_map(std::unordered_map<long, long> &stones) {

  std::unordered_map<long, long> new_stones(stones);
  for (auto stone_k : stones) {
    if (stone_k.first == 0) {
      new_stones[1] += stone_k.second;
      new_stones[0] -= stone_k.second;
    } else if (int(log10(stone_k.first)) % 2 == 1) {
      int n_digits = int(log10(stone_k.first) + 1);
      long right = stone_k.first % int(pow(10, n_digits / 2));
      long left = stone_k.first / int(pow(10, n_digits / 2));
      new_stones[right] += stone_k.second;
      new_stones[left] += stone_k.second;
      new_stones[stone_k.first] -= stone_k.second;
    } else {
      new_stones[stone_k.first] -= stone_k.second;
      new_stones[stone_k.first * 2024] += stone_k.second;
    }
  }
  return new_stones;
}

long count_stones_map(std::unordered_map<long, long> &stones) {

  long count(0);
  for (auto stone_k : stones) {
    count += stone_k.second;
  }
  return count;
}

long part1() {
  std::unordered_map<long, long> stones = read_stones_map("day_11_input.txt");
  for (int i(0); i < 25; i++) {
    stones = orderless_blink_map(stones);
  }

  return count_stones_map(stones);
}

long part2() {
  std::unordered_map<long, long> stones = read_stones_map("day_11_input.txt");
  for (int i(0); i < 75; i++) {
    stones = orderless_blink_map(stones);
  }

  return count_stones_map(stones);
}

int main() {
  auto p1(part1());
  std::cout << "Part 1 answer: " << p1 << "\n";
  auto p2(part2());
  std::cout << "Part 2 answer: " << p2 << "\n";
}
