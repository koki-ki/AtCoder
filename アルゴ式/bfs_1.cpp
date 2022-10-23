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

/* define short */
#define pb push_back
#define mp make_pair

/* repeat macro */
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)

int main() {
    ll n, m;
    cin >> n >> m;
    Graph g(n);
    rep(i, m) {
        ll a, b;
        cin >> a >> b;
        g[a].pb(b);
        g[b].pb(a);
    }
    vl dist(n, -1);
    vvl nodes(n);

    dist[0] = 0;
    nodes[0] = {0};

    rep2(k, 1, n) {
        for (auto v : nodes[k - 1]) {
            for (auto next_v : g[v]) {
                if (dist[next_v] != -1) {
                    continue;
                }

                dist[next_v] = dist[v] + 1;
                nodes[k].pb(next_v);
            }
        }
    }
    rep(k, n) {
        sort(nodes[k].begin(), nodes[k].end());
        for (auto v : nodes[k]) {
            cout << v << " ";
        }
        cout << endl;
    }
    cout << endl;
}