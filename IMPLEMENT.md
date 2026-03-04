# 구현 사항 (Implementation)

1. `icon.py` 수정 완료:
   - 상단에 `argparse`와 `sys` 모듈 import
   - CLI 인자 파싱을 관리할 `def main():` 블록 추가
   - 레이블 위치 옵션 고도화:
      - `--center` 옵션 추가.
      - `--center`, `--bottom`, `--below` 옵션을 다중 선택 가능하게 변경.
      - 옵션이 하나도 지정되지 않은 경우, 3가지 모드(`center`, `bottom`, `below`)를 모두 실행하는 로직 구현.
   - **`--all` 옵션 구현:**
      - `./input` 내 모든 JSON 파일을 처리하고 `./output/{name}/` 폴더에 분류하여 저장.
      - `--all` 모드 시 `in_path` 기본값은 `./input`, `out_dir` 기본값은 `./output`.
      - 3가지 레이블 위치 아이콘을 모두 자동 생성.
   - `build_uz_asset` 내 파일명 생성 규칙 변경:
      - **`icon-{label_pos}.svg`** 형식으로 저장 (폴더로 구분되므로 간결화).
2. `pyproject.toml` 파일 생성 완료:
   - `requests` 모듈 의존성 선언
   - CLI 호출을 위한 `uzbar` 엔트리포인트 구성
3. 로컬 환경에서 실행 확인:
   - `python icon.py --icon --in ... --out ...`
   - `pip install -e .` 및 `uzbar --icon ...` 명령 확인
   - `uzbar --icon --all` 명령 확인
4. 타입 안정성 확보:
   - `service["key"]` 직접 참조를 통해 정적 분석 에러 해결. (완료)
   - `generate_icons` 파라미터 타입을 `List[str]`로 변경하여 다중 처리 지원.
