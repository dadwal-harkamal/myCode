class JewelsandStones {
    public int numJewelsInStones(String J, String S) {
       int res=0;
       /* unordered_set <char> jewels;
        for (int k=0;k<J.length();++k)
            jewels.insert(J[k]);
         for (int i=0;i<S.length();++i)
             if(jewels.find(S[i]) != jewels.end()) res++;
        return res;*/
        Set<Character> s = new HashSet<>();
        for (Character ch: J.toCharArray())
            s.add(ch);
        for(Character ch : S.toCharArray())
            if(s.contains(ch))
                res++;
        return res;              
        
        
}
}
