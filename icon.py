import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List

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


def build_uz_asset(
    name: str,
    icon_name: str,
    colors: Dict[str, str],
    output_dir: Path,
    label_pos: str = "center",
) -> None:
    os.makedirs(output_dir, exist_ok=True)

    raw_svg = fetch_lucide_icon(icon_name)
    if not raw_svg:
        return

    # SVG 내부의 <path>, <circle> 등의 알맹이만 추출
    inner_svg_match = re.search(
        r"<svg[^>]*>(.*)</svg>", raw_svg, re.IGNORECASE | re.DOTALL
    )
    inner_svg = inner_svg_match.group(1) if inner_svg_match else raw_svg

    # Lucide 아이콘은 기본 24x24 사이즈입니다.
    # 512x512 캔버스에 맞게 12.5배 확대(300x300)하고 중앙으로 이동시킵니다.
    # translate(106, 106) = (512 - 300) / 2
    transform = "translate(106, 106) scale(12.5)"

    # 아이콘에 테마 색상을 입히고 투명도를 줍니다. (선 굵기 stroke-width=2 적용)
    styled_icon = f"""
    <g stroke="{colors["icon"]}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none" opacity="0.15" transform="{transform}">
        {inner_svg}
    </g>
    """

    # 라벨 위치에 따른 y 좌표 계산 (중앙: 275, 하단: 366, 아래: 446)
    label_y = 275
    if label_pos == "bottom":
        label_y = 366
    elif label_pos == "below":
        label_y = 446

    final_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <filter id="glow-{name}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect width="512" height="512" rx="120" fill="{colors["background"]}" />
  {styled_icon}
  <text x="256" y="{label_y}" text-anchor="middle" dominant-baseline="middle" font-family="sans-serif">
    <tspan fill="#94a3b8" font-weight="300" font-size="80">uz</tspan>
    <tspan fill="{colors["label"]}" font-weight="900" font-size="80" filter="url(#glow-{name})">{name}</tspan>
  </text>
</svg>"""

    output_path = os.path.join(output_dir, f"uz{name}-{label_pos}.svg")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_svg)
    print(f"✔️ 성공: {output_path} 생성 완료!")


def generate_icons(in_path: Path, out_dir: Path, label_positions: List[str]) -> None:
    uz_services: List[dict] = []

    if in_path.is_file() and in_path.suffix.lower() == ".json":
        with open(in_path, "r", encoding="utf-8") as f:
            uz_services.append(json.load(f))
    elif in_path.is_dir():
        for file in os.listdir(in_path):
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

        for pos in label_positions:
            build_uz_asset(
                name=service["name"],
                icon_name=service["icon"],
                colors=service["colors"],
                output_dir=out_dir,
                label_pos=pos,
            )


def main():
    parser = argparse.ArgumentParser(description="uzbar icon generator")
    parser.add_argument("--icon", action="store_true", help="Generate icon")
    parser.add_argument(
        "--in",
        dest="in_file",
        type=str,
        required=True,
        help="Input JSON file or directory",
    )
    parser.add_argument(
        "--out", type=str, default="./output/icon", help="Output directory"
    )
    # 라벨 위치 옵션
    parser.add_argument(
        "--center",
        action="store_true",
        help="Align label center (default if no other pos specified)",
    )
    parser.add_argument(
        "--bottom", action="store_true", help="Align label bottom with icon bottom"
    )
    parser.add_argument(
        "--below", action="store_true", help="Place label directly below icon"
    )

    args = parser.parse_args()

    if not args.icon:
        print("Please provide --icon flag to generate icons.")
        sys.exit(1)

    in_path = Path(args.in_file)
    out_dir = Path(args.out)

    label_positions = []
    if args.center:
        label_positions.append("center")
    if args.bottom:
        label_positions.append("bottom")
    if args.below:
        label_positions.append("below")

    # 아무것도 지정되지 않았으면 3가지 전부 생성
    if not label_positions:
        label_positions = ["center", "bottom", "below"]

    generate_icons(in_path, out_dir, label_positions)


if __name__ == "__main__":
    main()
