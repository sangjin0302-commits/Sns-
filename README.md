# 에토스 행정사사무소 — SNS 콘텐츠 파이프라인

> 글감 입력 하나 → 블로그 + 카드 2장 + 링크드인 포스트 자동 생성

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 개요

이 레포는 **Claude Code** 기반 콘텐츠 자동화 파이프라인이다.
네이버 블로그(한국어) + 링크드인(영문) 동시 운영을 위한 에토스 행정사사무소 전용 도구.

```
입력: 글감 + 독자 + 훅 + 상황
  ↓
Research 에이전트  → 팩트 검증, 출처 확보
Blog 에이전트      → 네이버 블로그 초안 (한국어)
Card 에이전트      → 카드 PNG 2장 (인스타 + 링크드인)
LinkedIn 에이전트  → 영문 포스트 + 태그
  ↓
출력: outputs/ 폴더에 파일 저장
```

---

## 폴더 구조

```
Sns-/
├── CLAUDE.md                  ← Claude Code 핵심 지침 (자동 로드)
├── DESIGN.md                  ← 에토스 브랜드 디자인 시스템
│
├── assets/
│   └── logo.png               ← 로고 파일 (직접 추가 필요)
│
├── skills/                    ← Claude Code 에이전트 스킬
│   ├── blog.md                ← 블로그 작성 에이전트
│   ├── card.md                ← 카드 생성 에이전트
│   ├── linkedin.md            ← 링크드인 에이전트
│   ├── research.md            ← 팩트 검증 원칙
│   ├── marketing.md           ← SEO·CTA 원칙
│   └── taste.md               ← 카드 디자인 원칙
│
├── scripts/
│   └── generate_card.py       ← 카드 PNG 생성 스크립트
│
├── templates/
│   └── brief.yaml             ← 콘텐츠 브리프 템플릿
│
└── outputs/                   ← 생성 결과물 (gitignore 가능)
    ├── blog/
    ├── cards/
    └── linkedin/
```

---

## 시작하기

### 1. 사전 요구사항

| 도구 | 버전 | 설치 |
|------|------|------|
| Node.js | 18+ | https://nodejs.org |
| Python | 3.9+ | https://python.org |
| Claude Code | 최신 | 아래 참조 |

### 2. Claude Code 설치

```bash
npm install -g @anthropic-ai/claude-code
```

설치 확인:
```bash
claude --version
```

### 3. 레포 클론

```bash
git clone https://github.com/sangjin0302-commits/Sns-.git
cd Sns-
```

### 4. 의존성 설치

```bash
pip install pillow
```

### 5. 로고 추가

```bash
mkdir -p assets
# 프로젝트 파일의 logo.png를 assets/ 폴더에 복사
cp /path/to/logo.png assets/logo.png
```

### 6. Claude Code 실행

```bash
claude
```

Claude Code가 자동으로 `CLAUDE.md`와 `skills/`를 읽고 준비 완료.

---

## 사용법

### 방법 1: 슬래시 커맨드 (권장)

Claude Code 터미널에서:

```
/all 글감: 동거계약서 필요성
```

또는 상세 입력:

```
/all
글감: 동거계약서 필요성
독자: 동성·비혼 커플 당사자
훅: 2026.6.5 서울중앙지법 동성커플 손해배상 1000만원 판결
상황: 법적 보호 없이 함께 살고 있음
```

### 방법 2: 브리프 파일 사용

`templates/brief.yaml` 복사 후 내용 작성:

```yaml
content:
  topic: "동거계약서 필요성"
  target_reader: "동성·비혼 커플 당사자 30대"
  hook: "2026.6.5 서울중앙지법 동성커플 손해배상 1000만원 판결"
  situation: "법적 보호 없이 함께 살고 있음"
  output: "all"
```

저장 후 Claude Code에서:
```
brief.yaml 읽고 /all 실행해줘
```

### 방법 3: 개별 실행

```
/blog 글감: 수쿠크 이슬람 채권
/card 글감: 수쿠크 이슬람 채권
/li   글감: 수쿠크 이슬람 채권
```

---

## 슬래시 커맨드 목록

| 커맨드 | 설명 |
|--------|------|
| `/all [글감]` | 블로그 + 카드 2장 + 링크드인 전체 생성 |
| `/blog [글감]` | 네이버 블로그 초안만 생성 |
| `/card [글감]` | 카드 PNG 2장만 생성 |
| `/li [글감]` | 링크드인 영문 포스트만 생성 |
| `/check [파일]` | 브랜드 컬러·구조 검수 |

---

## 출력 예시

`/all` 실행 후 생성되는 파일:

```
outputs/
├── blog/
│   └── 20260611_동거계약서.md        ← 네이버 블로그 초안
├── cards/
│   ├── 20260611_동거계약서_insta.png  ← 1080×1080 인스타 카드
│   └── 20260611_동거계약서_li.png     ← 1200×628 링크드인 카드
└── linkedin/
    └── 20260611_동거계약서.md         ← 영문 포스트 + 태그
```

---

## 브랜드 컬러

| 역할 | 색상 | HEX |
|------|------|-----|
| 주 텍스트·강조 | 네이비 | `#1B2B6B` |
| 포인트·장식 | 골드 | `#B8972A` |
| 카드 배경 | 크림 베이지 | `#F5F0E8` |

> ⚠️ 틸 그린, 코럴 등 브랜드 외 색상 절대 사용 금지

---

## 품질 게이트

발행 전 자동 체크 (`/check` 실행):

- [ ] 팩트 출처 URL 포함
- [ ] 브랜드 컬러만 사용
- [ ] 로고 포함 (카드)
- [ ] 글감 하나만 다룸
- [ ] CTA 1개
- [ ] 면책 문구 마지막 배치

---

## 레퍼런스 오픈소스

이 파이프라인은 아래 오픈소스를 참고하여 에토스 브랜드에 맞게 커스텀됐다.

| 레포 | 역할 | 라이선스 |
|------|------|---------|
| [AgriciDaniel/claude-blog](https://github.com/AgriciDaniel/claude-blog) | 블로그 4-agent 파이프라인 | MIT |
| [charlie947/social-media-skills](https://github.com/charlie947/social-media-skills) | 링크드인 포스트 생성 | MIT |
| [iamasters-academy/content-engine](https://github.com/iamasters-academy/content-engine) | SNS 파이프라인 구조 | MIT |
| [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) | 디자인 품질 원칙 | MIT |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | DESIGN.md 포맷 | MIT |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | SEO·CTA 전략 | MIT |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 팩트 검증 원칙 | MIT |

---

## 향후 고도화 계획

- [ ] `banana-claude` 연동 → AI 이미지 생성으로 카드 품질 업그레이드
- [ ] GitHub Actions → 브리프 파일 푸시 시 자동 파이프라인 실행
- [ ] 콘텐츠 캘린더 → `calendar.md`로 주제 목록 관리
- [ ] 성과 분석 → 발행 이력 추적, 패턴 분석

---

## 라이선스

MIT
