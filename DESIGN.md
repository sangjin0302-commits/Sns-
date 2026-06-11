# Ethos Administrative Office — Design System

## Brand Identity
Classical authority meets modern accessibility.
Symbol: Greek column (logic) + star (clarity) + hand (empathy) = Logos · Pathos · Ethos.
Tone: Trustworthy, precise, approachable. Never cold. Never loud.

## Color Tokens
```
--navy:       #1B2B6B   /* primary text, headers, accent bars */
--gold:       #B8972A   /* highlights, badges, decorative lines */
--cream:      #F5F0E8   /* warm background */
--white:      #FFFFFF   /* clean background */
--text-dark:  #2C2C2A   /* body text */
--text-muted: #5F5E5A   /* captions, labels */
--border:     #E0E0E0   /* dividers */
```

## Typography
- Headlines:  Bold, Navy (#1B2B6B)
- Subheads:   Medium, Navy
- Body:       Regular, Dark (#2C2C2A)
- Labels:     Small, Muted (#5F5E5A)
- Accent:     Gold (#B8972A) for decorative text only

## Card Layout Rules
```
Top accent bar:   8px, Navy or Gold
Padding:          72px all sides
Logo placement:   bottom-right, 85% opacity
Logo max size:    18% of card width
Dividers:         1px solid #E0E0E0
Badge pill:       cream bg + gold text + rounded
```

## Card Structure (1080×1080)
```
┌─────────────────────────────┐
│ ▓▓▓ 8px Navy accent bar     │
│                             │
│  [Badge pill]               │
│                             │
│  Headline                   │
│  (2-3 lines max)            │
│                             │
│  ─────────────────          │
│                             │
│  • Key point 1              │
│  • Key point 2              │
│  • Key point 3              │
│                             │
│  ─────────────────          │
│  Source caption    [Logo]   │
└─────────────────────────────┘
```

## Anti-Patterns (절대 금지)
- ❌ Teal green, coral, bright colors
- ❌ Drop shadows or gradients
- ❌ Cluttered layouts (3개 초과 색상)
- ❌ Text without hierarchy
- ❌ Logo missing
- ❌ Generic stock-photo aesthetic

## Voice & Tone
- Korean blog: 공감 → 정보 → 행동 유도
- LinkedIn:    Authoritative but accessible, English
- Both:        One clear message per piece
