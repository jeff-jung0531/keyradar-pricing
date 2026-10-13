# 변경 기록

형식: `YYYY-MM-DD` / 바뀐 프로바이더 / 사람이 확인한 PR

## 2026-10-13

- anthropic: `www.anthropic.com/pricing`가 `claude.com/pricing`으로 301 리다이렉트돼 리다이렉트된 주소에서 다시 확인했습니다. Opus 4.8 / Opus 4.7 / Opus 4.5 / Sonnet 5 / Sonnet 4.6 / Sonnet 4.5 / Haiku 4.5 모델에 페이지에 나와 있던 캐시 쓰기·읽기 단가가 빠져 있어 채웠습니다. 입력·출력 단가는 바뀌지 않았습니다.
- openai, google-gemini, perplexity, mistral, xai는 이 환경의 조직 egress 정책이 해당 도메인(openai.com, ai.google.dev, docs.perplexity.ai, mistral.ai, docs.x.ai)에 대한 CONNECT를 403으로 거부해 이번에도 확인하지 못했습니다. 저장소 개설(2026-07-12 스냅샷) 이후 이 다섯 프로바이더는 한 번도 재확인되지 않았습니다 — 네트워크 정책이 바뀌지 않는 한 이 루틴으로는 계속 확인할 수 없습니다.

## 2026-10-12

- anthropic: Fable 5.1 / Opus 5.5 / Sonnet 5.5 / Haiku 5.5 / Opus 5 / Fable 5 / Opus 4.6 모델을 새로 추가했습니다. 기존에 있던 모델의 단가는 바뀌지 않았습니다. Haiku 5.5는 10만 토큰 초과 구간의 단가가 따로 있지만, API가 보고하는 모델명이 구간과 무관하게 같아 앱이 조회할 수 없으므로 별도 모델로 넣지 않고 note로만 남겼습니다.
- openai, google-gemini, perplexity, mistral, xai, replicate는 이 환경의 네트워크 정책이 해당 도메인을 막아 이번에는 확인하지 못했습니다.

## 2026-09-24

- 저장소 개설. KeyRadar 앱에 동봉돼 있던 `2026-07-12` 스냅샷을 그대로 옮겨 왔습니다.
- 옮긴 것은 값뿐이며, **이 날짜에 가격 페이지를 다시 확인하지는 않았습니다.** 각 항목의 `checked_at`은 `2026-07-12`로 두었습니다.
- 첫 자동 갱신에서 실제 페이지와 대조합니다.
