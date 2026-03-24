#!/usr/bin/env python3
"""
Numerical experiments for 89utyu.md predictions.
Covers: freeze-out, M_X prefactor, proton lifetime, detection cross section,
        halo core profile, and dark energy equation of state.

All from the two-document basis (YM_mass_gap.tex + v77.md).
"""

import numpy as np
from scipy.special import ellipk
from scipy.optimize import brentq
from scipy.integrate import solve_ivp, quad

# ================================================================
#  0. Strict kernel data (from verify_numerics.py)
# ================================================================
LAMBDA_STAR = 246.0          # GeV
nu_br = 12
k_ker = 0.685548
m_ker = k_ker**2
Q_ker = np.exp(-2*np.pi * ellipk(1-m_ker) / ellipk(m_ker))
x_ker = 2*m_ker - 1
M_C = LAMBDA_STAR * Q_ker**(-4)
kp_ker = np.sqrt(1 - m_ker)

# Physical constants
M_Pl = 1.22e19              # Planck mass [GeV]
M_Pl_red = M_Pl / np.sqrt(8*np.pi)  # reduced Planck mass
m_proton = 0.9383           # proton mass [GeV]
G_F = 1.1664e-5             # Fermi constant [GeV^-2]
alpha_em = 1/127.9           # at M_Z
sin2_thetaW = 0.2312
hbar_c2 = 0.3894e-27        # hbar*c^2 in GeV^2 cm^2
sec_per_year = 3.156e7

print("=" * 70)
print("STRICT KERNEL DATA")
print("=" * 70)
print(f"  k_ker     = {k_ker:.6f}")
print(f"  Q_ker     = {Q_ker:.6e}")
print(f"  x_ker     = {x_ker:.5f}")
print(f"  M_C       = {M_C:.3e} GeV")
print(f"  k'_ker    = {kp_ker:.6f}")

# ================================================================
#  1. GUT COUPLING RUNNING AND M_X  (Priority #2 from 89utyu.md)
# ================================================================
print()
print("=" * 70)
print("1. GUT COUPLING RUNNING AND M_X")
print("=" * 70)

# One-loop RG running of SM gauge couplings (SU(5) normalization)
# alpha_i^{-1}(mu) = alpha_i^{-1}(M_Z) - b_i/(2pi) * ln(mu/M_Z)
# b_1 = 41/10, b_2 = -19/6, b_3 = -7  (SM with 3 generations)
# SU(5) normalization: alpha_1^{SU(5)} = (5/3) alpha_Y

M_Z = 91.1876  # GeV
alpha_1_MZ = (5/3) * alpha_em / (1 - sin2_thetaW)  # SU(5) normalized
alpha_2_MZ = alpha_em / sin2_thetaW
alpha_3_MZ = 0.1179  # strong coupling at M_Z

b1 = 41/10
b2 = -19/6
b3 = -7

def alpha_inv(alpha_MZ, b, mu):
    return 1/alpha_MZ - b/(2*np.pi) * np.log(mu/M_Z)

# Find unification scale where alpha_1 = alpha_2
def unif_eq_12(log_mu):
    mu = np.exp(log_mu)
    return alpha_inv(alpha_1_MZ, b1, mu) - alpha_inv(alpha_2_MZ, b2, mu)

log_M_GUT_12 = brentq(unif_eq_12, np.log(1e10), np.log(1e20))
M_GUT_12 = np.exp(log_M_GUT_12)

alpha_GUT_12 = 1 / alpha_inv(alpha_1_MZ, b1, M_GUT_12)
alpha_3_at_GUT = 1 / alpha_inv(alpha_3_MZ, b3, M_GUT_12)

print(f"  One-loop SM running:")
print(f"  alpha_1^-1(M_Z) = {1/alpha_1_MZ:.3f}")
print(f"  alpha_2^-1(M_Z) = {1/alpha_2_MZ:.3f}")
print(f"  alpha_3^-1(M_Z) = {1/alpha_3_MZ:.3f}")
print(f"  M_GUT (alpha_1=alpha_2) = {M_GUT_12:.3e} GeV")
print(f"  alpha_GUT (at M_GUT)    = {alpha_GUT_12:.5f}")
print(f"  alpha_3 at M_GUT        = {alpha_3_at_GUT:.5f}")
print(f"  alpha_GUT / alpha_3     = {alpha_GUT_12/alpha_3_at_GUT:.3f}")

