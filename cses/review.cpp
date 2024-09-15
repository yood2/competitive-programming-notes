#include <bits/stdc++.h>
using namespace std;

typedef long long ll; // typedef for long long -> ll
#define F first; // can define a macro like this, v[i].first -> v[i].F

#define REP(i,a,b) for (int i=a; i<=b; i++); // macro that simplifies loops?!???!
// for (int i=1;i<=n;i++) -> REP(i,1,n)

//g++ -std=c++11 -O2 -Wall review.cpp -o review
//run with ./review

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

void number_review() {
    // most cp programs will use long long
    ll x = 123456789123456789LL;
    // printf("%lld", x);

    // floating point
    float y = 0.1234567890;
    printf("%.9f\n", y); // prints to 9 decimals

    // beware floating point errors!
    // compare floating point nums and assume equal if difference is less than e
    float a = 1.09999998, b=1.099999999;
    if (abs(a-b) < 1e-9) {
        cout << "yay, equal\n";
    } else {
        cout << "not equal? huh\n";
    }
}

void math_review() {
    // sum formula
        // \sum^n_{x=1}x = \frac{n(n+1)}{2}
        // \sum^n_{x=1}x^2 = \frac{n(n+1)(2n+1)}{6}
    
    // sum of arithmetic progression
        // \frac{n(a+b)}{2}
            // n = # of numbers, a = first number, b = last number
    
    // geometric progression
        // \frac{bk-a}{k-1}
            // a = first num, b = last num, k = ratio between consecutive nums

    // harmonic sum
        // \sum^n_{x=1} 1/x

    // set theory
        // intersection = elements in both A and B
        // union = elements that are in A or B or both
        // complement = elements of A not in B in the universal set
        // difference = elements in A but not in B
    
    // logic
        // negation
        // conjunction
        // disjunction
        // implication
        // equivalence
}

int main() {
    // io_review();
    // number_review();
}