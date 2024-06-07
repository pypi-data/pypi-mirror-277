"""Inverted Index Tool."""

import nltk
from nltk.corpus import stopwords
from collections import defaultdict
import logging
from .cosmic_utils import text_tagger

def inverted_index(documents, topic, llm):
    """
    Create inverted indices based on the outputs of text tagger, or a general index.
    
    Args:
        documents (List[str]): List of document paths or strings of text.
        topic (str): Topic from text tagger (questions, answers) or None for a general inverted index.
        llm: Model object able to be called.

    Returns:
        defaultdict: Inverted index with words as keys and names of documents that contain the words as values.
    """
    nltk.download("stopwords")
    inv_index = defaultdict(list)
    
    if topic not in ["None", None]:
        for document in documents:
            try:
                logging.info("Starting text tagger for %s", document)
                output = text_tagger(document, llm)
                logging.info("Text tagging output: %s", output)
                logging.info("Finished tagging text")

                # Make the index based on tagged questions
                if topic == "questions":
                    for question in output["questions"]:
                        if document not in inv_index[question]:
                            inv_index[question].append(document)

                # Make the index based on tagged answers
                elif topic == "answers":
                    for answer in output["answers"]:
                        if document not in inv_index[answer]:
                            inv_index[answer].append(document)

            except Exception as e:
                logging.error("Error processing document %s: %s", document, str(e))
                continue

    else:
        for document in documents:
            try:
                with open(document, 'r') as f:
                    tempdoc = f.read()
                doc_list = " ".join(
                    [
                        word for word in tempdoc.split()
                        if word not in stopwords.words("english")
                    ]
                )
                logging.debug("Document after removing stopwords: %s", doc_list)
                doc_list = doc_list.lower().split()
                for word in doc_list:
                    if document not in inv_index[word]:
                        inv_index[word].append(document)
            except Exception as e:
                logging.error("Error processing document %s: %s", document, str(e))
                continue

    return inv_index
