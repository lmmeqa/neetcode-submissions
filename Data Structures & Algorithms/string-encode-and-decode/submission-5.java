class Solution {

    public String encode(List<String> strs) {
        if(strs.size() == 0) return "";
        String lens = "";
        String res = "";
        for(String word: strs){
            res+=word;
            lens+=word.length() + ",";
        }
        return res + "." + lens.substring(0,lens.length()-1);
    }

    public List<String> decode(String str) {
        System.out.println(str);
        if(str.length() == 0) return new ArrayList<String>();
        if(str.equals(".0")) {
            List<String> res = new ArrayList<String>();
            res.add("");
            return res;}
        String[] lensNcode = str.split("\\.");
        String[] lenstr = lensNcode[1].split(",");
        String code = lensNcode[0];
        String[] res = new String[lenstr.length];
        int[] lens = new int[lenstr.length];
        System.out.println(str);
        for(int i = 0; i< lenstr.length; i++){
            
            lens[i] = Integer.parseInt(lenstr[i]);

        }

        for(int i = 0, j = 0; i < code.length() && j<res.length; i+=(lens[j]),j++){
            System.out.println(code + " before " + lens[j]);
            System.out.println(code.length() + " " + i + " " + lens[j]);
            res[j] = code.substring(i, i + lens[j]);
            
            System.out.println(code + " after " + lens[j]);

        }
        return Arrays.asList(res);
    }
}
