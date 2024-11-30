Sure! Here’s the complete article with the LeetCode link and a test function included.

---

# LeetCode #127 - Word Ladder

## Problem Statement

Given two words, `beginWord` and `endWord`, along with a dictionary of words, your task is to find the length of the shortest transformation sequence from `beginWord` to `endWord`. Each transformed word must exist in the dictionary, and only one letter can be changed at a time. If no such transformation exists, return 0.

[LeetCode Problem Link](https://leetcode.com/problems/word-ladder/)

### Example 1

**Input:**
```
beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
```

**Output:**
```
5
```
**Explanation:** The transformation sequence is "hit" → "hot" → "dot" → "dog" → "cog".

### Example 2

**Input:**
```
beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log"]
```

**Output:**
```
0
```
**Explanation:** There is no possible transformation.

---

## mem limit exceed 

```python

from collections import deque
from typing import List

def ladderLength( beginWord: str, endWord: str, wordList: List[str]) -> int:

    def is_single_char_change(w1: str, w2: str) -> bool:
        if len(w1) != len(w2):
            return False

        diff_char_count = 0
        for a, b in zip(w1, w2):
            if a != b:
                diff_char_count += 1
                if diff_char_count > 1:
                    return False

        return diff_char_count == 1



    all_words = [beginWord]+wordList
    next_word_map = { x:[] for x in all_words}
    all_words_len = len(all_words)

    for i in range(all_words_len):
        for j in range(all_words_len):
            if(i == j):
                continue
            if(is_single_char_change(all_words[i], all_words[j])):
                next_word_map[all_words[i]].append(all_words[j])


    print(next_word_map)

    next_begins = []

    for w in all_words:
        if(is_single_char_change(beginWord, w)):
            next_begins.append(w)

    if(len(next_begins) == 0 or endWord not in all_words):
        return 0

    queue = deque([])
    queue.append((beginWord, 1, set([beginWord])))

    while(queue):
        print(f"queue:{queue}")
        current_word, current_len, visited_set = queue.popleft()

        for next_word in next_word_map[current_word]:
            if(next_word not in visited_set):
                if(next_word == endWord):
                    print(visited_set)
                    return len(visited_set)+1
                queue.append((next_word, current_len + 1 , visited_set | set([next_word])))

    return 0



# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5

# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# # 5

# beginWord ="a"
# endWord ="c"
# wordList =["a","b","c"]
# # 2


# beginWord ="lost"
# endWord ="cost"
# wordList =["most","fist","lost","cost","fish"]
# # 2


beginWord = "cet"
endWord = "ism"
# wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye"]

print(ladderLength(beginWord, endWord, wordList))


```



---


## Approach 1: Breadth-First Search (BFS)

BFS is an effective way to explore the shortest path in an unweighted graph, which fits this problem since each valid word is a node, and an edge exists between words that differ by one letter.

### Algorithm:
1. Initialize a queue with the `beginWord` and a step count of 1.
2. Use a loop to explore each word in the queue:
   - Generate all possible transformations.
   - If the new word is `endWord`, return the step count.
   - If it's valid (in the dictionary), enqueue it and remove from the dictionary.
3. If the queue is empty without finding `endWord`, return 0.

### Code:

```python
from collections import deque

def ladderLength(beginWord: str, endWord: str, wordList: set) -> int:
    if endWord not in wordList:
        return 0
    
    queue = deque([(beginWord, 1)])
    
    while queue:
        word, steps = queue.popleft()
        
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + char + word[i+1:]
                
                if new_word == endWord:
                    return steps + 1
                
                if new_word in wordList:
                    wordList.remove(new_word)
                    queue.append((new_word, steps + 1))
    
    return 0
```


=> this too still have performant issue


---

## Approach 2: Bidirectional BFS

Bidirectional BFS enhances the standard BFS approach by searching from both the start and the end simultaneously, which can reduce the search space significantly.

### Algorithm:
1. Initialize two queues, one from `beginWord` and one from `endWord`, along with their respective sets of visited words.
2. Alternate between exploring both directions:
   - Generate all possible transformations for the current word.
   - If a transformation meets the other queue, return the total number of steps.
3. Continue until a connection is found or both queues are exhausted.

### Code:

```python
def ladderLengthBidirectional(beginWord: str, endWord: str, wordList: set) -> int:
    if endWord not in wordList:
        return 0
    
    forward_queue = deque([beginWord])
    backward_queue = deque([endWord])
    forward_visited = {beginWord: 1}
    backward_visited = {endWord: 1}
    
    while forward_queue and backward_queue:
        if len(forward_queue) <= len(backward_queue):
            result = expandQueue(forward_queue, forward_visited, backward_visited, wordList)
        else:
            result = expandQueue(backward_queue, backward_visited, forward_visited, wordList)
        
        if result:
            return result
    
    return 0

def expandQueue(queue, visited_from_this_side, visited_from_other_side, wordList):
    current_word = queue.popleft()
    current_level = visited_from_this_side[current_word]
    
    for i in range(len(current_word)):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            new_word = current_word[:i] + char + current_word[i+1:]
            if new_word in visited_from_other_side:
                return current_level + visited_from_other_side[new_word]
            if new_word in wordList and new_word not in visited_from_this_side:
                visited_from_this_side[new_word] = current_level + 1
                queue.append(new_word)
                wordList.remove(new_word)
    
    return None
```

---

## Comparison of Approaches

| Approach                | Description                                          | Time Complexity       | Space Complexity     |
|-------------------------|------------------------------------------------------|-----------------------|----------------------|
| BFS                     | Explores all paths level by level from the start.   | O(N * K)              | O(N)                 |
| Bidirectional BFS       | Searches from both start and end to reduce space.    | O(N * K)              | O(N)                 |

- **N**: Number of words in the word list.
- **K**: Length of the words.

---

## Test Function

You can use the following test function to verify the implementations:

```python
def test_ladder_length(func):
    test_cases = [
        {
            "beginWord": "hit",
            "endWord": "cog",
            "wordList": set(["hot", "dot", "dog", "lot", "log", "cog"]),
            "expected": 5,
        },
        {
            "beginWord": "hit",
            "endWord": "cog",
            "wordList": set(["hot", "dot", "dog", "lot", "log"]),
            "expected": 0,
        },
        {
            "beginWord": "hit",
            "endWord": "hot",
            "wordList": set(["hot"]),
            "expected": 2,
        },
        {
            "beginWord": "a",
            "endWord": "c",
            "wordList": set(["a", "b", "c"]),
            "expected": 2,
        },
        {
            "beginWord": "leet",
            "endWord": "code",
            "wordList": set(["leet", "leet", "lote", "cote", "code"]),
            "expected": 5,
        },
        {
            "beginWord": "qa",
            "endWord": "zz",
            "wordList": set(["za", "zb", "zc", "zd", "ze", "zf", "zg", "zh", "zi", "zj", "zk", "zl", "zm", "zn", "zo", "zp", "zq", "zr", "zs", "zt", "zu", "zv", "zw", "zx", "zy", "zz"]),
            "expected": 3,
        },
    ]

    for i, case in enumerate(test_cases):
        result = func(case["beginWord"], case["endWord"], case["wordList"])
        assert result == case["expected"], f"Test case {i+1} failed: expected {case['expected']}, got {result}"

    print("All test cases passed!")

# Example usage
# test_ladder_length(ladderLength)  # Uncomment to run the tests

```

This function runs a series of test cases to validate your implementation of the Word Ladder problem. You can call `test_ladder_length` with either `ladderLength` or `ladderLengthBidirectional` to check both implementations.