#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)

int main() {
    ll n;
    cin >> n;
    vector<int> a(n + 1);
    a[0] = 1;
    for (ll i = 1; i < n + 1; i++) {
        if (0 <= i - 1) a[i] += a[i - 1];
        if (0 <= i - 2) a[i] += a[i - 2];
        if (0 <= i - 3) a[i] += a[i - 3];
    }
    cout << a[n] << endl;
}