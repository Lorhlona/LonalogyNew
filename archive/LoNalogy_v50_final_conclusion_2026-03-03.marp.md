---
marp: true
theme: default
paginate: true
title: LoNalogy v50 Final Conclusion
---

# LoNalogy v50 Final Conclusion

Date: 2026-03-03  
情報理論 + 位相 + 散逸 + Weierstrass/al + 観測拘束

---

## 結論（先に）

- LoNalogyは「散逸と回転の比率」を整数条件で離散化し、`s=3,4` を選ぶ鎖として成立。
- 観測整合は現時点で大崩壊していない。
- 予測は反証可能な形まで到達している（暗黒光子・第4世代・暗黒複合体）。
- 磁性再解釈も厳密積分段まで進んだが、高充填残差の微視的起源は未解決。

---

## 出発点（情報理論拡張）

```math
\Psi=\sqrt{p}\,e^{iS}e^{j\chi},\qquad j^2=+1
```

- `p`: 情報（確率）層
- `S`: 回転位相（可逆）
- `\chi`: 散逸位相（不可逆）

---

## セクター分解

```math
e_\pm=(1\pm j)/2,\quad \Psi=\Psi_+e_+ + \Psi_-e_-
```

- 可視 `(+ )` と不可視 `(-)` は二セクター。
- 「4つ」はセクター数ではなく位相状態（四分周期）として扱う。

---

## 鎖の核心（比率 -> 整数条件）

- 散逸/回転を混ぜると、自由度は本質的に比率1個へ圧縮される。
- その比率を連続自由度でなく整数条件で固定:

```math
(1+\kappa)^3 = 4s(s+1)\kappa
```

- これにより世代ラベル `s` が離散化される。

---

## Weierstrass鎖（数値）

`s=3`:
- `kappa=5.360280`
- `Omega=0.685548`
- `m=0.469977`
- `tau=1.027845 i`
- `j=1746.812` (1728近傍)

`s=4`:
- `kappa=7.394648`
- `Omega=0.761753`
- `m=0.580268`
- `tau=0.928794 i`
- `j=1867.956`

---

## Kimura-Thevenin射影（可視->全系）

作業式:

```math
src = A_+\Xi p + \epsilon A_-(Cd)
```

- 可視観測から `Xi, epsilon, mA` を同時拘束。
- 射影子で可視/不可視を一貫記述。
- 可視のみで全系予測を出す基盤になっている。

---

## v51 観測アンカー

- best `epsilon_phys = 5.039e-11`
- best `mA = 0.2201 GeV`
- best `obs_chi2 = 14.010`
- best `Xi = [45.29, 14.08, 1.0]`

意味:
- 暗黒光子質量が HyperCP近傍帯に入る。
- ただし決着は未済（実データ閉包が必要）。

---

## Sensitivity Gap（非検出の理由）

`mA~220 MeV`, `epsilon~5e-11` で:
- `ctau ~ 1.03e5 km`

`G_eps`:
- LHCb prompt: `131.26` (感度外)
- LHCb displaced: `50.67` (感度外)
- SHiP: `0.077` (到達可能)
- FASER2: `19.38` (感度外)

---

## v52 第4世代窓

REAL制約下:
- `m4 window = 339.82 - 365.17 GeV`
- `Omega4 h^2 ~ 0.113`（soft-best）
- `t_cool ~ 1.47e5 Gyr`（冷えにくい）

含意:
- ディスク化しにくい重い暗黒成分としてハロー骨格候補。

---

## 力の再定義（LoNalogy作業仮説）

- 重力（共通背景）
- 弱い力（有効的にはセクター間交換 `epsilon`）
- 可視電磁 `U(1)+`
- 可視強い力 `SU(3)+`
- 暗黒電磁 `U(1)-`
- 暗黒強い力 `SU(N)-`

計6系統。

---

## 強い力・電磁気・重力の立場

- 強い力:
  可視/不可視で別系統。セクター間で色荷の直接交流はない。
- 電磁気:
  `A` と `A_D` の二層。交流は運動学混合 `epsilon` のみ。
- 重力:
  現段階は背景幾何として扱い、グラビトンは基礎仮定に入れない。

---

## 銀河回転への読み替え

- 第4世代暗黒成分が冷えにくいハローを形成。
- その重力ポテンシャルで外縁回転速度を支える。
- 「見える質量だけでは足りない」不整合に対して自然な説明候補。

注:
- 多銀河同時フィットとレンズ/CMB同時整合は継続課題。

---

## v53 磁性再解釈（実験側）

- 前登録分類: `9/10`
- 参照チューニング: `10/10`
- Vのみ境界外れ（近臨界予測として解釈）
- v53.1でBCC補正:
  `phi=0.42475`, Curie比RMSE `0.8053 -> 0.0140`

---

## v53.2-v53.3 解析閉包

