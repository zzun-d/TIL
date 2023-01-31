#include <iostream>
#include <vector>

using namespace std;

int dp[32][1002];

int main()
{

    int T, W;
    cin >> T >> W;

    for (int i = 1; i <= T; i++)
    {
        int t_n;
        cin >> t_n;
        for (int j = 1; j <= W + 1 && j <= i + 1; j++)
        {
            if (t_n % 2 == j % 2)
            {
                if (dp[j][i - 1] + 1 > dp[j - 1][i - 1] + 1)
                {
                    dp[j][i] += dp[j][i - 1] + 1;
                }
                else
                {
                    dp[j][i] += dp[j - 1][i - 1] + 1;
                }
            }
            else
            {
                if (dp[j][i - 1] > dp[j - 1][i - 1])
                {
                    dp[j][i] += dp[j][i - 1];
                }
                else
                {
                    dp[j][i] += dp[j - 1][i - 1];
                }
            }
        }
    }

    int ans = 0;
    for (int i = 0; i <= W + 1; i++)
    {
        if (ans < dp[i][T])
        {
            ans = dp[i][T];
        }
    }

    cout << ans;

    return 0;
}