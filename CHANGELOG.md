# 변경 기록

형식: `YYYY-MM-DD` / 바뀐 프로바이더 / 사람이 확인한 PR

## 2026-09-23

- anthropic: 가격 페이지를 다시 확인해 `claude-fable-5-1`, `claude-opus-5-5`, `claude-opus-5`, `claude-fable-5`, `claude-opus-4-6` 모델과 전체 모델의 cache_read/cache_write 단가를 추가했습니다. 기존 모델의 input/output 단가는 변동이 없었습니다.
- openai, google-gemini, perplexity, mistral, xai, replicate는 네트워크 정책으로 페이지를 읽지 못해 그대로 두었습니다.

## 2026-09-24

- 저장소 개설. KeyRadar 앱에 동봉돼 있던 `2026-07-12` 스냅샷을 그대로 옮겨 왔습니다.
- 옮긴 것은 값뿐이며, **이 날짜에 가격 페이지를 다시 확인하지는 않았습니다.** 각 항목의 `checked_at`은 `2026-07-12`로 두었습니다.
- 첫 자동 갱신에서 실제 페이지와 대조합니다.
