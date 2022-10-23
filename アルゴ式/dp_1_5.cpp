#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)

int main() {
    ll n, m;
    cin >> n >> m;
    vector<ll> a(n);
    rep(i, n) cin >> a[i];
    vector<ll> s(n, pow(10, 10));
    s[0] = 0;
    for (ll i = 1; i < n; i++) {
        for (ll j = 1; j < m; j++) {
            if (0 <= i - j) s[i] = min(s[i], s[i - j] + j * a[i]);
        }
    }
    cout << s[n - 1] << endl;
}