#include <bits/stdc++.h>
using namespace std;
/* alias */
using ll = long long;
using ull = unsigned long long;
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

vector<ll> memo;

ll rec(ll n) {
    if (n == 0) return 1;
    if (memo[n] != -1) return memo[n];
    return memo[n] = rec(n / 2) + rec(n / 3);
}

int main() {
    ll n;
    cin >> n;
    memo.assign(n + 1, -1);
    ll ans = rec(n);
    cout << ans << endl;
}