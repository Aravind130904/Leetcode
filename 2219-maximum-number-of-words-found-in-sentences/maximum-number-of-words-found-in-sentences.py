class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_len=0
        for sentence in sentences:
            word_len=0
            for word in sentence:
                if word==" ":
                    word_len+=1
            if word_len>max_len:
                max_len=word_len
        return max_len+1