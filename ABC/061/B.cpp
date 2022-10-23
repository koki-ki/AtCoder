#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)

int main() {
    ll n, m;
    cin >> n >> m;
    vector<int> cnt(n);
    rep(i, m) {
        ll a, b;
        cin >> a >> b;
        a--;
        b--;
        cnt[a]++;
        cnt[b]++;
    }
    rep(i, n) cout << cnt[i] << endl;
}