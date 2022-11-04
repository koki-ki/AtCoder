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

const ll MOD = 998244353;
const ll INF = 2000000000;
/* define short */
#define pb push_back
#define mp make_pair

/* repeat macro */
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)

int main() {
    const ll p = 998244353;
    vl a(6);
    rep(i, 6) {
        cin >> a[i];
        a[i] %= p;
    }
    ll abc = a[0] * a[1] % p * a[2] % p;
    ll def = a[3] * a[4] % p * a[5] % p;
    ll ans = (abc - def + p) % p;
    cout << ans << endl;
}