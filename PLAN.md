# 개발 계획 (Plan)

1. `argparse`를 도입하여 `icon.py`에 CLI 인자 처리용 `main` 함수 수정
   - `--icon` (액션 플래그)
   - `--in` (JSON 파일 경로 혹은 디렉토리 지원, dest 값은 `in_file`)
   - `--out` (생성될 아이콘 폴더 경로)
   - `--center` (라벨을 중앙에 배치)
   - `--bottom` (라벨을 아이콘 내부 하단에 배치)
   - `--below` (라벨을 아이콘 외부 하단에 배치)
2. `icon.py`의 `generate_icons` 함수 수정
   - 레이블 옵션이 하나라도 있으면 해당 위치로 생성
   - 레이블 옵션이 하나도 없으면 `center`, `bottom`, `below` 3가지 모두 생성하도록 루프 구현
3. `icon.py`의 `build_uz_asset` 함수 수정
   - 파일명을 `uz{name}-{label_pos}.svg` 형식으로 생성하도록 변경
4. 프로젝트 루트에 `pyproject.toml` 파일 생성/확인
5. 로컬 환경에서 `pip install -e .` 명령 실행 후 테스트
6. `icon.py` 내 타입 에러 수정 (완료)
7. `uzbar --icon --in ./input/uzStock.json --out ./assets` 명령어 테스트
