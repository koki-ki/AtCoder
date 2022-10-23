#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)
using Graph = vector<vector<ll>>;

int main() {
    ll n, m, x;
    cin >> n >> m >> x;
    Graph g(n);
    ll a, b;
    rep(i, m) {
        cin >> a >> b;
        g[a].push_back(b);
        g[b].push_back(a);
    }
    set<ll> friends;
    for (auto v : g[x]) friends.insert(v);
    set<ll> result;
    for (auto v : friends) {
        for (auto w : g[v]) {
            if (x != w && !friends.count(w)) {
                result.insert(w);
            }
        }
    }
    cout << result.size() << endl;
}