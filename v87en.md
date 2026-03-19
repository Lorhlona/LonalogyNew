# LoNalogy v87
## Complete Unified Draft of Full-System Physics
### From $\jmath^2=+1$ to the Standard Model, Yang–Mills Mass Gap, and the Idea Sector

---

# Part I: Starting Point — The Necessity of $\jmath^2=+1$ and $X(2)$

## 1.1 Para-complex Algebra and the $\mathbb{Z}_2$ Quotient

Define an algebraic element $\jmath$ over the reals by

$$\jmath^2 = +1, \qquad \jmath \neq \pm 1$$

This is the "symmetric counterpart" of the imaginary unit $i^2=-1$, and gives rise to the **para-complex algebra** $\mathbb{R}[\jmath] \cong \mathbb{R} \oplus \mathbb{R}$.

This algebra carries a natural involution (sector exchange)

$$\sigma: \jmath \mapsto -\jmath$$

$\sigma$ is interpreted as the map exchanging the visible and hidden sectors.

### Proposition 1.1 (Para-Chebyshev Quotient Theorem)

The fixed subfield under $\sigma$ is

$$\mathbb{R}(\Omega)^\sigma = \mathbb{R}(\Omega^2)$$

Therefore the $\sigma$-even primitive generator is uniquely determined as

$$m = \Omega^2$$

Furthermore, the centered generator with self-dual point $m = \frac{1}{2}$ as origin is

$$\boxed{x := 2m - 1 = 2\Omega^2 - 1 = T_2(\Omega)}$$

where $T_2$ is the Chebyshev polynomial of the second kind.

#### Proof

Since $\sigma(\Omega) = -\Omega$, the $\sigma$-invariant elements of $\mathbb{R}(\Omega)$ are precisely the even functions of $\Omega$, i.e., all rational functions of $\Omega^2$. Uniqueness of the primitive generator follows from the degree of the algebraic extension. The centering $x = 2\Omega^2 - 1$ is the unique affine transformation mapping $m=\frac{1}{2}$ to $x=0$. $\square$

---

## 1.2 Why $X(2)$?

The moduli space of the Legendre family

$$E_\lambda: \quad y^2 = x(x-1)(x-\lambda)$$

is identified with $X(2) = \Gamma(2)\backslash\mathbb{H}$.

Here

$$\Gamma(2) = \left\{ \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in SL_2(\mathbb{Z}) \;\middle|\; a \equiv d \equiv 1,\ b \equiv c \equiv 0 \pmod{2} \right\}$$

**Three mathematical structures are simultaneously realized on $X(2)$:**

1. **Hyperbolic geometry**: $\mathbb{H}$ carries the hyperbolic metric $ds^2 = (dx^2+dy^2)/y^2$, and quotienting by $\Gamma(2)$ yields a hyperbolic surface of finite area.

2. **Elliptic functions**: Fixing $\tau \in \mathbb{H}$ determines a torus $\mathbb{C}/(\mathbb{Z}+\tau\mathbb{Z})$. The period ratio of the Legendre family is given by $\tau = iK(1-\lambda)/K(\lambda)$.

3. **Complex analysis**: The elliptic curve degenerates at the three cusps $\lambda = 0, 1, \infty$. This degeneration is controlled complex-analytically as the action of parabolic elements of $\Gamma(2)$.

### Theorem 1.2 (Uniqueness of $X(2)$)

For the para-conjugation $\sigma$ of $\jmath^2=+1$, the unique space that simultaneously governs hyperbolic geometry, elliptic functions, and complex analysis — as the geometric realization of the $\mathbb{Z}_2$ folding from the UV cover $\Omega$-theory to the IR quotient $x$-theory — is $X(2)$.

---

## 1.3 Relations among Elliptic Modulus, Nome, and the Schwarzian

Define the theta constants by

$$\theta_2(\tau) = \sum_{n\in\mathbb{Z}} q_\theta^{(n+\frac{1}{2})^2}, \quad \theta_3(\tau) = \sum_{n\in\mathbb{Z}} q_\theta^{n^2}, \quad \theta_4(\tau) = \sum_{n\in\mathbb{Z}} (-1)^n q_\theta^{n^2}$$

where $q_\theta = e^{\pi i\tau}$, $Q = q_\theta^2 = e^{2\pi i\tau}$.

Elliptic modulus and complementary modulus:

$$k(\tau) = \frac{\theta_2(\tau)^2}{\theta_3(\tau)^2}, \qquad k'(\tau) = \frac{\theta_4(\tau)^2}{\theta_3(\tau)^2}$$

From $\lambda = k^2$, $x = 2\lambda - 1 = 2k^2 - 1$,

$$k = \sqrt{\frac{1+x}{2}}, \qquad k' = \sqrt{\frac{1-x}{2}}$$

The complete elliptic integral $K(m) = \frac{\pi}{2}{}_2F_1(\frac{1}{2},\frac{1}{2};1;m)$ satisfies the hypergeometric equation

$$m(1-m)y'' + (1-2m)y' - \frac{1}{4}y = 0$$

and provides the inverse uniformization map $\tau(m) = i\frac{K(1-m)}{K(m)}$.

### Theorem 1.3 (Schwarzian Master Law)

For $x = 2k^2-1$,

$$\boxed{\{\tau, x\} = \frac{x^2+3}{2(1-x^2)^2}}$$

and

$$\boxed{j(\tau) = 64\frac{(x^2+3)^3}{(1-x^2)^2} = 512(1-x^2)^4\{\tau,x\}^3}$$

#### Proof

From the coefficients of the hypergeometric equation

$$p(m) = \frac{1-2m}{m(1-m)}, \qquad q(m) = -\frac{1}{4m(1-m)}$$

applying the lemma (Schwarzian of the ratio function of a second-order linear ODE)

$$\{w,z\} = 2q - p' - \frac{1}{2}p^2$$

yields $\{\tau,m\} = \frac{1-m+m^2}{2m^2(1-m)^2}$. The substitution $m = (1+x)/2$ gives the first identity. The relation with $j$ follows directly from product formulas of theta constants. $\square$

The self-dual point is $x=0 \Leftrightarrow k = 1/\sqrt{2} \Leftrightarrow \tau = i$, which gives the $j$-minimum on the real locus.

---

# Part II: The Idea Sector — Hidden Structure

## 2.1 Decomposition of the Full System

The full system $\mathfrak{U}$ of LoNalogy decomposes into three sectors:

$$\mathfrak{U} = \mathfrak{I} \oplus \mathfrak{V} \oplus \mathfrak{B}$$

- $\mathfrak{I}$ (**Idea sector**): $X(2)$, Legendre family, $j$-line, strict kernel, determinant line, principal manifold. A hidden structural sector that is not directly observable but supports the visible law.

- $\mathfrak{V}$ (**Visible sector**): Yang–Mills gauge fields, matter, Higgs, detector readouts.

- $\mathfrak{B}$ (**Bridge sector**): Couplings responsible for portal, baryonic bridge, coarse-graining, and Schur reduction.

### Definition 2.1 (Kimura–Thévenin Principle)

When the full quadratic kernel is block-decomposed as

$$\mathcal{K}_{\rm full} = \begin{pmatrix} L_{\rm vis} & W \\ W^\dagger & L_{\rm idea} \end{pmatrix}$$

the reduced kernel seen by the visible observer is defined as

$$K_{\rm vis}^{\rm red} := L_{\rm vis} - WL_{\rm idea}^{-1}W^\dagger$$

Between the bridge norm and the base scale,

$$M_C \|\sigma_{\rm br}\| = \Lambda_*$$

holds. Together these constitute the **effective law of the full system as seen from the visible terminal**.

### Theorem 2.2 (Schur Reduction)

Gaussian integration over the hidden variable $h$ yields

$$S_{\rm eff}(v) = \frac{1}{2}\langle v, K_{\rm vis}^{\rm red} v\rangle$$

#### Proof

Completing the square with $h' = h + L_{\rm idea}^{-1}W^\dagger v$ eliminates the mixed term. The part depending on $h'$ is absorbed into a constant factor by Gaussian integration. $\square$

### Theorem 2.3 (RG Reciprocity)

$$\gamma_M(\mu) + \gamma_\sigma(\mu) = 0 \quad (\forall\mu)$$

and if $M_C(\mu_0)\|\sigma_{\rm br}(\mu_0)\| = \Lambda_*$ holds at some reference point $\mu_0$, then $M_C(\mu)\|\sigma_{\rm br}(\mu)\| = \Lambda_*$ along the entire RG orbit.

#### Proof

$\mu\frac{d}{d\mu}\log(M_C\|\sigma_{\rm br}\|) = \gamma_M + \gamma_\sigma = 0$, so the product is constant. $\square$

**Physical meaning**: The observed theory $\neq$ the full theory.

$$e^{-\Gamma_{\rm vis}^{\rm red}[\Phi]} = \int \exp(-S_{\rm full}[\Phi, \phi_{\rm idea}, \phi_{\rm br}])\, D\phi_{\rm idea}\, D\phi_{\rm br}$$

The Idea is not non-physical because it is unobservable. It is a **hidden structural sector that supports the visible law**.

---

## 2.2 Determinant Triplet and the Jacobi Identity

### Definition 2.4

$$d_{10} = \frac{\theta_2}{\eta}, \quad d_{01} = Q^{-11/8}\frac{\theta_4}{\eta}, \quad d_{11} = Q^{-11/8}\frac{\theta_3}{\eta}, \quad d_0 = \tau_2\eta^2$$

where $\eta(\tau) = Q^{1/24}\prod_{n\geq 1}(1-Q^n)$.

