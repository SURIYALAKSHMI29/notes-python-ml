"""
Given a list of sentences:
- Filter out sentences that have less than 4 words.
- Convert all remaining sentences to lowercase.
- Count the total number of characters across all filtered sentences (ignore spaces).

Solve this using filter, map, and reduce (or a combination of them).
"""

from functools import reduce

sentences = [
    "I love machine learning",
    "Python is amazing for NLP",
    "Natural Language Processing is fun",
    "Deep learning models are powerful",
]


def display(content, title):
    print(title)
    print(len(content))
    for c in content:
        print(c)
    print()


sentences_gt_4_words = list(
    filter(lambda sentence: len(sentence.split()) >= 4, sentences)
)
display(sentences_gt_4_words, "Sentences that have less than 4 words are removed,")

sentences_gt_4_words_lower = list(map(str.lower, sentences_gt_4_words))
display(sentences_gt_4_words_lower, "Converting remaining sentences to lowercase,")

total_no_of_chars = reduce(
    lambda total, sentence: total + len(sentence.replace(" ", "")),
    sentences_gt_4_words_lower,
    0,
)
print(total_no_of_chars)
