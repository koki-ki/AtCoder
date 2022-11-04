#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)
using Graph = vector<vector<ll>>;
using pll = pair<ll, ll>;
using vl = vector<ll>;
using vvl = vector<vector<ll>>;

void rec(ll v, ll p, vl &depth, const vvl &chs) {
    if (v == 0) {
        depth[v] = 0;
    } else {
        depth[v] = depth[p] + 1;
    }
    for (auto ch : chs[v]) {
        rec(ch, v, depth, chs);
    }
}

int main() {
    ll n;
    cin >> n;
    vvl chs(n);
    rep2(v, 1, n) {
        ll p;
        cin >> p;
        chs[p].push_back(v);
    }
    vl depth(n);
    rec(0, -1, depth, chs);
    for (auto d : depth) cout << d << endl;
}