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

const ll MOD = 1000000007;
const ll INF = 2000000000;
/* define short */
#define pb push_back
#define mp make_pair

/* repeat macro */
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)

int main() {
    ll n;
    cin >> n;
    vl c(n), p(n);
    rep(i, n) cin >> c[i] >> p[i];
    ll q;
    cin >> q;
    vl l(q), r(q);
    rep(i, q) cin >> l[i] >> r[i];
    rep(i, q) {
        l[i]--;
        r[i]--;
    }
    vl acc1(n + 1), acc2(n + 1);
    if (c[0] == 1)
        acc1[1] = p[0];
    else
        acc2[1] = p[0];
    rep2(i, 2, n + 1) {
        if (c[i] == 1) {
            acc1[i] = acc1[i - 1] + p[i];
            acc2[i] = acc2[i - 1];
        } else {
            acc1[i] = acc1[i - 1];
            acc2[i] = acc2[i - 1] + p[i];
        }
    }
    rep2(i, 1, q + 1) {
        ll a, b;
        a = acc1[r[i]] - acc1[l[i] - 1];
        b = acc2[r[i]] - acc2[l[i] - 1];
        cout << a << " " << b << endl;
    }
    // rep2(i, 1, n + 1) { cout << acc1[i] << " " << acc2[i] << endl; }
}
