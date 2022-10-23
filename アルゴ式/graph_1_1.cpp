#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)
using Graph = vector<vector<int>>;

int main() {
    ll n, a, b;
    cin >> n >> a >> b;
    vector<string> s(n);
    for (auto &str : s) cin >> str;
    if (s[a][b] == 'o')
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
}