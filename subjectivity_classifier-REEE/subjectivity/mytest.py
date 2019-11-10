import os
_path = os.path.dirname(__file__)

from model import SubjectivityPredictor
from utils import is_subjective, convert_text_into_vector_sequence


def main():
    from subjectivity_classifier import SubjectivityClassifier
    classifier = SubjectivityClassifier(model_filename=os.path.join(_path, '../data/save/subj-29.tf'),
                                        word_filename=os.path.join(_path, '../data/word_embeddings/glove.6B.50d.txt'))
    return classifier.classify_sentences_in_text("I am donald trump")


print(main())
