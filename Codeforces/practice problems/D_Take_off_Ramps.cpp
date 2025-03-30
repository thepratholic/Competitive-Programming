#include <bits/stdc++.h>
#define int long long
#define pb push_back
#define mp make_pair
using namespace std;

map<int, vector<pair<pair<int, int>, int>>> adj;
set<pair<int, int>> sb;
map<int, int> d;
map<int, pair<int, int>> dad;
set<int> v;
int t;

void print(int u)
{
    if (u == 0)
    {
        cout << t << endl;
        return;
    }
    if (dad[u].second != -1)
        t++;
    print(dad[u].first);
    if (dad[u].second != -1)
        cout << dad[u].second + 1 << " ";
}
main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int n, l;
    cin >> n >> l;
    v.insert(0);
    v.insert(l);
    adj[0].pb(mp(mp(l, l), -1));
    for (int i = 0; i < n; i++)
    {
        int x, dt, t, p;
        cin >> x >> dt >> t >> p;
        if (x >= p)
        {
            adj[x - p].pb(mp(mp(x + dt, p + t), i));
            v.insert(x - p);
            v.insert(x + dt);
        }
    }
    while (v.size())
    {
        int a = *v.begin();
        v.erase(v.begin());
        int b = *v.begin();
        adj[a].pb(mp(mp(b, abs(b - a)), -1));
        adj[b].pb(mp(mp(a, abs(b - a)), -1));
    }
    d[0] = 0;
    dad[0] = mp(-1, -1);
    sb.insert(mp(0, 0));
    while (sb.size())
    {
        int x = sb.begin()->second;
        sb.erase(sb.begin());
        for (int i = 0; i < adj[x].size(); i++)
        {
            auto y = adj[x][i];
            int u = y.first.first, e = y.first.second, ind = y.second;
            if (d[u] == 0 || d[u] > d[x] + e)
            {
                sb.erase(mp(d[u], u));
                d[u] = d[x] + e;
                dad[u] = mp(x, ind);
                sb.insert(mp(d[u], u));
            }
        }
    }
    cout << d[l] << endl;
    print(l);
    return 0;
}
