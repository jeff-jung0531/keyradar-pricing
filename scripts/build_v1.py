#!/usr/bin/env python3
"""pricing.json(v2) → dist/providers.v1.json 변환.

현재 출시된 KeyRadar는 토큰 단가 두 칸짜리 구버전 형식만 읽는다. 앱이 v2를
읽도록 바뀌기 전까지, 토큰 과금 모델만 추려 구버전 형식으로도 내보낸다.
per_image/per_second 같은 단위는 구버전 형식으로 표현할 수 없으므로 빠진다.
"""
import json, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
doc = json.loads((root / "pricing.json").read_text(encoding="utf-8"))

providers, dropped = {}, 0
for pid, p in doc["providers"].items():
    rows = []
    for m in p["models"]:
        if m["unit"] != "per_mtoken":
            dropped += 1
            continue
        rows.append({"model": m["model"],
                     "inputPerMtoken": m["input"],
                     "outputPerMtoken": m["output"]})
    if rows:
        providers[pid] = rows

out = {
    "version": doc["updated_at"],
    "currency": "USD",
    "_doc": ("Generated from pricing.json by scripts/build_v1.py - do not edit by hand. "
             "Token-billed models only; other billing units cannot be expressed in this format."),
    "providers": providers,
}
(root / "dist").mkdir(exist_ok=True)
(root / "dist" / "providers.v1.json").write_text(json.dumps(out, indent=2) + "\n")
n = sum(len(v) for v in providers.values())
print(f"providers.v1.json: {len(providers)}곳 / {n}개 (단위가 달라 제외: {dropped}개)")
