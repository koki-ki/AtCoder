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

typedef pair<ll, ll> P;
vl dx = {1, 0, -1, 0};
vl dy = {0, 1, 0, -1};

int main() {
    ll r, c;
    cin >> r >> c;
    ll sy, sx, gy, gx;
    cin >> sy >> sx >> gy >> gx;
    queue<P> que;
    vvl d[r][c];
    vector<vector<char>> maze(r, vector<char>(c));
    rep(i, r) rep(j, c) cin >> maze[i][j];
    rep(i, r) rep(j, c) d[i][j] = INF;
    que.push(P(sy, sx));
    d[sy][sx] = 0;
    while (que.size()) {
        P p = que.front();
        que.pop();
        if (p.first == gy && p.second == gx) break;

        rep(i, 4) rep(j, 4) {
            ll nx = p.first + dx[i];
            ll ny = p.second + dy[i];
            .if (0 <= nx && nx < c && 0 <= ny && ny < r &&
                 maze[ny][nx] != '#' && d[ny][dx] == INF) {
                que.push(P(ny, nx));
                d[ny][nx] = d[p.first][p.second] + 1;
            }
        }
    }
    cout << d[gy][gx] << endl;
}