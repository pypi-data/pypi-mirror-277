import math
import numbers
import os
import pickle
import sys

from dateutil.parser import parse
from transformers import BertTokenizer, BertModel
import torch
from sentence_transformers import SentenceTransformer
from nltk.corpus import wordnet as wn

from pyhasura.synonyms import PartOfSpeech, is_part_of_speech

# Load a pre-trained model (e.g., 'all-MiniLM-L6-v2')
sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-large-uncased')
dict_index = 0
word_dic = dict()


def vectorize_string_mean(sentence):
    tokens = tokenizer.encode(sentence, add_special_tokens=True)
    input_ids = torch.tensor(tokens).unsqueeze(0)
    with torch.no_grad():
        outputs = model(input_ids)
        sentence_vector = outputs[0][:, 0, :].mean(dim=1)
        return sentence_vector.item()


def vectorize_string(sentence):
    return sentence_model.encode(sentence)


def vectorize_date_string(value):
    if value is None:
        return -sys.maxsize - 1
    if not is_numeric(value):
        try:
            # Parse the RFC 3339 timestamp into a datetime object (including timezone)
            dt = parse(value)
            # Convert to an epoch timestamp (in seconds)
            return int(dt.timestamp())
        except ValueError:
            # If parsing fails, return the original value
            return value
    return value


def is_numeric(value):
    return isinstance(value, numbers.Number)


def is_boolean(value):
    return isinstance(value, bool)


def is_dictionary(value):
    return isinstance(value, dict)


def is_list(value):
    return isinstance(value, list)


def vectorize_dict(dictionary, deep=None, fill_na=False):
    global dict_index
    for key, value in dictionary.items():
        if value is None:
            dictionary[key] = -sys.maxsize - 1
        if is_numeric(value):
            if fill_na and math.isnan(value):
                dictionary[key] = -sys.maxsize - 1
            else:
                dictionary[key] = value
        elif is_dictionary(value):
            dictionary[key] = vectorize_dict(value, deep=deep, fill_na=fill_na)
        elif is_list(value):
            dictionary[key] = vectorize_dicts(value, deep=deep, fill_na=fill_na)
        elif is_boolean(value):
            if value:
                dictionary[key] = 1.0
            else:
                dictionary[key] = 0.0
        elif deep is not None and deep.has_key(key):
            new_value = vectorize_date_string(value)
            if not is_numeric(new_value):
                new_value = vectorize_string_mean(value)
                dictionary[key] = new_value
            else:
                dictionary[key] = new_value
        else:
            new_value = word_dic.get(value)
            if new_value is None:
                new_value = dict_index
                word_dic[value] = dict_index
                dict_index = dict_index + 1
            dictionary[key] = new_value
    return dictionary


def vectorize_dicts(array_of_dicts, fill_na=False, deep=None):
    return list(map(lambda x: vectorize_dict(dict(x), deep=deep, fill_na=fill_na), array_of_dicts))


def cosine_similarity(a, b):
    return torch.nn.functional.cosine_similarity(a, b).item()


if os.path.exists('words.pkl'):
    with open('words.pkl', 'rb') as f:
        words = pickle.load(f)
else:
    words = list(filter(lambda x: x.isalpha() and len(x) > 1, list(wn.all_lemma_names())))
    # Save the generated embeddings to 'embeddings.pkl'
    with open('words.pkl', 'wb') as f:
        pickle.dump(words, f)

if os.path.exists('inputs.pkl'):
    with open('inputs.pkl', 'rb') as f:
        input_ids_list = pickle.load(f)
else:
    input_ids_list = [tokenizer.encode(word, add_special_tokens=True, return_tensors="pt") for word in words]
    # Save the generated embeddings to 'embeddings.pkl'
    with open('inputs.pkl', 'wb') as f:
        pickle.dump(input_ids_list, f)

if os.path.exists('embeddings.pkl'):
    with open('embeddings.pkl', 'rb') as f:
        embeddings_list = pickle.load(f)
else:
    with torch.no_grad():
        embeddings_list = [model(input_ids).last_hidden_state.mean(dim=1) for input_ids in input_ids_list]

    # Save the generated embeddings to 'embeddings.pkl'
    with open('embeddings.pkl', 'wb') as f:
        pickle.dump(embeddings_list, f)


def find_related_words(target_word, part_of_speech=PartOfSpeech.Noun, top_n=5):
    target_word_embedding = model(
        tokenizer.encode(target_word, add_special_tokens=True, return_tensors="pt")).last_hidden_state.mean(dim=1)

    similarity_scores = [(word, cosine_similarity(target_word_embedding, emb)) for word, emb in
                         zip(words, embeddings_list)]

    # Sort by similarity
    similarity_scores = list(filter(lambda x: x[1] >= .8 and is_part_of_speech(x[0], part_of_speech), similarity_scores))
    sorted_similar_words = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Select top-N similar words
    similar_words = [word for word, _ in sorted_similar_words[:top_n]]

    return similar_words
