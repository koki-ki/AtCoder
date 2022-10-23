#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)

int main() {
    ll n;
    cin >> n;
    vector<int> a(n);
    rep(i, n) cin >> a[i];
    vector<int> s(n);
    s[1] = a[1];
    for (ll i = 2; i < n; i++) {
        s[i] = min(s[i - 1] + a[i], s[i - 2] + 2 * a[i]);
    }
    cout << s[n - 1] << endl;
}