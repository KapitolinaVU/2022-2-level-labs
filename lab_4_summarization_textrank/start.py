"""
TextRank summarizer starter
"""
from pathlib import Path
import json
import string

from lab_4_summarization_textrank.main import (SentenceEncoder,
                                               SentencePreprocessor,
                                               SimilarityMatrix,
                                               TextRankSummarizer)

if __name__ == "__main__":
    # finding paths to the necessary utils
    PROJECT_ROOT = Path(__file__).parent
    ASSETS_PATH = PROJECT_ROOT / 'assets'
    TEXTS_PATH = ASSETS_PATH.joinpath('texts')

    # reading the text from which keywords are going to be extracted
    TARGET_TEXT_PATH = TEXTS_PATH / 'article_701.txt'
    with open(TARGET_TEXT_PATH, 'r', encoding='utf-8') as file:
        text = file.read()

    # reading list of stop words
    STOP_WORDS_PATH = ASSETS_PATH / 'stop_words.txt'
    with open(STOP_WORDS_PATH, 'r', encoding='utf-8') as file:
        stop_words = tuple(file.read().split('\n'))

    # reading IDF scores
    IDF_PATH = ASSETS_PATH / 'IDF.json'
    with open(IDF_PATH, 'r', encoding='utf-8') as file:
        idf = json.load(file)

    paths_to_texts = [str(path) for path in TEXTS_PATH.glob('*.txt')]

    punctuation = tuple(string.punctuation)
    preprocessor = SentencePreprocessor(stop_words, punctuation)
    encoder = SentenceEncoder()

    # step 5
    sentences = preprocessor.get_sentences(text)
    encoder.encode_sentences(sentences)

    # step 9
    matrix = SimilarityMatrix()
    matrix.fill_from_sentences(sentences)
    summarizer = TextRankSummarizer(matrix)
    summarizer.train()
    SUMMARY = summarizer.make_summary(5)
    print(SUMMARY)

    RESULT = SUMMARY
    # DO NOT REMOVE NEXT LINE - KEEP IT INTENTIONALLY LAST
    assert RESULT, 'Summaries are not extracted'
