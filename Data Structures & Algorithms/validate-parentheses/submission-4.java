class Solution {
    public boolean isValid(String s) {
        String opened = "";
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(isOpener(c)) opened += c;
            else{
                if(opened.length() == 0) return false;
                if(!checker(opened.charAt(opened.length()-1),c)) return false;
                else{
                    opened = opened.substring(0,opened.length()-1);
                }
            }
        }
        if(opened.length() == 0)return true;
        return false;
        
    }
    public boolean isOpener(char c){
        if(c == '(' || c == '{' || c == '[') return true;
        return false;
    }
    public boolean checker(char one, char two){
        switch(one){
            case '(':
                return two == ')';
            case '{':
                return two == '}';
            case '[':
                return two == ']';
        }
        return false;
    }
}
