"""
Given an array of words and an array of sentences, determine which words are anagrams of each other.
 Calculate how many sentences can be created by replacing any word with one of its anagrams, 
 Example wordSet = ['listen' 'silent, 'it', 'is'] sentence = "listen it is silent Determine that listen is an anagram of silent. 
 Those two words can be replaced with their anagrams.
 The four sentences that can be created are:  listen it is silent  listen it is listen  silent it is silent silent it is listen
"""
words = ["bats","tabs","in","cat","act"]
sentences = ["cat the bats", "in the act", "act tabs in"]
# words = ["listen", "silent", "it", "is"]
# sentences = ["listen it is silent"]

def calulateWord(words, sentences):
    ref = {}
    for word in words:
        x = list(word)
        x.sort()
        sortedWord = "".join(x)
        if sortedWord in ref.keys():
            ref[sortedWord] = ref[sortedWord] + 1
        else:
            ref[sortedWord] = 1
    resp = []
    for sentence in sentences:
        words = sentence.split()
        count = 1
        # c2 = 0
        for word in words:
            x = list(word)
            x.sort()
            sortedWord = "".join(x)
            if sortedWord in ref.keys() and ref[sortedWord] > 1:
                count = count * ref[sortedWord]
                # c2 += ref[sortedWord]
        resp.append(count)
    
    return resp

print(calulateWord(words, sentences))
