# 에토스 행정사사무소 — SNS 콘텐츠 파이프라인

블로그(네이버) + 링크드인 운영을 위한 Claude Code 기반 콘텐츠 자동 생성 파이프라인.

## 구조

```
Sns-/
├── CLAUDE.md              ← Claude Code 핵심 지침 (자동 로드)
├── DESIGN.md              ← 에토스 브랜드 디자인 시스템
├── assets/
│   └── logo.png           ← 로고 파일 (직접 추가 필요)
├── skills/
│   ├── research.md        ← 팩트 검증 원칙
│   ├── marketing.md       ← SEO·CTA 원칙
│   └── taste.md           ← 카드 디자인 원칙
├── scripts/
│   └── generate_card.py   ← 카드 PNG 생성
├── templates/
│   ├── blog_template.md   ← 블로그 구조
│   └── linkedin_template.md
└── outputs/
    ├── blog/
    ├── cards/
    └── linkedin/
```

## 시작 방법

### 1. Claude Code 설치
```bash
npm install -g @anthropic-ai/claude-code
```

### 2. 레포 클론
```bash
git clone https://github.com/sangjin0302-commits/Sns-.git
cd Sns-
```

### 3. 로고 추가
```bash
# assets/ 폴더에 logo.png 복사
cp ~/Downloads/logo.png assets/logo.png
```

### 4. 의존성 설치
```bash
pip install pillow
```

### 5. Claude Code 실행
```bash
claude
```

## 사용법

Claude Code 터미널에서 아래 형식으로 입력:

```
글감: [주제]
독자: [타깃 독자]
훅:   [최신 판결/뉴스/통계]
상황: [독자 처한 상황]
출력: all
```

### 예시

```
글감: 동거계약서 필요성
독자: 동성·비혼 커플 당사자
훅: 2026.6.5 서울중앙지법 동성커플 손해배상 1000만원 판결
상황: 법적 보호 없이 함께 살고 있음
출력: all
```

Claude Code가 자동으로:
1. 웹 검색으로 훅 팩트 검증
2. 블로그 초안 생성 → `outputs/blog/`
3. 카드 2장 생성 (인스타 + 링크드인) → `outputs/cards/`
4. 링크드인 영문 포스트 + 태그 → `outputs/linkedin/`

## 브랜드 컬러
| 용도 | 색상 | HEX |
|------|------|-----|
| 주 텍스트·강조 | 네이비 | #1B2B6B |
| 포인트·장식 | 골드 | #B8972A |
| 카드 배경 | 크림 베이지 | #F5F0E8 |

## 레퍼런스 레포
- [marketingskills](https://github.com/coreyhaines31/marketingskills)
- [academic-research-skills](https://github.com/Imbad0202/academic-research-skills)
- [taste-skill](https://github.com/leonxlnx/taste-skill)
- [awesome-design-md](https://github.com/VoltAgent/awesome-design-md)
