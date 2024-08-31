#include <iostream>

using namespace std;

int sum_of_digits(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    int k;
    cin >> k;
    
    int count = 0;
    int num = 19; // Starting point, 19 is the smallest perfect number

    while (count < k) {
        if (sum_of_digits(num) == 10) {
            count++;
        }
        if (count < k) {
            num++;
        }
    }

    cout << num << endl;
    
    return 0;
}
