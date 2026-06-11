# 에토스 행정사사무소 — SNS 콘텐츠 파이프라인

## 프로젝트 한 줄 설명
글감 입력 → 블로그 + 카드 2장 + 링크드인 포스트 동시 생성.

## 스킬 로드 순서
1. skills/blog.md      ← 블로그 작성 에이전트
2. skills/card.md      ← 카드 생성 에이전트
3. skills/linkedin.md  ← 링크드인 에이전트
4. skills/research.md  ← 팩트 검증
5. skills/marketing.md ← SEO·CTA
6. skills/taste.md     ← 디자인 원칙
7. DESIGN.md           ← 브랜드 토큰

## 브랜드 (모든 작업에 예외 없이 적용)
- 네이비  #1B2B6B — 주 텍스트, 강조, accent bar
- 골드    #B8972A — 포인트, badge, 장식
- 크림    #F5F0E8 — 카드 배경
- 금지    틸·코럴·브랜드 외 색상 절대 불가
- 로고    assets/logo.png → 카드 우하단, 투명도 85%

## 입력 형식 (표준)
```
글감:  [주제]
독자:  [타깃]
훅:    [최신 판결/뉴스/통계 — 웹 검색 필수]
상황:  [독자 처한 상황]
출력:  blog | card | linkedin | all
```

## 에이전트 실행 순서 (출력: all 시)
1. Research 에이전트  → 훅 팩트 검증, 출처 URL 확보
2. Blog 에이전트      → 블로그 초안 → outputs/blog/
3. Card 에이전트      → generate_card.py 실행 → outputs/cards/
4. LinkedIn 에이전트  → 영문 포스트 + 태그 → outputs/linkedin/

## 슬래시 커맨드
- /blog  [글감] — 블로그만 생성
- /card  [글감] — 카드만 생성 (인스타 + 링크드인)
- /li    [글감] — 링크드인 포스트만 생성
- /all   [글감] — 전체 파이프라인 실행
- /check [파일] — 브랜드 컬러·구조 검수

## 품질 게이트 (발행 전 체크)
- [ ] 팩트 출처 URL 포함됐나?
- [ ] 브랜드 컬러만 사용됐나?
- [ ] 로고 포함됐나?
- [ ] 글감 하나만 다뤘나?
- [ ] CTA가 1개인가?
- [ ] 면책 문구 마지막에 있나?
