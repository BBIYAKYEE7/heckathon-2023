import speech_recognition as sr

def stt_realtime():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("음성 입력을 시작합니다.")
        while True:
            audio = r.listen(source)

            try:
                result = r.recognize_google(audio, language='ko-KR', show_all=True)
                alternatives = result.get('alternative', [])
                if len(alternatives) > 0:
                    # 여러 번역 대안 중 가장 정확한 문장 선택
                    best_transcript = alternatives[0]['transcript']
                    print("인식 결과:", best_transcript)
            except sr.UnknownValueError:
                print("음성을 인식할 수 없습니다.")
            except sr.RequestError as e:
                print(f"오류 발생: {e}")

# STT 수행
stt_realtime()
