# 개발 계획 (Plan)

1. `argparse`에 `--all` 옵션(액션 플래그) 추가.
2. `icon.py`의 `build_uz_asset` 함수 수정:
   - 파일 명명 규칙을 `icon-{label_pos}.svg`로 변경.
3. `icon.py`의 `generate_icons` 또는 `main` 로직 수정:
   - `--all` 모드가 활성화된 경우:
     - `in_path`를 `./input`으로 기본 설정.
     - `out_dir`을 `./output`으로 기본 설정.
     - 각 서비스 데이터(`name`) 마다 `out_dir / service["name"]` 경로를 생성.
     - 세 가지 레이블 위치(`center`, `bottom`, `below`) 모두 생성되도록 로직 추가.
4. 구현 내용 `IMPLEMENT.md` 기록.
5. 테스트 시나리오 `TEST.md` 업데이트.
6. 로컬 명령어로 `--all` 옵션 작동 여부 검증.
