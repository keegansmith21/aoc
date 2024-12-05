#include <fstream>
#include <iostream>
#include <regex>

int eval_mul(std::string &mul) {
  std::regex r("mul\\((\\d+),(\\d+)\\)");
  std::smatch matches;
  std::regex_search(mul, matches, r);
  int n1 = std::stoi(matches[1]);
  int n2 = std::stoi(matches[2]);
  /* std::cout << mul << " -- " << n1 << "*" << n2 << " = " << n1 * n2 << "\n";
   */
  return n1 * n2;
}
int mul_from_line(std::string &line) {
  int counter(0);
  std::regex r("(mul\\(\\d+,\\d+\\))");
  std::smatch matches;
  std::sregex_iterator begin(line.begin(), line.end(), r);
  std::sregex_iterator end;

  for (std::sregex_iterator i = begin; i != end; ++i) {
    std::smatch match = *i;
    std::string match_str = match.str();
    counter += eval_mul(match_str);
  }
  return counter;
}

std::string purge_dont(std::string &line) {
  std::regex r("((do\\(\\)).+?(don\\'t\\(\\)))");
  std::smatch matches;
  std::sregex_iterator begin(line.begin(), line.end(), r);
  std::sregex_iterator end;
  std::string purged("");

  for (std::sregex_iterator i = begin; i != end; ++i) {
    std::smatch match = *i;
    std::string match_str = match.str();
    purged += match_str;
  }
  /* std::cout << purged << "\n\n\n"; */
  return purged;
}

int add_muls() {
  std::ifstream input("input.txt");
  std::string line;
  int counter(0);
  while (std::getline(input, line)) {
    counter += mul_from_line(line);
  }
  return counter;
}

int add_domuls() {
  std::ifstream input("input.txt");
  std::string line;
  std::string input_str("do()");
  int counter(0);

  while (std::getline(input, line)) {
    input_str += line;
  };
  input_str += "don't()"; // Add don't to the end for regex matching

  input_str = purge_dont(input_str);
  return mul_from_line(input_str);
}

int main() {
  int pt1(add_muls());
  std::cout << "Part 1 answer: " << pt1 << "\n";
  int pt2(add_domuls());
  std::cout << "Part 2 answer: " << pt2 << "\n";
  return 0;
}
