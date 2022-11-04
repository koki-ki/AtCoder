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
    ll n;
    cin >> n;
    string s;
    cin >> s;
    ll cnt = 1;
    ll ans = 0;
    rep(i, n) {
        if (s[i] == s[i + 1]) {
            cnt++;
        } else {
            ans += cnt * (cnt - 1) / 2;
            cnt = 1;
        }
    }
    cout << ans << endl;
}