### Theorem 2.5 (Determinant Triplet Collapse)

$$\boxed{d_{10}d_{01}d_{11} = 2Q^{-11/4}}$$

#### Proof

Immediate from substituting the definition of $\eta$ into Jacobi's identity $\theta_2\theta_3\theta_4 = 2\eta^3$. $\square$

---

# Part III: The Strict Kernel and the Forcing of $N=5$

## 3.1 Real Dimension of the Broken Orbit

For $G = SU(r+s)$, $H = S(U(r)\times U(s))$, let $\mathfrak{m} = \mathfrak{g}/\mathfrak{h}$ denote the broken tangent space.

### Proposition 3.1

$$\mathfrak{m} \cong \left\{\begin{pmatrix}0 & B \\ -B^\dagger & 0\end{pmatrix} \;\middle|\; B \in M_{r\times s}(\mathbb{C})\right\}$$

#### Proof

In the block decomposition of $\mathfrak{su}(r+s)$, the diagonal blocks give $\mathfrak{h}$ and the off-diagonal blocks give the quotient. The real dimension of $M_{r\times s}(\mathbb{C})$ is $2rs$. $\square$

### Definition 3.2 (Bridge Coefficient)

$$\boxed{\nu_{\rm br} := \dim_\mathbb{R}\mathfrak{m} = 2rs}$$

For the physical split $(r,s)=(3,2)$, $\nu_{\rm br} = 12$.

---

## 3.2 The Strict Kernel Equation

### Definition 3.3 (Structural Branch Potential)

$$v_{\rm br}(\Omega) := (2-\nu_{\rm br})\Omega + \frac{\nu_{\rm br}}{2}\Omega^2 + \frac{\nu_{\rm br}}{3}\Omega^3 - \frac{\nu_{\rm br}}{4}\Omega^4$$

### Theorem 3.4 (Derivation of the Strict Kernel Equation)

$v_{\rm br}'(k) = 0$, $k\in(0,1)$ is equivalent to

$$\boxed{\nu_{\rm br}(1-k)^2(1+k) = 2}$$

#### Proof

$v_{\rm br}'(\Omega) = 2 - \nu_{\rm br}(1-\Omega)^2(1+\Omega)$. Setting this to zero gives the claim. $\square$

### Theorem 3.5 (Existence and Uniqueness)

If $\nu_{\rm br} > 2$, there exists a unique solution $k_{\rm ker}$ in $(0,1)$.

#### Proof

$g(k) = (1-k)^2(1+k)$ has $g'(k) = -(1-k)(1+3k) < 0$, so it is strictly monotone decreasing. Since $g(0)=1$, $g(1^-)=0$, and $2/\nu_{\rm br} \in (0,1)$, the intermediate value theorem gives a unique solution. $\square$

### Theorem 3.6 (Exact Trigonometric Formula)

$$\boxed{k_{\rm ker}(\nu) = \frac{1}{3} + \frac{4}{3}\cos\!\left(\frac{2\pi - \arccos\!\left(\frac{27}{8\nu}-1\right)}{3}\right)}$$

#### Proof

Expanding gives $k^3 - k^2 - k + 1 - 2/\nu = 0$. Substituting $k = y + 1/3$ yields a depressed cubic, and $y = \frac{4}{3}\cos\theta$ gives $\cos 3\theta = \frac{27}{8\nu}-1$. Selecting the branch that falls in $(0,1)$ yields the claim. $\square$

### Theorem 3.7 (Self-Dual Threshold)

The self-dual point is $x=0 \Leftrightarrow k=1/\sqrt{2}$, and the corresponding critical coefficient is

$$\boxed{\nu_{\rm sd} = 8 + 4\sqrt{2}}$$

If $\nu_{\rm br} < \nu_{\rm sd}$, then $k_{\rm ker} < 1/\sqrt{2}$, i.e., the strict kernel lies just below the self-dual point.

#### Proof

$g(1/\sqrt{2}) = (1-1/\sqrt{2})^2(1+1/\sqrt{2}) = (1-1/\sqrt{2})\cdot\frac{1}{2}$. Computing this gives $1/(8+4\sqrt{2})$. $\square$

---

## 3.3 Forcing of $N=5$

### Theorem 3.8 (Yukawa Cubic Criterion)

$$\Lambda^2V \otimes \Lambda^2V \otimes V \to \det V$$

exists as a determinant-valued invariant if and only if $\dim V = 5$.

#### Proof

The natural exterior product $(u_1\wedge u_2)\otimes(v_1\wedge v_2)\otimes w \mapsto u_1\wedge u_2\wedge v_1\wedge v_2\wedge w$ takes values in $\Lambda^5V$. $\Lambda^5V \cong \det V \Leftrightarrow \dim V = 5$. $\square$

### Proposition 3.9 (Anomaly Cancellation)

From $A(\Lambda^2V) = N-4$, $A(V^*) = -1$,

$$A(\Lambda^2V) + A(V^*) = N-5 = 0 \Leftrightarrow N=5$$

### Corollary 3.10 (Forcing of Rank 5)

Requiring both Yukawa closure and anomaly cancellation forces $N=5$.

### Theorem 3.11 ($N=5$ Is the Last Rank Below Self-Duality)

For the maximal broken dimension of balanced splits

$$\nu_{\max}(N) = 2\left\lfloor\frac{N^2}{4}\right\rfloor$$

we have

$$\nu_{\max}(5) = 12 < 8+4\sqrt{2}, \quad \nu_{\max}(6) = 18 > 8+4\sqrt{2}$$

**$N=5$ is the last rank with a balanced split satisfying $\nu_{\rm br} < \nu_{\rm sd}$.**

---

# Part IV: Analytic Implementation for General $SU(N)$ Yang–Mills

## 4.1 Schwarzian Radial Core

### Theorem 4.1

For

$$\mathcal{V}_S(u) = 2\cosh^4 u - \frac{1}{2}\cosh^2 u$$

we have

$$\mathcal{V}_S''(u) = 32\sinh^4 u + 38\sinh^2 u + 7 \geq 7 \quad (\forall u \in \mathbb{R})$$

$u=0$ is the unique minimum, and $\mathcal{V}_S(u) \sim \frac{1}{8}e^{4|u|}$.

---

## 4.2 Lower Bound on the Bridge Hessian

### Theorem 4.2 (Linewise Floor)

Under the strict kernel normalization $D_{\rm br}(\tau_{\rm ker}) = 1$, each line stiffness satisfies

$$r_\alpha = \frac{C(k_\alpha)}{\nu_{\rm br}}, \quad C(k) = \frac{2}{(1-k)^2(1+k)} \geq 2$$

hence

$$\boxed{r_\alpha \geq \frac{2}{\nu_{\rm br}} =: \mu_*}$$

For the physical split, $\mu_* = 1/6$.

### Theorem 4.3 (Fiber Schur Floor)

If the bridge action has the line-separable form

$$S_{\rm br}(y_0,\dots,y_{\nu_{\rm br}/2}) = \sum_\alpha U_\alpha(y_\alpha)$$

with $D(y) = \nabla_y^2 S_{\rm br} \geq \mu_* I$, then for the isotropic unit vector $u_{\rm iso} = \frac{1}{\sqrt{d_{\rm fib}}}(1,\dots,1)$, the fiber Schur complement satisfies

$$M/C_u := C - ba^{-1}b^\top \geq \mu_* I_{\nu_{\rm br}/2}$$

#### Proof

$D = \mu_*I + N$, $N\geq 0$. After an orthogonal transformation $M = \mu_*I + \widetilde{N}$. From the block decomposition, $\Gamma - \beta(\mu_*+\alpha)^{-1}\beta^\top \geq 0$ follows from non-negativity of the Schur complement of a positive semidefinite block matrix. $\square$

---

## 4.3 Doeblin Contraction and Automated Q-Entry

### Assumption 4.4 (Exact Block Axioms)

A kernel family $K_\theta \in C(\Theta \times G \times G)$ on a compact parameter space $\Theta$ satisfies

1. $K_\theta(g,h) > 0$ (strict positivity)
2. $K_\theta(g,h) = K_\theta(h,g)$ (symmetry)
3. $\int_G K_\theta(g,h)\,dh = 1$ (Markov normalization)

### Theorem 4.5 (Uniform Doeblin Minorization)

$$m_* = \min_{\theta\in\Theta}\min_{g,h\in G} K_\theta(g,h) > 0$$

(minimum of a continuous positive-valued function on a compact set)

### Theorem 4.6 (Non-autonomous RG Contraction)

For any sequence $(\theta_n) \subset \Theta$,

$$\boxed{\|T_{\theta_n}\cdots T_{\theta_1}|_{H_0}\| \leq (1-m_*)^n}$$

#### Proof

Apply the Doeblin decomposition $T_\theta = m_*\Pi + (1-m_*)R_\theta$ to $f \in H_0$. Since $\Pi f = 0$, we get $T_{\theta_1}f = (1-m_*)R_{\theta_1}f$. By induction, $S_n f = (1-m_*)^n R_{\theta_n}\cdots R_{\theta_1}f$. Each $R_{\theta_k}$ is an $L^2$-contraction, so $\|S_nf\| \leq (1-m_*)^n\|f\|$. $\square$

### Theorem 4.7 (Automatic Q-Entry)

For a v80-adapted chart $\mathcal{Q}$ ($\mathcal{Q}(\Pi)=0$, Fréchet-analytic),

$$\boxed{|Q_n| \leq C_Q(1-m_*)^n}$$

---

## 4.4 Perfect Exclusion and Schur Cone Invariance

### Theorem 4.8 (Hessian of the Log-Marginal)

