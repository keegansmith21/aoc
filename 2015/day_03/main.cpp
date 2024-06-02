#include <fstream>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

string stringify_coords(vector<int> loc) {
  string str_loc;
  str_loc = to_string(loc[0]) + "," + to_string(loc[1]);
  return str_loc;
}

int part_1(string instructions) {
  vector<int> location_1{0, 0};
  unordered_map<string, int> umap;

  // Add 0, 0 to map
  umap[stringify_coords(location_1)] = 1;

  for (char c : instructions) {
    if (c == '^') {
      ++location_1[1];
    }
    if (c == 'v') {
      --location_1[1];
    }
    if (c == '>') {
      ++location_1[0];
    }
    if (c == '<') {
      --location_1[0];
    }
    umap[stringify_coords(location_1)] = 1;
  }
  return umap.size();
}

int part_2(string instructions) {
  vector<int> location_1{0, 0};
  vector<int> location_2{0, 0};
  vector<int> *proxy_loc;
  int count{0};

  unordered_map<string, int> umap;

  // Add 0, 0 to map
  umap[stringify_coords(location_1)] = 1;

  for (char c : instructions) {
    ++count;
    if (count % 2 == 0) {
      proxy_loc = &location_2;
    } else {
      proxy_loc = &location_1;
    };
    if (c == '^') {
      ++(*proxy_loc)[1];
    }
    if (c == 'v') {
      --(*proxy_loc)[1];
    }
    if (c == '>') {
      ++(*proxy_loc)[0];
    }
    if (c == '<') {
      --(*proxy_loc)[0];
    }
    umap[stringify_coords(*proxy_loc)] = 1;
  }
  return umap.size();
}

int main() {
  ifstream file{"input.txt"};
  string instructions;

  // Read file to instructions
  if (file.is_open()) {
    getline(file, instructions);
  }

  int pt1 = part_1(instructions);
  cout << "Pt1 Answer: " << pt1 << endl;

  int pt2 = part_2(instructions);
  cout << "Pt2 Answer: " << pt2 << endl;
};
