# 구현 사항 (Implementation) - Unified Asset Generator (UAG)

## 1. 파일명 규칙 최적화
- **로고 파일명 변경**: `logo-horizontal.svg`에서 `-horizontal`을 제거하여 `logo.svg`로 일원화하였습니다.
- **서비스명 제거**: 파일명 충돌을 방지하기 위해 서비스 이름을 포함하던 접두사(`uz{Name}-`)를 모든 에셋에서 제거하였습니다. (사용자 요청에 따라 고정된 파일명 규칙 사용)
- **접미사 로직**:
  - `not include_bg`일 때 `-transparent`가 파일명에 붙도록 구현.
  - `not include_icon`일 때 `-no-img`가 파일명에 붙도록 구현.

## 2. 모듈화 구현
- `cli.py`, `icon.py`, `logo.py`, `common.py`로 역할을 분리하여 유지보수성을 확보하였습니다.
- `argparse`를 통해 `--center`, `--bottom`, `--below` 등 위치 제어 옵션을 통합 관리합니다.

## 3. 설치 및 패키징
- `pyproject.toml`을 통해 `pip install .` 및 `uzbar` 커맨드라인 도구 설치를 지원합니다.
- `cli` 모듈 누락 문제(ModuleNotFoundError)를 수정하여 정상 설치를 보장합니다.
