class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
      /*  int left = 0;
        int right = nums.size()-1;
        int mid;
        if(target> nums[right-1]){
            return right;
        }
        while(left< right){
             mid = left + (right -left)/2;
            if(nums[mid]== target){
                return mid;
            }else if(nums[mid]< target){
                left = mid +1;
            }else{
                right = mid -1;
            }
        }
        return left;*/
        // the array is sorted approach is - binary search 
        // in binary search we know uppper bound and lower bound
        int n = nums.size();
        int lb = n;
        int low = 0;
        int high = n-1;
        while(low<=high){
            int mid = low + (high - low)/2;
            if(nums[mid] == target){
                return mid;
            }
            if (nums[mid]> target){
                lb = mid;
                high = mid-1;
            }else{
                low = mid + 1;
            }
        }
        


        return lb;
    }
};