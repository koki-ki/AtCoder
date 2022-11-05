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
    ll n, m;
    cin >> n >> m;
    Graph G(n);
    rep(i, m) {
        ll a, b;
        cin >> a >> b;
        G[a].pb(b);
        G[b].pb(a);
    }
    vl dist(n, -1);
    queue<ll> que;

    dist[0] = 0;
    que.push(0);

    while (!que.empty()) {
        ll v = que.front();
        que.pop();

        for (auto next_v : G[v]) {
            if (dist[next_v] != -1) {
                continue;
            }
            dist[next_v] = dist[v] + 1;
            que.push(next_v);
        }
    }
    ll result = 0;
    rep2(v, 1, n) result = max(result, dist[v]);
    cout << result << endl;
}