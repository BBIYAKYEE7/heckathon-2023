import re
import string
from konlpy.tag import Mecab
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


# 정규표현식을 이용한 특수문자 제거
def remove_special_characters(text):
    text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9\s]', '', text)
    return text

# 불용어 제거
def remove_stopwords(text):
    stop_words = set(stopwords.words('korean'))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

# 형태소 분석
def tokenize(text):
    tokenizer = Mecab()
    tokens = tokenizer.morphs(text)
    return tokens

# 전처리 함수
def preprocess(text):
    text = remove_special_characters(text)
    text = remove_stopwords(text)
    tokens = tokenize(text)
    return tokens

# 예시
text = "안녕하세요! 한국어 전처리 코드 예제입니다."
preprocessed_text = preprocess(text)
print(preprocessed_text)
