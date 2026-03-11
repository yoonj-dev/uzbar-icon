# 개발 계획 (Plan) - Unified Asset Generator (UAG)

## 1. 현재 구조 및 명칭 최적화
- `logo.py`에서 불필요한 `-horizontal` 접미사를 제거하고 `logo.svg`로 통일합니다.
- 모든 에셋 생성 함수에서 파일명에 `name`을 포함하던 로직을 완전히 제거하고 고정 파일명을 사용하도록 정리합니다.

## 2. 옵션 처리 및 검증
- `--bg / --no-bg` 옵션에 따라 `-transparent` 접미사가 파일명에 정확히 반영되는지 검증합니다.
- `pip install -e .` 상태에서 `ontap --all` 호출 시 결과물 구조가 `Service/icon-*.svg`, `Service/logo.svg` 형태가 되는지 확인합니다.

## 3. 문서 최신화
- `IMPLEMENT.md` 및 `TEST.md`를 최종 파일명 규칙에 맞게 업데이트하여 작업 완료를 명시합니다.
