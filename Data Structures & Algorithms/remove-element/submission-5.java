class Solution {
    public int removeElement(int[] nums, int val) {
        int l = 0;
        int r = 1;
        int n = nums.length;
        if (n == 0) {
            return 0;
        }
        if (n < 2 && nums[0] == val) {
            return 0;
        }
        boolean flag00 = false;
        boolean flag01 = false;
        Arrays.sort(nums);
        while (r < n) {
            if (nums[l] == val) {
                while(r < n && nums[r] == val) {
                    if (r + 1 == n) {
                        flag01 = true;
                        break;
                    }
                    ++r;
                }
                nums[l] = nums[r];
                flag00 = true;
            }
            if (flag00) {
                nums[l] = nums[r];
            }
            if (flag01) {
                break;
            }
            ++l;
            ++r;
        }
        return (flag00) ? l : l + 1;
    }
}