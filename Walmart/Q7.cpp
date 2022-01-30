class Solution{
  public:
    vector<int> find3Numbers(vector<int> a, int n) {
       stack<int> s;
       for(int i=n-1;i>=0;i--){
           while(!s.empty()&&s.top()<=a[i])
           s.pop();    
           s.push(a[i]); 
           if(s.size()==3)break; 
       }
       vector<int> ans;
       while(!s.empty()){
           ans.push_back(s.top());
           s.pop();
       }
       if(ans.size()!=3)return {}; // when we don't get three numbers
       return ans;
   
   }
};