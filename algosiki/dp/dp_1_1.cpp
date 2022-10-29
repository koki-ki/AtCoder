#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)

int main() {
    ll n, x, y;
    cin >> n >> x >> y;
    vector<int> a(n);
    a[0] = x;
    a[1] = y;
    for (ll i = 2; i < n; i++) {
        a[i] = (a[i - 1] + a[i - 2]) % 100;
    }
    cout << a[n - 1] << endl;
}