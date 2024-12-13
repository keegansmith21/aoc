#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

void print_blocks(std::vector<long> &blocks) {
  for (auto i : blocks) {
    std::cout << i;
  }
  std::cout << "\n";
}

long count_files(std::vector<long> &blocks) {
  long n_free(std::count(blocks.begin(), blocks.end(), -1));
  long n_file(blocks.size() - n_free);
  return n_file;
}

std::vector<long> input_to_blocks(std::string line) {
  // -1 represents empty space
  long n;
  std::string n_string;
  std::vector<long> blocks;
  for (std::string::size_type i(0); i < line.size(); i++) {
    n = line[i] - '0'; // Convert char to long
    if (i % 2 == 0) {
      for (long j(0); j < n; j++) {
        blocks.push_back(i / 2);
      }
    } else {
      for (long j(0); j < n; j++) {
        blocks.push_back(-1);
      }
    }
  }
  return blocks;
}

void rearrange_blocks(std::vector<long> &blocks) {
  long n_file(count_files(blocks));
  auto free_it = std::find(blocks.begin(), blocks.end(), -1);
  auto files_it = blocks.end();
  files_it--;
  // We're done when the last-most file is at index n_file - 1
  while (std::distance(blocks.begin(), files_it) != n_file - 1) {
    if (*files_it == -1) {
      files_it--;
      continue; // Force check of the condition
    }
    while (*free_it != -1) { // Find the next free space
      free_it++;
    }
    /* std::cout << "Swapping" << *files_it << " with " << *free_it << "\n"; */
    std::swap(*files_it, *free_it);
  }
}

int find_free_block(std::vector<long> &blocks, int size) {
  // Find the first chunch of free space that is >= size
  int start_i(-1), dist(-1);
  for (int i(0); i < blocks.size(); i++) {
    if (blocks[i] == -1) {
      if (start_i == -1) { // Inititalise new block to track
        start_i = i;
        dist = 0;
      }
      dist++;
    } else if (start_i != -1) {
      if (dist >= size) {
        return start_i;
      } else {
        start_i = -1; // Start a new block
      }
    }
  }

  // edge case - the last block was the only possible free space
  if (dist >= size) {
    return start_i;
  } else {
    // Return -1 for no blocks of valid size
    return -1;
  }
}

void swap_blocks(std::vector<long> &blocks, int start1, int start2, int dist) {
  for (int i(0); i < dist; i++) {
    std::swap(blocks[start1 + i], blocks[start2 + i]);
  }
}

void rearrange_blocks2(std::vector<long> &blocks) {
  int left_i(-1), right_i(-1);
  long tracking(-2);

  // We're done when we reach the start of the iterator
  for (int i(blocks.size() - 1); i > 0; i--) {
    if (tracking == -2 && blocks[i] == -1) {
      // Useless, keep iterating
      continue;
    } else if (tracking == -2 && blocks[i] != -1) {
      // Update the tracker to the new subject
      tracking = blocks[i];
      right_i = i;
    } else if (blocks[i] != tracking) {
      // Do the swapping
      left_i = i + 1;
      int n = right_i - left_i + 1;
      int free_block_start = find_free_block(blocks, n);
      if (free_block_start >= 0 && free_block_start < right_i) {
        swap_blocks(blocks, free_block_start, left_i, n);
      }
      tracking = -2;
      if (blocks[i] != -1) { // If we're currently on a new file block
        tracking = blocks[i];
        right_i = i;
      }
    }
  }
}

long calc_checksum(std::vector<long> &blocks) {
  long cs(0);
  for (long i(0); i < blocks.size(); i++) {
    if (blocks[i] != -1) {
      cs += i * blocks[i];
    }
  }
  return cs;
}
long part1() {
  std::fstream input("day_09_input.txt");
  /* std::fstream input("day_09_demo.txt"); */
  std::string line;
  input >> line;
  auto blocks = input_to_blocks(line);
  rearrange_blocks(blocks);
  return calc_checksum(blocks);
}

long part2() {
  std::fstream input("day_09_input.txt");
  /* std::fstream input("day_09_demo.txt"); */
  std::string line;
  input >> line;
  auto blocks = input_to_blocks(line);
  rearrange_blocks2(blocks);
  return calc_checksum(blocks);
}
int main() {
  long p1(part1());
  std::cout << "Part 1 answer: " << p1 << "\n";
  long p2(part2());
  std::cout << "Part 2 answer: " << p2 << "\n";
  return 0;
}
