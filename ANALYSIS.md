# 분석 (Analysis)

사용자는 기존의 `icon.py` 스크립트를 `pip install` 가능한 커맨드 라인 툴(CLI)로 변환하고자 합니다.
요구사항:
1. `pip install .` 형식으로 해당 저장소(repo)를 설치.
2. `uzbar` 라는 명령어로 터미널에서 실행될 수 있어야 함.
3. 입력 플래그: `--icon`, `--in [JSON파일경로]`, `--out [출력디렉토리경로]`
예) `uzbar --icon --in ./input/uzStock.json --out ./assets`

분석 결과:
- 현재 `icon.py`는 모듈화되어 있으나, CLI 파라미터를 받지 않고 `./input` 폴더에 있는 모든 JSON을 대상으로 `./output/icon`에 출력하는 하드코딩된 방식을 사용합니다.
- python의 `argparse` 모듈을 도입하여 인자를 처리할 수 있는 `main()` 함수를 `icon.py` 내부에 구현해야 합니다.
- 패키징을 위해 프로젝트 루트에 `pyproject.toml`을 작성하여 `project.scripts` 엔트리 포인트를 `uzbar=icon:main`으로 설정해야 합니다.
- 의존성 패키지인 `requests`가 `pyproject.toml` 내 `dependencies`에 포함되어야 올바르게 동작합니다.
- 라벨 위치 제어 요구사항:
  - `--bottom`: 라벨 하단을 아이콘 하단 경계선에 맞춤 (내부 배치).
  - `--below`: 라벨 상단을 아이콘 하단 경계선에 맞춤 (아이콘 아래 외부 배치).
  - 기본값은 기존처럼 중앙 배치.
20: - 타입 불일치 에러 (New):
21:   - `icon.py`의 `generate_icons` 함수 내부에서 `service.get("icon")`을 호출할 때 `Unknown | None` 타입이 반환될 수 있으나, `build_uz_asset`은 `icon_name: str`을 기대함.
22:   - 원인: `service` 변수가 `dict` 타입이며, `.get()` 메서드는 키가 없을 경우 `None`을 반환할 수 있기 때문임.
23:   - 해결방안: 상단에서 `required_keys` 확인을 통해 키의 존재가 보장되므로, `.get()` 대신 `service["icon"]` 처럼 직접 참조를 사용하거나 명시적으로 `str`로 캐스팅하여 타입 체크를 통과시킴.
