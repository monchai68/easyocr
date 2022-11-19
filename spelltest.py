from pythainlp import correct
from pythainlp import spell
from pythainlp.spell import NorvigSpellChecker
from pythainlp.corpus import ttc  # Thai Textbook Corpus
from pythainlp import word_tokenize, Tokenizer
from pythainlp.util import normalize

from pythainlp.corpus import thai_words
words=list(thai_words())

def find_word(word):
  return [i for i in words if i.startswith(word)]
 
kum =  find_word("ตำ")
print(kum)



# text = "และเมื่อจับจ่ายอย่างฟุมเฟือย ภก็มีแต่จนลงจนลง"
# print("newmm  :", word_tokenize(text))  # default engine is "newmm"

# kum =  correct("ก์")
# print(kum)

# sp = spell("ตำ")
# print(sp)

# checker = NorvigSpellChecker(custom_dict=ttc.word_freqs())
# # sp = checker.spell("เซ็ค")
# # print(sp)
# ch = checker.correct("เตื่น")
# print(ch)

# text = "เตื่น"
# print(normalize(text))