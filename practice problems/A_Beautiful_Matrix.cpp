#include<bits/stdc++.h>
#define ll long long
#define ull signed long long int
#define int64 int64_t
#define mod 1000000007
#define repi(x,y,z) for(ll i=x;i<=y;i+=z)
#define repj(x,y,z) for(ll j=x;j<=y;j+=z)
#define repk(x,y,z) for(ll k=x;k<=y;k+=z)
#define pb push_back
#define con continue
#define eb emplace_back
#define ub upper_bound
#define lb lower_bound
#define mod1 998244353
#define nl '\n'
#define ff first
#define ss second
#define all(x) x.begin(),x.end()
#define accending(a,n) sort(a,a+n)
#define decending(a,n) sort(a,a+n,greater<ll>())
#define sortacc(v) sort(v.begin(),v.end())
#define sortde(v) sort(v.rbegin(),v.rend())
#define rev(v) reverse(v.begin(),v.end())
#define mapll map<ll,ll>
#define vecll vector<ll>
#define revrepi(x,y,z) for(ll i=x;i>=y;i-=z)
#define revrepj(x,y,z) for(ll j=x;j>=y;j-=z)
#define INF 1e9
using namespace std;
const ll MAX_CHAR = 256;

bool isprime(ll n);
bool ispallindrome(string s);
void primeFactors(ll n,vector<ll> &v);
void yes();
void no();
ll count_set_bit(ll n);
bool isPerfectSquare(ll x);
ll nCrModp(ll n,ll r,ll p);
bool is_power2(ll n);
ll add(ll x,ll y);
ll multiply(ll x,ll y);
ll power(ll x,ll y,ll p);
bool is_sorted(ll a[],ll n);
void get_factors(ll n,set<ll> &st);
ll SieveOfEratosthenes(ll n);
bool is_prime(ll x);
bool is_sub(string &s,string &t);
bool is_sort(vecll v);

// ll lsb_setbit_no(ll x1)
// {
//     ll set_bit_no = x1 & ~(x1 - 1);
//     return set_bit_no;
//     cin.tie(NULL);
// }

void solve() {
    vector<vector<int>> matrix(5, vector<int> (5));

    for(int i = 0; i < 5; i++) {
        for(int j = 0; j < 5; j++) {
            cin >> matrix[i][j];
            if(matrix[i][j] == 1) {
                cout << abs(2 - i) + abs(2 - j) << endl;
                break;
            }
        }
    }

}

int main()
{
    // ll tc;
    // cin >> tc;
    // while (tc--)
    // {
    solve();
    // }
    return 0;
}

bool isprime(ll n)
{
    bool flag = true;
    for (ll i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
        {
            flag = false;
            break;
        }
    }
    if (n <= 1)
    {
        flag = false;
    }
    return flag;
}
bool ispallindrome(string s)
{
    string t(s.rbegin(), s.rend());
    return (t == s);
}
ll nCrModp(ll n, ll r, ll p)
{
    if (r > n - r)
        r = n - r;
    ll C[r + 1];
    memset(C, 0, sizeof(C));
    C[0] = 1;
    for (ll i = 1; i <= n; i++)
    {
        for (ll j = min(i, r); j > 0; j--)
        {
            C[j] = (C[j] + C[j - 1]) % p;
        }
    }
    return C[r];
}
void primeFactors(ll n, vector<ll> &v)
{
    while (n % 2 == 0)
    {
        v.pb(2);
        n = n / 2;
    }
    for (ll i = 3; i <= sqrt(n); i = i + 2)
    {
        while (n % i == 0)
        {
            v.pb(i);
            n = n / i;
        }
    }
    if (n > 2)
        v.pb(n);
}
void yes()
{
    cout << "YES" << nl;
}
void no()
{
    cout << "NO" << nl;
}
ll count_set_bit(ll n)
{
    ll count = 0;
    while(n != 0)
    {
        if(n & 1 == 1)
        {
            count++;
        }
        n = n >> 1; // right shift 1 bit
    }
    return count;
}
bool isPerfectSquare(ll x)
{
    if (x >= 0)
    {
        ll sr = sqrt(x);
        return (sr * sr == x);
    }
    return false;
}
bool is_power2(ll n)
{
    if(n & (n - 1))
    {
        return false;
    }
    else
    {
        return true;
    }
}
ll add(ll x, ll y)
{
    ull ans = (((x % mod) + (y % mod)) % mod);
    if(ans < 0)
    {
        ans += mod;
    }
    return ans;
}
ll multiply(ll x, ll y)
{
    ll ans = (((x % mod) * (y % mod)) % mod);
    return ans;
}
ll power(ll x, ll y, ll p)
{
    ll res = 1;
    x = x % p;
    if(x == 0)
    {
        return 0;
    }
    while(y > 0)
    {
        if(y & 1)
        {
            res = multiply(res, x);
        }
        x = multiply(x, x);
        y = (y / 2);
    }
    return res;
}
bool is_sorted(ll a[], ll n)
{
    repi(1, n - 1, 1)
    {
        if(a[i] < a[i - 1])
        {
            return false;
        }
    }
    return true;
}
bool is_sortedstring(string s, ll n)
{
    repi(1, n - 1, 1)
    {
        if(s[i] < s[i - 1])
        {
            return false;
        }
    }
    return true;
}
void get_factors(ll n, set<ll> &st)
{
    vecll v;
    for(ll i = 2; i * i <= n; i++)
    {
        if(n % i == 0)
        {
            st.insert(i);
            st.insert((n / i));
        }
    }
}
ll SieveOfEratosthenes(ll n)
{
    ll c = 0;
    bool prime[n + 1];
    memset(prime, true, sizeof(prime));
    for (int p = 2; p * p <= n; p++)
    {
        if (prime[p] == true)
        {
            for (int i = p * 2; i <= n; i += p)
                prime[i] = false;
        }
    }
    for (int p = 2; p <= n; p++)
        if (prime[p])
            c++;
    return c;
}
bool is_prime(ll x)
{
    for(ll i = 2; i <= sqrt(x); i++)
        if(x % i == 0)
        {
            return false;
        }
    return true;
}
bool is_sub(string &s, string &t)
{
    ll n = s.size(), m = t.size();
    int x = 0;
    repi(0, n - 1, 1)
    {
        if(s[i] == t[x])
        {
            x++;
            if(x == m)
            {
                return true;
            }
        }
    }
    return false;
}
bool is_sort(vecll v)
{
    vecll v1 = v;
    sortacc(v1);
    if(v1 == v)
    {
        return true;
    }
    else
    {
        return false;
    }
}