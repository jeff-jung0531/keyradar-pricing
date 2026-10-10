# 변경 기록

형식: `YYYY-MM-DD` / 바뀐 프로바이더 / 사람이 확인한 PR

## 2026-10-10

- anthropic: claude.com/pricing 및 platform.claude.com 모델 문서 대조. 기존 모델 단가는 변동 없음. Fable 5.1, Mythos 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5, Opus 4.6, Opus 5, Fable 5, Mythos 5 모델을 추가하고, 모든 모델에 캐시 쓰기/읽기 단가를 채웠습니다. Haiku 5.5는 프롬프트 100K 토큰을 넘으면 단가가 달라져 `tiered_pricing`을 표시했고, 구버전 변환본(`dist/providers.v1.json`)에서는 뺐습니다.
- validate.py가 cache_read/cache_write 값도 형식·변동 검사하도록 범위를 넓혔습니다.
- openai, google-gemini, perplexity, mistral, xai, replicate: 네트워크 정책이 해당 도메인을 막아 이번 회차에는 확인하지 못했습니다.

## 2026-09-24

- 저장소 개설. KeyRadar 앱에 동봉돼 있던 `2026-07-12` 스냅샷을 그대로 옮겨 왔습니다.
- 옮긴 것은 값뿐이며, **이 날짜에 가격 페이지를 다시 확인하지는 않았습니다.** 각 항목의 `checked_at`은 `2026-07-12`로 두었습니다.
- 첫 자동 갱신에서 실제 페이지와 대조합니다.
