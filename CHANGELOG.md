# 변경 기록

형식: `YYYY-MM-DD` / 바뀐 프로바이더 / 사람이 확인한 PR

## 2026-09-26

- anthropic: 가격 페이지(claude.com/pricing, anthropic.com/pricing에서 리다이렉트)를 다시 확인해 Opus 5.5 / Fable 5.1 / Opus 5 / Fable 5 / Opus 4.6 모델을 추가하고, 전 모델에 프롬프트 캐싱(cache_read/cache_write) 단가를 채웠습니다. 기존 모델의 input/output 단가는 변동이 없었습니다.
- openai, google-gemini, perplexity, mistral, xai, replicate: 이번 실행 환경의 네트워크 정책이 해당 도메인을 차단해 페이지를 읽지 못했습니다. 값은 그대로 두었습니다.

## 2026-09-24

- 저장소 개설. KeyRadar 앱에 동봉돼 있던 `2026-07-12` 스냅샷을 그대로 옮겨 왔습니다.
- 옮긴 것은 값뿐이며, **이 날짜에 가격 페이지를 다시 확인하지는 않았습니다.** 각 항목의 `checked_at`은 `2026-07-12`로 두었습니다.
- 첫 자동 갱신에서 실제 페이지와 대조합니다.
