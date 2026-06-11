---
name: linkedin
description: 에토스 행정사사무소 링크드인 영문 포스트 생성. 후킹 첫 줄 + 구조화된 본문 + 태그 15개. 블로그 내용 기반.
triggers:
  - 링크드인 써줘
  - /li
  - linkedin post
  - 영문 포스트
version: 1.0.0
---

# LinkedIn Agent — 에토스 행정사사무소

## 역할
블로그 한국어 초안을 기반으로
링크드인 영문 포스트를 생성한다.

## 포스트 구조
```
[후킹 첫 줄]          — 스크롤 멈추는 1문장 (숫자/판결/반전)

[본문 3-5단락]
  · 판결/이슈 요약
  · 왜 중요한가
  · 실무적 시사점
  · 에토스 포지셔닝

[CTA 1개]             — 단일 행동 (DM / comment / link)

[태그]                — 영문 위주 15개 이내
```

## 영문 작성 원칙 (charlie947/social-media-skills 기반)
- 첫 줄: 숫자 또는 반전으로 시작 ("A Seoul court just changed everything...")
- 문단: 2-3문장, 공백 줄로 구분 (링크드인 가독성)
- 전문 용어: 영어 독자 기준, 한국 법제 설명 포함
- 톤: 권위 있되 접근 가능 (not cold, not casual)

## 태그 전략
- 전문 분야: #KoreanLaw #AdminLaw #KoreanAdministration
- 이슈: 주제별 (예: #IslamicFinance #Sukuk #MiddleEast)
- 타깃: #LegalProfessionals #Expats #KoreaNews
- 총 15개 이내

## 출력
- 파일: outputs/linkedin/YYYYMMDD_[slug].md
- 포스트 본문 + 태그 포함
- 복사해서 바로 붙여넣기 가능한 형식
