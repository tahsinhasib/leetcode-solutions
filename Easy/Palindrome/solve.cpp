class Solution {
public:
    bool isPalindrome(int x) {
        long long int rem = 0;
        long long int rev = 0;
        long long int stored = x;

        while(x > 0){
            rem = x % 10;
            rev = (rev * 10) + rem;
            x /= 10;
        }
        if(stored == rev){
            return true;
        }
        return false;
    }
};