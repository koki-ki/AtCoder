#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)

int main() {
    vector<int> vec = {1, 5, 3};
    reverse(vec.begin(), vec.end());
    rep(i, vec.size()) { cout << vec[i] << endl; }
}