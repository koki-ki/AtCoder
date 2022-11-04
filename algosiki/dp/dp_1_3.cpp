#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)

int main() {
    ll n;
    cin >> n;
    vector<int> a(n + 1);
    a[0] = 1;
    a[1] = 1;
    for (ll i = 2; i <= n; i++) {
        a[i] = a[i - 1] + a[i - 2];
    }
    cout << a[n] << endl;
}