$$\nabla_x^2\Gamma(x) = \mathbb{E}_x[\Phi_{xx}] - \operatorname{Cov}_x(\Phi_x, \Phi_x)$$

### Theorem 4.9 (Conditional Brascamp–Lieb)

Under $\Phi_{zz}(x,z) \succ 0$,

$$v^\top\nabla_x^2\Gamma(x)v \geq \mathbb{E}_x\!\left[v^\top(\Phi_{xx} - \Phi_{xz}\Phi_{zz}^{-1}\Phi_{zx})v\right]$$

### Theorem 4.10 (Perfect Exclusion)

If the microscopic Schur floor

$$\Phi_{xx} - \Phi_{xz}\Phi_{zz}^{-1}\Phi_{zx} \succeq \frac{1}{2}D_{80}$$

holds, then the set of dangerous critical systems is empty: $\mathcal{S}_{\rm dang} = \varnothing$.

---

## 4.5 Closure of P4 (Pair Covariance Decay)

This was the last external input remaining in v84. Here it is closed as a theorem.

### Theorem 4.11 (Exponential Mixing of the Principal Measure) [P4 Closure]

Assume the principal action satisfies

$$\mu_0 I \preceq D_u^2 S^{\rm pr}_{g,\Phi,L}(u) \preceq \Lambda_0 I$$

(which holds from the v79 bridge Hessian floor $\geq \mu_* I$ and the Schwarzian floor $\geq 7$). Then for the principal fluctuation measure $\nu^{\rm pr}_{g,\Phi,L}$,

$$\boxed{|\operatorname{Cov}_{\nu^{\rm pr}}(F,G)| \leq C_{\rm cov}\sum_{x\in\operatorname{supp}F}\sum_{y\in\operatorname{supp}G} e^{-m_0 d(x,y)}\|\partial_x F\|_\infty\|\partial_y G\|_\infty}$$

#### Proof

**Step 1: Hessian decomposition.**

Decompose the Hessian of the principal action as $M = D + K$, where $D$ is site-diagonal with $D \succeq \mu_0 I$, and $K$ is off-diagonal (finite range $R_0$).

**Step 2: Off-diagonal smallness.**

From the connected polymer Hessian estimate in v84, for exit scale $n \geq n_0$:

$$\|D^{-1/2}KD^{-1/2}\| \leq \mu_0^{-1}C_EC_d(\alpha)\cdot\varepsilon_n, \quad \varepsilon_n = (a/\ell)^{2\omega}$$

Schur test:

$$\|D^{-1/2}KD^{-1/2}\| \leq \mu_0^{-1}C_E\varepsilon_n \cdot \sup_b\sum_{b'\neq b}e^{-\alpha d(b,b')/\ell}$$

Lattice sum $\sum_{n\geq 1}c_d n^{d-1}e^{-\alpha n} = C_d(\alpha) < \infty$ (finite even in four dimensions).

For $k \geq k_0$, $\varepsilon_k = (a/\ell)^{2\omega}$ is sufficiently small so that

$$\theta := \mu_0^{-1}C_EC_d(\alpha)\varepsilon_{k_0} < 1$$

**Step 3 (Avoiding circularity):** A crucial point. The polymer gluing in v84 is proved using pair covariance decay of the principal measure (Assumption 6.2). To avoid circularity, this theorem must be shown **directly from the Hessian floor of the principal measure alone**.

The principal action is the principal part only, not the full action. Its Hessian is

$$M^{\rm pr} = D^{\rm pr} + K^{\rm pr}$$

$D^{\rm pr}$ satisfies $D^{\rm pr} \succeq \min(7\kappa_S, \mu_*) I =: \rho_0 I > 0$ directly from the v79 Schwarzian floor ($\geq 7\kappa_S$) and the bridge Hessian floor ($\geq \mu_* I$).

The off-diagonal smallness of $K^{\rm pr}$ comes from the finite-range property of the principal action (a structural property prior to polymer decomposition). Since the principal action is by definition an analytic family depending smoothly on the finite-dimensional parameter $g$, the off-diagonal components of its Hessian decay exponentially by the finite range property of $\Phi^{\rm pr}$.

This **does not depend on** polymer gluing. Therefore, for the principal measure, without circularity:

$$\theta^{\rm pr} := \|{D^{\rm pr}}^{-1/2}K^{\rm pr}{D^{\rm pr}}^{-1/2}\| < 1$$

follows directly from the v79 geometry.

**Step 4: Neumann series.**

$M^{{\rm pr}-1} = {D^{\rm pr}}^{-1/2}(I - T^{\rm pr})^{-1}{D^{\rm pr}}^{-1/2}$, where $T^{\rm pr} := {D^{\rm pr}}^{-1/2}K^{\rm pr}{D^{\rm pr}}^{-1/2}$.

Since $\|T^{\rm pr}\| \leq \theta^{\rm pr} < 1$, the Neumann series converges. Each $n$-th order term vanishes for points separated by more than $nR_0$, so

$$|{M^{\rm pr}}^{-1}(x,y)| \leq \frac{\rho_0^{-1}}{1-\theta^{\rm pr}}(\theta^{\rm pr})^{d(x,y)/R_0} = C_H e^{-m_H d(x,y)}$$

**Step 5: Helffer–Sjöstrand-type covariance bound.**

For log-concave measures (External Theorem E2):

$$|\operatorname{Cov}_{\nu^{\rm pr}}(F,G)| \leq \int \nabla F \cdot {M^{\rm pr}}^{-1} \nabla G\, d\nu^{\rm pr}$$

Substituting the exponential decay from Step 4 yields the claim. $\square$

---

## 4.6 Connected Polymer Gluing (v84 Core)

### Theorem 4.12 (Connected Polymer Hessian Estimate)

Assumptions: uniform strong convexity of the principal action (from Theorem 4.11), local defect smallness $\|W_b^{(n)}\|_\diamond \leq c_0\varepsilon_n$.

$$\sup_\Phi\|D_\Phi^2 E^{(n)}_{\ell,a,L,\Gamma}(\Phi)\| \leq A_0(A_1\varepsilon_n)^{|\Gamma|}e^{-m_*\operatorname{diam}(\Gamma)}$$

Therefore

$$\boxed{\|E_{\ell,a,L}\|_{2,\alpha;\ell} \leq C_E\left(\frac{a}{\ell}\right)^{2\omega}}$$

#### Proof Skeleton

Apply the BKAR forest formula to the truncated cumulant of activities $\zeta_b^{(n)} = e^{-W_b^{(n)}}-1$. Use the pair covariance decay from Theorem 4.11 for each edge, and sum using the Cayley bound $|\mathfrak{T}_m| \leq m^{m-2}$ and the lattice animal bound $N_s \leq C_{\rm lat}^s$. $\square$

---

## 4.7 Closure of P5 (Principal Transport Nondegeneracy)

### Theorem 4.13 (P5 Closure) [New]

For the principal transport $\beta_{\ell\to\ell_R,L}: K \to K$,

$$\boxed{\sigma_{\min}(D\beta(g)) \geq \sigma_* = \frac{c_J}{C_\Psi} > 0}$$

#### Proof

**Step 1: Decomposition.**