# M_X from strict kernel
# M_X = sqrt(5/3) * M_C * (g_5 / sqrt(4 pi alpha_5))
# With alpha_5 = alpha_GUT: g_5 = sqrt(4 pi alpha_GUT)
# So g_5 / sqrt(4 pi alpha_5) = 1 (trivially!)
# Therefore M_X = sqrt(5/3) * M_C
M_X_minimal = np.sqrt(5/3) * M_C
print(f"\n  M_X = sqrt(5/3) * M_C = {M_X_minimal:.3e} GeV")
print(f"  (Paper claims M_X = 3.464e15 GeV)")

# If we use the GUT scale from running:
# X boson mass in SU(5) = M_GUT itself
M_X_running = M_GUT_12
print(f"  M_X from one-loop running = {M_X_running:.3e} GeV")

# The ratio
print(f"\n  M_X(running) / M_X(sqrt(5/3)*M_C) = {M_X_running/M_X_minimal:.2f}")
print(f"  This factor (~{M_X_running/M_X_minimal:.0f}x) is what's missing")
print(f"  from the two-document basis to close M_X = 3.46e15.")

# ================================================================
#  2. PROTON LIFETIME  (Priority #3 from 89utyu.md)
# ================================================================
print()
print("=" * 70)
print("2. PROTON LIFETIME  p -> e+ pi0")
print("=" * 70)

# Standard SU(5) dimension-6 proton decay: p -> e+ pi0
# Gamma = (alpha_GUT^2 * m_p^5) / (4 * M_X^4) * |A_L|^2 * |<pi0|(ud)_R u_L|p>|^2
#
# Lattice hadronic matrix element (FLAG 2024):
# alpha_N = <pi0|(ud)_R u_L|p> ~ 0.0090(9) GeV^3 (direct lattice, RQCD 2022)
# or W_0 = alpha_N * (1 + D + F) / f_pi with short-distance A_L ~ 2-3

# Use standard formula:
# tau_p = (4 * M_X^4) / (alpha_GUT^2 * m_p * alpha_H^2)
# where alpha_H = lattice hadronic matrix element ~ 0.012 GeV^3

alpha_H = 0.012  # GeV^3 (lattice, approximate)

# Enhancement factor from short-distance running
A_L = 2.5  # renormalization factor (running from M_GUT to 1 GeV)

def proton_lifetime(M_X, alpha_GUT, A_L=2.5, alpha_H=0.012):
    """Proton partial lifetime for p -> e+ pi0 in years."""
    # Gamma = alpha_GUT^2 * m_p / (4 pi) * (A_L * alpha_H)^2 / M_X^4
    # with phase space factor ~ m_p^4/(8 pi f_pi^2) absorbed into alpha_H
    Gamma = (alpha_GUT**2 * m_proton**5) / (4 * np.pi * M_X**4) * (A_L * alpha_H)**2 * (np.pi/4)
    # Convert to seconds: tau = hbar / Gamma, hbar = 6.582e-25 GeV*s
    hbar = 6.582e-25  # GeV*s
    tau_sec = hbar / Gamma
    tau_yr = tau_sec / sec_per_year
    return tau_yr

# With M_X from running
tau_running = proton_lifetime(M_X_running, alpha_GUT_12)
print(f"  Using M_X = M_GUT(running) = {M_X_running:.3e} GeV:")
print(f"  tau_p(p->e+pi0) = {tau_running:.2e} years")

# With M_X from paper's claim
M_X_paper = 3.464e15
tau_paper = proton_lifetime(M_X_paper, alpha_GUT_12)
print(f"\n  Using M_X = 3.464e15 GeV (paper):")
print(f"  tau_p(p->e+pi0) = {tau_paper:.2e} years")

# Current bound
tau_SK = 2.4e34  # Super-K bound [years]
print(f"\n  Super-K bound:  tau > {tau_SK:.1e} years")
print(f"  Hyper-K target: tau ~ 1e35 years")
print(f"  tau(running)/tau_SK = {tau_running/tau_SK:.1f}")
print(f"  tau(paper)/tau_SK   = {tau_paper/tau_SK:.1f}")

