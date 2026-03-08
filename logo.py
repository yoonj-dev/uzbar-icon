import os
from pathlib import Path
from typing import Dict

import common


def build_uz_logo(
    name: str,
    icon_val: str,
    colors: Dict[str, str],
    output_dir: Path,
    include_bg: bool = True,
    include_icon: bool = True,
) -> None:
    os.makedirs(output_dir, exist_ok=True)

    # 로고 캔버스 사이즈 및 배치 설정
    height = 200
    icon_size = 100
    text_size = 80
    gap = 40  # 텍스트와 아이콘 사이 간격
    padding = 60  # 좌우 여백

    # 텍스트 너비 추정 (font-size 80px 기준)
    # 'uz' (weight 300) 약 85px + 각 글자(weight 900)당 약 55px로 계산
    estimated_text_width = 85 + (len(name) * 55)

    # 전체 너비 계산 (좌여백 + 텍스트 + 간격 + 아이콘 + 우여백)
    # 아이콘 영역이 필요 없는 경우(--no-img)도 고려
    if include_icon:
        width = padding + estimated_text_width + gap + icon_size + padding
        icon_x_base = padding + estimated_text_width + gap
    else:
        width = padding + estimated_text_width + padding
        icon_x_base = 0

    # 배치 좌표
    text_x = padding
    text_y = 100
    icon_y_base = 50

    icon_content = ""
    if include_icon:
        is_icon_emoji = common.is_emoji(icon_val)

        if is_icon_emoji:
            # 이모지 처리 (중앙 정렬을 위해 x좌표 조정)
            icon_content = f"""
            <text x="{icon_x_base + (icon_size / 2)}" y="100" text-anchor="middle" dominant-baseline="middle" font-size="{icon_size}">
                {icon_val}
            </text>
            """
        else:
            # Lucide 아이콘 처리
            raw_svg = common.fetch_lucide_icon(icon_val)
            if raw_svg:
                inner_svg = common.extract_inner_svg(raw_svg)
                scale = icon_size / 24
                icon_content = f"""
                <g stroke="{colors["icon"]}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none" transform="translate({icon_x_base}, {icon_y_base}) scale({scale})">
                    {inner_svg}
                </g>
                """

    glow_filter = common.get_glow_filter(name)

    bg_rect = (
        f'<rect width="{width}" height="{height}" rx="40" fill="{colors["background"]}" />'
        if include_bg
        else ""
    )

    final_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    {glow_filter}
  </defs>
  {bg_rect}
  <text x="{text_x}" y="{text_y}" dominant-baseline="middle" font-family="sans-serif">
    <tspan fill="#94a3b8" font-weight="300" font-size="{text_size}">uz</tspan>
    <tspan fill="{colors["label"]}" font-weight="900" font-size="{text_size}" filter="url(#glow-{name})">{name}</tspan>
  </text>
  {icon_content}
</svg>"""

    suffix = ""
    if not include_bg:
        suffix += "-transparent"
    if not include_icon:
        suffix += "-no-img"

    output_path = os.path.join(output_dir, f"logo{suffix}.svg")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_svg)
    print(f"✔️ 성공: {output_path} 생성 완료!")


def generate_logos(
    in_path: Path,
    out_dir: Path,
    use_subdir: bool = False,
    include_bg: bool = True,
    include_icon: bool = True,
) -> None:
    uz_services = common.load_services(in_path)

    for service in uz_services:
        target_dir = out_dir / service["name"] if use_subdir else out_dir
        build_uz_logo(
            name=service["name"],
            icon_val=service["icon"],
            colors=service["colors"],
            output_dir=target_dir,
            include_bg=include_bg,
            include_icon=include_icon,
        )
