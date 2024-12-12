#include <fstream>
#include <iostream>
#include <math.h>
#include <sstream>
#include <vector>

struct LineOp {
  long ans;
  std::vector<long> parts;
};

LineOp read_line(std::string line) {
  std::stringstream ss(line);
  std::string i;
  LineOp line_op;

  ss >> line_op.ans;
  ss >> i; // Skip the colon
  while (ss >> i) {
    line_op.parts.push_back(std::stoi(i));
  }
  return line_op;
}

std::vector<std::vector<int>> gen_operands(int n) {
  std::vector<std::vector<int>> operands;

  int total_combinations = std::pow(2, n);

  for (int i(0); i < total_combinations; i++) {
    std::vector<int> combination;

    for (int j(0); j < n; j++) {
      int bit = (i >> j) & 1;
      combination.push_back(bit);
    }
    operands.push_back(combination);
  }
  return operands;
}

std::vector<std::vector<int>> generate_operands(int length, int base) {
  int total_combinations = std::pow(base, length);
  std::vector<std::vector<int>> operands;

  for (int i(0); i < total_combinations; i++) {
    std::vector<int> combination;

    for (int j(0); j < length; j++) {
      int val = (i / static_cast<int>(std::pow(base, j))) % base;
      combination.push_back(val);
    }
    operands.push_back(combination);
  }
  return operands;
}

long line_solution(LineOp &line_op) {
  auto combinations(generate_operands(line_op.parts.size() - 1, 2));

  for (auto &combo : combinations) {
    long ans(line_op.parts[0]);
    for (size_t i(0); i < combo.size(); i++) {
      if (combo[i] == 0) {
        ans += line_op.parts[i + 1];
      } else if (combo[i] == 1) {
        ans *= line_op.parts[i + 1];
      }
    }
    if (ans == line_op.ans) {
      return line_op.ans;
    }
  }

  return 0;
}

long line_solution2(LineOp &line_op) {
  auto combinations(generate_operands(line_op.parts.size() - 1, 3));

  for (auto &combo : combinations) {

    long ans(line_op.parts[0]);
    for (size_t i(0); i < combo.size(); i++) {
      if (combo[i] == 0) {
        ans += line_op.parts[i + 1];
      } else if (combo[i] == 1) {
        ans *= line_op.parts[i + 1];
      } else {
        // Concatenation
        ans = ans * pow(10, static_cast<int>(log10(line_op.parts[i + 1])) + 1) +
              line_op.parts[i + 1];
      }
    }
    if (ans == line_op.ans) {
      return line_op.ans;
    }
  }

  return 0;
}

auto part1() {
  std::fstream input("day_07_input.txt");
  std::string line;
  long count(0);
  LineOp line_op;
  while (std::getline(input, line)) {
    line_op = read_line(line);
    count += line_solution(line_op);
  }

  return count;
}

auto part2() {
  std::fstream input("day_07_input.txt");
  std::string line;
  long count(0);
  LineOp line_op;
  while (std::getline(input, line)) {
    line_op = read_line(line);
    count += line_solution2(line_op);
  }

  return count;
}

int main() {
  auto p1(part1());
  std::cout << "Part 1 answer: " << p1 << "\n";
  auto p2(part2());
  std::cout << "Part 2 answer: " << p2 << "\n";
}
