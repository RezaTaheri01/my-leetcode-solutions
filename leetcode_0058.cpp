#include <string>
using namespace std;

class Solution
{
public:
    int lengthOfLastWord(string s)
    {
        int counter = 0;

        for (int i = s.length() - 1; i >= 0; i--)
        {
            if (s[i] != ' ')
                counter++;
            else if (counter != 0)
                break;
        }

        return counter;
    }
};

#include <iostream>

int main() {
    Solution sol;
    string test = "Hello World";
    cout << sol.lengthOfLastWord(test) << endl;  // Output: 5
    return 0;
};