# 검증 방식 (Test)

1. `pyproject.toml` 패키징 정상 여부 판단 (`pip install -e .` 실행)
2. 터미널에서 `uzbar --help` 실행 시 argparse 도움말 출력 여부 확인
3. `uzbar --icon --in ./input/uzStock.json --out ./assets` 명령어 실행
4. 터미널 명령으로 `./assets/uz주식.svg` (또는 지정된 JSON의 name에 따른 결과파일) 생성 확인 및 에러 미발생 검증
5. `uzbar --icon --in ./input` 으로도 작동 가능한지 여부 검증 (디렉토리 인자 주입 시 정상 처리 확인)
