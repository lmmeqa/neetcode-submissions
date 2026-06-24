class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> answer = new ArrayList<List<String>>();
        Map<String,Integer> seen = new HashMap<String, Integer>();
        for(String word: strs){
           boolean skip = false;
            for(String key: seen.keySet()){
                if(isAnagram(key, word)){
                    answer.get(seen.get(key)).add(word);
                    skip = true;
                }
                
            }
            if(skip) continue;
            ArrayList<String> newSection = new ArrayList<String>();
            newSection.add(word);
            answer.add(newSection);
            seen.put(word, seen.size());
          
        
        }
        return answer;
    }
    
    private boolean isAnagram(String s1, String s2){
        if(s1.length()!=s2.length()) return false;
        char[] charsInWord = new char[26];
        for(int i = 0; i<s1.length(); i++){
            charsInWord[s1.charAt(i)-'a']++;
            charsInWord[s2.charAt(i)-'a']--;
        }
        for(char charInWord:charsInWord){
            if(charInWord != 0) return false;
        }
        return true;
    }
}
