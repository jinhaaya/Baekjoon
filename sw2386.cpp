#include <stdio.h>
#include <stdlib.h>

#define MAX_N 1000000000

int main()
{
    int T, N, Ai;
    scanf("%d", &T);

    for (int t = 0; t < T; t++)
    {
        int *lst = (int *)malloc(sizeof(int) * MAX_N);
        int sum_nums = 0;

        scanf("%d", &N);

        for (int i = 0; i < N; i++)
        {
            scanf("%d", &Ai);
            lst[Ai] = 1 - lst[Ai];
            if (lst[Ai] == 1)
                sum_nums++;
            else
                sum_nums--;
        }

        printf("#%d %d\n", t + 1, sum_nums);
        free(lst);
    }

    return 0;
}
