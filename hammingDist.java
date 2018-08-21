class hammingDist {
    public int hammingDistance(int x, int y) {
        int bitcounter=0;
        for (int i=0;i<32;++i)
        {
            if((((x^y) >> i)&1) > 0)
                ++bitcounter;
        }
        return bitcounter;
    }
}
