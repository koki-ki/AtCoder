#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)

int main() {
    ll n;
    cin >> n;
    vector<int> a(n);
    rep(i, n) cin >> a[i];
    ll alice = 0, bob = 0;
    sort(a.begin(), a.end());
    reverse(a.begin(), a.end());
    rep(i, n) {
        if (i % 2 == 0)
            alice += a[i];
        else
            bob += a[i];
    }
    cout << alice - bob << endl;
}