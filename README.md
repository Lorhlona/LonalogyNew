# LoNalogy

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19115338.svg)](https://doi.org/10.5281/zenodo.19115338)

**A Constructive Framework for Yang–Mills and Unified Physics from Elliptic Modular Geometry**

---

## Overview

LoNalogy is a theoretical physics framework that derives the structure of the Standard Model and addresses the Yang–Mills mass gap problem from a single algebraic starting point: the para-complex unit $\jmath^2 = +1$.

The theory decomposes the full physical system into three sectors:

$$\mathfrak{U} = \mathfrak{I} \oplus \mathfrak{V} \oplus \mathfrak{B}$$

| Sector | Name | Content |
|--------|------|---------|
| $\mathfrak{I}$ | **Idea** | $X(2)$ geometry, strict kernel, determinant line — hidden structure supporting visible law |
| $\mathfrak{V}$ | **Visible** | Yang–Mills gauge fields, matter, Higgs — what detectors read |
| $\mathfrak{B}$ | **Bridge** | Portal, baryonic bridge, Schur reduction — coupling between sectors |

The observed physics is the **Schur complement** (reduced law) of the full system, formalized through the **Kimura–Thévenin principle**.

## Main Papers

### Yang–Mills Existence and Mass Gap (v3)

**"Yang–Mills Existence and Mass Gap: A Constructive Proof via Elliptic Modular Geometry and Transfer-Poincaré Descent"**

Four-stage proof: Modular Geometry → Three-Sector Structure → Gluing → Transfer-Poincaré Descent. For every compact simple gauge group $G$, constructs a non-trivial quantum Yang–Mills theory on $\mathbb{R}^4$ with mass gap $\Delta > 0$.

### Standard Model Structure, GUT Scale, and Dark Sector (v3)

**"Standard Model Structure, GUT Scale, and Dark Sector from Elliptic Modular Geometry: Predictions of LoNalogy"**

Derives SM gauge group, three generations, GUT scale via the determinant master law $M_X = M_C R_{\rm trip}^{2/9} = 3.4638 \times 10^{15}$ GeV, proton lifetime $\tau_p/\tau_p^{\rm HK} = 1.1649$, cosmological constant, and dark sector predictions — all from $\nu_{\rm br} = 12$ and $d = 4$.

### A Cubic Equation for the Cosmological Constant

**GRF 2026 essay: "A Cubic Equation for the Cosmological Constant from Modular Geometry"**

The strict kernel equation $12(1-k)^2(1+k)=2$ determines nome $Q_{\rm ker} \approx 1.568 \times 10^{-3}$. The cosmological constant emerges as the smallest root of a cubic: $\Lambda_{\rm eff} = \Lambda_*^4 Q_{\rm ker}^{20} \approx 2.9 \times 10^{-47}$ GeV$^4$ — 18% agreement with observation, zero free parameters.

## Key Results

| Result | Statement |
|--------|-----------|
| **Gauge group** | $SU(5) \to SU(3)_C \times SU(2)_L \times U(1)_Y$ forced by Yukawa closure + anomaly cancellation |
| **Families** | $N_{\rm fam}^{\rm vis} = 3$ (cusps of $\bar{X}(2)$), $N_{\rm fam}^{\rm full} = 4$ (+ self-dual point) |
| **Mass gap** | Schwarzian wall $\mathcal{V}_S''(u) \geq 7$ confines states; spectral gap $> 0$ |
| **GUT scale** | $M_X = M_C R_{\rm trip}^{2/9} = \Lambda_* Q^{-14/3}\Xi_0^{2/3} = 3.4638 \times 10^{15}$ GeV (determinant master law) |
| **Proton decay** | $\tau_p/\tau_p^{\rm HK} = 1.1649$ |
| **Higgs vev** | $\Lambda_* = 246$ GeV geometrically fixed |
| **Cosmological constant** | $\Lambda_{\rm eff} = \Lambda_*^4 Q_{\rm ker}^{20} \approx 2.9 \times 10^{-47}$ GeV$^4$ (obs: $2.5 \times 10^{-47}$), 18% agreement with no free parameters |
| **Nome** | $Q_{\rm ker} = 1.568 \times 10^{-3}$, determined by strict kernel equation $12(1-k)^2(1+k)=2$ |
| **Suppression exponent** | $n = d \times N = 4 \times 5 = 20$ ($n_{\rm exact} = 20.025$) |
| **Fourth generation** | Confined to the Idea sector; visible only through dark matter and neutrino anomalies |

## Key Numerical Results

All claims verified: **50/50 PASS** ([`verify_numerics.py`](verify_numerics.py), [`verification_results.md`](verification_results.md))

| Quantity | Value |
|---|---|
| $k_{\rm ker}(12)$ | $0.685548$ |
| $Q_{\rm ker} = e^{-2\pi K'/K}$ | $1.568 \times 10^{-3}$ |
| $j(\tau_{\rm ker})$ | $1746.8$ ($j - 1728 = 18.8$) |
| $M_C = \Lambda_* Q^{-4}$ | $4.07 \times 10^{13}$ GeV |
| $\Xi_0(\tau_{\rm ker})$ | $1.22965$ |
| $M_X = \Lambda_* Q^{-14/3}\Xi_0^{2/3}$ | $3.4638 \times 10^{15}$ GeV |
| $\tau_p/\tau_p^{\rm HK}$ | $1.1649$ |
| $\Lambda_{\rm eff} = \Lambda_*^4 Q^{20}$ | $2.9 \times 10^{-47}$ GeV$^4$ |
| pred/obs | $1.178$ (18% match, zero free parameters) |
| $n_{\rm exact}$ | $20.025 \approx 20 = 4 \times 5$ |
| $w_{\rm DE} + 1$ | $\sim 2.5 \times 10^{-6}$ |

## Files

| File | Description |
|------|-------------|
| `YM_mass_gap_v3.tex` | Yang–Mills existence and mass gap — full proof (v3, English) |
| `YM_mass_gap_v3.pdf` | Compiled PDF |
| `YM_mass_gap_ja.tex` | Yang–Mills existence and mass gap — full proof (v3, Japanese) |
| `YM_mass_gap_ja..pdf` | Compiled PDF |
| `particle_cosmology_v3.tex` | SM structure, GUT scale, dark sector — predictions (v3) |
| `particle_cosmology_v3.pdf` | Compiled PDF |
| `GRF2026_Nakamura.tex` | GRF 2026 essay — cubic equation for the cosmological constant |
| `GRF2026_Nakamura.pdf` | Compiled PDF |
| `verify_numerics.py` | Numerical verification script (numpy/scipy) — 50/50 PASS |
| `verification_results.md` | Detailed verification results with classification table |
| `archive/` | Previous versions (v77–v89) and development history |

## Author

**Lorhlona**

## License

This work is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
