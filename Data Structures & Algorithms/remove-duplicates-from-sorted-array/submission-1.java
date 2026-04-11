class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        int k = n;
        if (n < 2) {
            return 1;
        }
        for (int i = 0; i < n - 1; ++i) {
            if (nums[i] == 101) {
                break;
            }
            if (nums[i] == nums[i + 1]) {
                k -= 1;
                i -= 1;
                for (int j = i + 1; j < k; ++j) {
                    nums[j] = nums[j + 1];
                    if (j + 1 == k) {
                        nums[j + 1] = 101;
                    }
                }
            }
        }
        return k;
    }
}