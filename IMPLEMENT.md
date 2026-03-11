# 구현 사항 (Implementation) - "on Tap" Asset Engine

## 1. "on Tap" 시각적 요소 구현
- **Brick Pattern**: `common.get_brick_pattern()`을 통해 미세한 0.05 불투명도의 벽돌 패턴을 SVG 배경에 삽입.
- **Neon beer tap**: `common.get_beer_tap_components()`를 통해 탭 핸들, 바디, 스파우트 및 **애니메이션 물방울(Drop)** 요소를 구현.
- **Neon Glow**: `feFlood`와 `feComposite`를 조합하여 서비스 고유 컬러에 최적화된 네온 광조 효과 구현.

## 2. 텍스트 레이아웃 최적화
- **Prefix 제거**: 모든 생성 로직에서 'uz' 텍스트를 제거하고 서비스 명칭만 노출.
- **가독성 향상**: 아이콘 내 텍스트 폰트 사이즈를 80 -> 100으로 확대하고, 로고의 텍스트 너비 추정 방식을 텍스트만 존재할 때에 맞춰 재조정.

## 3. 기능성 모듈
- **React TSX 지원**: `react_gen.py`를 통해 SVG를 React 컴포넌트로 변환. 
  - `stroke-width` -> `strokeWidth` 등 속성 변환 로직 포함.
  - `{...props}` 지원으로 스타일 커스터마이징 가능.
- **통합 CLI**: `ontap --all --react` 등의 명령어로 모든 조합의 자산을 한 번에 생성 가능.

## 4. 버그 수정 및 안정화
- **CLI 경로 처리**: `Path` 객체와 `str` 객체 혼용으로 발생하던 속성 에러 수정.
- **패키징**: `pyproject.toml`에 모든 신규 모듈(`react_gen`)을 등록하여 `pip install` 환경 보장 및 `ontap` 명령 지원.
