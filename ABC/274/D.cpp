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

bool f(ll x, vl a) {
    unordered_set<ll> s;
    s.insert(0);
    for (ll na : a) {
        unordered_set<ll> p;
        swap(p, s);
        for (ll nx : p) {
            s.insert(nx - na);
            s.insert(nx + na);
        }
    }
    return s.count(x);
}

int main() {
    ll n, x, y;
    cin >> n >> x >> y;
    vl a(n);
    rep(i, n) cin >> a[i];
    x -= a[0];
    vl xa, ya;
    rep2(i, 1, n) {
        if (i % 2 == 1)
            ya.pb(a[i]);
        else
            xa.pb(a[i]);
    }
    if (f(x, xa) && f(y, ya))
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
}
