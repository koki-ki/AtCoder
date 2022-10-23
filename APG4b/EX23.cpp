#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)
using Graph = vector<vector<ll>>;

int main() {
    ll n;
    cin >> n;
    vector<int> a(n);
    rep(i, n) cin >> a[i];
    map<ll, ll> cnt;
    for (ll x : a) {
        if (cnt.count(x))
            cnt[x]++;
        else
            cnt[x] = 1;
    }
    ll max_cnt = 0;
    int ans = -1;
    for (ll x : a) {
        if (max_cnt < cnt[x]) {
            max_cnt = cnt[x];
            ans = x;
        }
    }
    cout << ans << " " << max_cnt << endl;
}