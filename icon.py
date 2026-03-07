import os
from pathlib import Path
from typing import Dict, List

import common


def build_uz_asset(
    name: str,
    icon_val: str,
    colors: Dict[str, str],
    output_dir: Path,
    label_pos: str = "center",
    include_bg: bool = True,
    include_icon: bool = True,
) -> None:
    os.makedirs(output_dir, exist_ok=True)

    icon_content = ""
    if include_icon:
        is_icon_emoji = common.is_emoji(icon_val)

        if is_icon_emoji:
            # 이모지인 경우 text로 처리
            icon_content = f"""
            <text x="256" y="256" text-anchor="middle" dominant-baseline="middle" font-size="280" opacity="0.15">
                {icon_val}
            </text>
            """
        else:
            # Lucide 아이콘인 경우
            raw_svg = common.fetch_lucide_icon(icon_val)
            if raw_svg:
                inner_svg = common.extract_inner_svg(raw_svg)
                # Lucide 아이콘 확대 및 중앙 이동
                transform = "translate(106, 106) scale(12.5)"
                icon_content = f"""
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

    glow_filter = common.get_glow_filter(name)
    bg_rect = (
        f'<rect width="512" height="512" rx="120" fill="{colors["background"]}" />'
        if include_bg
        else ""
    )

    final_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    {glow_filter}
  </defs>
  {bg_rect}
  {icon_content}
  <text x="256" y="{label_y}" text-anchor="middle" dominant-baseline="middle" font-family="sans-serif">
    <tspan fill="#94a3b8" font-weight="300" font-size="80">uz</tspan>
    <tspan fill="{colors["label"]}" font-weight="900" font-size="80" filter="url(#glow-{name})">{name}</tspan>
  </text>
</svg>"""

    suffix = ""
    if not include_bg:
        suffix += "-transparent"
    if not include_icon:
        suffix += "-no-img"

    output_path = os.path.join(output_dir, f"icon-{label_pos}{suffix}.svg")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_svg)
    print(f"✔️ 성공: {output_path} 생성 완료!")


def generate_icons(
    in_path: Path,
    out_dir: Path,
    label_positions: List[str],
    use_subdir: bool = False,
    include_bg: bool = True,
    include_icon: bool = True,
) -> None:
    uz_services = common.load_services(in_path)

    for service in uz_services:
        target_dir = out_dir / service["name"] if use_subdir else out_dir

        for pos in label_positions:
            build_uz_asset(
                name=service["name"],
                icon_val=service["icon"],
                colors=service["colors"],
                output_dir=target_dir,
                label_pos=pos,
                include_bg=include_bg,
                include_icon=include_icon,
            )
