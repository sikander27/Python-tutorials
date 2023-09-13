def CountingAnagrams(input):
    words = input.split()
    anagrams = {}
    word_set = set()
    for word in words:
        if word in word_set:
            continue
        sort_word = sorted(word)
        anagrams[tuple(sort_word)] = anagrams.get(tuple(sort_word), 0) + 1
        word_set.add(word)
    values = anagrams.values()
    result = list(filter(lambda x: x > 1, values))

    return len(result)


print('Test 1 passed: {}'.format(CountingAnagrams('cars are very cool so are arcs and my os') == 2))
print('Test 2 passed: {}'.format(CountingAnagrams('a b c d run urn urn') == 1))
print('Test 2 passed: {}'.format(CountingAnagrams('a b c run run urn urn') == 1))
print('Test 2 passed: {}'.format(CountingAnagrams('a b c run urn unr') == 1))
print('Test 2 passed: {}'.format(CountingAnagrams('this is going great.') == 0))
print('Test 2 passed: {}'.format(CountingAnagrams('') == 0))