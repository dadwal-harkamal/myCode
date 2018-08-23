class flip_and_invertImg {
    public int[][] flipAndInvertImage(int[][] A) {
      int[][] answer = new int[A.length][A[0].length];
        int k = 0;
        for(int i = 0; i < A.length; i++ ){
            for(int j = A[0].length-1; j>=0;j--){
            answer[i][j] = A[i][k];
            k++;
            if(answer[i][j] == 1){
                answer[i][j] = 0;
            }
            else{
                   answer[i][j] = 1; 
                }
        }
        k = 0;
           return answer;
    }
    
    // Found belwo soln on leetcodesweb site need to uderstand it a bit more
     
       /* int C = A[0].length;
        for (int[] row: A)
            for (int i = 0; i < (C + 1) / 2; ++i) {
                int tmp = row[i] ^ 1;
                row[i] = row[C - 1 - i] ^ 1;
                row[C - 1 - i] = tmp;
            }

        return A;/*
}
       
    
}
