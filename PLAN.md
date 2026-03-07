# 개발 계획 (Plan)

## 1. `cli.py` 통합 구현
- `argparse`를 사용하여 단일 진입점 구현.
- 인자 구성:
  - `--icon`, `--logo`, `--all`: 작업 모드 선택 (다중 선택 가능).
  - `--in`, `--out`: 입출력 경로.
  - `--bg`, `--no-bg`: 배경색 제어.
  - `--center`, `--bottom`, `--below`: 아이콘 레이블 위치 (아이콘 모드 시).
- `--all` 모드 시 `icon`과 `logo` 생성을 순차적으로 호출.

## 2. 기존 스크립트 라이브러리화
- `icon.py` 및 `logo.py`에서 `main()` 함수 제거.
- 생성 함수(`build_uz_asset`, `build_uz_logo`, `generate_icons`, `generate_logos`)만 남기고 모듈로 활용.
- `icon.py`에도 `--bg/--no-bg` 옵션에 대응하는 `include_bg` 파라미터 추가.

## 3. `pyproject.toml` 및 환경 정리
- `uzbar` 엔트리포인트를 `cli:main`으로 변경.
- 불필요해진 `uzlogo` 엔트리포인트 제거 또는 별칭으로 유지 (사용자 요청은 "이전 거는 필요 없어").

## 4. `no-img` 옵션 구현 및 검증
- `cli.py`에 `--no-img` 플래그 추가.
- `icon.py` 및 `logo.py`의 생성 함수에 `include_icon: bool` 파라미터 추가.
- `include_icon`이 `False`일 경우 SVG 내 아이콘 관련 엘리먼트 제외.
- 파일명 구분 처리 (예: `-no-img` 접미사).
- `IMPLEMENT.md`, `README.md`, `TEST.md` 업데이트.
