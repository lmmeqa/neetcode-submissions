class Solution {
    public boolean isPalindrome(String s) {
       s = s.toLowerCase();
       String strippedS = "";
       for(int i = 0; i < s.length(); i++){
        char current = s.charAt(i);
        if( (current>='a' && current<='z') || (current>='0' && current<='9')) strippedS += current;
       }
       if(strippedS.length() <=1) return true;
       if(strippedS.length()==2 && strippedS.charAt(0) != strippedS.charAt(strippedS.length()-1)) return false;
       boolean even = false;
       if(strippedS.length()%2 == 0) even = true;
        for(int i = 0; i< strippedS.length(); i++){
            if(even && strippedS.charAt(i) != strippedS.charAt(strippedS.length()-1-i)) return false;
            if(!even && strippedS.charAt(i) != strippedS.charAt(strippedS.length()-1-i) && (i != Math.floor(strippedS.length()/2)+1 )) return false;
        }
        return true;
    }
}
