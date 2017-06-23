#include <stdio.h>
#include <stdlib.h>

int least_change(int sum, int num_of_coins, int *coins)
{
	int *table;
	int val, coin_idx, prev_min;

	if (coins == NULL)
		return 0;
	/* each idx represent a sum, needs to have idx table[sum] */
	table = calloc(0, (sum + 1) * sizeof(int));
	if (table == NULL)
		return 0;
	for (val = 1; val <= sum; val++)
	{
		for (coin_idx = 0; coin_idx < num_of_coins; coin_idx++)
		{
			if (coins[coin_idx] < val)
			{
				/* gives the previous min of coins*/
				prev_min = table[val - coins[coin_idx]];
				if (table[val] == 0 || prev_min + 1 < table[val])
					table[val] = prev_min + 1;
			}
		}
	}
	return (table[sum]);
}

int main(void)
{
	int coins[] = {9, 6, 5, 1};
	int sum, num_of_coins;

	num_of_coins = sizeof(coins)/sizeof(int);
	sum = 11;
	printf("Least coins: %d\n",least_change(sum, num_of_coins, coins));
}