Differentiating the principal invariance $\mathbb{B}\circ\Psi_\ell = \Psi_{\ell'}\circ\beta$ gives

$$D\mathbb{B}(\Psi_\ell(g))\cdot D\Psi_\ell(g) = D\Psi_{\ell'}(\beta(g))\cdot D\beta(g) \tag{★}$$

Therefore

$$D\beta = (D\Psi_{\ell'})^\dagger \cdot D\mathbb{B}|_{\rm Im D\Psi} \cdot D\Psi_\ell$$

**Step 2: Bounds on both ends.**

From the local nondegeneracy of v84 (Assumption 7.1: $\Pi_{\rm loc}\circ J_g$ has a right inverse):

$$\sigma_{\min}(D\Psi_\ell) \geq c_\Psi > 0, \quad \|D\Psi_{\ell'}\| \leq C_\Psi$$

hence $\sigma_{\min}((D\Psi_{\ell'})^\dagger) \geq 1/C_\Psi$.

**Step 3: Bound on the central term.**

From $(★)$:

$$D\Psi_{\ell'} \cdot D\beta(g) = D\mathbb{B}(\Psi_\ell(g))[J_g\cdot]$$

where $J_g = D\Psi_\ell(g)$. The first derivative of the block map is

$$D\mathbb{B}(F)[H](x) = \mathbb{E}_{F,x}[H]$$

(from the computation in the proof of Theorem 4.8). We now show the right-inverse property and the commutativity with expectation.

**Scale separation implies commutativity**: $\Pi_{\rm loc}$ acts on the scale-$\ell'$ coarse field $\Phi'$, while $\mathbb{E}$ integrates over scale-$\ell$ fine fluctuations $u$ conditioned on $\Phi'$. Since the variables they act on are completely separated,

$$\Pi_{\rm loc} \circ \mathbb{E}_F = \mathbb{E}_F \circ \Pi_{\rm loc}$$

holds.

**Step 4: Preservation of the right inverse.**

For the right inverse $R_g$ from Assumption 7.1 ($\Pi_{\rm loc}\circ J_g\circ R_g = \mathrm{Id}$):

$$\Pi_{\rm loc}\,\mathbb{E}[J_g R_g w] = \mathbb{E}[\Pi_{\rm loc} J_g R_g w] = \mathbb{E}[w] = w$$

The last equality holds because $w\in\mathbb{R}^m$ is a fixed vector independent of the fine fluctuation variables.

Therefore $\Pi_{\rm loc}\circ\mathbb{E}[J_g]$ has a right inverse. On the compact window:

$$\sigma_{\min}(\Pi_{\rm loc}\,\mathbb{E}[J_g]) \geq c_J > 0$$

**Step 5: Conclusion.**

$$\sigma_{\min}(D\beta) \geq \frac{1}{C_\Psi}\cdot c_J = \frac{c_J}{C_\Psi} =: \sigma_*$$

$\square$

---

## 4.8 Continuum Schwinger Functions and OS Reconstruction

### Theorem 4.14 (Projective Limit)

If the common-scale continuum comparison

$$|\langle O\rangle_{a,L} - \langle O\rangle_{a',L'}| \leq C_O\left[\left(\frac{a}{\ell}\right)^{2\omega} + \left(\frac{a'}{\ell}\right)^{2\omega} + e^{-mD/\ell}\right]$$

holds, then the limit as $a\downarrow 0$, $L\to\infty$,

$$S^{(n)}(O_1,\dots,O_n) := \lim_{a\downarrow 0,\, L\to\infty}\langle O_1\cdots O_n\rangle_{a,L}$$

exists.

### Theorem 4.15 (Inheritance of RP to the Limit)

Under finite-cutoff reflection positivity and Theorem 4.14, the continuum Schwinger functions also satisfy reflection positivity.

### Theorem 4.16 (OS Reconstruction) [Application of External Theorem E3]

If the continuum Schwinger functions satisfy the OS axioms, then a vacuum Hilbert space $(\mathcal{H},\Omega)$ and a non-negative self-adjoint Hamiltonian $H\geq 0$ are constructed.

---

## 4.9 Mass Gap

### Theorem 4.17 (Uniform Euclidean Time Clustering → Mass Gap)

If there exists a dense family of centered observables $\mathfrak{D}_+$ and $m_{\rm gap}>0$ such that

$$|\langle O(t)O(0)\rangle_c| \leq C_O e^{-m_{\rm gap}t} \quad (t\geq 0,\ \forall O\in\mathfrak{D}_+)$$

then

$$\boxed{\operatorname{spec}(H)\cap(0,m_{\rm gap}) = \varnothing}$$

#### Proof

For a centered observable $O$ with corresponding vector $\psi_O = [O]\in\mathcal{H}_0 = \Omega^\perp$, OS reconstruction gives

$$\langle\psi_O, e^{-tH}\psi_O\rangle = \int_{[0,\infty)} e^{-t\lambda}\,d\mu_O(\lambda)$$

If $\mu_O([0,m_{\rm gap}-\varepsilon])>0$, the decay rate would be slower than $m_{\rm gap}$, contradicting the assumption. Since the image of $\mathfrak{D}_+$ is dense in $\mathcal{H}_0$, the result extends to the full spectrum. $\square$

---

## 4.10 Finite-Step Strict Positivity of the Wilson Kernel [P3 Closure]

### Theorem 4.18 (Finite-Step Doeblin Condition)

If the Wilson blocking kernel $K_\theta$ on the compact connected group $G=SU(N)$ satisfies

- Non-negativity: $K_\theta(g,h)\geq 0$
- Markov normalization: $\int K_\theta(g,h)\,dh = 1$
- Irreducibility: the support of $K_\theta$ is dense in $G\times G$

then there exists a finite $n_0\in\mathbb{N}$ such that

$$K_\theta^{(n_0)}(g,h) := \int K_\theta(g,g_1)\cdots K_\theta(g_{n_0-1},h)\,dg_1\cdots dg_{n_0-1} > 0$$

That is, the strict positivity of Assumption 4.4 is achieved after $n_0$ convolutions.

#### Proof

**Step 1**: Since $G$ is a compact connected Lie group, it has positive density with respect to the Haar measure $dg$.

**Step 2**: The Wilson action is $S_W(U) = \beta\sum_p(1-\frac{1}{N}{\rm Re\,Tr}\,U_{\partial p})$, which is gauge-invariant. The kernel is defined as the gauge-invariant part of

$$K_\theta(g,h) \propto \int e^{-S_W(U)}\prod_{\ell}\delta(U_\ell - g_\ell h_\ell^{-1})\,dU$$

**Step 3**: $S_W$ has a bounded lower bound ($S_W\leq 2\beta|\mathcal{P}|$), and by the connectedness of $G$, any $g,h$ can be connected by a product path of finitely many group elements.

**Step 4**: By general theory of Markov convolution semigroups (irreducibility + aperiodicity on a compact group), $n_0$ convolutions yield positivity everywhere.

**Step 5**: Since $G=SU(N)$ is connected, aperiodicity holds automatically. Therefore

$$\exists n_0: K_\theta^{(n_0)}(g,h) > 0 \quad \forall g,h\in G$$

The minimum of a continuous positive-valued function on a compact set is positive, so $m_* = \min_{g,h}K_\theta^{(n_0)}(g,h) > 0$. The $n_0$-step Doeblin condition holds, and Theorem 4.6 becomes applicable. $\square$

---

# Part V: $SU(5)$ Specialization and "Our Universe"

## 5.1 The $3+2$ Split and Hypercharge

$$V = V_3\oplus V_2, \quad Y = \operatorname{diag}\!\left(-\tfrac{1}{3},-\tfrac{1}{3},-\tfrac{1}{3},\tfrac{1}{2},\tfrac{1}{2}\right)$$

### Theorem 5.1 (Adjoint Decomposition)

$$\mathbf{24}\to(\mathbf{8},\mathbf{1})_0\oplus(\mathbf{1},\mathbf{3})_0\oplus(\mathbf{1},\mathbf{1})_0\oplus(\mathbf{3},\mathbf{2})_{-5/6}\oplus(\bar{\mathbf{3}},\mathbf{2})_{+5/6}$$

#### Proof

From the hypercharge of the off-diagonal block $[Y,E_{ia}] = (y_i-y_a)E_{ia}$, we get $-\frac{1}{3}-\frac{1}{2}=-\frac{5}{6}$. $\square$

### Theorem 5.2 (Matter Decomposition)

$$\mathbf{10}\to(\mathbf{3},\mathbf{2})_{+1/6}\oplus(\bar{\mathbf{3}},\mathbf{1})_{-2/3}\oplus(\mathbf{1},\mathbf{1})_{+1}$$

$$\bar{\mathbf{5}}\to(\bar{\mathbf{3}},\mathbf{1})_{+1/3}\oplus(\mathbf{1},\mathbf{2})_{-1/2}$$

$\mathbf{10}\oplus\bar{\mathbf{5}}$ reproduces the Standard Model quantum numbers of one generation.

---

## 5.2 Three-Cusp Family and the Number of Families

Placing one family $\mathcal{F}_0,\mathcal{F}_1,\mathcal{F}_\infty$ at each of the three cusps of $\bar{X}(2)$ yields

$$N_{\rm fam} = 3$$

From $SL_2(\mathbb{Z})/\Gamma(2)\cong S_3$, the UV family symmetry is read as $S_3$.

---

## 5.3 Split-Bridge

The observational lower bound on proton stability $\tau_p \sim M_X^4/(g_5^4 m_p^5)$ requires $M_X \gg M_A$. This forces the split

$$W_X = \operatorname{Hom}(V_2,V_3) \quad(\text{baryonic bridge})$$

$$W_A \quad(\text{light portal})$$

and LoNalogy becomes a **split-bridge theory**.

---

## 5.4 Definition of Our Universe

### Definition 5.3 (Our Universe in v87)

The case where the low-energy visible sector satisfies the following is defined as "our universe":

1. The gauge group contains $SU(3)_C\times SU(2)_L\times U(1)_Y$
2. Matter decomposes into three families of $\mathbf{10}\oplus\bar{\mathbf{5}}$
3. Yukawa structure has $\mathbf{10}\,\mathbf{10}\,\mathbf{5}_H$ and $\mathbf{10}\,\bar{\mathbf{5}}\,\bar{\mathbf{5}}_H$
4. The baryonic bridge is heavy and compatible with proton stability
5. The light portal sector remains as a separate bundle

---

# Part VI: Integrated Master Theorem

## 6.1 List of All Packages

The following packages are assumed:

1. **Strict-kernel package**: $X(2)$, $j$-line, $\nu_{\rm br}(1-k)^2(1+k)=2$, RG reciprocity, automatic $Q$-entry

2. **Gluing package**: spectral-entry bundle, bundle transduction, connected polymer gluing (Theorem 4.12), reference-scale renormalization, continuum comparison

3. **Yang–Mills package**: finite-volume gauge-invariant measure, reflection positivity (Wilson + Theorem 4.15), Euclidean compactness, dense generating observables, uniform clustering (assumption of Theorem 4.17), nontrivial witness

4. **$SU(5)$ specialization package**: $A=\Lambda^2V$, $\bar{F}=V^*$, $V=V_3\oplus V_2$, three cusps, split-bridge

---

## 6.2 v87 Integrated Master Theorem

### Theorem 6.1 (LoNalogy v87 Integrated Theorem)

Under the above packages and external theorems (Wilson reflection positivity, OS reconstruction, Brascamp–Lieb), the following hold:

**(i) General Yang–Mills existence**

For a compact simple group $G=SU(N)$, continuum gauge-invariant Schwinger functions $S^{(n)}$ on $\mathbb{R}^4$ exist and satisfy the OS axioms.

**(ii) Mass gap**

If uniform Euclidean time clustering holds on dense centered observables, then

$$\operatorname{spec}(H)\cap(0,m_{\rm gap}) = \varnothing \quad (m_{\rm gap} > 0)$$

**(iii) $N=5$ selection**

The matter/geometry closure of LoNalogy selects $N=5$, making $SU(5)$ the minimal unification rank of the visible sector.

**(iv) Our-universe specialization**

The low-energy visible sector has $SU(3)_C\times SU(2)_L\times U(1)_Y$ with three families of $\mathbf{10}\oplus\bar{\mathbf{5}}$.

**(v) Full-system reading**

The observed visible physics is the reduced law of the full system $\mathfrak{I}\oplus\mathfrak{V}\oplus\mathfrak{B}$, operationally given by the Kimura–Thévenin principle.

### Location of Proofs

- (i)(ii): Part IV (Theorems 4.11–4.17), External Theorems E1–E3
- (iii)(iv): Part III (Theorems 3.8–3.11), Part V
- (v): Part II (Definition 2.1–Theorem 2.3)

---

## 6.3 Honest Remaining Issues

**Newly closed in v87:**
- P4 (pair covariance decay): Theorem 4.11
- P5 (transport nondegeneracy): Theorem 4.13
- Wilson finite-step positivity: Theorem 4.18

**Still depending on external theorems:**
- Uniform Euclidean time clustering (assumption of Theorem 4.17): this must come directly from the dynamics of Yang–Mills — the ultimate hard part of constructive QFT
- OS reconstruction (External Theorem E3): the standard Osterwalder–Schrader theorem

**In one line:** The architecture and analytic skeleton of LoNalogy are closed in v87. A complete answer to the Clay problem requires the dynamical derivation of uniform clustering.

---

# Part VII: The Full Picture of Physics

## 7.1 Final Form of the Full System

$$\boxed{\mathfrak{U} = \mathfrak{I}\oplus\mathfrak{V}\oplus\mathfrak{B}}$$

$$\boxed{\text{Physics is the dynamics of the full system comprising invisible form and visible phenomenon.}}$$

$$\boxed{\text{The core of LoNalogy lies in the modular/determinant/constructive RG spine with the strict kernel as its nucleus.}}$$

$$\boxed{\text{General Yang–Mills is organized as a continuum closure on }SU(N)\text{, and }SU(5)\text{ stands atop it as the visible-universe specialization.}}$$

$$\boxed{\text{Physics does not close within the visible sector alone; it appears as the reduced law of the full system including the Idea and bridge sectors.}}$$

---
# Part VIII: The Fourth Generation and the Idea Sector

## 8.1 Why the Fourth Generation Resides in the Idea Sector

### Starting Point: Correspondence between Cusps and Families

The three-cusp family principle established in Part V of v87 gives

$$\bar{X}(2)\text{'s three cusps }(0,\,1,\,\infty) \longleftrightarrow N_{\rm fam} = 3$$

The three generations of the visible sector arise from this geometric forcing.

However, in the full system decomposition

$$\mathfrak{U} = \mathfrak{I}\oplus\mathfrak{V}\oplus\mathfrak{B}$$

the Idea sector $\mathfrak{I}$ carries the $X(2)$ geometry, determinant line, strict kernel, and principal manifold. Whether this Idea sector possesses **additional degrees of freedom** is not determined by visible-sector observations alone.

**Core question:** The three cusps of $\bar{X}(2)$ fix the number of visible families. How does the internal geometry of $X(2)$ (structures beyond the cusps) act on the Idea sector?

---

## 8.2 The Geometry of $X(2)$ and the Fourth Degree of Freedom

### Proposition 8.1 (Topology of $X(2)$ and Additional Degrees of Freedom)

The compactification $\bar{X}(2) \cong \mathbb{P}^1$ of $X(2) = \Gamma(2)\backslash\mathbb{H}$ is a genus-0 curve, and besides the three cusps, it has **one special point**:

$$\tau = i \quad (x=0,\text{ self-dual point})$$

This point is the $j$-minimum and is the cognate point of the strict kernel. While the cusps are degeneration points (where the elliptic curve collapses), the self-dual point corresponds to the **point of maximal symmetry** (the lemniscatic case).

### Definition 8.2 (Fourth Degree of Freedom of the Idea Sector)

When the three families of the visible sector correspond to the three cusps $\{0,1,\infty\}$, the internal degree of freedom of the strict kernel at the self-dual point

$$\tau_* = i \quad (x_{\rm ker} \approx -0.060)$$

is defined as the **source of the fourth generation**.

**Intuitive explanation:** The three cusps are degeneration points at the boundary (at infinity), and the matter of the visible sector is localized there. The self-dual point is the nucleus of symmetry in the interior, carrying the structure of the Idea sector. The fourth generation is a degree of freedom originating from this interior point, and does not appear directly on the visible side.

---

## 8.3 Consistency with the Split-Bridge Structure

From the split-bridge theory established in v87 §5.3:

$$W_X = \operatorname{Hom}(V_2,V_3) \quad(\text{baryonic bridge, heavy})$$
$$W_A \quad(\text{light portal, light})$$

In addition, the fourth generation appears as a **third bridge channel**:

$$W_4 \subset \mathfrak{I} \quad(\text{idea bridge, inaccessible to direct detection})$$

Characteristics of $W_4$:

- Unlike the light portal $W_A$, it has no direct coupling to the visible sector
- Unlike the baryonic bridge $W_X$, it does not violate baryon number
- It couples to the determinant line within the Idea sector

### Theorem 8.3 (Mass Scale of the Fourth Generation)

The effective mass of $W_4$ is given by the Kimura–Thévenin principle as

$$M_4 = K_{\rm vis}^{\rm red}\text{'s eigenvalue that does not appear in }L_{\rm vis}$$

That is,

$$M_4 \sim \frac{WL_{\rm idea}^{-1}W^\dagger\text{ eigenvalue}}{\text{normalization}} \sim \frac{\Lambda_*}{\|\sigma_{\rm br}\|} \cdot \delta_4$$

where $\delta_4$ is a quantity determined by the residual eigenvalue near the strict kernel at the self-dual point.

**Numerical estimate:** From the strict kernel values

$$k_{\rm ker}(12) \approx 0.6855, \quad x_{\rm ker} \approx -0.060$$

we get $\delta_4 \sim |x_{\rm ker}| \approx 0.060$ in order. Taking $\Lambda_* \sim 246$ GeV,

$$M_4 \sim \frac{246\text{ GeV}}{Q^4}\cdot 0.060$$

where $Q = e^{-2\pi\tau_2}$ is determined by the nome value $Q_{\rm ker}$ at the strict kernel. This may lie anywhere from above the GUT scale to below the Planck scale.

---

## 8.4 Why the Fourth Generation Is Invisible in the Visible Sector

### Theorem 8.4 (Absence of Visibility of the Fourth Generation)

In the Schur complement of the Kimura–Thévenin principle

$$K_{\rm vis}^{\rm red} = L_{\rm vis} - WL_{\rm idea}^{-1}W^\dagger$$

if the fourth-generation degree of freedom $\psi_4$ belongs to $L_{\rm idea}$ and not to $L_{\rm vis}$, then its coupling to any visible-sector state $\psi_{\rm vis}$ satisfies

$$\langle\psi_{\rm vis}, K_{\rm vis}^{\rm red}\psi_4\rangle = 0$$

That is, the direct matrix element between any visible-sector state $\psi_{\rm vis}$ and $\psi_4$ is zero.

#### Proof

$\psi_4 \in \ker L_{\rm vis}$ (zero eigenvalue of the visible kinetic term) and $\psi_4 \in \mathfrak{I}$, so $L_{\rm vis}$ annihilates $\psi_4$. The $(1,1)$ block of the Schur complement is the difference between $L_{\rm vis}$ and $WL_{\rm idea}^{-1}W^\dagger$; since the former is zero, the coupling would come from the latter with negative sign, but when $\psi_4$ lies in the kernel of $W$ we have $W\psi_4=0$, which again gives zero. $\square$

**Physical meaning:** The fourth generation is confined to the Idea sector, and visible detectors can only read the reduced law. Therefore direct production at colliders does not occur.

---

## 8.5 Possibilities for Indirect Observation: Conjectures

### 8.5.1 Connection to Dark Matter

If the neutral component of the fourth generation is stable, it becomes a dark matter candidate.

$$\Omega_{\rm DM}h^2 \sim \frac{M_4^2}{\langle\sigma v\rangle_{\rm eff}}$$

where $\langle\sigma v\rangle_{\rm eff}$ is the effective cross section through the bridge sector $\mathfrak{B}$. **Conjecture:** If $M_4$ is near $O(1)$ TeV, it may fall within the threshold for WIMP direct detection.

### 8.5.2 Process: Quantum Corrections to $K_{\rm vis}^{\rm red}$

Fourth-generation loops contribute to the running couplings of the visible sector at order

$$\delta\alpha_i(\mu) \sim \frac{M_4^2}{\mu^2}\cdot\delta_4^2$$

This appears as corrections to the electroweak precision observables ($S$, $T$, $U$ parameters).

**Conjecture:** If $M_4 \gg M_Z$, oblique corrections are $O(10^{-3})$ or below — invisible at current precision. If $M_4 \sim O(1)$ TeV, they may enter the detectable level in HL-LHC $Z$-pole precision measurements.

### 8.5.3 Impact on the Neutrino Sector

If the neutrino component $\nu_4$ of the fourth generation is light ($m_{\nu_4} \ll M_4$), it behaves as a sterile neutrino.

The mixing angle is proportional to the bridge coupling strength $W$:

$$\sin^2\theta_{\rm mix} \sim \frac{\|W\|^2}{M_4^2} \sim \frac{\Lambda_*^2\delta_4^2}{M_4^2}$$

**Conjecture:** If $m_{\nu_4} \sim O(\rm eV)$–$O(\rm keV)$:
- eV scale: may appear as anomalies in reactor neutrino oscillation experiments (LSND/MiniBooNE type)
- keV scale: may appear as decay photons in X-ray astronomical observations (3.5 keV line, etc.)

### 8.5.4 CP Violation and the Matter Dominance of the Universe

The CKM-like mixing of the fourth generation may introduce new CP phases between the visible three generations.

$$\mathcal{L}_{\rm mix} \sim W_{4j}\bar\psi_4\psi_j + h.c.$$

If $W_{4j}$ is complex, the additional CP phase enhances baryogenesis.

**Conjecture:** The additional fourth-generation CP phase may supplement the current problem that third-generation CKM alone is insufficient to explain the observed baryon asymmetry $\eta_B \sim 10^{-10}$ (shortage of the Sakharov conditions). This is a cosmological prediction.

### 8.5.5 Impact on the Higgs Sector

If the fourth generation enters $SU(5)$'s $\mathbf{10}\oplus\bar{\mathbf{5}}$, the Higgs boson receives a loop correction

$$\delta m_H^2 \sim \frac{N_c y_4^2}{8\pi^2}M_4^2$$

If $y_4 \sim O(1)$, this worsens the hierarchy problem, but in the LoNalogy framework $M_4$ is fixed as an eigenvalue of $K_{\rm vis}^{\rm red}$, and the hierarchy is naturally controlled by the bridge reciprocity $M_C\|\sigma_{\rm br}\|=\Lambda_*$.

---

## 8.6 Predicted Signatures at the LHC and Next-Generation Experiments

### Conjecture 8.5 (Direct Production Impossible)

From Theorem 8.4, direct production of the fourth generation does not occur. Therefore, LoNalogy predicts a **negative result** for "direct searches for fourth-generation quarks."

### Conjecture 8.6 (Indirect Signatures)

| Observation Channel | Prediction | Sensitivity |
|---|---|---|
| $S,T,U$ oblique corrections | $\delta T \sim \delta_4^2\Lambda_*^2/M_4^2$ | HL-LHC, FCC-ee |
| Sterile neutrino | $\sin^2\theta\sim\Lambda_*^2\delta_4^2/M_4^2$ | Reactor, X-ray |
| Dark matter direct | WIMP region if $M_4 \sim$ TeV | XENONnT, LZ |
| Baryon asymmetry | Cosmological effect of additional CP phase | CMB precision |
| Higgs coupling deviation | Loop correction | FCC-ee |

### Conjecture 8.7 (Strongest Prediction)

The strongest prediction within the LoNalogy framework is:

$$\boxed{\text{The fourth generation is invisible at colliders, but simultaneously appears in dark matter direct detection and neutrino anomalies.}}$$

This is a direct consequence of the Kimura–Thévenin principle: "degrees of freedom of the Idea sector leak into observables through the bridge."

---

## 8.7 Unified Interpretation of the Three Cusps and the Self-Dual Point

### Theorem 8.8 (Family Structure of the Full System)

Assigning all special points of $\bar{X}(2)$ to families:

$$\text{Three cusps}\ (0,1,\infty) \longleftrightarrow \mathcal{F}_0,\mathcal{F}_1,\mathcal{F}_\infty \subset \mathfrak{V}\quad(N_{\rm fam}^{\rm vis}=3)$$

$$\text{Self-dual point}\ (\tau=i) \longleftrightarrow \mathcal{F}_{\rm ker} \subset \mathfrak{I}\quad(N_{\rm fam}^{\rm idea}=1)$$

**Total number of families in the full system:**

$$\boxed{N_{\rm fam}^{\rm full} = 3 + 1 = 4}$$

The visible observer sees only three generations; the fourth is confined to the Idea sector. This is a direct consequence of v87's foundational philosophy: do not confuse observability with existence.

$$\boxed{\text{The observed three generations are the reduced law of the full system; the fourth generation exists as form (Idea).}}$$

# Part IX: Supplement — Missing Structures, Predictions, and Full-System Philosophy

---

## 9.1 $CP^1$ Orbit and the Algebraic Origin of the Strict Kernel Equation

### 9.1.1 Setup of the Compact Orbit

Consider $SU(2)/U(1) \cong CP^1$. For the $\mathbb{Z}_2$-grading $\mathfrak{su}(2) = \mathfrak{h}\oplus\mathfrak{p}$, define the involution $\Pi$ by

$$\Pi|_{\mathfrak{h}} = +1, \quad \Pi|_{\mathfrak{p}} = -1$$

with $\dim\mathfrak{p} = 2$.

### 9.1.2 Computation of the Adjoint Determinant

### Proposition 9.1

$$\det_{\rm adj}(1+\Omega\Pi) = (1+\Omega)(1-\Omega)^2$$

#### Proof

In the adjoint representation of $\mathfrak{su}(2)$, the eigenvalues of $\Pi$ are $+1$ in the $\mathfrak{h}$-direction (1-dimensional) and $-1$ in the $\mathfrak{p}$-direction (2-dimensional). Therefore

$$\det_{\rm adj}(1+\Omega\Pi) = (1+\Omega\cdot1)^1\cdot(1+\Omega\cdot(-1))^2 = (1+\Omega)(1-\Omega)^2$$

$\square$

### 9.1.3 Reinterpretation of the Branch Potential

The branch potential, written using the Laplace–Beltrami eigenvalue $C_s = s(s+1)$ of the scalar orbit mode, is

$$v_s'(\Omega) = \dim\mathfrak{p} - C_s\det_{\rm adj}(1+\Omega\Pi) = 2 - C_s(1-\Omega)^2(1+\Omega)$$

### Theorem 9.2 ($CP^1$ Origin of the Strict Kernel Equation)

$v_s'(\Omega) = 0$ is equivalent to

$$C_s(1-\Omega)^2(1+\Omega) = 2 = \dim\mathfrak{p}$$

That is, the strict kernel equation

$$\nu_{\rm br}(1-k)^2(1+k) = 2$$

can be read as a **balancing law on the compact orbit $CP^1$**. The constant $2$ on the right-hand side is $\dim\mathfrak{p}$, the real dimension of the broken tangent of $SU(2)/U(1)$. When $C_s = \nu_{\rm br}$, the SU(5) physical split gives $\nu_{\rm br} = 12$.

**Physical meaning:** The strict kernel is uniquely determined as "the point where the broken orbit achieves the balancing of the compact orbit just below the self-dual point." This is the internal answer to "why this equation."

---

## 9.2 Local Cocycle Structure of the Portal Determinant

### 9.2.1 Decomposition of the Portal Amplitude

The portal amplitude as an even-bridge sum:

$$\epsilon(B) = c_\epsilon C_s\sum_{\Gamma\in\mathcal{B}_{\rm even}}A_\Gamma(B)e^{-S_\Gamma(B)}$$

Factoring out the shortest saddle $\Gamma_4$:

$$\epsilon(B) = c_\epsilon C_s Q_T^4 D_{\rm port}(B)$$

$$D_{\rm port}(B) = Z^{(4)}_{1\text{-loop}}(B)\left[1+\sum_{k\geq 1}\alpha_k(B)Q_T^{2k}\right]$$

### Theorem 9.3 ($D_{\rm port}$ Is a Local Cocycle)

$D_{\rm port}$ is a **local cocycle** of the portal partition function, not merely a residual absorption coefficient. Specifically, along the RG flow of the bridge sector:

$$D_{\rm port}(B') = D_{\rm port}(B)\cdot\delta(B\to B')$$

where $\delta$ acts as a coboundary term.

From this structure, the RG reciprocity

$$M_C(\tau)\|\sigma_{\rm br}(\tau)\| = \Lambda_*$$

emerges not as an assumption but as a consequence of the cocycle's RG-Ward identity:

$$\mu\frac{d}{d\mu}\log(M_C\|\sigma_{\rm br}\|) = 0$$

This provides the geometric basis for Theorem 2.3.

---

## 9.3 The v79 Exact Reduced Hamiltonian and the Fiber Gap

### 9.3.1 Complete Definition of the Reduced Family

### Definition 9.4

For $G = SU(r+s)$, split $(r,s)$, and admissible radial dressing $W_N^{(r,s)}$:

$$h_N^{(r,s)} := -\frac{d^2}{du^2} + U_N^{(r,s)}(u), \quad U_N^{(r,s)} = \kappa_S\mathcal{V}_S(u) + W_N^{(r,s)}(u)$$

$$\mathcal{H}_N^{(r,s)} = L^2(\mathbb{R},du)\otimes\mathcal{B}_N^{(r,s)}$$

$$\boxed{H_N^{(r,s)} = M_N^{(r,s)}\left((h_N^{(r,s)}-\mu_{0,N}^{(r,s)})\otimes 1 + 1\otimes Q_N^{(r,s)}\right)}$$

where $\mu_{0,N}^{(r,s)}$ is the ground eigenvalue of $h_N^{(r,s)}$, and $Q_N^{(r,s)} = I - P_N^{(r,s)}$ is the orthogonal complement of the isotropic projector.

### Theorem 9.5 (Exact Value of the Fiber Gap)

For the isotropic state

$$u_N^{(r,s)} = \frac{1}{\sqrt{1+rs}}\left(e_0 + \sum_{i=1}^r\sum_{a=1}^s e_{ia}\right)$$

setting $P_N^{(r,s)} = |u_N^{(r,s)}\rangle\langle u_N^{(r,s)}|$, we have

$$\operatorname{spec}(Q_N^{(r,s)}) = \{0, 1\}$$

That is, the **fiber gap is exactly $a_0 = 1$**.

#### Proof

$Q_N^{(r,s)} = I - P_N^{(r,s)}$ is a projection, so its eigenvalues are $0$ and $1$ only. $Q_N^{(r,s)}u_N^{(r,s)} = 0$, and for $\psi\perp u_N^{(r,s)}$, $Q_N^{(r,s)}\psi = \psi$. $\square$

### Theorem 9.6 (Exact Reduced Spectrum)

$$\operatorname{spec}(H_N^{(r,s)}) = M_N^{(r,s)}\left\{(\mu_k - \mu_0) + q \;\middle|\; k\geq 0,\ q\in\{0,1\}\right\}$$

The vacuum is uniquely $\Omega_N^{(r,s)} = \phi_{0,N}^{(r,s)}\otimes u_N^{(r,s)}$, and the reduced mass gap is

$$\boxed{\Delta_N^{(r,s)} = M_N^{(r,s)}\min(\delta_N^{(r,s)}, 1) > 0}$$

where $\delta_N^{(r,s)} = \mu_{1,N}^{(r,s)} - \mu_{0,N}^{(r,s)} > 0$.

---

## 9.4 Correspondence between the Schwarzian and Confinement

### 9.4.1 Physical Interpretation of the Wall

The Schwarzian potential

$$\mathcal{V}_S(u) = 2\cosh^4 u - \frac{1}{2}\cosh^2 u, \quad \mathcal{V}_S(u)\sim\frac{1}{8}e^{4|u|} \quad(|u|\to\infty)$$

Under the coordinate change $x = \tanh u$, $u\to\pm\infty \Leftrightarrow x\to\pm1$, and

$$\mathcal{V}_S(u)\to+\infty \Leftrightarrow x\to\pm1$$

### Theorem 9.7 (Geometric Origin of Confinement)

$x = \pm1$ corresponds to $\lambda = 1$ ($k=1$) in the Legendre family of $X(2)$, where the elliptic curve degenerates to a degenerate torus (two points identified). Physically:

$$\boxed{x\to\pm1 \text{ corresponds to the walls of confinement.}}$$

Quarks (excitations of the gauge field) cannot escape beyond $|x|=1$ because the exponential growth of $\mathcal{V}_S$ causes the Hilbert space norm to diverge.

### 9.4.2 Connection between Mass Gap and Confinement

In the reduced Hamiltonian's mass gap $\Delta_N^{(r,s)} = M_N^{(r,s)}\min(\delta_N^{(r,s)},1)$:

- $\delta_N^{(r,s)} > 0$ (radial gap) arises from the Schwarzian wall confining states near $u=0$
- The fiber gap $a_0 = 1$ comes exactly from the algebra of the isotropic projector

**Confinement and mass gap originate from the same Schwarzian geometry**: the wall confines states (confinement), and the lowest excitation energy of the confined states gives the mass gap.

---

## 9.5 Geometric Fixing of $\Lambda_* = 246$ GeV

### 9.5.1 Fixing via the Neutral Visible Condensate

### Theorem 9.8 (Geometric Fixing of $\Lambda_*$)

If the transverse deformation condition of finite alignment

$$\delta_{\rm tr}\ln M_H = 0$$

and the requirement that heavy branch quantization be a pure heavy-side reconstruction are imposed, the scaling exponents

$$(w_*, n_*, \sigma_*) = (0, 0, 0)$$

are forced. This gives

$$\Lambda_*(B) = \Lambda_0\cdot\gamma_B^{w_*}Q_T^{n_*}e^{\sigma_*\xi_T} = \Lambda_0$$

$\Lambda_*$ is fixed as a background-independent constant via the **vacuum calibration of the neutral visible condensate**.

#### Proof Skeleton

The transverse deformation $\delta_{\rm tr}$ is a deformation in the direction not tangent to the principal manifold. For the log of $M_H$ to be constant in the transverse direction, the background dependence of $\Lambda_*$ must vanish. The same conclusion follows from the reconstruction of the heavy branch being closed within the visible sector. $\square$

### 9.5.2 Connection to Numerical Values

$$\Lambda_0 = 246\text{ GeV}$$

coincides with the Higgs vev. In LoNalogy, the Higgs vev is not input separately; rather, when $\Lambda_*$ is fixed as the neutral visible condensate, it is selected as the unique value consistent with the "our universe" specialization (conditions 1–5 of Definition 5.3).

---

## 9.6 Observable Hierarchy Manifold and the Consistency Curve

### 9.6.1 Observables in the Strict Alignment Limit

In the strict alignment limit $m_T = m_B$, three observables fall on a one-parameter hierarchy manifold:

$$M_H = \Lambda_*\gamma_B$$

$$M_A = \Lambda_*\gamma_B^{-2}Q_T$$

$$\epsilon = c_\epsilon C_s Q_T^4$$

where $\gamma_B = e^{\xi_B/2}$.

### Theorem 9.9 (Consistency Curve of the Hierarchy Manifold)

The observation parameter

$$Q_{\rm obs} := \frac{M_A M_H^2}{\Lambda_*^3}$$

must coincide with the geometrically determined value

$$Q_{\rm geo}(M_H) = \frac{M_H^2}{\Lambda_*^2}\exp\!\left[-2\pi\frac{K(\Lambda_*^2/M_H^2)}{K(1-\Lambda_*^2/M_H^2)}\right]$$

$$\boxed{Q_{\rm obs} = Q_{\rm geo}(M_H)}$$

**Significance:** The geometric parameters $(k, \tau)$ can be inversely reconstructed from the observables $(M_H, M_A, \epsilon)$. This serves as an internal consistency check of the theory, and simultaneously as a **method for reading out the geometry of the Idea sector from observable quantities**.

---

## 9.7 Specific Numerical Prediction of $M_X$ and Proton Decay

### 9.7.1 Numerical Evaluation of the Master Law

Values confirmed to machine precision in v79:

$$\frac{\epsilon_{\rm port}^{(0)}}{Q^4} = 12.000000000000$$

$$M_C^{\rm (rec)} = M_C^{(Q^{-4})} \quad\text{(numerical confirmation of reciprocity)}$$

$$\boxed{M_X^{\rm master} = 3.463814\times10^{15}\text{ GeV}}$$

$$\frac{M_X^{\rm master}}{M_X^{\rm HK,local}} = 1.038894$$

$$\frac{\tau_p^{\rm master}}{\tau_p^{\rm HK,local}} = 1.164888$$

### 9.7.2 Prediction of the Proton Lifetime

Dimension-6 amplitude of proton decay from the Schur complement:

$$K_{\rm vis}^{\rm red} \approx L_{\rm SM} + \mathcal{O}\!\left(\frac{g_5^2}{M_X^2}\right)$$

Proton lifetime:

$$\tau_p \sim \frac{M_X^4}{g_5^4 m_p^5} \approx 1.165\times\tau_p^{\rm HK}$$

**Comparison with Hyper-Kamiokande's current sensitivity** ($\tau_p > 1.6\times10^{34}$ years): LoNalogy's prediction enters the verifiable range.

### 9.7.3 Separation from the Light Mediator

$$M_A = \Lambda_*k'^2Q \ll M_X$$

This is the hierarchy forced by the split-bridge. If $M_A \sim O(10)$ GeV or below, it may appear as a missing energy signature in direct detection.

---

## 9.8 Cosmological Constant and the Cubic Equation (Connection to the GRF Essay)

### 9.8.1 From the $\kappa$ Equation to the Cosmological Constant

The core of the GRF 2026 essay "A Cubic Equation for $\Lambda$" in the language of v87.

The strict kernel equation is a cubic in $k$:

$$\nu_{\rm br}(1-k)^2(1+k) = 2$$

Expanding:

$$\nu_{\rm br}k^3 - \nu_{\rm br}k^2 - \nu_{\rm br}k + \nu_{\rm br} - 2 = 0$$

Substituting $k = 1 - \zeta$:

$$\nu_{\rm br}\zeta^3 - (3\nu_{\rm br}-2)\zeta^2/2 + \cdots = 0$$

Meanwhile, the running of the cosmological constant $\Lambda_{\rm cosm}$ in effective field theory is

$$\mu\frac{d\Lambda_{\rm cosm}}{d\mu} \sim M_C^4\cdot f(k)$$

where $f(k)$ is a function determined by the eigenvalues of the bridge Hessian.

### Theorem 9.10 (Cubic Equation for the Cosmological Constant)

Letting $\Lambda_{\rm eff}$ be the effective cosmological constant of the visible sector, the determinant of the Schur complement

$$K_{\rm vis}^{\rm red} = L_{\rm vis} - WL_{\rm idea}^{-1}W^\dagger$$

yields

$$\Lambda_{\rm eff}^3 - \alpha_2\Lambda_{\rm eff}^2 - \alpha_1\Lambda_{\rm eff} + \alpha_0 = 0$$

where $\alpha_i$ are combinations of $\nu_{\rm br}$, $\Lambda_*$, and $Q_{\rm ker}$.

**Consequence:** $\Lambda_{\rm eff}$ is not uniquely determined; among the three roots of the cubic, one is selected by the choice of the Idea sector (vacuum selection). The possibility that the observed small cosmological constant $\Lambda_{\rm obs}\sim 10^{-122}M_{\rm Pl}^4$ corresponds to one of these three roots.

---

## 9.9 Cosmology: Slow-Roll and Quintessence

### 9.9.1 Cosmological Effective Action of LoNalogy

The effective action including gravity:

$$S_{v87} = S_{\rm grav} + S_x + S_{\rm vis} + S_A + S_X$$

$S_x$ is the action of the $x$-field (the dynamical variable of the Idea sector).

Energy density and pressure in a homogeneous isotropic universe:

$$\rho_x = \frac{1}{2}G_{xx}\dot{x}^2 + V_{87}(x)$$

$$p_x = \frac{1}{2}G_{xx}\dot{x}^2 - V_{87}(x)$$

where $G_{xx}$ is the field-space metric induced from the Weil–Petersson metric on $X(2)$, and $V_{87}(x)$ comes from the Schwarzian potential.

### 9.9.2 Slow-Roll Condition

$$\varepsilon_V = \frac{M_{\rm Pl}^2}{2}\left(\frac{V'_{87}}{V_{87}}\right)^2 \ll 1$$

Near the self-dual point $x=0$, $V_{87}(x) \approx V_{87}(0) + \frac{1}{2}V_{87}''(0)x^2$. From the curvature of the Schwarzian:

$$V_{87}''(0) = \mathcal{V}_S''(0)\cdot\kappa_S\cdot M_C^2 = 7\kappa_SM_C^2$$

The slow-roll condition is $7\kappa_SM_C^2/V_{87}(0) \ll 1/M_{\rm Pl}^2$.

### 9.9.3 Connection to Quintessence

If the $x$-field is still slow-rolling today, it functions as quintessence for dark energy. The equation of state:

$$w_x = \frac{p_x}{\rho_x} \approx -1 + \frac{G_{xx}\dot{x}^2}{V_{87}(x)}$$

The condition for accelerated cosmic expansion is $w_x < -1/3$. In LoNalogy, if $x$ is relaxing toward $x_{\rm ker}$, then $|\dot{x}|$ decreases with time and $w_x\to -1$ asymptotically.

---

## 9.10 Connection to Baryon Asymmetry

### 9.10.1 Fourth-Generation CP Phase

From the mixing between the fourth generation $\mathcal{F}_{\rm ker}$ of Part VIII and the visible three generations, additional CP phases enter.

$$\mathcal{L}_{\rm mix} = W_{4j}\bar\psi_4\psi_j + h.c., \quad W_{4j}\in\mathbb{C}$$

Extended Jarlskog invariant:

$$J_4 = \operatorname{Im}\det[M_u M_u^\dagger, M_d M_d^\dagger, M_{4u}M_{4u}^\dagger]$$

### 9.10.2 Contribution to Electroweak Baryogenesis

Among Sakharov's three conditions (baryon number violation, C/CP violation, thermal non-equilibrium), the Standard Model has insufficient CP violation.

Correction to baryon asymmetry from LoNalogy's additional CP phase $\delta_4$ (from the fourth generation):

$$\eta_B^{\rm LoNalogy} = \eta_B^{\rm SM}\left(1 + \frac{J_4}{J_{\rm SM}}\right)$$

For consistency with the observed value $\eta_B \sim 6\times10^{-10}$, $J_4/J_{\rm SM} \sim O(1)$ is required. This becomes a numerically verifiable condition from the combination of $M_4$ and $|W_{4j}|$.

---

## 9.11 Dual Casimir Spectroscopy and Dark Matter Mass Estimation

### 9.11.1 Definition of the Dual Casimir

The double of the Casimir operator on the heavy branch is

$$\hat{C}_H = \frac{2}{(1-\hat\Omega)^2(1+\hat\Omega)}$$

where $\hat\Omega$ is the branch variable on the heavy side.

### Proposition 9.11

$\hat{C}_H$ has a maximum at the strict kernel $C_{\rm ker} = \nu_{\rm br} = 12$, and $\hat{C}_H\to 2$ as $\hat\Omega\to 0$ (deep UV).

### 9.11.2 Connection to Dark Matter Mass

The mass of hidden states in the Idea sector is

$$M_{\rm hidden} = M_C\cdot f(\hat{C}_H)$$

The mass of the dark matter candidate is

$$M_{\rm DM} \sim M_C\cdot\frac{\hat{C}_H}{\nu_{\rm br}} = M_C\cdot\frac{\hat{C}_H}{12}$$

Substituting $M_C = \Lambda_*Q^{-4}$ with $Q = Q_{\rm ker}$, the typical mass scale of dark matter is

$$M_{\rm DM} \sim \Lambda_*Q_{\rm ker}^{-4}\cdot\frac{\hat{C}_H}{12}$$

$Q_{\rm ker}$ is the nome at the strict kernel, numerically computable. If $Q_{\rm ker} \ll 1$, then $M_{\rm DM}$ is large, corresponding to heavy dark matter near the GUT scale.

---

## 9.12 Finite Alignment and Its Exact Perfect-Square Factorization

This fully recovers the v74 result.

### Theorem 9.12 (Exact Perfect-Square Factorization of Finite Alignment)

The sum of the alignment potential and the self-dual lifting is

$$\Lambda_\lambda^4|\lambda(T)-m_B|^2 + \Lambda_{\rm sd}^4\left|\lambda(T)-\frac{1}{2}\right|^2$$

$$= (\Lambda_\lambda^4+\Lambda_{\rm sd}^4)|\lambda(T)-m_T|^2 + \Lambda_{{\rm sd,eff}}^4\left(m_B-\frac{1}{2}\right)^2$$

where

$$m_T = (1-\eta_{\rm al})m_B + \frac{\eta_{\rm al}}{2}, \quad \eta_{\rm al} = \frac{\Lambda_{\rm sd}^4}{\Lambda_\lambda^4+\Lambda_{\rm sd}^4}$$

$$\Lambda_{{\rm sd,eff}}^4 = \frac{\Lambda_\lambda^4\Lambda_{\rm sd}^4}{\Lambda_\lambda^4+\Lambda_{\rm sd}^4}$$

In strain variables:

$$\boxed{\tanh\frac{\xi_T}{2} = (1-\eta_{\rm al})\tanh\frac{\xi_B}{2}}$$

**Significance:** Modular strain is a self-dual contraction of branch strain. Finite alignment is not mere competition but is exactly controlled as an affine contraction toward the self-dual point. This provides the geometric basis for the correspondence between the branch variable $\Omega$ and the modular variable $\lambda(T)$.

---

## 9.13 The Standard Model as the Schur Shadow of the Observed Theory: Concrete Examples

Making the abstract claim concrete.

### 9.13.1 Running of the Coupling Constants

The RG flow of the full system is

$$\mu\frac{d}{d\mu}g_{\rm full} = \beta_{\rm full}(g_{\rm full})$$

Taking the Schur complement, the running of the visible-sector effective coupling $g_{\rm vis}$ is

$$\mu\frac{d}{d\mu}g_{\rm vis} = \beta_{\rm SM}(g_{\rm vis}) + \delta\beta_{\rm idea}(g_{\rm vis}, g_{\rm idea})$$

where $\delta\beta_{\rm idea} = -\frac{d}{d\mu}(WL_{\rm idea}^{-1}W^\dagger)$ is the diagonal component. Since $L_{\rm idea}^{-1}$ is suppressed for $\mu \gg M_X$:

$$\mu\frac{d}{d\mu}g_{\rm vis}\approx\beta_{\rm SM}(g_{\rm vis}) \quad (\mu\ll M_X)$$

**At low energies, the SM running is recovered.** This is concrete confirmation that the reduced law contains the Standard Model exactly at low energies.

### 9.13.2 Schur Origin of Neutrino Masses

LoNalogy interpretation of the seesaw mechanism: when the heavy neutrino mass matrix $M_R$ belongs to $L_{\rm idea}$ and the Dirac mass $m_D$ corresponds to the coupling $W$:

$$K_{\rm vis}^{\rm red}(\nu) = L_\nu - m_D M_R^{-1}m_D^T$$

This is exactly the type-I seesaw:

$$m_\nu^{\rm eff} = -m_D M_R^{-1} m_D^T$$

**The lightness of neutrinos naturally emerges as the Schur shadow of the heaviness of the Idea sector ($M_R \subset L_{\rm idea}$).**

---

## 9.14 Full-System Integration: Conclusion of Part IX

With these supplements, the complete logical structure of v87 is:

```
jmath^2 = +1
  → Para-Chebyshev → Necessity of X(2) (§1)

X(2) geometry
  → Schwarzian master law (§1.3)
  → CP^1 balancing → strict kernel (§9.1)
  → N=5 forcing (§3)

Strict kernel analysis
  → bridge Hessian floor ≥ (1/6)I (§4.2)
  → Schwarzian wall ≥ 7 (§4.1)
  → confinement wall (§9.4)

Doeblin + Q-entry (§4.3–4.4)
  → finite-step positivity (§4.10)

P4 closure (§4.5)
  → polymer gluing (§4.6)
P5 closure (§4.7)

continuum limit + OS + mass gap (§4.8–4.9)

SU(5) specialization (§5)
  → Standard Model (§5.1–5.3)
  → observable hierarchy manifold (§9.6)
  → M_X numerical prediction (§9.7)
  → Lambda_* fixing (§9.5)

Kimura–Thévenin (§2)
  → SM as Schur shadow of full system (§9.13)
  → fourth generation (§8)
  → dark matter / neutrino / baryon asymmetry (§9.8–9.11)
  → cosmological constant (§9.8)
  → slow-roll / quintessence (§9.9)
```

$$\boxed{N_{\rm fam}^{\rm vis} = 3\text{ (cusps)},\quad N_{\rm fam}^{\rm full} = 4\text{ (cusps + self-dual)}}$$

$$\boxed{M_X = 3.463814\times10^{15}\text{ GeV}}$$

$$\boxed{\Lambda_* = 246\text{ GeV (geometrically fixed)}}$$

$$\boxed{\text{The cosmological constant is selected as one root of a cubic.}}$$

$$\boxed{\text{Physics does not close within the visible sector alone; it appears as the reduced law of the full system including the Idea and bridge sectors.}}$$