# ================================================================
#  3. HIDDEN SECTOR MASS WINDOW  (Proposition 2.1)
# ================================================================
print()
print("=" * 70)
print("3. HIDDEN SECTOR MASS WINDOW")
print("=" * 70)

def M_H(x):
    """Hidden mass scale: M_H(x) = Lambda_* * sqrt(2/(1-x))."""
    return LAMBDA_STAR * np.sqrt(2 / (1 - x))

# kappa_j envelope
def kappa_j(x, kappa0=1.0):
    """Hidden coupling envelope: kappa_j(x) = kappa0 * (1-x^2)."""
    return kappa0 * (1 - x**2)

# At coupling maximum (x=0)
m_j_max = M_H(0)
print(f"  M_H(x=0) = Lambda_* * sqrt(2) = {m_j_max:.1f} GeV")

# At strict kernel
m_j_ker = M_H(x_ker)
print(f"  M_H(x_ker={x_ker:.5f}) = {m_j_ker:.1f} GeV")
print(f"  kappa_j(x_ker) = {kappa_j(x_ker):.6f}")
print(f"  kappa_j(0)     = {kappa_j(0):.6f}")
print(f"\n  Detection mass window: {m_j_ker:.0f} -- {m_j_max:.0f} GeV (for xi_f=1)")

# ================================================================
#  4. FREEZE-OUT AND RELIC DENSITY  (Priority #1 from 89utyu.md)
# ================================================================
print()
print("=" * 70)
print("4. FREEZE-OUT CALCULATION: chi_j chi_j -> A'A'")
print("=" * 70)

# For m_j >> M_A (light mediator limit):
# <sigma v> = g_j^4 kappa_j^4 / (16 pi m_j^2)  [s-wave]
# Standard freeze-out: Omega h^2 ~ 0.12 * (3e-26 cm^3/s) / <sigma v>

m_j = 338.0  # GeV (benchmark)

def sigma_v_ann(g_j_kappa, m_j):
    """Annihilation cross section * velocity [cm^3/s]."""
    # Natural units: sigma*v = g^4/(16 pi m^2) in GeV^-2
    # Convert: 1 GeV^-2 = 0.3894e-27 cm^2, and v ~ c
    sigma_v_nat = g_j_kappa**4 / (16 * np.pi * m_j**2)  # GeV^-2
    # Convert to cm^3/s: multiply by (hbar*c)^2 * c
    # = 0.3894e-27 cm^2 * 3e10 cm/s = 1.168e-17 cm^3/s per GeV^-2
    conv = hbar_c2 * 3e10  # cm^3/s per GeV^-2
    return sigma_v_nat * conv

def omega_h2(sigma_v):
    """Approximate relic density from standard freeze-out."""
    # Omega h^2 ~ 3e-26 / <sigma v> * 0.12
    return 0.12 * 3e-26 / sigma_v

# Scan g_j*kappa_j to find the value giving Omega h^2 = 0.12
g_j_kappa_values = np.linspace(0.1, 1.0, 100)
omega_values = []
for g in g_j_kappa_values:
    sv = sigma_v_ann(g, m_j)
    omega_values.append(omega_h2(sv))
omega_values = np.array(omega_values)

# Find the crossing
g_j_kappa_target = brentq(
    lambda g: omega_h2(sigma_v_ann(g, m_j)) - 0.12,
    0.1, 2.0
)

sv_target = sigma_v_ann(g_j_kappa_target, m_j)
print(f"  Benchmark: m_j = {m_j} GeV")
print(f"  Annihilation: chi_j chi_j -> A'A' (light mediator)")
print()
print(f"  For Omega_chi h^2 = 0.120:")
print(f"    g_j*kappa_j = {g_j_kappa_target:.4f}")
print(f"    <sigma v>   = {sv_target:.3e} cm^3/s")
print(f"    (canonical thermal relic: 3e-26 cm^3/s)")
print()