v53.2:
- `chi_Delta` を Bloch全域厳密積分で評価。
- `chi ~ Delta^{-gamma_eff}` を数値で閉じた。

v53.3:
- `gamma_eff = gamma_pred + alpha_res` 分解を導入。
- `alpha_res` を明示的に切り出して定量化。

---

## v53.4-v53.7 残差の追跡

- v53.4:
  有限`q` coherenceだけでは `alpha_res` を説明できず。
- v53.5:
  単一form-factor `W_p` で不足。
- v53.6-v53.7:
  2作用素混合でも改善は小さい（RMSE `0.138 -> 0.1345`）。

結論:
- 高充填側残差は、より豊かな頂点/演算子構造が必要。

---

## 予測（現時点）

- 暗黒光子:
  `mA ~ 0.22 GeV`, `epsilon ~ 10^-11`
- 第4世代暗黒粒子:
  `m4 ~ 340-365 GeV`
- 暗黒強結合複合体（dark baryon様）
- 磁性:
  Vは近臨界応答が強い

---

## 反証可能性

- SHiPで暗黒光子帯を直接検証可能。
- HyperCP系は実データ閉包でGO/NO-GO判定。
- 磁性は高充填残差を外部データで切り分け可能。
- どこか1本でも系統的に崩れれば理論鎖は修正必須。

---

## v50最終判定

`STRONGLY_CONSTRAINED_WORKING_THEORY`

- 単なる思いつきではなく、拘束された鎖として成立。
- ただし完成理論ではない。
- 価値は「離散化原理 + 予測 + 反証可能性」を同時に持つ点にある。

---

## 次の実装タスク（v50完結版）

1. 多演算子 `q=0` 頂点モデルで `alpha_res` を再現。
2. 可視->全系の Kimura-Thevenin 射影を固定版として凍結。
3. SHiP/天文制約を同一尤度で再統合。
4. v50を基準版として v60 系へ移行。

追記
# LoNalogy Cross-Domain Analogy Memo

Date: 2026-03-03  
Scope: Applying LoNalogy to fields other than particle physics / cosmology (e.g., ecology, neuroscience, social dynamics, finance, materials).

## 1) Principle

Use LoNalogy as a **state-transition geometry** first, not as a direct causal claim.

- Safe claim: "This domain can be represented in the same dynamical form."
- Unsafe claim (without extra evidence): "This domain is physically caused by X from another domain."

## 2) What To Keep Fixed vs Free

### Keep fixed (structural invariants)

- Core state form (`amplitude + phase` style representation).
- Minimal conservation/homeostasis term.
- Same objective decomposition pattern:
  - visible fit term
  - structural projection term
  - regularization term

These are the "grammar" of LoNalogy. If these change, the experiment is no longer comparable.

### Keep free (domain adaptation knobs)

- Observation map (what is "visible channel" in the new field).
- Coupling matrix and coupling gain parameters.
- Damping/saturation parameters (`gamma`, `alpha` analogs).
- Intervention operators (domain-specific actions).
- Prior weights (must be explicitly controllable).
- Initialization of latent/dark-like parameters.

Rule: if a parameter is not directly measured in the new domain, it must be tested under multiple initializations.

## 3) Minimum Ablation Protocol (Required)

For each cross-domain claim, run all 3:

1. **Anchored run**  
   With priors/anchors enabled.
2. **No-prior run**  
   Prior weights set to zero.
3. **No-prior + different init run**  
   Same as #2, but latent parameters initialized far from anchors.

Interpretation:

- If #2 and #3 converge to different latent values with similar fit: latent is **not identifiable**.
- Then only claim "mathematical compatibility," not "independent physical inference."

## 4) Claim Levels (Use in reports)

- Level A: Representation works (fit quality acceptable).
- Level B: Intervention ranking is stable across cohorts/initializations.
- Level C: Latent parameters are identifiable without priors.
- Level D: External causal validation (prospective or mechanistic) confirms prediction.

Do not skip levels in wording.

## 5) Recommended Defaults For New Domains

- Start with weak priors, not hard priors.
- Expose CLI flags for all prior weights and latent initialization mode.
- Include toxicity/cost penalty when modeling interventions.
- Report:
  - fit error
  - intervention gain
  - responder rate
  - initialization sensitivity

## 6) Overclaim Guardrails

Never write:

- "Data from domain A determines fundamental parameters of domain B"
  unless no-prior identifiability is demonstrated and externally validated.

Prefer:

- "A shared LoNalogy dynamical form provides a consistent joint description."
- "Intervention geometry appears transferable, pending causal validation."

## 7) Practical Template (Copy)

Use this in new project notes:

```text
Model form preserved: [yes/no]
Observation map adapted: [description]
Priors used: [weights]
No-prior ablation run: [yes/no]
Init sensitivity checked: [yes/no]
Stable intervention ranking: [yes/no]
Latent identifiability: [yes/no]
Allowed claim level: [A/B/C/D]
```
