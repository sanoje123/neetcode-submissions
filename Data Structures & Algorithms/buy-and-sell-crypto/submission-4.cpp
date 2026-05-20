class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() < 2) return 0;

        int buyDay = 0, sellDay = 1;
        int maxProf = 0;

        while (sellDay < prices.size()) {
            if (prices[buyDay] < prices[sellDay]) {
                int profit = prices[sellDay] - prices[buyDay];
                maxProf = max(maxProf, profit);
            }
            else {
                buyDay = sellDay;
            }

            sellDay++;
        }
        return maxProf;
    }
};
