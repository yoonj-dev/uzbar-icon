# uzbar-icon
uzbar 서비스의 브랜드 에셋(아이콘, 로고) 자동 생성 도구입니다.

## 설치 방법
```powershell
pip install -e .
```

## 사용 방법
단일 명령어 `uzbar`를 사용하여 모든 자산을 생성할 수 있습니다.

### 1. 전역 생성 (`--all`)
모든 서비스에 대해 아이콘(3종)과 로고(가로형)를 일괄 생성합니다.
```powershell
uzbar --all
```

### 2. 아이콘 생성 (`--icon`)
정방형 아이콘을 생성합니다.
```powershell
uzbar --icon --in ./input/uzStock.json --out ./output
```
*   `--center`, `--bottom`, `--below` 옵션으로 특정 위치만 생성 가능합니다.

### 3. 로고 생성 (`--logo`)
가로형 워드마크 로고를 생성합니다.
```powershell
uzbar --logo --in ./input/uzStock.json --out ./output
```

### 4. 공통 옵션
*   `--in`: 입력 JSON 파일 또는 디렉토리 경로. (기본값: `./input`)
*   `--out`: 출력 디렉토리 경로. (기본값: `./output`)
*   `--bg` / `--no-bg`: 배경색(`rect`) 포함 여부 결정. (기본값: `--bg`)
*   `--no-img`: 아이콘이나 이모지를 제외하고 텍스트만 렌더링합니다.

## 라이브러리 구조
*   `cli.py`: 통합 명령행 인터페이스(CLI) 진입점.
*   `icon.py`: 아이콘 생성 핵심 모듈.
*   `logo.py`: 로고 생성 핵심 모듈.
*   `common.py`: 공통 유틸리티 및 데이터 로더.