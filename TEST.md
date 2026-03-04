# 검증 방식 (Test)

1. `pyproject.toml` 패키징 정상 여부 판단 (`pip install -e .` 실행)
2. 터미널에서 `uzbar --help` 실행 시 `--all`, `--center` 등 새로운 옵션 출력 여부 확인
3. **`--all` 옵션 테스트:**
   - `uzbar --icon --all` 실행
   - `./output/` 하위에 각 서비스 이름 폴더(예: `output/주식/`)가 생성되었는지 확인.
   - 각 폴더 내에 `icon-center.svg`, `icon-bottom.svg`, `icon-below.svg` 파일이 있는지 확인.
4. **다중 생성 테스트 (Default):**
   - `uzbar --icon --in ./input/uzStock.json --out ./assets` 실행
   - 결과물로 `icon-center.svg`, `icon-bottom.svg`, `icon-below.svg` 3개 파일이 생성되는지 확인.
5. **단일 옵션 테스트:**
   - `uzbar --icon --in ./input/uzStock.json --out ./assets --center` 실행
   - `icon-center.svg`만 생성되는지 확인.
6. `uzbar --icon --in ./input` 으로도 작동 가능한지 여부 검증 (디렉토리 인자 주입 시 정상 처리 확인)
7. 정적 타입 체크 확인: Pyright 등을 통해 `Icon.py` 내 타입 에러 미발생 확인.
