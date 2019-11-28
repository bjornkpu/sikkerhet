#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *str_replace(char *orig, char *rep, char *with) {
  char *result;
  char *ins_point;
  char *tmp;
  int len_front;
  int count;
  int len_rep = strlen(rep);
  int len_with = strlen(with);

  // Teller hvor mye vi må utvide
  ins_point = orig;
  for (count = 0; (tmp = strstr(ins_point, rep)); ++count) {
    ins_point = tmp + len_rep;
  }
  // Setter av plassen i minnet
  tmp = result = malloc(strlen(orig) + (len_with - len_rep) * count + 1);

  if (!result) //om allokeringen feilet hopper vi ut
    return NULL;

  while (count--) {
    ins_point = strstr(orig, rep);
    len_front = ins_point - orig;
    tmp = strncpy(tmp, orig, len_front) + len_front;
    tmp = strcpy(tmp, with) + len_with;
    orig += len_front + len_rep;
  }
  strcpy(tmp, orig);
  return result;
}

char *escaper(char *message) {
  message = str_replace(message, "&", "&amp");
  message = str_replace(message, "<", "&lt");
  message = str_replace(message, ">", "&gt");
  return message;
}

int main() {
  char *message = "hei & < > && << >>";
  printf("%s\n", message);
  printf("%s\n", escaper(message));
}
