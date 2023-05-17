import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

from konlpy.tag import Hannanum

# 한나눔 형태소 분석기 초기화
hannanum = Hannanum()

# 데이터 파일 다운로드
hannanum.download()

# 텍스트 형태소 분석
text = "안녕하세요. 자연어 처리를 위한 형태소 분석을 진행해봅시다."
morphs = hannanum.morphs(text)