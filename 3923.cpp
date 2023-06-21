#include <cstdio>
int main()
{
    int a, b, d, B, S, i, j, k;
    while (1)
    {
        scanf("%d %d %d", &a, &b, &d);
        if (a == 0 && b == 0 && d == 0)
            break;
        B = b;
        S = a;
        if (a > b)
        {
            B = a;
            S = b;
        }
        for (i = 1;; i++)
        {
            for (j = 0; j <= i; j++)
            {
                k = i - j;
                if (B * j == S * k + d || B * j + d == S * k || B * j + S * k == d)
                    goto finished;
            }
        }
    finished:
        if (a > b)
            printf("%d %d\n", j, k);
        else
            printf("%d %d\n", k, j);
    }
}