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

using Node = pair<ll, ll>;

vl dx = {1, 0, -1, 0};
vl dy = {0, 1, 0, -1};

int main() {
    ll h, w;
    cin >> h >> w;
    ll x0, y0, x1, y1;
    cin >> x0 >> y0 >> x1 >> y1;
    vector<string> s(h);
    rep(i, h) cin >> s[i];
    vvl dist(h, vl(w, -1));
    queue<Node> que;
    dist[x0][y0] = 0;
    que.push(Node(x0, y0));

    while (!que.empty()) {
        auto [x, y] = que.front();
        que.pop();

        rep(d, 4) {
            ll x2 = x + dx[d];
            ll y2 = y + dy[d];

            if (x2 < 0 || x2 >= h || y2 < 0 || y2 >= w || s[x2][y2] == 'B') {
                continue;
            }
            if (dist[x2][y2] != -1) {
                continue;
            }
            dist[x2][y2] = dist[x][y] + 1;
            que.push(Node(x2, y2));
        }
    }

    cout << dist[x1][y1] << endl;
}