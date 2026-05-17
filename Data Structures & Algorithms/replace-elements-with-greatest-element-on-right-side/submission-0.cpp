class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int len = arr.size();
        int bigger = -1;
        for (int i = len - 1; i > -1; i--) {
            if (bigger > arr[i]) {
                arr[i] = bigger;
            } else {
                int help = arr[i];
                arr[i] = bigger;
                bigger = help;
            }
        }

        arr[len-1] = -1;

        return arr;
    }
};