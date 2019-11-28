#include "assert.hpp"
#include "utility.hpp"
#include <cstring>

int main() {
  char *str = "";
  ASSERT(replace(str) == "");

  str = "Hello & < > & < >";
  ASSERT(replace(str) == "Hello &amp &lt &gt &amp &lt &gt");

  str = "&& << >>";
  ASSERT(replace(str) == "&amp&amp &lt&lt &gt&gt");
}
