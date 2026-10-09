# 변경 기록

형식: `YYYY-MM-DD` / 바뀐 프로바이더 / 사람이 확인한 PR

## 2026-10-09

- anthropic: 공식 가격 페이지(claude.com/pricing, platform.claude.com/docs/en/about-claude/pricing)를 다시 확인했습니다. 기존 모델의 단가 변경은 없었고, 새로 올라온 모델(Fable 5.1, Mythos 5.1, Opus 5.5, Sonnet 5.5, Opus 5, Fable 5, Mythos 5, Opus 4.6)을 추가했습니다.
- anthropic: 캐시 읽기 단가(cache_read)를 모든 모델에 채웠습니다. 캐시 쓰기 단가(cache_write)는 5분/1시간 TTL에 따라 값이 달라 스키마가 구분을 표현하지 못하므로 넣지 않았습니다. Haiku 5.5는 프롬프트 길이(100K 토큰 기준)에 따라 단가가 5배 차이 나고 역시 스키마가 구간을 표현하지 못해 이번에는 등록하지 않았습니다 — 코덱스 리뷰 지적 반영.
- openai, google-gemini, perplexity, mistral, xai, replicate: 이 환경의 네트워크 정책이 해당 도메인을 막고 있어 이번 회차에는 확인하지 못했습니다.

## 2026-09-24

- 저장소 개설. KeyRadar 앱에 동봉돼 있던 `2026-07-12` 스냅샷을 그대로 옮겨 왔습니다.
- 옮긴 것은 값뿐이며, **이 날짜에 가격 페이지를 다시 확인하지는 않았습니다.** 각 항목의 `checked_at`은 `2026-07-12`로 두었습니다.
- 첫 자동 갱신에서 실제 페이지와 대조합니다.
