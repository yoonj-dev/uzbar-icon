import os
from pathlib import Path
from typing import Dict, List

import common
import react_gen


def build_uz_asset(
    name: str,
    icon_val: str,
    colors: Dict[str, str],
    output_dir: Path,
    label_pos: str = "center",
    include_bg: bool = True,
    include_icon: bool = True,
    as_react: bool = False,
) -> None:
    os.makedirs(output_dir, exist_ok=True)

    icon_content = ""
    if include_icon:
        is_icon_emoji = common.is_emoji(icon_val)
        if is_icon_emoji:
            icon_content = f"""
            <text x="256" y="256" text-anchor="middle" dominant-baseline="middle" font-size="280" opacity="0.1">
                {icon_val}
            </text>
            """
        else:
            raw_svg = common.fetch_lucide_icon(icon_val)
            if raw_svg:
                inner_svg = common.extract_inner_svg(raw_svg)
                transform = "translate(106, 106) scale(12.5)"
                icon_content = f"""
                <g stroke="{colors["icon"]}" stroke-width="2" fill="none" opacity="0.1" transform="{transform}">
                    {inner_svg}
                </g>
                """

    # 라벨 위치에 따른 y 좌표
    label_y = 275
    if label_pos == "bottom":
        label_y = 366
    elif label_pos == "below":
        label_y = 446

    glow_filter = common.get_glow_filter(name, colors["label"])
    brick_pattern = common.get_brick_pattern()
    beer_tap = common.get_beer_tap_components(name, colors["label"])

    bg_content = ""
    if include_bg:
        bg_content = f"""
        <rect width="512" height="512" rx="120" fill="#0a0a0c" />
        <rect width="512" height="512" rx="120" fill="url(#brick-pattern)" />
        <linearGradient id="bg-glow-{name}" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" style="stop-color:{colors["background"]};stop-opacity:0.3" />
          <stop offset="100%" style="stop-color:#000000;stop-opacity:0" />
        </linearGradient>
        <rect width="512" height="512" rx="120" fill="url(#bg-glow-{name})" />
        """

    final_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    {glow_filter}
    {brick_pattern}
  </defs>
  {bg_content}
  {beer_tap}
  {icon_content}
  <text x="256" y="{label_y}" text-anchor="middle" dominant-baseline="middle" font-family="sans-serif">
    <tspan fill="{colors["label"]}" font-weight="900" font-size="100" filter="url(#glow-{name})">{name}</tspan>
  </text>
</svg>"""

    suffix = ""
    if not include_bg:
        suffix += "-transparent"
    if not include_icon:
        suffix += "-no-img"

    filename = f"icon-{label_pos}{suffix}.svg"

    if as_react:
        pascal_name = "".join(x.capitalize() for x in name.split())
        pascal_pos = label_pos.capitalize()
        pascal_suffix = suffix.replace("-", "").capitalize()
        component_name = f"Uz{pascal_name}Icon{pascal_pos}{pascal_suffix}"
        react_gen.save_as_tsx(output_dir, filename, final_svg, component_name)
    else:
        output_path = output_dir / filename
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(final_svg)
        print(f"✔️ 성공: {output_path} 생성 완료!")


def generate_icons(
    in_path: Path,
    out_dir: Path,
    label_positions: List[str],
    bg_modes: List[bool],
    use_subdir: bool = False,
    include_icon: bool = True,
    as_react: bool = False,
) -> None:
    uz_services = common.load_services(in_path)
    for service in uz_services:
        target_dir = out_dir / service["name"] if use_subdir else out_dir
        for pos in label_positions:
            for bg_mode in bg_modes:
                build_uz_asset(
                    name=service["name"],
                    icon_val=service["icon"],
                    colors=service["colors"],
                    output_dir=target_dir,
                    label_pos=pos,
                    include_bg=bg_mode,
                    include_icon=include_icon,
                    as_react=as_react,
                )
