import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Mouth import speak

# Download NLTK resourceshi
nltk.download('punkt')
nltk.download('stopwords')

def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        qna_pairs = [line.strip().split(':') for line in lines if ':' in line]
        dataset = [{'question': q, 'answer': a} for q, a in qna_pairs]
        return dataset

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = word_tokenize(text.lower())
    tokens = [ps.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(tokens)


def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]
    vectorizer = TfidfVectorizer()
    x = vectorizer.fit_transform(corpus)
    return vectorizer, x


def get_answer(question, vectorizer, x, dataset):
    question = preprocess_text(question)
    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, x)
    best_match_index = similarities.argmax()
    return dataset[best_match_index]['answer']


def mind(text):
    dataset_path = r'C:\Users\adith\OneDrive\Desktop\nova_2.0\nova_2.0\Data\brain_data\qna_data.txt'
    dataset = load_dataset(dataset_path)
    vectorizer, x = train_tfidf_vectorizer(dataset)
    answer = get_answer(text, vectorizer, x, dataset)
    return answer



