---
name: card
description: 에토스 브랜드 카드뉴스 PNG 생성. 인스타(1080x1080) + 링크드인(1200x628). 네이비/골드/크림 컬러 고정. 로고 자동 삽입.
triggers:
  - 카드 만들어줘
  - /card
  - 카드뉴스 생성
  - PNG 만들어줘
version: 1.0.0
---

# Card Agent — 에토스 행정사사무소

## 역할
블로그 내용에서 핵심 메시지를 추출하여
브랜드 카드 2장(인스타 + 링크드인)을 생성한다.

## 실행 방법
```bash
python scripts/generate_card.py \
  --type insta \
  --badge "[배지 텍스트]" \
  --headline "[헤드라인 1]" "[헤드라인 2]" \
  --rows "[레이블1]" "[값1]" "[레이블2]" "[값2]" \
  --source "[출처]" \
  --filename "[파일명].png"
```

## 카드당 콘텐츠 추출 규칙
블로그에서 다음만 추출:
- 핵심 메시지 1개 (헤드라인)
- 핵심 데이터 3개 이하 (rows)
- 출처 1개
- 배지: 주제 카테고리 (예: "행정사 실무", "법률 업데이트")

## 브랜드 강제 적용
- accent_color: NAVY (#1B2B6B) 기본
  - 긴급/경고성 주제: GOLD (#B8972A)
- 배경: CREAM (#F5F0E8)
- 로고: assets/logo.png 자동 삽입
- 금지: 다른 색상 절대 불가

## 품질 체크
생성 후 자동 확인:
- [ ] 브랜드 컬러만 사용
- [ ] 로고 우하단 포함
- [ ] 출처 표기
- [ ] 텍스트 잘림 없음

## 출력
- outputs/cards/YYYYMMDD_[slug]_insta.png   (1080×1080)
- outputs/cards/YYYYMMDD_[slug]_linkedin.png (1200×628)
