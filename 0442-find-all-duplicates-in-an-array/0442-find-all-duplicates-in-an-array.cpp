class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        int n = size(nums);
        unordered_map<int,int>mp;
        for(int i=0;i<n;i++){
            mp[nums[i]]++;
        }
        vector<int>res;
        for(auto i : mp){
            if(i.second > 1){
            res.push_back(i.first);
            }
        }
        return res;
    }
};