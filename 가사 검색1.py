class Trie:
    def __init__(self):
        self.child = dict()
        self.cnt = 0

    def insert(self, string):
        curr = self
        for chara in string:
            curr.cnt += 1 # 링크타고 내려가기전에 cnt 증가
            if chara not in curr.child:
                curr.child[chara] = Trie()

            curr = curr.child[chara]
        curr.cnt += 1

    def search(self, string):
        curr = self
        for chara in string:
            if chara == '?':
                return curr.cnt
            if chara not in curr.child:
                return 0
            curr = curr.child[chara]
        return curr.cnt

def solution(words, queries):
    TrieRoot = [Trie() for _ in range(10000)]
    ReTrieRoot = [Trie() for _ in range(10000)]
    answer = []

    for string in words:
        TrieRoot[len(string)-1].insert(string)
        ReTrieRoot[len(string) - 1].insert(string[::-1])

    for string in queries:
        if string[0] != '?':
            answer.append(TrieRoot[len(string)-1].search(string))
        else:
            answer.append(ReTrieRoot[len(string)-1].search(string))
        return answer
