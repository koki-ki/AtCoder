#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)

int main() {
    ll h, w;
    cin >> h >> w;
    bool goodx[110];
    bool goody[110];
    string board[110];
    rep(i, h) cin >> board[i];
    rep(i, h) rep(j, h) {
        if (board[i][j] == '#') {
            goodx[i] = true;
            goody[j] = true;
        }
    }
    rep(i, h) {
        if (goodx[i]) {
            rep(j, w) {
                if (goody[j]) {
                    cout << board[i][j];
                }
            }
        }
        cout << endl;
    }
}