#include <iostream>
#include <vector>

int f(int a, int b) {
    if (a > b) return 1;
    if (a == b) return 0;
    if (a < b) return -1;
    return 0;
}

int main() {
    int t;
    std::cin >> t;

    while (t--) {
        int a, b, c, d;
        std::cin >> a >> b >> c >> d;

        int ans = 0;
        if (f(a, c) + f(b, d) > 0) ans++;
        if (f(a, d) + f(b, c) > 0) ans++;
        if (f(b, c) + f(a, d) > 0) ans++;
        if (f(b, d) + f(a, c) > 0) ans++;

        std::cout << ans << std::endl;
    }

    return 0;
}