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
using pll = pair<ll, ll>;

const ll MOD = 1000000007;
const ll INF = 2000000000;
/* define short */
#define pb push_back
#define mp make_pair

/* repeat macro */
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)

void quick_sort(vl &v) {
    if (!v.size()) return;
    vl L, R;
    ll x = v.size() / 2;
    rep(i, v.size()) {
        if (i == x) continue;
        if (v[i] < v[x])
            L.pb(v[i]);
        else
            R.pb(v[i]);
    }
    quick_sort(L);
    quick_sort(R);

    L.push_back(v[x]);
    L.insert(L.end(), R.begin(), R.end());
    v = L;
}

int main() {
    ll n;
    cin >> n;
    vl a(n);
    rep(i, n) cin >> a[i];
    quick_sort(a);
    rep(i, a.size()) cout << a[i] << " ";
    cout << endl;
}