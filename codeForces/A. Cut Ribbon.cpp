#include<iostream>

using namespace std;

int main() {
    int n, a, b, c;
    cin >> n >> a >> b >> c;
    int x, y, z;
    x = y = z = 0;
    int result[] = { 0, 0, 0 };
    if (a == 1 || b == 1 || c == 1) {
        cout << n;
    }
    else {
        for (x = 0; a * x + b * y + c * z <= n; x++) {
            for (y = 0; a * x + b * y + c * z <= n; y++) {
                for (z = 0; a * x + b * y + c * z <= n; z++) {
                    if (a * x + b * y + c * z == n) {
                        if (x + y + z > result[0] + result[1] + result[2]) {
                            result[0] = x;
                            result[1] = y;
                            result[2] = z;
                        }
                    }
                }
                z = 0;
            }
            y = 0;
        }
        cout << result[0] + result[1] + result[2];
    }
}
