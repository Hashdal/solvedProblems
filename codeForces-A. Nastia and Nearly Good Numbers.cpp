#include<iostream>

using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        long long a, b;
        cin >> a >> b;
        long long x, y, z;
        int counter = 2;
        bool check = true;
        if (b == 1) {
            cout << "NO" << "\n";
            continue;
        }
        if (check) {
            counter = 1;
            x = a * b;
            y = counter * a;
            while (!((x + y) % a == 0)) {
                if ((counter + b) % b == 0) {
                    counter ++;
                }
                y *= counter;
            }
            cout << "YES" << "\n" << x << " " << y << " " << x + y << "\n";
        }
        
    }
}
