#include<iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int len, a, b;
        cin >> len >> a >> b;
        string s;
        cin >> s;
        if (a * b >= 0 && (a > 0 || b > 0)) cout << (a + b) * len << "\n";
        else if (b == 0) cout << (a + b) * len << "\n";
        else {
            if (a < b && !(a < 0 && b < 0)) cout << (a + b) * len << "\n";
            else {
                int counter = 0;
                for (int i = 1; i < s.length(); i++) if (s[i] != s[i - 1]) counter++;
                if (counter == 0) cout << (a * len) + b << "\n";
                else cout << (((counter + 1) / 2) + 1) * b + (a * len) << "\n";
            }
        }
    }
}
