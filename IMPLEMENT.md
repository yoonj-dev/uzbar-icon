# 구현 사항 (Implementation)

1. `icon.py` 수정 중:
   - 상단에 `argparse`와 `sys` 모듈 import
   - CLI 인자 파싱을 관리할 `def main():` 블록 추가
   - 기존의 파일 I/O를 새로운 인자에 맞게 변경:
     - `--in` 인자가 파일인 경우 단일 JSON 처리
     - `--in` 인자가 디렉터리인 경우 내부 모든 JSON 순회 처리 하거나 단일 디렉토리로 취급. (사용자는 `uzbar --icon --in ~~.json`으로 기술하였으므로, 단일 파일 처리를 지원해야 함)
     - `args.out` 인자로 `output_dir`을 동적 매핑
2. `pyproject.toml` 파일 생성 중:
   - `requests` 모듈 의존성 선언
   - CLI 호출을 위한 `uzbar` 엔트리포인트 구성
3. 로컬 환경에서 실행 확인:
   - `python icon.py --icon --in ... --out ...`
   - `pip install -e .` 및 `uzbar --icon ...` 명령 확인
