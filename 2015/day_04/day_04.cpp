#include <fstream>
#include <iostream>
#include <openssl/evp.h>

std::string read_input() {
  std::ifstream file{"input.txt"};
  std::string contents;
  getline(file, contents);
  return contents;
}

std::string md5(const std::string &content) {
  EVP_MD_CTX *context = EVP_MD_CTX_new();
  const EVP_MD *md = EVP_md5();
  unsigned char md_value[EVP_MAX_MD_SIZE];
  unsigned int md_len;
  std::string output;

  EVP_DigestInit_ex2(context, md, NULL);
  EVP_DigestUpdate(context, content.c_str(), content.length());
  EVP_DigestFinal_ex(context, md_value, &md_len);
  EVP_MD_CTX_free(context);

  output.resize(md_len * 2);
  for (unsigned int i = 0; i < md_len; ++i)
    std::sprintf(&output[i * 2], "%02x", md_value[i]);
  return output;
}

int main() {
  std::string const alpha{read_input()};
  std::string hashed;
  std::string modified;
  std::string ns;
  int n{0};

  while (true) {
    ns = std::to_string(n);
    modified = alpha + ns;
    hashed = md5(modified);
    if (hashed.substr(0, 5) == "00000") {
      break;
    }
    ++n;
  }
  std::cout << hashed << "\n";
  std::cout << "PT1 Answer: " << ns << "\n";

  while (true) {
    ns = std::to_string(n);
    modified = alpha + ns;
    hashed = md5(modified);
    if (hashed.substr(0, 6) == "000000") {
      break;
    }
    ++n;
  }
  std::cout << hashed << "\n";
  std::cout << "PT2 Answer: " << ns << "\n";
}
