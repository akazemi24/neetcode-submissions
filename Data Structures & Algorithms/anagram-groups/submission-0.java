class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> occurence = new HashMap<>();
        for (String s : strs){
            int[] count = new int[26];
            for (char c : s.toCharArray()){
                count[c - 'a'] ++;
            }
            String key = Arrays.toString(count);
            occurence.putIfAbsent(key, new ArrayList<>());
            occurence.get(key).add(s);
        }
        return new ArrayList<>(occurence.values());
    
    }
}
