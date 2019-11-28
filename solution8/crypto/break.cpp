#include "break.hpp"
#include <string>
#include <ctime>
using namespace std;

int main() {
  string alfabet = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMDNUPQRSTUVWXYZÆØÅ1234567890"; // QwE
  string hash = "ab29d7b5c589e18b52261ecba1d3a7e7cbf212c6";
  string salt = "Saltet til Ola";
  int keylength = (hash.length()/2);
  int itterasjoner = 2048;
  //size_t passord_lengde = 3; //bugged, fungerer ikke. må hardkode lengden
  char passord[3];
  std::clock_t    start;
  
  // Length 1
  cout<<"Kalkulerer for passwordlengde 1... "<<flush;
  start = std::clock();
  for (char c : alfabet) {
    passord[0] = c;
    string key = hex(kcs5(passord, salt, itterasjoner, keylength));
    if (key == hash) {
      cout << endl <<"Fant passordet: "<< passord<<endl;
      return 0;
    }
  }
  cout<< "fant ingen."<<"  "<<(std::clock() - start) / (double)(CLOCKS_PER_SEC / 1000) << " ms"<<endl;
  
  // Length 2
  cout<<"Kalkulerer for passwordlengde 2... "<<flush;
  for (char c1 : alfabet) {
    passord[0] = c1;
    for (char c2 : alfabet) {
      passord[1] = c2;
      string key = hex(kcs5(passord, salt, itterasjoner, keylength));
      if (key == hash) {
        cout << endl<< "Fant passordet: "<< passord<<endl;
        return 0;
      }
    }
  }
  cout<< "fant ingen."<<"  "<<(std::clock() - start) / (double)(CLOCKS_PER_SEC) << " s"<<endl;
  
  // Length 3
  cout<<"Kalkulerer for passwordlengde 3... "<<flush;
  for (char c1 : alfabet) {
    passord[0] = c1;
    for (char c2 : alfabet) {
      passord[1] = c2;
      for (char c3 : alfabet) {
        passord[2] = c3;
        string key = hex(kcs5(passord, salt, itterasjoner, keylength));
        
        
        if (key == hash) {
          cout << "Fant passordet: "<< passord<<"  "<<(std::clock() - start) / (double)(CLOCKS_PER_SEC) << " s"<<endl;
          return 0;
        }
      }
    }
  }
  cout<< "fant ingen."<<"  "<<(std::clock() - start) / (double)(CLOCKS_PER_SEC) << " s"<<endl;
}