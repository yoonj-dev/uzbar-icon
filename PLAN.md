# 개발 계획 (Plan)

1. `argparse`를 도입하여 `icon.py`에 CLI 인자 처리용 `main` 함수 구현
   - `--icon` (액션 플래그)
   - `--in` (JSON 파일 경로 혹은 디렉토리 지원, dest 값은 `in_file`)
   - `--out` (생성될 아이콘 폴더 경로)
   - `--bottom` (라벨을 아이콘 내부 하단에 배치)
   - `--below` (라벨을 아이콘 외부 하단에 배치)
2. `icon.py`의 `build_uz_asset` 함수가 라벨 위치 인자를 받도록 수정 및 `y` 좌표 계산 로직 추가
3. 프로젝트 루트에 `pyproject.toml` 파일 생성
   - name: `uzbar-icon`
   - `requires-python`: `>=3.8` (최신파이썬 지원을 위해)
   - `dependencies`: `["requests"]`
   - `[project.scripts]`: `uzbar = "icon:main"` 정의
4. 로컬 환경에서 `pip install -e .` 명령 실행 후 테스트
6. `icon.py` 내 타입 에러 수정
7. `uzbar --icon --in ./input/uzStock.json --out ./assets` 명령어 테스트
