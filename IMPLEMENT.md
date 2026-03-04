# 구현 사항 (Implementation)

1. `icon.py` 수정 완료:
   - 상단에 `argparse`와 `sys` 모듈 import
   - CLI 인자 파싱을 관리할 `def main():` 블록 추가
   - 기존의 파일 I/O를 새로운 인자에 맞게 변경:
      - `--in` 인자가 파일인 경우 단일 JSON 처리
      - `--in` 인자가 디렉터리인 경우 내부 모든 JSON 순회 처리
      - `args.out` 인자로 `output_dir`을 동적 매핑
   - 레이블 위치 옵션 고도화:
      - `--center` 옵션 추가.
      - `--center`, `--bottom`, `--below` 옵션을 다중 선택 가능하게 변경.
      - 옵션이 하나도 지정되지 않은 경우, 3가지 모드(`center`, `bottom`, `below`)를 모두 실행하는 로직 구현.
   - `build_uz_asset` 내 파일명 생성 규칙 변경:
      - `uz{name}-{label_pos}.svg` 형식으로 저장하여 다중 생성 시 덮어쓰기 방지.
2. `pyproject.toml` 파일 생성 완료:
   - `requests` 모듈 의존성 선언
   - CLI 호출을 위한 `uzbar` 엔트리포인트 구성
3. 로컬 환경에서 실행 확인:
   - `python icon.py --icon --in ... --out ...`
   - `pip install -e .` 및 `uzbar --icon ...` 명령 확인
4. 타입 안정성 확보:
   - `generate_icons` 내에서 `service.get()` 대신 직접 참조(`[]`)를 사용하여 `Unknown | None` 관련 정적 분석 에러 해결. (완료)
   - `generate_icons` 파라미터 타입을 `List[str]`로 변경하여 다중 처리 지원.
