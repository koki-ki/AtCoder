#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)
#define rep2(i, s, n) for (ll i = s; i < (ll)n; i++)
using Graph = vector<vector<ll>>;

int main() {
    map<string, int> score;
    score["Alice"] = 100;
    score["Bob"] = 89;
    score["Charlie"] = 95;
    cout << score.at("Alice") << endl;
    cout << score.at("Bob") << endl;
    cout << score.at("Charlie") << endl;
}