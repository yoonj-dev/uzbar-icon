import json
import os
import re
import sys
from pathlib import Path
from typing import List

import requests


def fetch_lucide_icon(icon_name: str) -> str:
    """Lucide 오픈소스 아이콘 SVG를 가져옵니다."""
    url = f"https://unpkg.com/lucide-static@latest/icons/{icon_name}.svg"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            print(f"⚠️ 아이콘 다운로드 실패 ({icon_name})")
            return ""
    except Exception as e:
        print(f"Error fetching icon {icon_name}: {e}")
        return ""


def extract_inner_svg(raw_svg: str) -> str:
    """SVG 태그 내부의 알맹이(<path>, <circle> 등)만 추출합니다."""
    inner_svg_match = re.search(
        r"<svg[^>]*>(.*)</svg>", raw_svg, re.IGNORECASE | re.DOTALL
    )
    return inner_svg_match.group(1) if inner_svg_match else raw_svg


def is_emoji(text: str) -> bool:
    """텍스트가 이모지인지 판단합니다 (단일 문자 및 몇 가지 조합)."""
    # 아주 간단한 판별: Lucide 아이콘 이름은 보통 영어와 하이픈 조합임.
    # 그 외의 경우(특히 유니코드 범위가 크면) 이모지일 가능성 높음.
    if not text:
        return False
    # Lucide 아이콘 이름 규칙 패턴 (알파벳, 숫자, 하이픈)
    if re.match(r"^[a-z0-9-]+$", text):
        return False
    return True


def load_services(in_path: Path) -> List[dict]:
    """JSON 파일 또는 디렉토리에서 서비스 정보를 로드합니다."""
    uz_services: List[dict] = []

    if in_path.is_file() and in_path.suffix.lower() == ".json":
        with open(in_path, "r", encoding="utf-8") as f:
            uz_services.append(json.load(f))
    elif in_path.is_dir():
        for file in sorted(os.listdir(in_path)):
            if file.endswith(".json"):
                with open(in_path / file, "r", encoding="utf-8") as f:
                    uz_services.append(json.load(f))
    else:
        print(
            f"Error: Invalid input path '{in_path}'. Must be a JSON file or a directory containing JSON files."
        )
        sys.exit(1)

    required_keys = ["name", "icon", "colors"]
    for service in uz_services:
        if not all(key in service for key in required_keys):
            print(f"Error: Missing required keys in {service}")
            sys.exit(1)

    return uz_services


def get_glow_filter(name: str) -> str:
    """텍스트나 아이콘에 적용할 Glow 필터 정의를 반환합니다."""
    return f"""
    <filter id="glow-{name}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    """
