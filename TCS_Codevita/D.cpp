#include<bits/stdc++.h>
using namespace std;
typedef pair<int, int> iPair;
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define SET(a,b) memset(a,b,sizeof(a))
#define rep1(i, a, b) for (int i = (a); i < (b); ++i)
#define rep(i, n) rep1(i, 0, n)
#define sc(n) scanf("%d",&n)
#define sout(n) printf("%s\n",n)
#define dout(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define lldout(n) printf("%lld\n",n)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)
#define mod 1000000007
// #define int long long int
int pwr(int base,int p){
int ans = 1;while(p){if(p&1)ans=((ans%mod)*(base%mod))%mod;base=((base%mod)*(base%mod))%mod;p/=2;}return ans;
}
int gcd(int a, int b){
      if(b == 0)  return a;
    return gcd(b, a%b);
}
int powr(int base, int p){
int ans = 1;while(p){if(p&1)ans=(ans*base);base=(base*base);p/=2;}return ans;
}
int dx[] = {1,1,-1,-1,1,-1,0,0};
int dy[] = {1,-1,1,-1,0,0,1,-1};
bool solve(vector<int> set, int n, int sum)
{
    
    bool subset[n+1][sum+1];
    for (int i = 0; i <= n; i++)
      subset[i][0] = true;
    for (int i = 1; i <= sum; i++)
      subset[0][i] = false;
    for (int i = 1; i <= n; i++)
    {
       for (int j = 1; j <= sum; j++)
       {
            if(j<set[i-1])
                subset[i][j] = subset[i-1][j];
            if (j >= set[i-1])
                subset[i][j] = subset[i-1][j] || subset[i - 1][j-set[i-1]];
       }
    }
    for(int i =1;i<=sum;i++){
        if(!subset[n][i])
            return 0;
    }
    return true;
}
int main(){ 
    int n;
    sc(n);
    vector<int> v;
    for(int i = 1;i<=15;i++){
        v.PB(i);
    }
    vector<vector<int> > ans,ans1,ans2,ans3,ans4;
    int minn = n;
    int minn_sum = INT_MAX,maxx = INT_MAX;
    double median = 100000; 
    for(int i = 0;i<(1<<15);i++){
        vector<int> v1;
        int s = 0;
        for(int j = 0;j<15;j++){
            if(i & (1<<j)){
                v1.PB(v[j]);
            }
        }
        if(solve(v1 , v1.size() ,n)){
           ans.PB(v1);
           if(minn > v1.size())
                minn = v1.size();
        }
    }
    int l = ans.size();
    rep(i,l){
        int s = 0;
        int x = ans[i].size();
        rep(j,x){
            s+=ans[i][j];
        }
        if(x == minn && s==n){
            ans1.PB(ans[i]);
            maxx = min(maxx , ans[i][x-1]);
        }
    }
    l = ans1.size();
    rep(i,l){
        int x = ans1[i].size();
        if(maxx == ans1[i][x-1]){
            ans2.PB(ans1[i]);
            double ss;
            if(x & 1)
                ss = ans1[i][x/2];
            else{
                ss = (ans1[i][(x/2)-1]+ans1[i][x/2])/(2*1.0);
            } 
            median = min(ss , median);
        }
    }
    l = ans2.size();
    rep(i,l){
        int x = ans2[i].size();
        double ss;
        if(x & 1)
            ss = ans2[i][x/2];
        else{
            ss = (ans2[i][(x/2)-1]+ans2[i][x/2])/(2*1.0);
        } 
        if(median == ss)
            ans3.PB(ans2[i]);
    }
    l = ans3.size();
    rep(i,l){
        int x = ans3[i].size();
        cout<<"{";
        rep(j,x){
            if(j != x-1)
                cout<<ans3[i][j]<<",";
            else
                cout<<ans3[i][j];
        }
        cout<<"}";
        if(i!=l-1)
            cout<<"OR";
    }
    return 0;
} 
