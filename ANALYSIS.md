# 분석 (Analysis) - Unified Asset Generator (UAG) / "on Tap" Edition

## 1. 브랜드 개요: "on Tap"
기존 **uz{Service}** 브랜딩을 생맥주 펍의 탭(Tap)에서 영감을 받은 **{Service} on Tap** 컨셉으로 전환하였습니다. 
- **의미**: "언제든 수도꼭지를 틀면 나오듯 즉각적으로 제공되는 프리미엄 서비스"
- **시각적 키워드**: Neon, Pub, Brick, Flow, Amber Glow, Tactile.

## 2. 디자인 시스템
- **배경**: 심야의 펍 벽면을 연상시키는 다크 톤(#0a0a0c) 및 미세한 벽돌(Brick) 패턴.
- **주요 요소**: 
  - **Beer Tap**: 서비스 고유 컬러의 네온 광택을 머금은 맥주 탭 핸들 실루엣.
  - **Animating Drip**: 탭에서 떨어지는 물방울 애니메이션을 통해 '흐름(Flow)'을 시각화.
- **타이포그래피**: 'uz' 접두사를 제거하고 서비스 명칭(예: Stock, Youtube)만 볼드하게 강조. 네온 글로우 필터를 적용하여 시인성 확보.

## 3. 에셋 레이아웃
- **Icon**: 512x512 정방형. 중앙에 서비스명, 배경에 탭 실루엣과 벽돌 패턴 배치.
- **Logo**: 가변 너비. 좌측 텍스트, 우측 탭 실루엣 배치. 하단 정렬(Base-line) 유지.

## 4. 기술적 구현
- **React 통합**: `--react` 옵션을 통해 SVG를 TSX 컴포넌트로 즉시 변환. CamelCase 자동 변환 및 Props 투과 전달.
- **`react_gen.py`**: SVG를 TSX 컴포넌트로 변환하는 엔진.
- **`pyproject.toml`**: `ontap` 명령어를 통한 CLI 접근 지원.
- **모듈화**: `cli`, `common`, `icon`, `logo`, `react_gen`으로 역할 분담.
