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
    vl a(n);
    rep(i, n) cin >> a[i];
    rep(k, n - 1) {
        ll m = k;
        rep2(i, k, n) {
            if (a[i] < a[m]) {
                m = i;
            }
        }
        swap(a[k], a[m]);
        rep(i, n) cout << a[i] << " ";
        cout << endl;
    }
}