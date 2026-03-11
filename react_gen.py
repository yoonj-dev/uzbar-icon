import re
from pathlib import Path


def convert_to_tsx(svg_content: str, component_name: str) -> str:
    """SVG 콘텐츠를 React Functional Component(TSX) 코드로 변환합니다."""
    # SVG 속성 중 React에서 CamelCase를 사용하는 경우 변환
    attr_map = {
        "stroke-width": "strokeWidth",
        "stroke-linecap": "strokeLinecap",
        "stroke-linejoin": "strokeLinejoin",
        "fill-rule": "fillRule",
        "clip-rule": "clipRule",
        "stop-color": "stopColor",
        "stop-opacity": "stopOpacity",
        "flood-color": "floodColor",
        "flood-opacity": "floodOpacity",
        "font-family": "fontFamily",
        "font-weight": "fontWeight",
        "font-size": "fontSize",
        "text-anchor": "textAnchor",
        "dominant-baseline": "dominantBaseline",
    }

    tsx_content = svg_content
    for svg_attr, react_attr in attr_map.items():
        tsx_content = tsx_content.replace(f"{svg_attr}=", f"{react_attr}=")

    # <svg ...> 태그에 {...props} 추가
    tsx_content = re.sub(r"(<svg[^>]*)(>)", r"\1 {...props}\2", tsx_content, count=1)

    return f"""import React from 'react';

export const {component_name} = (props: React.SVGProps<SVGSVGElement>) => (
  {tsx_content}
);
"""


def save_as_tsx(
    output_dir: Path, filename: str, svg_content: str, component_name: str
) -> None:
    """SVG 콘텐츠를 TSX 파일로 저장합니다."""
    tsx_filename = filename.replace(".svg", ".tsx")
    output_path = output_dir / tsx_filename
    tsx_content = convert_to_tsx(svg_content, component_name)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(tsx_content)
    print(f"✔️ 성공: {output_path} (React 컴포넌트) 생성 완료!")
