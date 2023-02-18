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

int main() {
    string abc;
    cin >> abc;
    ll a = ll(abc[0] - '0');
    ll b = ll(abc[1] - '0');
    ll c = ll(abc[2] - '0');
    ll ans = (a + b + c) * 100 + (a + b + c) * 10 + (a + b + c);
    cout << ans << endl;
}