# Check with paper's benchmark g_j*kappa_j = 0.35
g_bench = 0.35
sv_bench = sigma_v_ann(g_bench, m_j)
omega_bench = omega_h2(sv_bench)
print(f"  Paper benchmark g_j*kappa_j = 0.35:")
print(f"    <sigma v>     = {sv_bench:.3e} cm^3/s")
print(f"    Omega_chi h^2 = {omega_bench:.4f}")
print(f"    Omega_chi h^2 / 0.120 = {omega_bench/0.120:.2f}")

# More precise: solve Boltzmann equation numerically
# Y' = -<sigma v> s / H * (Y^2 - Y_eq^2)
# with Y = n/s, s = entropy density

g_star = 86.25  # relativistic dof at T ~ 10-30 GeV (SM without top)
g_star_s = g_star

def Y_eq(T, m, g_chi=2):
    """Equilibrium yield Y_eq = n_eq/s."""
    x = m / T
    if x > 50:
        return 0.0
    n_eq = g_chi * (m * T / (2 * np.pi))**1.5 * np.exp(-x)
    s = 2 * np.pi**2 / 45 * g_star_s * T**3
    return n_eq / s

def boltzmann_rhs(x, Y, m_chi, sigma_v_0):
    """dY/dx for freeze-out, x = m/T."""
    T = m_chi / x
    s = 2 * np.pi**2 / 45 * g_star_s * T**3
    H = np.sqrt(np.pi**2 * g_star / 90) * T**2 / M_Pl_red
    Yeq = Y_eq(T, m_chi)
    # sigma_v in GeV^-2
    sigma_v_GeV2 = sigma_v_0  # already in GeV^-2
    dYdx = -sigma_v_GeV2 * s / (H * x) * (Y**2 - Yeq**2)
    return dYdx

def compute_relic(m_chi, g_j_k):
    """Compute relic density Omega h^2 from Boltzmann equation."""
    sigma_v_GeV2 = g_j_k**4 / (16 * np.pi * m_chi**2)

    x_start = 1.0  # T = m_chi (very early)
    x_end = 1000.0  # T = m_chi/1000 (long after freeze-out)
    Y0 = Y_eq(m_chi / x_start, m_chi)

    sol = solve_ivp(boltzmann_rhs, [x_start, x_end], [Y0],
                    args=(m_chi, sigma_v_GeV2),
                    method='RK45', rtol=1e-8, atol=1e-15,
                    max_step=1.0)

    Y_inf = sol.y[0, -1]

    # Omega h^2 = m * s_0 * Y_inf / rho_crit
    # s_0 = 2891.2 cm^-3 (current entropy density)
    # rho_crit / h^2 = 1.054e-5 GeV/cm^3
    s_0 = 2891.2  # cm^-3
    rho_crit_h2 = 1.054e-5  # GeV/cm^3
    Oh2 = m_chi * s_0 * Y_inf / rho_crit_h2

    return Oh2, Y_inf

print()
print("  --- Boltzmann equation (numerical) ---")
Oh2_num, Y_inf = compute_relic(m_j, g_j_kappa_target)
print(f"  g_j*kappa_j = {g_j_kappa_target:.4f}, m_j = {m_j} GeV:")
print(f"    Y_inf       = {Y_inf:.4e}")
print(f"    Omega h^2   = {Oh2_num:.4f}")

Oh2_bench, Y_bench = compute_relic(m_j, g_bench)
print(f"  g_j*kappa_j = 0.35, m_j = {m_j} GeV:")
print(f"    Y_inf       = {Y_bench:.4e}")
print(f"    Omega h^2   = {Oh2_bench:.4f}")

# Scan to find exact coupling for Omega h^2 = 0.12
g_exact = brentq(lambda g: compute_relic(m_j, g)[0] - 0.12, 0.1, 2.0)
Oh2_check, _ = compute_relic(m_j, g_exact)
print(f"\n  Exact: g_j*kappa_j = {g_exact:.4f} gives Omega h^2 = {Oh2_check:.4f}")


# ================================================================
#  5. DIRECT DETECTION CROSS SECTION  (Proposition 2.3)
# ================================================================
print()
print("=" * 70)
print("5. DIRECT DETECTION CROSS SECTION")
print("=" * 70)

