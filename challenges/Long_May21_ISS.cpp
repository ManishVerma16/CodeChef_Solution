#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    // ios_base::sync_with_stdio(false);
    // cin.tie(NULL);
    ll t;
    cin >> t;
    while(t--){
        ll x;
        cin >>x;
        ll count=0;
        for (int i=1; i<=2*x; i++)
        {
            count += __gcd(x+i*i, x+(i+1)*(i+1));
        }
        cout << count << endl;
    }
    return 0;
}

