#include <bits/stdc++.h>

#define NEMOX ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#define ll  long long
#define loop(n) for(ll i=0;i<n;i++)
#define loopj(n)    for(int j=0;j<n;j++)
#define endl "\n"
#define all(v) ((v).begin()),((v).end())
#define allr(v) ((v).rbegin()), ((v).rend())
#define out(v)  for(int&i:v)cout<<i<<' ';
#define pp(x)   push_back(x)
#define yes "YES"
#define no "NO"
using namespace std;
int dx[] = {0, 0, 1, -1, 1, -1, 1, -1}; // 8 directions
int dy[] = {1, -1, 0, 0, 1, -1, -1, 1}; // 8 directions
int dxx[] = {-2, -1, 1, 2, 2, 1, -1, -2}; // for chess knights
int dyy[] = {1, 2, 2, 1, -1, -2, -2, -1}; // for chess knights
const int oo = 0x3f3f3f3f;
const ll ooll = 0x3f3f3f3f3f3f3f3f;
const int N = 2e5 + 4, mod = 1e9 + 7;

ll n, d, k, m;

//dsadadadadadadasdsad
int main() {
    NEMOX
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    int t = 1;
    cin>>t;
    while (t--) {
        int l,r,a ; cin>>l>>r>>a;
        ll x = r/a + l%a;
        ll y = (r-1)/a + (r-1)%a;
        if(a-1>=l && a-1<=r){
            x= (a-1);

            y= r/a + r%a;
            cout<<max(x,y)<<endl;
        }else {
            if(r%a==0) r--;
            x== (r-1)/a + (r-1)%a;
            y=r/a + r%a;
            cout<<max(x,y)<<endl;
        }
    }

    return 0;
}