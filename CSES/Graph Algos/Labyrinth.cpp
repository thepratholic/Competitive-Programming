#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<string> grid(n);
    for (int i = 0; i < n; i++) {
        cin >> grid[i];
    }

    vector<vector<bool>> vis(n, vector<bool>(m, false));
    vector<vector<pair<int,int>>> parent(n, vector<pair<int,int>>(m, {-1, -1}));
    vector<vector<char>> prev_dir(n, vector<char>(m, 0));

    pair<int,int> start, end;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == 'A') start = {i, j};
            if (grid[i][j] == 'B') end = {i, j};
        }
    }

    int dr[4] = {0, 1, -1, 0};
    int dc[4] = {1, 0, 0, -1};
    char dch[4] = {'R', 'D', 'U', 'L'};

    queue<pair<int,int>> q;
    q.push(start);
    vis[start.first][start.second] = true;

    bool found = false;

    while (!q.empty() && !found) {
        auto [r, c] = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr >= 0 && nr < n && nc >= 0 && nc < m &&
                grid[nr][nc] != '#' && !vis[nr][nc]) {

                vis[nr][nc] = true;
                parent[nr][nc] = {r, c};
                prev_dir[nr][nc] = dch[i];
                q.push({nr, nc});

                if (make_pair(nr, nc) == end) {
                    found = true;
                    break;
                }
            }
        }
    }

    if (!vis[end.first][end.second]) {
        cout << "NO\n";
        return 0;
    }

    cout << "YES\n";

    string path;
    pair<int,int> cur = end;

    while (cur != start) {
        char ch = prev_dir[cur.first][cur.second];
        path.push_back(ch);
        cur = parent[cur.first][cur.second];
    }

    reverse(path.begin(), path.end());

    cout << path.size() << "\n";
    cout << path << "\n";

    return 0;
}
