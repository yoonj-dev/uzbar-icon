# 검증 방식 (Test)

1. `pyproject.toml` 패키징 정상 여부 판단 (`pip install -e .` 실행)
2. 터미널에서 `uzbar --help` 실행 시 `--center` 등 새로운 옵션 출력 여부 확인
3. **다중 생성 테스트 (Default):**
   - `uzbar --icon --in ./input/uzStock.json --out ./assets` 실행
   - 결과물로 `uz주식-center.svg`, `uz주식-bottom.svg`, `uz주식-below.svg` 3개 파일이 생성되는지 확인.
4. **단일 옵션 테스트:**
   - `uzbar --icon --in ./input/uzStock.json --out ./assets --center` 실행
   - `uz주식-center.svg`만 생성되는지 확인.
5. **다중 옵션 지정 테스트:**
   - `uzbar --icon --in ./input/uzStock.json --out ./assets --center --bottom` 실행
   - `center`와 `bottom` 두 가지만 생성되는지 확인.
6. `uzbar --icon --in ./input` 으로도 작동 가능한지 여부 검증 (디렉토리 인자 주입 시 정상 처리 확인)
7. 정적 타입 체크 확인: Pyright 또는 Pylance를 통해 `icon.py`의 111라인 부근에서 발생하던 에러가 해결되었고, `List[str]` 타입 전달이 정상인지 확인.
