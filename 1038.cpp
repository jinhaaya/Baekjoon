#include <stdio.h>
#include <stdlib.h>

int *sep(int n)
{
    int *lst = (int *)malloc(20 * sizeof(int)); // allocate memory for the array
    int idx = 0;
    if (n == 0)
    {
        lst[idx++] = 0;
    }
    while (n != 0)
    {
        lst[idx++] = n % 10;
        n = n / 10;
    }
    lst[idx] = -1; // add a sentinel value to mark the end of the array
    return lst;
}

int is_decreasing(int *nums)
{
    int j = 0;
    while (nums[j + 1] != -1)
    {
        if (nums[j] < nums[j + 1])
        {
            return 0;
        }
        j++;
    }
    return 1;
}

int main()
{
    int N, idx = 0;
    int *res = (int *)malloc(1000001 * sizeof(int)); // allocate memory for the array
    scanf("%d", &N);
    for (int i = 0; i <= 987654321; i++)
    {
        int *nums = sep(i);
        if (is_decreasing(nums))
        {
            res[idx++] = i;
        }
        if (idx >= N + 1)
        {
            break;
        }
    }
    if (idx <= N)
    {
        printf("-1\n");
    }
    else
    {
        printf("%d\n", res[N]);
    }
    for (int i = 0; i < N; i++)
        printf("[%d]/n", res[N]);
    free(res); // free memory
    return 0;
}
