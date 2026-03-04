# 구현 사항 (Implementation)

1. `icon.py` 수정 완료:
   - 상단에 `argparse`와 `sys` 모듈 import
   - CLI 인자 파싱을 관리할 `def main():` 블록 추가
   - 기존의 파일 I/O를 새로운 인자에 맞게 변경:
      - `--in` 인자가 파일인 경우 단일 JSON 처리
      - `--in` 인자가 디렉터리인 경우 내부 모든 JSON 순회 처리
      - `args.out` 인자로 `output_dir`을 동적 매핑
      - `args.bottom`, `args.below` 여부에 따라 `label_pos` 변수 설정 및 `build_uz_asset` 전달
   - `build_uz_asset` 내 `y` 좌표 결정:
     - `center`(default): `y=275`
     - `bottom`: `y=366`
     - `below`: `y=446`
2. `pyproject.toml` 파일 생성 완료:
   - `requests` 모듈 의존성 선언
   - CLI 호출을 위한 `uzbar` 엔트리포인트 구성
3. 로컬 환경에서 실행 확인:
   - `python icon.py --icon --in ... --out ...`
   - `pip install -e .` 및 `uzbar --icon ...` 명령 확인
4. 타입 안정성 확보:
   - `generate_icons` 내에서 `service.get()` 대신 직접 참조(`[]`)를 사용하여 `Unknown | None` 관련 정적 분석 에러 해결.
