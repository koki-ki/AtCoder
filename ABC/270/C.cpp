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
    ll n, x, y;
    cin >> n >> x >> y;
    vvl to(n + 1);
    rep(i, n - 1){
        ll a, b;
        cin >> a >> b;
        to[a].pb(b);
        to[b].pb(a);
    }

    vl ans;
    auto dfs = [&](auto f, int v, int p=-1) -> bool {
        if(v == x){
            ans.pb(v);
            return true;
        }
        for (ll u: to[v]){
            if(u == p) continue;
            if(f(f, u, v)){
                ans.pb(v);
                return true;
            }
        }
        return false;
    };
    dfs(dfs, y);
    rep(i, ans.size()) cout << ans[i] << ' ';
    cout << endl;
    return 0;
}
