<h1>Project Overview</h1>

This project focuses on building a Named Entity Recognition (NER) model using SpaCy to identify entities such as Organizations (companies) and Locations from raw text.
The model is trained using the CoNLL-2003 dataset and can extract meaningful entities from unseen real-world sentences.

<h1>Objective</h1>

1. Extract structured information from unstructured text
2. Identify entities like company names and locations
3. Build an end-to-end NLP pipeline: data preparation → model training → inference

<h1>Technologies Used</h1>

1. Python
2. SpaCy
3. CoNLL-2003 Dataset
4. NLP (Named Entity Recognition)

<h1>Project Structure</h1>


```text
company_ner_project/
├── config.cfg            # SpaCy training configuration
├── train.spacy           # Training data (SpaCy binary)
├── valid.spacy           # Validation data
├── output/
│   ├── model-best/       # Best trained model
│   └── model-last/       # Last trained model
├── test_model.py         # Script to test the trained model
└── README.md
```
<h1>Dataset</h1>

Dataset: CoNLL-2003

Entity Labels Used:

ORG → Organization
LOC → Location
PER → Person

The dataset was converted into SpaCy’s .spacy format using DocBin for efficient training.

<h1>How the Project Works</h1>
1. Load and preprocess the CoNLL-2003 dataset

2. Convert text and entity annotations into SpaCy format

3. Configure an NLP pipeline with NER

4. Train the model using SpaCy’s training framework

5. Test the trained model on unseen text

<h1>How to Run the Project</h1>
 Create Virtual Environment & Install Dependencies

```text
pip install spacy
```

<h1>Train the NER Model</h1>

```text
python -m spacy train config.cfg \
--output ./output \
--paths.train ./train.spacy \
--paths.dev ./valid.spacy

```

<h1>Test the Model</h1>
Create a file test_model.py and run:

```text
import spacy

nlp = spacy.load("output/model-best")

text = "Google and Microsoft are multinational companies based in the USA."

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)

```

<h1>Output</h1>

```text
Google ORG
Microsoft ORG
USA LOC

```
