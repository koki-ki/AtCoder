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
    vl a(n);
    rep(i, n) cin >> a[i];
    ll q;
    cin >> q;
    vl b(q);
    rep(i, q) cin >> b[i];

    sort(a.begin(), a.end());
    rep(i, q) {
        auto pos1 = lower_bound(a.begin(), a.end(), b[i]);
        ll Diff1 = INF, Diff2 = INF;
        if (*pos1 <= n) Diff1 = abs(b[i] - a[*pos1]);
        if (*pos1 >= 2) Diff2 = abs(b[i] - a[*pos1 - 1]);
        cout << min(Diff1, Diff2) << endl;
    }
}