#include <bits/stdc++.h>
using namespace std;

//g++ -std=c++11 -O2 -Wall review.cpp -o review
//run with ./review

int main() {
    // input_output();

}

void number_review() {
    // most cp programs will use long long
    long long x = 123456789123456789LL;

    // floating point
    printf("%.9f\n", x) // prints to 9 decimals
}

void io_review() {
    // typical cout/cin
    ios::sync_with_stdio(0); // use these
    cin.tie(0); // makes cin/cout faster

    string s;
    cin >> s;
    cout << "hello " << s << "\n";

    // alternative input/output: 
    int a, b;
    scanf("%d %d", &a, &b); // takes input AND outputs
    printf("%d, %d\n", a, b); // more lower level, usable in C. Biggest difference is that it requires format specifiers while cout is type safe

    // getting a full line
    // note: getline() reads whole line. cin takes chars up to first whitespace.
    string s;
    getline(cin, s);

    // loop that keeps taking input!
    // ***ends when ctrl+d or when reading file, end of file reached
    // string x;
    // while (cin >> x) {
    //     //code
    // }

    // file io
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
}