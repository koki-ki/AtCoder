#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)
using Graph = vector<vector<ll>>;
using pll = pair<ll, ll>;

void rec(ll v, const vector<vector<ll>> &chs) {
    cout << v << " ";
    for (auto ch : chs[v]) {
        rec(ch, chs);
    }
}

int main() {
    ll n;
    cin >> n;
    vector<vector<ll>> chs(n);
    rep2(v, 1, n) {
        ll p;
        cin >> p;
        chs[p].push_back(v);
    }
    rec(0, chs);
    cout << endl;
}