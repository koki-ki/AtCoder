#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)
using Graph = vector<vector<ll>>;
using pll = pair<ll, ll>;

int main() {
    ll n, x;
    cin >> n >> x;
    vector<ll> a(n);
    rep2(i, 1, n - 1) cin >> a[i];

    ll ans = 0;
    while (x != 0) {
        ans++;
        x = a[x];
    }
    cout << ans << endl;
}