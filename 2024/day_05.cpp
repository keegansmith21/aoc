#include <algorithm>
#include <fstream>
#include <iostream>
#include <regex>
#include <sstream>
#include <vector>

void append_rule(std::vector<std::vector<int>> &rules, std::string &line) {
  std::regex r("(\\d+)\\|(\\d+)");
  std::smatch matches;
  std::regex_search(line, matches, r);
  int n1 = std::stoi(matches[1]);
  int n2 = std::stoi(matches[2]);
  std::vector<int> t{n1, n2};
  rules.push_back(t);
}

std::vector<int> vec_from_line(std::string &line) {
  std::string n;
  std::vector<int> v;
  std::stringstream ss(line);

  while (std::getline(ss, n, ',')) {
    v.push_back(std::stoi(n));
  }
  return v;
}

auto violated_rules(std::vector<int> &v, std::vector<std::vector<int>> &rules) {
  std::vector<std::vector<int>> v_rules;
  for (auto &r : rules) {
    auto n1_it = std::find(v.begin(), v.end(), r[0]);
    auto n2_it = std::find(v.begin(), v.end(), r[1]);
    if (n1_it != v.end() && n2_it != v.end() && n1_it > n2_it) {
      v_rules.push_back(r);
    }
  }
  return v_rules;
}

bool is_valid(std::vector<int> &v, std::vector<std::vector<int>> &rules) {
  return violated_rules(v, rules).size() == 0;
}

int pt1() {
  int ans(0);
  int count(0);
  std::string line;
  std::stringstream ss;
  std::ifstream input("day_05_input.txt");
  std::vector<std::vector<int>> rules;

  while (std::getline(input, line)) {
    if (line.empty()) {
      continue;
    } else if (line.find("|") != std::string::npos) {
      append_rule(rules, line);
    } else if (line.find(",") != std::string::npos) {
      std::vector<int> v(vec_from_line(line));
      if (is_valid(v, rules)) {
        ans += v[v.size() / 2]; // the middle
      }
    }
  }

  return ans;
}

void make_valid(std::vector<int> &v, std::vector<std::vector<int>> &rules) {
  std::vector<std::vector<int>> vrules;

  for (auto &r : rules) {
    auto n1_it = std::find(v.begin(), v.end(), r[0]);
    auto n2_it = std::find(v.begin(), v.end(), r[1]);
    if (n1_it != v.end() && n2_it != v.end()) {
      vrules.push_back(r);
    }
  }

  std::vector<int> r{0, 0};
  while (!is_valid(v, vrules)) {
    for (size_t i(0); i < v.size(); i++) {
      r[1] = v[i];
      for (size_t j(i + 1); j < v.size(); j++) {
        r[0] = v[j];
        if (std::find(vrules.begin(), vrules.end(), r) != vrules.end()) {
          std::swap(v[i], v[j]);
        }
      }
    }
  }
}

int pt2() {
  int ans(0);
  int count(0);
  std::string line;
  std::stringstream ss;
  std::ifstream input("day_05_input.txt");
  std::vector<std::vector<int>> rules;

  while (std::getline(input, line)) {
    if (line.empty()) {
      continue;
    } else if (line.find("|") != std::string::npos) {
      append_rule(rules, line);
    } else if (line.find(",") != std::string::npos) {
      std::vector<int> v(vec_from_line(line));
      if (!is_valid(v, rules)) {
        make_valid(v, rules);
        ans += v[v.size() / 2];
      }
    }
  }

  return ans;
}

int main() {
  int pt1a(pt1());
  std::cout << "Part 1 answer: " << pt1a << "\n";
  int pt2a(pt2());
  std::cout << "Part 2 answer: " << pt2a << "\n";
  return 0;
}
