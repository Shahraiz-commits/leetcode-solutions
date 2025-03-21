#include<stack>
#include<string>
class Solution {
public:
    bool isValid(std::string s) {
    std::stack<char> opStack;
 
    for(char c : s){
        if(c == '(' || c == '[' || c == '{') opStack.push(c);
        else {
            if(opStack.empty()) return false; // no corresponding open bracket
            char compare = opStack.top();
            opStack.pop();
            if(c==')' && compare!=(c-1)) return false;
            if(c!=')' && compare!=(c-2)) return false;
        }
    }
    if(!opStack.empty()) return false;
    return true;
        
    }
};