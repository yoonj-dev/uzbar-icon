# 검증 방식 (Test) - Unified Asset Generator (UAG)

## 1. 파일명 결과물 확인
- `uzbar --all` 명령어 실행 시 생성되는 파일의 이름이 정확한지 확인합니다:
  - `icon-center.svg`, `icon-bottom.svg`, `icon-below.svg`
  - `logo.svg`
- `--no-bg` 옵션 부여 시 `logo-transparent.svg` 등이 생성되는지 확인합니다.

## 2. CLI 작동 테스트
- `uzbar --help` 도움말 출력 확인.
- `uzbar --icon --in ./input/uzStock.json --out ./assets` 실행 후 파일명에 `Stock`이 포함되지 않는지 확인.

## 3. 구조적 무결성
- 각 서비스별로 생성된 폴더 내부에 명칭이 고정된 에셋들이 정확히 위치하는지 검증합니다.
