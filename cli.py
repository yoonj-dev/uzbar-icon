import argparse
import sys
from pathlib import Path

import icon
import logo


def main():
    parser = argparse.ArgumentParser(description="ontap - Unified Asset Generator")

    # 작업 모드
    mode_group = parser.add_argument_group("Job Modes")
    mode_group.add_argument("--icon", action="store_true", help="Generate square icons")
    mode_group.add_argument(
        "--logo", action="store_true", help="Generate horizontal logos"
    )
    mode_group.add_argument(
        "--all", action="store_true", help="Generate all assets (icon, logo)"
    )

    # 입출력 설정
    path_group = parser.add_argument_group("Path Settings")
    path_group.add_argument(
        "--in", dest="in_file", type=str, help="Input JSON file or directory"
    )
    path_group.add_argument("--out", type=str, help="Output directory")

    # 공통 옵션
    common_group = parser.add_argument_group("Common Options")
    common_group.add_argument("--bg", action="store_true", help="Include background")
    common_group.add_argument("--no-bg", action="store_true", help="Exclude background")
    common_group.add_argument(
        "--no-img", action="store_true", help="Exclude icon/emoji (text only)"
    )
    common_group.add_argument(
        "--react",
        action="store_true",
        help="Generate React components (.tsx) instead of SVG",
    )

    # 아이콘 전용 옵션
    icon_group = parser.add_argument_group("Icon Options")
    icon_group.add_argument("--center", action="store_true", help="Align label center")
    icon_group.add_argument("--bottom", action="store_true", help="Align label bottom")
    icon_group.add_argument(
        "--below", action="store_true", help="Place label below icon"
    )

    args = parser.parse_args()

    # 모드가 하나도 없으면 에러
    if not (args.icon or args.logo or args.all):
        print("Error: Please specify a job mode (--icon, --logo, or --all).")
        sys.exit(1)

    # 경로 설정
    in_path = Path(args.in_file) if args.in_file else Path("./input")
    out_dir = Path(args.out) if args.out else Path("./output")
    use_subdir = True if args.all or in_path.is_dir() else False

    # 아이콘 레이블 위치 결정
    label_positions = []
    if args.center:
        label_positions.append("center")
    if args.bottom:
        label_positions.append("bottom")
    if args.below:
        label_positions.append("below")

    # 아무것도 지정되지 않았거나 --all 이면 전체 포지션 생성
    if not label_positions or args.all:
        label_positions = ["center", "bottom", "below"]

    # 배경 모드 결정
    bg_modes = []
    if args.bg:
        bg_modes.append(True)
    if args.no_bg:
        bg_modes.append(False)
    if not bg_modes:
        bg_modes = [True, False]

    # 실행
    include_icon = not args.no_img

    try:
        if args.icon or args.all:
            print("🚀 Generating icons...")
            target_icon_dir = out_dir if use_subdir else out_dir / "icon"
            icon.generate_icons(
                in_path=in_path,
                out_dir=target_icon_dir,
                label_positions=label_positions,
                bg_modes=bg_modes,
                use_subdir=use_subdir,
                include_icon=include_icon,
                as_react=args.react,
            )

        if args.logo or args.all:
            print("🚀 Generating logos...")
            target_logo_dir = out_dir if use_subdir else out_dir / "logo"
            logo.generate_logos(
                in_path=in_path,
                out_dir=target_logo_dir,
                bg_modes=bg_modes,
                use_subdir=use_subdir,
                include_icon=include_icon,
                as_react=args.react,
            )

        print("\n✨ All tasks completed successfully!")

    except Exception as e:
        print(f"❌ Error during execution: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
