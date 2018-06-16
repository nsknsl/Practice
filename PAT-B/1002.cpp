#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;
int main()
{
  string a;
  cin >> a;
  int sum = 0;
  for(int i=0; i< a.length(); i++)
  {
    int digit = a[i] - '0';
    sum += digit;
  }
  string s = to_string(sum);
  string digits[10] = {"ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"};
  for(int i=0; i< s.length(); i++ )
  {
    int mark = s[i] - '0';
    if (i< s.length() -1)
    {
      cout<<digits[mark]<<" ";
    }
    else{
      cout<<digits[mark];
    }
  }
  return 0;
}