# sigma_p^SI = (mu_p^2 / pi) * (e * g_j * eps_kin * kappa_j / M_A^2)^2
# at q^2 << M_A^2

# v77 dictionary values
M_A_v77 = 0.2044      # GeV (dark photon mass)
S_max = 0.967900       # spectral function max
g_Y = np.sqrt(4*np.pi * alpha_em / (1 - sin2_thetaW))  # U(1)_Y coupling ~ 0.357

# eps_kin = g_Y * g_D / (16 pi^2) * S_max * eta_split
def sigma_SI(g_j, g_D, eta_split, kappa, M_A, m_chi):
    """SI cross section on proton [cm^2]."""
    e = np.sqrt(4*np.pi/137.036)
    eps_kin = g_Y * g_D / (16 * np.pi**2) * S_max * eta_split
    mu_p = m_proton * m_chi / (m_proton + m_chi)  # reduced mass
    # sigma = mu_p^2 / pi * (e * g_j * eps_kin * kappa / M_A^2)^2
    sigma_GeV2 = mu_p**2 / np.pi * (e * g_j * eps_kin * kappa / M_A**2)**2
    return sigma_GeV2 * hbar_c2  # convert to cm^2

# Benchmark: g_j = g_D = 1, eta_split = 1e-8
kj = kappa_j(x_ker)
sig = sigma_SI(1.0, 1.0, 1e-8, kj, M_A_v77, m_j)
print(f"  Benchmark parameters:")
print(f"    m_j = {m_j} GeV, M_A = {M_A_v77} GeV")
print(f"    kappa_j(x_ker) = {kj:.6f}")
print(f"    g_j = g_D = 1, eta_split = 1e-8")
print(f"    sigma_p^SI = {sig:.3e} cm^2")
print()

# Scan eta_split
for eta in [1e-7, 1e-8, 1e-9]:
    s = sigma_SI(1.0, 1.0, eta, kj, M_A_v77, m_j)
    print(f"    eta_split = {eta:.0e}: sigma = {s:.2e} cm^2")

print(f"\n  LZ bound at 338 GeV:  ~ 1e-47 cm^2")
print(f"  XENONnT at 338 GeV:  ~ 2e-47 cm^2")


# ================================================================
#  6. DARK ENERGY EQUATION OF STATE  (Theorem 3.2)
# ================================================================
print()
print("=" * 70)
print("6. DARK ENERGY EQUATION OF STATE")
print("=" * 70)

w_dev = Q_ker**2
Lambda_eff = LAMBDA_STAR**4 * Q_ker**20
rho_obs = 2.51e-47  # PDG 2025 [GeV^4]

print(f"  Lambda_eff = Lambda*^4 Q^20 = {Lambda_eff:.3e} GeV^4")
print(f"  rho_obs (PDG 2025) = {rho_obs:.2e} GeV^4")
print(f"  Lambda_eff / rho_obs = {Lambda_eff/rho_obs:.3f}")
print(f"  w_DE + 1 ~ Q^2 = {w_dev:.3e}")
print(f"  Fractional drift per Hubble: 3 Q^2 = {3*w_dev:.3e}")
print(f"  PDG 2025: w = -1.028(31)")
print(f"  LoNalogy deviation {w_dev:.1e} is {0.031/w_dev:.0e}x below PDG uncertainty")


# ================================================================
#  7. HALO CORE PROFILE  (Proposition 2.6)
# ================================================================
print()
print("=" * 70)
print("7. HALO CORE PROFILE FROM kappa_j = kappa_0 sech^2(r/r_c)")
print("=" * 70)

# Show that kappa_j(r) = kappa_0 sech^2(r/r_c) gives cored profile
# Reduced Poisson-Jeans: rho(r) with kappa_j as coupling

r_c = 1.0  # in units of core radius
r = np.linspace(0, 5*r_c, 1000)

kappa_profile = 1.0 / np.cosh(r/r_c)**2
print(f"  kappa_j(0) = {kappa_profile[0]:.4f} (maximum)")
print(f"  kappa_j(r_c) = {1/np.cosh(1)**2:.4f}")
print(f"  kappa_j(2r_c) = {1/np.cosh(2)**2:.6f}")
print(f"  kappa_j(3r_c) = {1/np.cosh(3)**2:.8f}")
print()

