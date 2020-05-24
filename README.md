reproduce steps

- download python3.8 https://www.python.org/downloads/
- model 폴더에서 pip3 install -r requirements.txt
- 데이터프로세싱, 모델 학습, 저장
- model 폴더에서 python3 main.py --parse_data true --train true
- 데이터로딩, 모델로딩
- writer 폴더에서 npm install
- writer 폴더에서 node main.js
- model 폴더에서 python3 test.py
- 두 개 동시에 실행
