#include <bits/stdc++.h>
using namespace std;
/* alias */
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vl = vector<ll>;
using vvl = vector<vector<ll>>;
using vs = vector<string>;
using Graph = vector<vector<ll>>;

/* define short */
#define pb push_back
#define mp make_pair

/* repeat macro */
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)

void rec(ll v, const vvl &chs) {
    cout << v << " ";
    for (auto ch : chs[v]) {
        rec(ch, chs);
    }
}

int main() {
    ll n;
    cin >> n;
    vvl chs(n);
    rep2(v, 1, n - 1) {
        ll p;
        cin >> p;
        chs[p].pb(v);
    }
    rec(0, chs);
    cout << endl;
}