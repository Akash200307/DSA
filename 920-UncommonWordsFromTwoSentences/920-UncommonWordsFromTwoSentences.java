// Last updated: 2/3/2026, 9:38:11 PM
import java.util.*;

class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        // Split the sentences into words
        String[] words1 = s1.split(" ");
        String[] words2 = s2.split(" ");

        // Create a frequency map
        Map<String, Integer> freqMap = new HashMap<>();
        for (String word : words1) {
            freqMap.put(word, freqMap.getOrDefault(word, 0) + 1);
        }
        for (String word : words2) {
            freqMap.put(word, freqMap.getOrDefault(word, 0) + 1);
        }

        // Find uncommon words (frequency == 1)
        List<String> uncommonWords = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : freqMap.entrySet()) {
            if (entry.getValue() == 1) {
                uncommonWords.add(entry.getKey());
            }
        }

        // Return the uncommon words as an array
        return uncommonWords.toArray(new String[0]);
    }
}