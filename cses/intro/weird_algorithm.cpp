#include <iostream>

using namespace std;

int main() {
    long long n;
    cin >> n;
    cout << n;
    while (n > 1) {
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = (n * 3) + 1;
        }
        cout << " " << n;
    }
    return 0;
}

// g++ -std=c++11 -O2 -Wall -o <output_file> <source_file>
