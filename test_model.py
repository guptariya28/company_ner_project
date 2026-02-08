import spacy

# Load the trained model
nlp = spacy.load("output/model-best")

text = "Amazon and Flipkart have their headquarters in Bengaluru and Seattle."


doc = nlp(text)

print("Named Entities found:")
for ent in doc.ents:
    print(ent.text, "->", ent.label_)
