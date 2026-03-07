# 검증 방식 (Test)

## 1. 패키지 재설치 및 엔트리포인트 확인
- `pip install -e .` 실행.
- `uzbar --help` 및 `uzlogo --help` 명령어가 정상 작동하는지 확인.

## 2. 로고 생성 테스트 (`logo.py`)
- `uzlogo --logo --in ./input/uzStock.json --out ./output/logo` 실행.
- `./output/logo/logo-horizontal.svg` 파일 생성 여부 확인.
- SVG 결과물을 열어 `[아이콘] uzStock` 형태의 가로 로고가 정상 디자인(색상, 폰트 웨이트 등)으로 출력되는지 확인.

## 3. 이모지 지원 테스트
- `input/emoji_test.json` 생성 (내용: `"icon": "📈"`).
- `uzbar --icon --all --in ./input/emoji_test.json` 실행.
- `uzlogo --logo --all --in ./input/emoji_test.json` 실행.
- 아이콘 중앙에 이모지가 렌더링되는지, 로고 배치가 깨지지 않는지 확인.

## 4. 공통 모듈 일관성 확인
- `uzbar --icon --all`을 실행하여 기존 아이콘 생성 기능이 깨지지 않았는지 확인.
- `common.py` 수정으로 인해 두 스크립트가 동일한 Lucide 아이콘 데이터를 사용하는지 확인.

## 5. 일괄 생성 테스트
- `uzlogo --logo --all` 실행 시 `./output/{name}/logo-horizontal.svg`가 모든 서비스에 대해 생성되는지 확인.
