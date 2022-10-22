#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)

int main() {
    ll a, b;
    cin >> a >> b;
    if ((a * b) % 2 == 1) {
        cout << "Odd" << endl;
    } else {
        cout << "Even" << endl;
    }
}