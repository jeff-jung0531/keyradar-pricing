# 변경 기록

형식: `YYYY-MM-DD` / 바뀐 프로바이더 / 사람이 확인한 PR

## 2026-09-23

- anthropic: 가격 페이지를 다시 확인해 `claude-fable-5-1`, `claude-opus-5-5`, `claude-opus-4-6` 모델과 전체 모델의 cache_read/cache_write(표준/5분 TTL 기준) 단가를 추가했습니다. 기존 모델의 input/output 단가는 변동이 없었습니다.
- `claude-opus-5`, `claude-fable-5`는 페이지에 API 모델 ID가 표기돼 있지 않아 리뷰 피드백에 따라 제외했습니다. ID를 확인할 수 있게 되면 다시 추가합니다.
- `scripts/validate.py`가 이제 `cache_read`/`cache_write` 값의 형식과 급변동을 함께 검사합니다.
- `pricing.json`의 `_doc`과 README에 cache_read/cache_write가 표준(5분 TTL) 캐시 단가이며 연장 TTL은 포함하지 않는다는 점을 명시했습니다.
- openai, google-gemini, perplexity, mistral, xai, replicate는 네트워크 정책으로 페이지를 읽지 못해 그대로 두었습니다.

## 2026-09-24

- 저장소 개설. KeyRadar 앱에 동봉돼 있던 `2026-07-12` 스냅샷을 그대로 옮겨 왔습니다.
- 옮긴 것은 값뿐이며, **이 날짜에 가격 페이지를 다시 확인하지는 않았습니다.** 각 항목의 `checked_at`은 `2026-07-12`로 두었습니다.
- 첫 자동 갱신에서 실제 페이지와 대조합니다.
