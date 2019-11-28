#include "utility.hpp"
#include <cstring>
#include <iostream>
using namespace std;

int main() {
  char *str = "Hello & < > & < >";
  std::cout << replace(str) << std::endl;

  str = "&& << >>";
  std::cout << replace(str) << std::endl;
}