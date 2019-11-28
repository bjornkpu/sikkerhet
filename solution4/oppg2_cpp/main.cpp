#include <iostream>
using namespace std;

string replace(string str) {
  size_t pos = str.find("&");
  while (str.find("&", pos) != string::npos) {
    str = str.replace(pos, 1, "&amp");
    pos = str.find("&", pos + 1);
  }
  pos = str.find("<");
  while (str.find("<", pos) != string::npos) {
    str = str.replace(pos, 1, "&lt");
    pos = str.find("<", pos + 1);
  }
  pos = str.find(">");
  while (str.find(">", pos) != string::npos) {
    str = str.replace(pos, 1, "&gt");
    pos = str.find(">", pos + 1);
  }

  return str;
}

int main() {
  string str("Hello & < > & < > && << >>");
  cout << str << endl;
  cout << replace(str) << endl;
}