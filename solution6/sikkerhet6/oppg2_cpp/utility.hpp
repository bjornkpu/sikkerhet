#pragma once

#include <iostream>

std::string replace(std::string str) {
  size_t pos = str.find("&");
  while (str.find("&", pos) != std::string::npos) {
    str = str.replace(pos, 1, "&amp");
    pos = str.find("&", pos + 1);
  }
  pos = str.find("<");
  while (str.find("<", pos) != std::string::npos) {
    str = str.replace(pos, 1, "&lt");
    pos = str.find("<", pos + 1);
  }
  pos = str.find(">");
  while (str.find(">", pos) != std::string::npos) {
    str = str.replace(pos, 1, "&gt");
    pos = str.find(">", pos + 1);
  }

  return str;
}
