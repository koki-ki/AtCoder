#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)
using Graph = vector<vector<ll>>;

int main() {
    ll n, m;
    cin >> n >> m;
    Graph G(n);
    ll a, b;
    rep(i, m) {
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }
    ll student = -1;
    ll max_num = -1;
    rep(v, n) {
        ll num = (ll)G[v].size();
        if (max_num < num) {
            max_num = num;
            student = v;
        }
    }
    sort(G[student].begin(), G[student].end());
    for (auto v : G[student]) {
        cout << v << " ";
    }
    cout << endl;
}