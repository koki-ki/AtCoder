#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)

int main() {
    vector<vector<int>> data(3, vector<int>(4));
    data = {{7, 4, 0, 8}, {2, 0, 3, 5}, {6, 1, 7, 0}};
    ll cnt = 0;
    rep(i, 3) rep(j, 4) {
        if (data[i][j] == 0) cnt++;
    }
    cout << cnt << endl;
}