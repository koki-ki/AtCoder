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

double distance(ll i, ll j, ll k, ll l){
    return sqrt((i - k) ^ 2 + (j - l) ^ 2);
}

int main() {
    ll n, m;
    cin >> n >> m;
    vector<pair<ll, ll>> dij;
    for(int di = -n; di < n; di++){
        for(int dj = -n; dj < n; dj++){
            if(di * di + dj * dj == m) dij.emplace_back(di, dj);
        }
    }
    const ll INF = 1001001001;
    vector dist(n, vector<ll>(n, INF));
    queue<pair<ll, ll>> q;

}