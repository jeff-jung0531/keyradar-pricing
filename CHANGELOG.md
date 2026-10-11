# 변경 기록

형식: `YYYY-MM-DD` / 바뀐 프로바이더 / 사람이 확인한 PR

## 2026-10-11

- anthropic: 기존 모델 입출력 단가는 변동 없음. 캐시 단가(cache_read/cache_write)를 모든 모델에 채우고, 새 모델 7종(claude-opus-4-6, claude-opus-5, claude-opus-5-5, claude-sonnet-5-5, claude-haiku-5-5, claude-fable-5, claude-fable-5-1)을 추가했습니다.
- openai, google-gemini, perplexity, mistral, xai, replicate: 네트워크 정책으로 페이지 접근이 차단돼 확인하지 못했습니다. `checked_at` 유지.

## 2026-09-24

- 저장소 개설. KeyRadar 앱에 동봉돼 있던 `2026-07-12` 스냅샷을 그대로 옮겨 왔습니다.
- 옮긴 것은 값뿐이며, **이 날짜에 가격 페이지를 다시 확인하지는 않았습니다.** 각 항목의 `checked_at`은 `2026-07-12`로 두었습니다.
- 첫 자동 갱신에서 실제 페이지와 대조합니다.
