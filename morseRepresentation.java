class morseRepresentation {
    public int uniqueMorseRepresentations(String[] words) {
      String[] MORSE = new String[]{".-","-...","-.-.","-..",".","..-.","--.",
                         "....","..",".---","-.-",".-..","--","-.",
                         "---",".--.","--.-",".-.","...","-","..-",
                         "...-",".--","-..-","-.--","--.."};
       /* String  az = new String("abcdefghijklmnopqrstuvwxyz");
        
        Map <String,String> mp = new HashMap<>();
        Set<String> sstr = new HashSet<>();
        for(int i=0;i<az.length();++i)
        {
            mp.put(""+az.charAt(i),MORSE[i]);
        }
        
        for (String word : words)
        {
            String str = new String("");
            //Array ch[] = words[i].toCharArray();
            for (char ch: word.toCharArray())
            {
                str+=mp.get(ch);
            }
            sstr.add(str);
        }*/

       Set<String> seen = new HashSet();
        for (String word: words) {
            //StringBuilder code = new StringBuilder();
            String str = new String("");
            for (char c: word.toCharArray())
                //code.append(MORSE[c - 'a']);
                str+=MORSE[c - 'a'];
            //seen.add(code.toString());
            seen.add(str);
        }
        
        
        
        

        return seen.size();
    }
}
