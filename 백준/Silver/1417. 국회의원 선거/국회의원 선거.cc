#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <queue>

#define endl '\n'
#define npos string::npos

using namespace std;

int solve(int dasom, priority_queue<int> pq) {
    int ans{0};
    while (!pq.empty() && dasom <= pq.top()) {
        pq.push(pq.top()-1);
        pq.pop();
        ++ans;
        ++dasom;
    }

    return ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n, dasom;
    cin >> n >> dasom;

    priority_queue<int> pq;
    int tmp;
    while (--n) {
        cin >> tmp;
        pq.push(tmp);
    };

    cout << solve(dasom, pq) << endl;

    return 0;
}