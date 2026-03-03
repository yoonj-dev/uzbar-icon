# 개발 계획 (Plan)

1. `argparse`를 도입하여 `icon.py`에 CLI 인자 처리용 `main` 함수 구현
   - `--icon` (액션 플래그)
   - `--in` (JSON 파일 경로 혹은 디렉토리 지원, dest 값은 `in_file`)
   - `--out` (생성될 아이콘 폴더 경로)
2. `icon.py`의 `__main__` 블록을 `main()` 호출로 교체 후 스크립트 모드로 테스트
3. 프로젝트 루트에 `pyproject.toml` 파일 생성
   - name: `uzbar-icon`
   - `requires-python`: `>=3.8` (최신파이썬 지원을 위해)
   - `dependencies`: `["requests"]`
   - `[project.scripts]`: `uzbar = "icon:main"` 정의
4. 로컬 환경에서 `pip install -e .` 명령 실행 후 테스트
5. `uzbar --icon --in ./input/uzStock.json --out ./assets` 명령어 테스트
