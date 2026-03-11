import os
from pathlib import Path
from typing import Dict, List

import common
import react_gen


def build_uz_logo(
    name: str,
    icon_val: str,
    colors: Dict[str, str],
    output_dir: Path,
    include_bg: bool = True,
    include_icon: bool = True,
    as_react: bool = False,
) -> None:
    os.makedirs(output_dir, exist_ok=True)

    # 로고 캔버스 사이즈 및 배치 설정
    height = 200
    icon_size = 100
    text_size = 80
    gap = 40
    padding = 60

    # 서비스 명칭(weight 900)당 약 55px로 계산
    estimated_text_width = len(name) * 55

    if include_icon:
        width = padding + estimated_text_width + gap + icon_size + padding
        icon_x_base = padding + estimated_text_width + gap
    else:
        width = padding + estimated_text_width + padding
        icon_x_base = 0

    text_x = padding
    text_y = 150
    icon_y_base = 50

    icon_content = ""
    if include_icon:
        is_icon_emoji = common.is_emoji(icon_val)
        if is_icon_emoji:
            icon_content = f"""
            <text x="{icon_x_base + (icon_size / 2)}" y="150" text-anchor="middle" font-size="{icon_size}" opacity="0.3">
                {icon_val}
            </text>
            """
        else:
            raw_svg = common.fetch_lucide_icon(icon_val)
            if raw_svg:
                inner_svg = common.extract_inner_svg(raw_svg)
                scale = icon_size / 24
                icon_content = f"""
                <g stroke="{colors["icon"]}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none" transform="translate({icon_x_base}, {icon_y_base}) scale({scale})" opacity="0.3">
                    {inner_svg}
                </g>
                """

    glow_filter = common.get_glow_filter(name, colors["label"])
    brick_pattern = common.get_brick_pattern()
    beer_tap = common.get_beer_tap_components(name, colors["label"])

    bg_content = ""
    if include_bg:
        bg_content = f"""
        <rect width="{width}" height="{height}" rx="40" fill="#0a0a0c" />
        <rect width="{width}" height="{height}" rx="40" fill="url(#brick-pattern)" />
        """

    final_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    {glow_filter}
    {brick_pattern}
  </defs>
  {bg_content}
  <g transform="translate({width - 150}, -50) scale(0.8)">
    {beer_tap}
  </g>
  <text x="{text_x}" y="{text_y}" font-family="sans-serif">
    <tspan fill="{colors["label"]}" font-weight="900" font-size="{text_size}" filter="url(#glow-{name})">{name}</tspan>
  </text>
  {icon_content}
</svg>"""

    suffix = ""
    if not include_bg:
        suffix += "-transparent"
    if not include_icon:
        suffix += "-no-img"

    filename = f"logo{suffix}.svg"

    if as_react:
        pascal_name = "".join(x.capitalize() for x in name.split())
        pascal_suffix = suffix.replace("-", "").capitalize()
        component_name = f"Uz{pascal_name}Logo{pascal_suffix}"
        react_gen.save_as_tsx(output_dir, filename, final_svg, component_name)
    else:
        output_path = output_dir / filename
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(final_svg)
        print(f"✔️ 성공: {output_path} 생성 완료!")


def generate_logos(
    in_path: Path,
    out_dir: Path,
    bg_modes: List[bool],
    use_subdir: bool = False,
    include_icon: bool = True,
    as_react: bool = False,
) -> None:
    uz_services = common.load_services(in_path)
    for service in uz_services:
        target_dir = out_dir / service["name"] if use_subdir else out_dir
        for bg_mode in bg_modes:
            build_uz_logo(
                name=service["name"],
                icon_val=service["icon"],
                colors=service["colors"],
                output_dir=target_dir,
                include_bg=bg_mode,
                include_icon=include_icon,
                as_react=as_react,
            )
