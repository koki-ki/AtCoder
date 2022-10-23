#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (ll i = 0; i < (ll)n; i++)

int my_min(int x, int y) {
    if (x < y)
        return x;
    else
        return y;
}
int main() {
    int answer = my_min(10, 5);
    cout << answer << endl;
}