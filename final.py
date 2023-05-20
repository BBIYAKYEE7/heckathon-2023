import re
import speech_recognition as sr

def load_dictionary(file_path):
    # 사전 데이터 파일을 XML로 저장하고 로드하는 기능은 제거합니다.
    # 사전 데이터는 정규식을 활용하여 띄어쓰기 교정에 사용됩니다.
    return None

def correct_spacing(text):
    corrected = re.sub(r"([가-힣]+)([^\ 가-힣ㄱ-ㅎㅏ-ㅣ])", r"\1 \2", text)
    corrected = re.sub(r"([^\ 가-힣ㄱ-ㅎㅏ-ㅣ])([가-힣]+)", r"\1 \2", corrected)
    return corrected

def correct_korean_text(text, correction_rules):
    # 띄어쓰기 교정
    corrected_text = correct_spacing(text)
    return corrected_text

# 사전 데이터 파일 경로
dictionary_file = 'korean_dictionary.xml'

# 사전 데이터 불러오기
correction_rules = load_dictionary(dictionary_file)

# 음성 입력 처리
r = sr.Recognizer()
with sr.Microphone() as source:
    print("말씀해주세요:")
    audio = r.listen(source)

# 음성을 텍스트로 변환
try:
    recognized_text = r.recognize_google(audio, language='ko-KR')
    print("음성 인식 결과:", recognized_text)
    corrected_text = correct_korean_text(recognized_text, correction_rules)
    print("맞춤법 교정 결과:", corrected_text)
except sr.UnknownValueError:
    print("음성을 인식할 수 없습니다.")
except sr.RequestError as e:
    print("음성 인식 서비스에 접근할 수 없습니다:", str(e))

# 사전 데이터를 XML 파일로 저장
# save_dictionary(dictionary_file, correction_rules)
