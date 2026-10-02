# 변경 기록

형식: `YYYY-MM-DD` / 바뀐 프로바이더 / 사람이 확인한 PR

## 2026-10-02

- anthropic: 공식 가격 페이지(claude.com/pricing)를 다시 확인해 캐싱 단가(`cache_read`/`cache_write`)를 추가하고, 새 모델(Fable 5.1, Opus 5.5, Sonnet 5.5, Sonnet 5, Opus 5, Fable 5, Opus 4.6)을 반영했습니다. 기존 모델의 입력/출력 단가는 변동이 없었습니다.
- openai, google-gemini, perplexity, mistral, xai, replicate: 네트워크 egress 정책에 막혀 공식 페이지를 직접 읽지 못해 이번 갱신에서 제외했습니다.

## 2026-09-24

- 저장소 개설. KeyRadar 앱에 동봉돼 있던 `2026-07-12` 스냅샷을 그대로 옮겨 왔습니다.
- 옮긴 것은 값뿐이며, **이 날짜에 가격 페이지를 다시 확인하지는 않았습니다.** 각 항목의 `checked_at`은 `2026-07-12`로 두었습니다.
- 첫 자동 갱신에서 실제 페이지와 대조합니다.
