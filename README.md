
[SVM model]
- download python3.8 https://www.python.org/downloads/
- model 폴더에서 pip3 install -r requirements.txt
- 데이터프로세싱, 모델 학습, 저장
- model 폴더에서 python3 main.py --parse_data true --train true
- 데이터로딩, 모델로딩
- writer 폴더에서 npm install
- writer 폴더에서 node main.js
- model 폴더에서 python3 test.py
- 두 개 동시에 실행

[STT]
1. 일반 powershell 실행

2. 서버  실행
경로: C:\Works\Mascreen\writer
실행 커맨드: node main.js

3. 클라이언트 실행
경로: C:\Works\Mascreen\stt\STT.py
실행 커맨드: python ./STT.py

4. 구글 클라우드 Speech to Text
1) anaconda에서 실행한 vscode shell 켜기

2) $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Works\Mascreen\mascreen-967da9d741be.json"

3) python mascreen_google_speechToText.py


4) python mascreen_google_translate.py
(입모양 모델 1,2) --> 
C:\Works\Mascreen\model
lips.py
lips_e.py

(STT) -->
C:\Works\Mascreen\stt
STT.py

(Translation) -->
C:\Works\Mascreen\translater


https://jungwoon.github.io/google%20cloud/2018/01/03/Translation-Api/

## Google Cloud
export GOOGLE_CLOUD_SDK_PATH=C:\Works\google-cloud-sdk
export PATH=$PATH:$GOOGLE_CLOUD_SDK_PATH/bin
export GOOGLE_APPLICATION_CREDENTIALS=C:\Works\google-cloud-sdk

translate language:
https://cloud.google.com/translate/docs/languages?hl=ko