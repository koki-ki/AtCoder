#include <bits/stdc++.h>
using namespace std;

// 連結リストの各ノード
struct Node {
    Node* nex;     // 次がどのノードを指すか
    string value;  // ノードに付随している値
    Node(const string& value = "") : nex(NULL), value(value) {}
};

// 番兵を表すノード (ここではグローバルに置いておく)
Node* nil;

// 連結リストの初期化
void init() {
    nil = new Node();
    nil->nex = nil;  // 初期状態では nil が nil を指すように
}

// 連結リストへ先頭への要素の挿入
void insert(Node* v) {
    v->nex = nil->nex;  // v の次を、現在の先頭に
    nil->nex = v;       // 先頭を v に書き換える
}

int main() {
    // 連結リストの初期化
    init();

    int Q;
    cin >> Q;
    for (int query = 0; query < Q; ++query) {
        int type;
        cin >> type;
        if (type == 0) {
            string S;
            cin >> S;

            // ノードを作成する
            Node* v = new Node(S);
            insert(v);
        } else {
            int k;
            cin >> k;

            // 先頭から k 個
            Node* v = nil;
            for (int i = 0; i < k; ++i) {
                v = v->nex;
                if (v == nil) break;
                cout << v->value << " ";
            }
            cout << endl;
        }
    }
}