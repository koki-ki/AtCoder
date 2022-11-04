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

const ll MOD = 1000000007;
const ll INF = 2000000000;
/* define short */
#define pb push_back
#define mp make_pair

/* repeat macro */
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)

// 幅優先探索
void search(const Graph &G, ll s) {
    ll n = (ll)G.size();

    vector<bool> seen(n, false);
    queue<ll> todo;
    seen[s] = true;
    todo.push(s);

    while (!todo.empty()) {
        ll v = todo.front();
        todo.pop();

        for (ll x : G[v]) {
            if (seen[x]) continue;
            seen[x] = true;
            todo.push(x);
        }
    }
}

int main() {}
