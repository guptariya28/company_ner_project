import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import random
from pathlib import Path

# -----------------------------
# STEP 1: Read CoNLL format file
# -----------------------------
def read_conll(file_path):
    sentences = []
    labels = []

    with open(file_path, "r", encoding="utf-8") as f:
        words = []
        tags = []

        for line in f:
            line = line.strip()
            if not line or line.startswith("-DOCSTART"):
                if words:
                    sentences.append(words)
                    labels.append(tags)
                    words = []
                    tags = []
            else:
                parts = line.split()
                words.append(parts[0])
                tags.append(parts[-1])

    return sentences, labels


# -----------------------------
# STEP 2: Convert to spaCy format
# -----------------------------
def convert_to_spacy(sentences, labels, nlp, output_file):
    doc_bin = DocBin()

    for words, tags in tqdm(zip(sentences, labels), total=len(sentences)):
        doc = nlp.make_doc(" ".join(words))
        ents = []

        start = 0
        for word, tag in zip(words, tags):
            end = start + len(word)

            if tag != "O":
                label = tag.split("-")[-1]
                ents.append((start, end, label))

            start = end + 1  # space

        doc.ents = [doc.char_span(s, e, label=l) for s, e, l in ents if doc.char_span(s, e, label=l)]
        doc_bin.add(doc)

    doc_bin.to_disk(output_file)


# -----------------------------
# STEP 3: Main execution
# -----------------------------
def main():
    nlp = spacy.blank("en")

    train_sent, train_labels = read_conll("train.txt")
    valid_sent, valid_labels = read_conll("valid.txt")

    convert_to_spacy(train_sent, train_labels, nlp, "train.spacy")
    convert_to_spacy(valid_sent, valid_labels, nlp, "valid.spacy")

    print("✅ Data converted successfully!")


if __name__ == "__main__":
    main()
