"""
에토스 행정사사무소 — 카드 생성 스크립트
브랜드 컬러 고정: 네이비 #1B2B6B, 골드 #B8972A, 배경 #F5F0E8
사용: python scripts/generate_card.py
"""

from PIL import Image, ImageDraw, ImageFont
import os, sys, textwrap

# ── 브랜드 토큰 ──────────────────────────────────────────────
NAVY   = "#1B2B6B"
GOLD   = "#B8972A"
CREAM  = "#F5F0E8"
WHITE  = "#FFFFFF"
DARK   = "#2C2C2A"
MUTED  = "#5F5E5A"
BORDER = "#E0E0E0"

LOGO_PATH = "assets/logo.png"
OUT_DIR   = "outputs/cards"
os.makedirs(OUT_DIR, exist_ok=True)

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def get_font(size, bold=False):
    candidates = [
        f"/usr/share/fonts/truetype/nanum/NanumGothic{'Bold' if bold else ''}.ttf",
        f"/usr/share/fonts/truetype/dejavu/DejaVuSans{'-Bold' if bold else ''}.ttf",
        f"/usr/share/fonts/truetype/liberation/LiberationSans{'-Bold' if bold else '-Regular'}.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def add_logo(img, logo_path, padding=40):
    """우하단 워터마크 로고 삽입"""
    if not os.path.exists(logo_path):
        return
    logo = Image.open(logo_path).convert("RGBA")
    max_w = int(img.width * 0.18)
    ratio = max_w / logo.width
    new_size = (max_w, int(logo.height * ratio))
    logo = logo.resize(new_size, Image.LANCZOS)
    # 투명도 85%
    alpha = logo.split()[3]
    alpha = alpha.point(lambda p: int(p * 0.85))
    logo.putalpha(alpha)
    x = img.width - new_size[0] - padding
    y = img.height - new_size[1] - padding
    img.paste(logo, (x, y), logo)

def make_card_insta(
    badge_text: str,
    headline_lines: list,
    rows: list,          # [(label, value), ...]
    source_text: str,
    filename: str,
    accent_color: str = NAVY,
):
    """
    1080×1080 인스타그램 카드 생성
    rows: [("레이블", "내용"), ...]
    """
    W, H = 1080, 1080
    PAD = 72

    img = Image.new("RGB", (W, H), hex_to_rgb(CREAM))
    d = ImageDraw.Draw(img)

    # 상단 accent bar
    d.rectangle([0, 0, W, 10], fill=hex_to_rgb(accent_color))

    # 폰트
    f_badge    = get_font(26)
    f_headline = get_font(52, bold=True)
    f_headline2= get_font(46, bold=True)
    f_label    = get_font(24)
    f_value    = get_font(30, bold=True)
    f_footer   = get_font(21)

    y = 60

    # Badge pill
    bw = d.textlength(badge_text, font=f_badge) + 40
    d.rounded_rectangle([PAD, y, PAD + bw, y + 44], radius=22,
                        fill=hex_to_rgb(WHITE))
    d.rectangle([PAD, y, PAD + bw, y + 44],
                outline=hex_to_rgb(GOLD), width=2)
    d.text((PAD + 20, y + 8), badge_text, font=f_badge,
           fill=hex_to_rgb(GOLD))
    y += 68

    # Headline
    for i, line in enumerate(headline_lines):
        f = f_headline if i == 0 else f_headline2
        d.text((PAD, y), line, font=f, fill=hex_to_rgb(NAVY))
        y += 62
    y += 16

    # Divider
    d.line([PAD, y, W - PAD, y], fill=hex_to_rgb(BORDER), width=1)
    y += 32

    # Rows
    for label, value in rows:
        d.rectangle([PAD, y + 4, PAD + 6, y + 56],
                    fill=hex_to_rgb(GOLD))
        d.text((PAD + 22, y), label, font=f_label, fill=hex_to_rgb(MUTED))
        # 긴 텍스트 줄 나눔
        max_chars = 38
        if len(value) > max_chars:
            lines = textwrap.wrap(value, width=max_chars)
            for j, ln in enumerate(lines[:2]):
                d.text((PAD + 22, y + 28 + j * 34), ln,
                       font=f_value, fill=hex_to_rgb(DARK))
            y += 28 + len(lines[:2]) * 34 + 24
        else:
            d.text((PAD + 22, y + 28), value, font=f_value,
                   fill=hex_to_rgb(DARK))
            y += 96

    # 하단 divider + source
    d.line([PAD, H - 110, W - PAD, H - 110], fill=hex_to_rgb(BORDER), width=1)
    d.text((PAD, H - 88), source_text, font=f_footer, fill=hex_to_rgb(MUTED))
    d.text((PAD, H - 58), "에토스 행정사사무소", font=f_footer,
           fill=hex_to_rgb(GOLD))

    # 하단 accent bar
    d.rectangle([0, H - 10, W, H], fill=hex_to_rgb(accent_color))

    # 로고
    add_logo(img, LOGO_PATH)

    path = os.path.join(OUT_DIR, filename)
    img.save(path)
    print(f"✅ 저장: {path}")
    return path


def make_card_linkedin(
    badge_text: str,
    headline: str,
    blocks: list,        # [(block_title, [item1, item2, ...]), ...]
    source_text: str,
    filename: str,
    accent_color: str = NAVY,
):
    """
    1200×628 링크드인 카드 생성
    blocks: [("블록제목", ["항목1", "항목2"]), ...]
    """
    W, H = 1200, 628
    PAD = 64

    img = Image.new("RGB", (W, H), hex_to_rgb(WHITE))
    d = ImageDraw.Draw(img)

    # 좌측 네이비 사이드바
    d.rectangle([0, 0, 12, H], fill=hex_to_rgb(accent_color))

    f_badge   = get_font(22)
    f_headline= get_font(40, bold=True)
    f_label   = get_font(20)
    f_item    = get_font(22)
    f_footer  = get_font(18)

    y = 48

    # Badge
    bw = d.textlength(badge_text, font=f_badge) + 36
    d.rounded_rectangle([PAD, y, PAD + bw, y + 38], radius=19,
                        fill=hex_to_rgb(CREAM))
    d.text((PAD + 18, y + 7), badge_text, font=f_badge,
           fill=hex_to_rgb(NAVY))
    y += 56

    # Headline
    wrapped = textwrap.wrap(headline, width=52)
    for line in wrapped[:2]:
        d.text((PAD, y), line, font=f_headline, fill=hex_to_rgb(NAVY))
        y += 50
    y += 12

    # Divider
    d.line([PAD, y, W - PAD, y], fill=hex_to_rgb(BORDER), width=1)
    y += 20

    # Blocks (2열 배치)
    col_w = (W - PAD * 2) // 2
    col_positions = [PAD, PAD + col_w]
    for idx, (blabel, items) in enumerate(blocks[:2]):
        cx = col_positions[idx]
        cy = y
        d.text((cx, cy), blabel, font=f_label, fill=hex_to_rgb(MUTED))
        cy += 28
        for item in items[:3]:
            d.text((cx, cy), f"· {item}", font=f_item, fill=hex_to_rgb(DARK))
            cy += 32

    # Footer
    d.line([PAD, H - 70, W - PAD, H - 70], fill=hex_to_rgb(BORDER), width=1)
    d.text((PAD, H - 50), source_text, font=f_footer, fill=hex_to_rgb(MUTED))

    # 로고
    add_logo(img, LOGO_PATH, padding=32)

    path = os.path.join(OUT_DIR, filename)
    img.save(path)
    print(f"✅ 저장: {path}")
    return path


# ── 사용 예시 ─────────────────────────────────────────────────
if __name__ == "__main__":
    # 인스타 카드 예시
    make_card_insta(
        badge_text="행정사 실무",
        headline_lines=["동거계약서,", "지금 필요한 이유"],
        rows=[
            ("판결일", "2026.6.5 서울중앙지법"),
            ("인정 금액", "1,000만 원 배상"),
            ("핵심 근거", "사실혼 유사 생활공동체"),
        ],
        source_text="출처: 헤럴드경제 2026.6.10",
        filename="sample_insta.png",
        accent_color=NAVY,
    )

    # 링크드인 카드 예시
    make_card_linkedin(
        badge_text="Korean Law Update",
        headline="Same-sex couples can now claim damages for infidelity",
        blocks=[
            ("Court ruling", ["Seoul Central District Court", "June 5, 2026", "₩10M awarded"]),
            ("What it means", ["De facto partnership recognized", "Constitutional right to happiness", "Documentation now critical"]),
        ],
        source_text="Source: Herald Economy · Ethos Administrative Office",
        filename="sample_linkedin.png",
        accent_color=NAVY,
    )
