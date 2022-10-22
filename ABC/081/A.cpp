#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)

int main() {
    string s;
    cin >> s;
    ll ans = 0;
    rep(i, 3) {
        if (s[i] == '1') ans++;
    }
    cout << ans << endl;
}