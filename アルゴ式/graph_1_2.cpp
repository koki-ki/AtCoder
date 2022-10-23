#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)
using Graph = vector<vector<int>>;

int main() {
    ll n, m;
    cin >> n >> m;
    Graph g(n);
    rep(i, m) {
        ll a, b;
        cin >> a >> b;
        g[a].push_back(b);
    }
    rep(v, n) {
        sort(g[v].begin(), g[v].end());
        for (auto to : g[v]) cout << to << " ";
        cout << endl;
    }
}