// Last updated: 3/21/2026, 11:27:26 PM
1class Solution {
2    public int characterReplacement(String s, int k) {
3        int l = 0;
4        int lon = 0;
5        int[] counts = new int[26];
6
7        for (int r = 0; r < s.length(); r++) {
8            counts[s.charAt(r) - 'A']++;
9
10            while ((r - l + 1) - getMax(counts) > k) {
11                counts[s.charAt(l) - 'A']--;
12                l++;
13            }
14
15            lon = Math.max(lon, r - l + 1);
16        }
17        return lon;
18    }
19
20    private int getMax(int[] counts) {
21        int max = 0;
22        for (int c : counts) {
23            max = Math.max(max, c);
24        }
25        return max;
26    }
27}
28