#!/usr/bin/env python3
"""pricing.json 검사. 형식 위반과 의심스러운 변동을 잡는다.

갱신 루틴은 PR을 열기 전에 이 검사를 통과해야 한다. 값이 크게 흔들릴 때
막는 것이 목적이다 — 가격 페이지를 잘못 읽은 초안이 조용히 머지되면
앱이 틀린 금액을 사실처럼 보여준다.

사용:
    python3 scripts/validate.py                 # 형식만
    python3 scripts/validate.py --base old.json # 이전 값과 비교까지
"""
import argparse, json, re, sys

UNITS_IO = {"per_mtoken", "per_mchar"}
UNITS_FLAT = {"per_image", "per_second", "per_request"}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
# 하루 사이 2배 이상 뛰면 사람이 봐야 한다. 실제 인하/인상은 보통 이보다 작다.
JUMP_RATIO = 2.0


def check_shape(doc, errors):
    if doc.get("schema_version") != 2:
        errors.append("schema_version이 2가 아닙니다")
    if doc.get("currency") != "USD":
        errors.append("currency가 USD가 아닙니다")
    if not DATE.match(str(doc.get("updated_at", ""))):
        errors.append("updated_at 형식이 YYYY-MM-DD가 아닙니다")

    for pid, p in (doc.get("providers") or {}).items():
        if not p.get("source_url"):
            errors.append(f"{pid}: source_url이 비었습니다")
        if not DATE.match(str(p.get("checked_at", ""))):
            errors.append(f"{pid}: checked_at 형식이 잘못됐습니다")
        seen = set()
        for m in p.get("models") or []:
            name, unit = m.get("model"), m.get("unit")
            if not name:
                errors.append(f"{pid}: model 이름이 없는 항목이 있습니다")
                continue
            if name in seen:
                errors.append(f"{pid}/{name}: 같은 모델이 두 번 있습니다")
            seen.add(name)
            if unit in UNITS_IO:
                for f in ("input", "output"):
                    v = m.get(f)
                    if not isinstance(v, (int, float)) or v < 0:
                        errors.append(f"{pid}/{name}: {f} 값이 잘못됐습니다 ({v!r})")
            elif unit in UNITS_FLAT:
                v = m.get("price")
                if not isinstance(v, (int, float)) or v < 0:
                    errors.append(f"{pid}/{name}: price 값이 잘못됐습니다 ({v!r})")
            else:
                errors.append(f"{pid}/{name}: 모르는 unit입니다 ({unit!r})")
            for f in ("cache_read", "cache_write"):
                if f not in m:
                    continue
                v = m.get(f)
                if not isinstance(v, (int, float)) or v < 0:
                    errors.append(f"{pid}/{name}: {f} 값이 잘못됐습니다 ({v!r})")


def flat(doc):
    out = {}
    for pid, p in (doc.get("providers") or {}).items():
        for m in p.get("models") or []:
            for f in ("input", "output", "price", "cache_read", "cache_write"):
                if isinstance(m.get(f), (int, float)):
                    out[(pid, m["model"], f)] = m[f]
    return out


def check_drift(new, base, warnings):
    a, b = flat(base), flat(new)
    for k, old in a.items():
        cur = b.get(k)
        if cur is None:
            warnings.append(f"{k[0]}/{k[1]} {k[2]}: 사라졌습니다 (이전 {old})")
            continue
        if old == 0 or cur == 0:
            continue
        r = cur / old
        if r >= JUMP_RATIO or r <= 1 / JUMP_RATIO:
            warnings.append(f"{k[0]}/{k[1]} {k[2]}: {old} → {cur} ({r:.1f}배)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default="pricing.json")
    ap.add_argument("--base", help="비교할 이전 pricing.json")
    args = ap.parse_args()

    doc = json.load(open(args.path, encoding="utf-8"))
    errors, warnings = [], []
    check_shape(doc, errors)
    if args.base:
        check_drift(doc, json.load(open(args.base, encoding="utf-8")), warnings)

    for w in warnings:
        print(f"확인 필요: {w}")
    for e in errors:
        print(f"오류: {e}")

    n = sum(len(p.get("models") or []) for p in (doc.get("providers") or {}).values())
    print(f"프로바이더 {len(doc.get('providers') or {})}곳 / 모델 {n}개 / 오류 {len(errors)}건 / 확인 필요 {len(warnings)}건")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