# Taylor expansion at r=0
print(f"  Taylor: kappa_j(r) = kappa_0 [1 - (r/r_c)^2 + (2/3)(r/r_c)^4 - ...]")
print(f"  => rho(r) = rho_0 + rho_2 r^2 + O(r^4)")
print(f"  => rho'(0) = 0  (NO cusp)")
print(f"  => v_c(r) ~ r near center (solid-body rotation)")
print()

# Isothermal Jeans equation with position-dependent coupling:
# d/dr [r^2 / rho * d(rho sigma^2) / dr] = -4piG rho r^2 * kappa_j(r)
# For self-gravitating halo with kappa_j modulation

# Simplified: solve d^2 phi/dr^2 + (2/r) dphi/dr = 4piG rho_0 kappa_j(r)
# with rho = rho_0 exp(-phi/sigma^2) (isothermal)

# Non-dimensionalize: xi = r/r_c, psi = phi/sigma^2
# psi'' + 2/xi * psi' = (r_c^2 * 4piG rho_0 / sigma^2) * sech^2(xi) * exp(-psi)

# Just show the density profile shape
def jeans_rhs(xi, y):
    """y = [psi, psi'], non-dim Jeans equation with sech^2 coupling."""
    psi, dpsi = y
    if xi < 1e-10:
        return [dpsi, 0]
    kj = 1.0 / np.cosh(xi)**2
    ddpsi = kj * np.exp(-psi) - 2/xi * dpsi
    return [dpsi, ddpsi]

sol = solve_ivp(jeans_rhs, [1e-4, 5.0], [0.0, 0.0],
                max_step=0.01, rtol=1e-10)

rho_profile = np.exp(-sol.y[0])
r_profile = sol.t

print(f"  Jeans equation density profile (normalized):")
for frac in [0.0, 0.5, 1.0, 2.0, 3.0, 5.0]:
    idx = np.argmin(np.abs(r_profile - frac))
    if idx < len(rho_profile):
        print(f"    rho(r={frac:.1f} r_c) / rho_0 = {rho_profile[idx]:.4f}")

# Core slope (log-log)
mask = (r_profile > 0.5) & (r_profile < 1.5)
if np.sum(mask) > 2:
    log_r = np.log(r_profile[mask])
    log_rho = np.log(rho_profile[mask])
    slope = np.polyfit(log_r, log_rho, 1)[0]
    print(f"\n  Inner log-slope d(ln rho)/d(ln r) at r~r_c: {slope:.3f}")
    print(f"  (NFW would give -1, our model gives shallower)")


# ================================================================
#  SUMMARY
# ================================================================
print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"""
  1. M_X:
     sqrt(5/3)*M_C = {M_X_minimal:.3e} GeV  (two-doc, no running)
     One-loop SM running: M_GUT = {M_X_running:.3e} GeV
     Paper claim: 3.464e15 GeV (requires threshold corrections)

  2. Proton lifetime (p -> e+ pi0):
     tau(M_GUT running) = {tau_running:.2e} yr  (vs Super-K > 2.4e34 yr)
     tau(paper M_X)      = {tau_paper:.2e} yr

  3. Hidden mass window:
     m_j = {m_j_ker:.0f} -- {m_j_max:.0f} GeV (xi_f=1)

  4. Freeze-out:
     g_j*kappa_j = {g_exact:.4f} gives Omega h^2 = 0.120
     (paper benchmark 0.35 gives Omega h^2 = {Oh2_bench:.3f})

  5. Direct detection:
     sigma_SI ~ {sigma_SI(1,1,1e-8,kj,M_A_v77,m_j):.1e} cm^2
     (g_j=g_D=1, eta=1e-8; LZ limit ~ 1e-47)

  6. Dark energy:
     Lambda_eff/rho_obs = {Lambda_eff/rho_obs:.3f}
     w+1 ~ Q^2 = {w_dev:.2e} (undetectable with current surveys)

  7. Halo profile:
     kappa_j = sech^2(r/r_c) => cored density, no cusp
""")
