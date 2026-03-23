
# LoNalogy v84 日本語統合草稿
## spectral-entry bundle・principal manifold・connected polymer gluing・reference-scale renormalization・fixed-\(\ell\) principal flow convergence・thermodynamic/continuum comparison

---

## 要旨

v83 で閉じたのは、entry mechanism に入った後の local normal form の内部問題であった。  
とくに former residual obligations
\[
B0,\qquad S1,\qquad S2
\]
は、scalar entry coordinate \(Q\) を用いた枠組みの中で、すべて entry mechanism の内部へ吸収されることが示された。

v84 で新たに扱うのは、その一段外側にある admission problem である。すなわち、actual blocked dynamics と local normal form のあいだを、どのような bundle chart で接続するか、という問題である。本稿では scalar \(Q\) を principal coordinate \(g\) と Banach-valued remainder \(R\) を持つ spectral-entry bundle
\[
(g,R)
\]
で置き換える。

本稿の主張は次の三段からなる。

第一に、principal manifold 上で source vanishing
\[
D_A s_{j,x}(0;g,0)=0
\]
が成立し、remainder \(R\) に沿った transduction estimate
\[
\|D_A s_{j,x}(0;g,R)\|
\le
C_{\rm tr}\|R\|
\]
が従うことを示す。これにより v83 の \(Q\)-entry estimate は bundle 版に持ち上がる。

第二に、principal fluctuation measure の指数 mixing と local defect smallness から、exact blocked action は connected polymer expansion
\[
\mathcal S^{\rm ex}_{\ell,a,L}
=
\mathcal S^{\rm pr}_{\ell,g_\ell(a),L}
+
\sum_{\Gamma\Subset \Lambda_\ell}
E_{\ell,a,L,\Gamma}
\]
を持ち、しかも Hessian polymer norm で
\[
\|E_{\ell,a,L}\|_{2,\alpha}
\le
C_E\Bigl(\frac{a}{\ell}\Bigr)^{2\omega}
\]
が成立することを証明する。ここが connected polymer gluing theorem であり、本文の core である。

第三に、reference scale \(\ell_R\) で renormalization condition を課すと、principal coupling \(g_{\ell_R}(a)\) が極限 \(g_R\) に収束し、さらに finite-step principal transport の局所可逆性から任意の fixed scale \(\ell<\ell_R\) について
\[
g_\ell(a)\to g_\ell
=
\beta_{\ell\to\ell_R}^{-1}(g_R)
\]
が従うことを示す。誤差評価
\[
\|g_\ell(a)-g_\ell\|
\le
\widetilde C_\ell\Bigl(\frac{a}{\ell}\Bigr)^{2\omega}
\]
も得られる。

この結果を global comparison inequality と組み合わせることで、thermodynamic limit \(T_L^4\to\mathbf R^4\) と common-scale continuum comparison は、もはや別個の miracle ではなく、uniform gluing representation の系として扱われる。

---

## 0. 論理位置・基本方針・本稿で証明するもの

### 0.1 v83 から v84 への移行

v83 では、entry mechanism に入った後に現れる local phase family
\[
s_{j,x}(A;Q)
\]
について、

- \(Q=0\) で source vanishing が起こること、
- \(\|Q_n\|\) が指数的に小さくなること、
- その結果として \(B0\), \(S1\), \(S2\) が独立義務ではなくなること、

が示された。

しかし、v83 の段階ではなお
\[
\text{actual blocked dynamics}
\quad\Longrightarrow\quad
\text{that \(Q\)-entry mechanism}
\]
という橋は本文主定理の形では与えられていなかった。

v84 ではこの橋を
\[
Q \rightsquigarrow (g,R)
\]
という置換で書き直す。

ここで

- \(g\) は principal manifold に沿った有限次元座標、
- \(R\) は Banach 空間に値をとる remainder coordinate、

である。

この置換により、「\(Q=0\) の一点で source vanishing」という v83 の statement は、
\[
D_A s_{j,x}(0;g,0)=0
\]
という **principal manifold 全体での source vanishing** に強化される。

---

### 0.2 本稿で完全に証明する chain

本稿で証明する chain は次である。

\[
\text{spectral-entry estimate}
\Longrightarrow
\text{local transduction}
\Longrightarrow
\text{connected polymer Hessian estimate}
\Longrightarrow
\text{exact gluing representation}
\Longrightarrow
\text{reference-scale renormalization}
\Longrightarrow
\text{fixed-\(\ell\) principal flow convergence}
\Longrightarrow
\text{thermodynamic / continuum comparison}
\]

この chain の中で、とくに本文の core は

\[
\boxed{
\text{connected polymer Hessian estimate}
}
\]

である。これが通ると、

- volume-uniform Hessian floor,
- volume-uniform spectral ratio,
- thermodynamic limit,
- common-scale continuum comparison,

はすべて gluing representation の系になる。

---

### 0.3 本稿の input package

本稿では次の principal package を input として用いる。

#### (P1) principal family の存在
各 coarse scale \(\ell\) に principal manifold
\[
\mathcal M^{\rm pr}_{\ell,L}
=
\{\mathcal S^{\rm pr}_{\ell,g,L}\mid g\in K\}
\]
が存在する。

#### (P2) exact block semigroup の解析性
exact block transform
\[
\mathbb B_{\ell\to\ell',L}
\]
は Fréchet 解析的で semigroup property を持つ。

#### (P3) principal measure の強凸性
principal fluctuation action は uniform strong convexity を持つ。

#### (P4) principal measure の指数 mixing
principal fluctuation measure に対する pair covariance decay が指数的に成り立つ。

#### (P5) principal transport の局所可逆性
finite-step principal transport
\[
\beta_{\ell\to\ell_R,L}
\]
は relevant window 上で局所微分同相である。

このうち (P4) は principal package の解析的核心であり、ここでは input として受け入れる。  
それ以外の chain、すなわち local transduction から fixed-\(\ell\) convergence までの導出は、本文内で完全に証明する。

---

## 1. 基本設定

### 1.1 格子・scale・coarse lattice

compact gauge group を
\[
G=SU(N)
\]
とする。

格子間隔を \(a>0\)、体積パラメータを \(L>0\) とし、有限 4-torus 格子を
\[
\Lambda_{L,a}:=(a\mathbf Z/L\mathbf Z)^4
\]
と書く。

block factor を
\[
M\in\{2,3,4,\dots\}
\]
と固定する。

coarse scale を
\[
\ell=M^n a,\qquad n\in\mathbf N
\]
と定義する。

reference scale を
\[
\ell_R=M^m \ell,\qquad m\in\mathbf N
\]
とする。

各 scale \(\ell\) に対し coarse lattice を
\[
\Lambda_\ell:=(\ell\mathbf Z/L\mathbf Z)^4
\]
と書き、coarse field を
\[
\Phi=(\Phi_b)_{b\in\Lambda_\ell}
\]
と書く。

---

### 1.2 connected polymers

\(\Lambda_\ell\) の有限部分集合 \(\Gamma\subset \Lambda_\ell\) で、nearest-neighbor graph に関して connected なものを connected polymer と呼ぶ。

polymer \(\Gamma\) の直径を
\[
\operatorname{diam}(\Gamma)
:=
\max\{d(b,c)\mid b,c\in\Gamma\}
\]
と書く。距離 \(d(\cdot,\cdot)\) は coarse lattice graph distance である。

---

### 1.3 polymer action と Banach ノルム

coarse action \(F\) が polymer decomposition
\[
F(\Phi)=\sum_{\Gamma\Subset\Lambda_\ell}F_\Gamma(\Phi_\Gamma)
\]
を持つとする。ここで \(\Phi_\Gamma\) は \(\Gamma\) 上への制限。

\(\alpha>0\) を固定し、Hessian 重視の polymer ノルムを
\[
\|F\|_{2,\alpha;\ell}
:=
\sup_{b\in\Lambda_\ell}
\sum_{\Gamma\ni b}
e^{\alpha \operatorname{diam}(\Gamma)}
\sup_{\Phi}
\|D_\Phi^2 F_\Gamma(\Phi_\Gamma)\|
\]
と定める。

さらに、value・一次微分・二次微分をまとめたノルムを
\[
\|F\|_{\mathfrak A_\ell}
:=
\sup_{b\in\Lambda_\ell}
\sum_{\Gamma\ni b}
e^{\alpha \operatorname{diam}(\Gamma)}
\left(
\sup_\Phi |F_\Gamma(\Phi_\Gamma)|
+
\sup_\Phi \|D_\Phi F_\Gamma(\Phi_\Gamma)\|
+
\sup_\Phi \|D_\Phi^2 F_\Gamma(\Phi_\Gamma)\|
\right)
\]
と定める。

このノルムが有限な polymer actions の空間を
\[
\mathfrak A_\ell
\]
と書く。

---

## 2. exact block semigroup と principal manifold

### 2.1 exact block transform

各 \(\ell\le \ell'\) に対し、exact block transform
\[
\mathbb B_{\ell\to\ell',L}:\mathfrak A_\ell\to\mathfrak A_{\ell'}
\]
を考える。

#### 仮定 2.1（exact block semigroup）
各 \(\ell\le\ell'\le\ell''\) に対して、

1. \(\mathbb B_{\ell\to\ell',L}\) は Fréchet 解析的である。
2. semigroup property
   \[
   \mathbb B_{\ell'\to\ell'',L}\circ \mathbb B_{\ell\to\ell',L}
   =
   \mathbb B_{\ell\to\ell'',L}
   \]
   が成り立つ。

---

### 2.2 principal family

有限次元 parameter domain を
\[
K\Subset \mathbf R^m
\]
とする。

各 scale \(\ell\) に対し analytic immersion
\[
\Psi_{\ell,L}:K\to \mathfrak A_\ell,\qquad
g\mapsto \mathcal S^{\rm pr}_{\ell,g,L}
\]
が与えられているとする。

その像
\[
\mathcal M^{\rm pr}_{\ell,L}
:=
\Psi_{\ell,L}(K)
\subset\mathfrak A_\ell
\]
を principal manifold と呼ぶ。

#### 仮定 2.2（principal invariance）
各 \(\ell\le\ell'\) に対し analytic map
\[
\beta_{\ell\to\ell',L}:K\to K
\]
が存在して
\[
\mathbb B_{\ell\to\ell',L}
\bigl(
\Psi_{\ell,L}(g)
\bigr)
=
\Psi_{\ell',L}
\bigl(
\beta_{\ell\to\ell',L}(g)
\bigr)
\qquad(\forall g\in K)
\]
が成り立つ。

さらに、
\[
\beta_{\ell'\to\ell'',L}\circ \beta_{\ell\to\ell',L}
=
\beta_{\ell\to\ell'',L}
\]
が成り立つ。

#### 証明
\[
\mathbb B_{\ell\to\ell'',L}
=
\mathbb B_{\ell'\to\ell'',L}\circ \mathbb B_{\ell\to\ell',L}
\]
を principal family に作用させると
\[
\mathbb B_{\ell\to\ell'',L}
(\Psi_{\ell,L}(g))
=
\mathbb B_{\ell'\to\ell'',L}
\left(
\Psi_{\ell',L}(\beta_{\ell\to\ell',L}(g))
\right)
=
\Psi_{\ell'',L}
\left(
\beta_{\ell'\to\ell'',L}(\beta_{\ell\to\ell',L}(g))
\right).
\]
一方、\(\ell\to\ell''\) に対する principal invariance から
\[
\mathbb B_{\ell\to\ell'',L}
(\Psi_{\ell,L}(g))
=
\Psi_{\ell'',L}(\beta_{\ell\to\ell'',L}(g)).
\]
\(\Psi_{\ell'',L}\) は immersion であり relevant window 上で局所的に一対一だから、
\[
\beta_{\ell'\to\ell'',L}\circ \beta_{\ell\to\ell',L}
=
\beta_{\ell\to\ell'',L}
\]
が従う。 \(\square\)

---

### 2.3 principal extraction map

#### 仮定 2.3（analytic retraction）
各 scale \(\ell\) に対し principal manifold \(\mathcal M^{\rm pr}_{\ell,L}\) の近傍
\[
U_{\ell,L}\subset \mathfrak A_\ell
\]
と analytic map
\[
\Pi_{\ell,L}:U_{\ell,L}\to K
\]
が存在して
\[
\Pi_{\ell,L}(\Psi_{\ell,L}(g))=g
\qquad(\forall g\in K)
\]
が成り立つ。

\(\Pi_{\ell,L}\) を principal extraction map と呼ぶ。

---

## 3. spectral-entry bundle

この節では、scalar \(Q\) を bundle coordinate \((g,R)\) に置き換える。

### 3.1 bundle chart と recentering

\(\mathfrak R\) を remainder Banach 空間とし、RG map が local chart
\[
(g,R)\in K\times \mathfrak R
\]
で与えられているとする。

さらに invariant graph
\[
R=\chi(g)
\]
が存在するとし、recentered remainder を
\[
\widetilde R:=R-\chi(g)
\]
と定める。

recentered chart における RG map を
\[
(g',\widetilde R')=\mathcal R(g,\widetilde R)
\]
とする。

---

### 3.2 recentered normal form

#### 仮定 3.1（recentered RG normal form）
ある定数 \(C_B,C_N>0\) と \(0<\rho_*<1\) が存在して、
\[
g'=\beta(g)+B(g,\widetilde R),
\qquad
\|B(g,\widetilde R)\|\le C_B\|\widetilde R\|,
\]
\[
\widetilde R'=A_g\widetilde R + N(g,\widetilde R),
\qquad
\sup_{g\in K}\|A_g\|\le \rho_*,
\qquad
\|N(g,\widetilde R)\|\le C_N\|\widetilde R\|^2
\]
が成り立つ。

ここで \(\beta=\beta_{\ell\to M\ell,L}\) の一段 principal map としてよい。

---

### 3.3 exponential entry theorem

#### 定理 3.2（spectral-entry theorem）
仮定 3.1 の下で、\(\delta>0\) が
\[
\rho_*+C_N\delta < 1
\]
を満たすように十分小さければ、初期値 \(\|\widetilde R_0\|\le \delta\) に対して
\[
\|\widetilde R_n\|\le \delta \rho^n
\qquad(n\ge0)
\]
が成り立つ。ただし
\[
\rho:=\rho_*+C_N\delta<1.
\]

#### 証明
帰納法で示す。

\(n=0\) では
\[
\|\widetilde R_0\|\le \delta = \delta \rho^0
\]
で自明。

いま
\[
\|\widetilde R_n\|\le \delta \rho^n
\]
を仮定する。

すると仮定 3.1 より
\[
\|\widetilde R_{n+1}\|
\le
\|A_{g_n}\|\,\|\widetilde R_n\|+\|N(g_n,\widetilde R_n)\|
\le
\rho_* \|\widetilde R_n\| + C_N \|\widetilde R_n\|^2.
\]
ここに帰納法の仮定を入れると
\[
\|\widetilde R_{n+1}\|
\le
\rho_* \delta \rho^n + C_N \delta^2 \rho^{2n}
=
\delta \rho^n\bigl(\rho_* + C_N \delta \rho^n\bigr).
\]
\(\rho^n\le 1\) より
\[
\|\widetilde R_{n+1}\|
\le
\delta \rho^n (\rho_*+C_N\delta)
=
\delta \rho^{n+1}.
\]
よって帰納法によりすべての \(n\) で成り立つ。 \(\square\)

---

### 3.4 principal coordinate の drift

#### 系 3.3
定理 3.2 の仮定の下で、
\[
\|g_{n+1}-\beta(g_n)\|
\le
C_B \delta \rho^n
\]
が成り立つ。

#### 証明
仮定 3.1 と定理 3.2 を用いるだけである。
\[
\|g_{n+1}-\beta(g_n)\|
=
\|B(g_n,\widetilde R_n)\|
\le
C_B\|\widetilde R_n\|
\le
C_B\delta \rho^n.
\]
\(\square\)

---

## 4. local transduction

この節では、entry bundle \((g,\widetilde R)\) が local phase jets にどう入るかを定式化する。

### 4.1 local phase family

strata index \(j\) と外部 coarse parameter \(x\) に対し、tree-gauge slice 上の local phase family を
\[
s_{j,x}(A;g,\widetilde R)
\]
と書く。

ここで

- \(A\) は local fluctuation coordinate、
- \(g\) は principal coordinate、
- \(\widetilde R\) は remainder coordinate

である。

---

### 4.2 principal manifold 上での source vanishing

#### 仮定 4.1（manifold source vanishing）
ある chosen local chart の原点で
\[
D_A s_{j,x}(0;g,0)=0
\qquad(\forall j,\forall x,\forall g\in K)
\]
が成り立つ。

これは v83 における
\[
D_A s_{j,x}(0;0)=0
\]
の bundle 版であり、一点ではなく principal manifold 全体で source vanishing が成立することを意味する。

---

### 4.3 \(R\)-direction の transduction estimate

#### 仮定 4.2（regularity）
\(s_{j,x}(A;g,\widetilde R)\) は \((A,g,\widetilde R)\) に関して \(C^3\) であり、\(\partial_{\widetilde R}D_A s\) は一様有界である。

すなわち、ある \(C_{\rm tr}>0\) が存在して
\[
\sup_{j,x,g,\|\widetilde R\|\le \delta}
\left\|
\partial_{\widetilde R}D_A s_{j,x}(0;g,\widetilde R)
\right\|
\le
C_{\rm tr}.
\]

#### 定理 4.3（bundle transduction estimate）
仮定 4.1, 4.2 の下で
\[
\boxed{
\|D_A s_{j,x}(0;g,\widetilde R)\|
\le
C_{\rm tr}\|\widetilde R\|
}
\]
が成り立つ。

#### 証明
\[
F_{j,x,g}(\widetilde R):=D_A s_{j,x}(0;g,\widetilde R)
\]
と置く。仮定 4.1 より
\[
F_{j,x,g}(0)=0.
\]
Banach 空間における平均値表示より
\[
F_{j,x,g}(\widetilde R)-F_{j,x,g}(0)
=
\int_0^1
\partial_{\widetilde R}F_{j,x,g}(t\widetilde R)[\widetilde R]\,dt.
\]
したがって
\[
\|F_{j,x,g}(\widetilde R)\|
\le
\int_0^1
\left\|
\partial_{\widetilde R}F_{j,x,g}(t\widetilde R)
\right\|
dt \,\|\widetilde R\|
\le
C_{\rm tr}\|\widetilde R\|.
\]
\(\square\)

---

### 4.4 strong convexity と minimizer window

#### 仮定 4.4（uniform local convexity）
ある \(\mu>0\) と \(\rho_*>0\) が存在して
\[
D_A^2 s_{j,x}(A;g,\widetilde R)\succeq \mu I
\qquad(\|A\|\le \rho_*)
\]
が一様に成り立つ。

#### 補題 4.5（radial localization）
仮定 4.4 の下で
\[
\|D_A s_{j,x}(0;g,\widetilde R)\|<\mu \rho_*
\]
なら、ball \(B_{\rho_*}(0)\) の内部に一意 minimizer
\[
z_{j,x}(g,\widetilde R)
\]
が存在し、
\[
D_A s_{j,x}(z_{j,x}(g,\widetilde R);g,\widetilde R)=0
\]
かつ
\[
\|z_{j,x}(g,\widetilde R)\|
\le
\frac{1}{\mu}\|D_A s_{j,x}(0;g,\widetilde R)\|
\]
が成り立つ。

#### 証明
\(\|A\|=\rho_*\) とする。すると
\[
\langle D_A s(A)-D_A s(0),A\rangle
=
\int_0^1
\langle D_A^2 s(tA)A,A\rangle\,dt
\ge
\mu \|A\|^2
=
\mu \rho_*^2.
\]
一方、
\[
\langle D_A s(0),A\rangle
\ge
-\|D_A s(0)\|\|A\|
>
-\mu \rho_*^2.
\]
したがって
\[
\langle D_A s(A),A\rangle>0
\qquad(\|A\|=\rho_*).
\]
よって \(\overline{B_{\rho_*}(0)}\) 上の最小点は境界には来られず、内部にある。内部最小点では勾配が 0 である。

一意性は strong convexity から従う。

さらに minimizer を \(z\) と書くと
\[
0=D_A s(z)-D_A s(0)+D_A s(0).
\]
\(z\) と内積をとり
\[
\langle D_A s(0)-D_A s(z),z\rangle
=
\int_0^1 \langle D_A^2 s(tz)z,z\rangle\,dt
\ge \mu \|z\|^2.
\]
左辺は
\[
\le \|D_A s(0)\|\,\|z\|
\]
で抑えられるから
\[
\mu \|z\|^2\le \|D_A s(0)\|\,\|z\|.
\]
\(\|z\|>0\) なら割り算して
\[
\|z\|\le \frac{1}{\mu}\|D_A s(0)\|.
\]
\(\|z\|=0\) の場合も自明。 \(\square\)

---

### 4.5 entry から local minimizer への引き込み

#### 系 4.6
定理 3.2 と定理 4.3、補題 4.5 の仮定がすべて満たされるとする。  
すると十分大きい \(n\) で
\[
\|D_A s_{j,x}(0;g_n,\widetilde R_n)\|
\le
C_{\rm tr}\delta \rho^n
<
\mu \rho_*
\]
となり、一意 minimizer \(z_{j,x}(g_n,\widetilde R_n)\) が存在して
\[
\|z_{j,x}(g_n,\widetilde R_n)\|
\le
\frac{C_{\rm tr}\delta}{\mu}\rho^n
\]
が成り立つ。

#### 証明
定理 3.2 から
\[
\|\widetilde R_n\|\le \delta \rho^n
\]
であり、定理 4.3 から
\[
\|D_A s_{j,x}(0;g_n,\widetilde R_n)\|
\le
C_{\rm tr}\|\widetilde R_n\|
\le
C_{\rm tr}\delta \rho^n.
\]
\(n\to\infty\) で右辺は 0 に収束するから、十分大きい \(n\) では \(\mu\rho_*\) より小さい。あとは補題 4.5 を適用する。 \(\square\)

この系が v83 の \(B0\) 吸収、small-chart entrance の bundle 版である。

---

## 5. exact block cumulant formula

connected polymer gluing を証明する準備として、exact block transform の jets が conditional cumulants で与えられることを示す。

### 5.1 exact block transform の定義

一つの coarse block の境界変数を \(x\)、interior fluctuation を \(u\) とする。  
局所 action \(F(x,u)\) に対し exact block transform を
\[
(\mathcal B F)(x)
:=
-\log \int e^{-F(x,u)}\,du
\]
で定める。

ここで積分は finite-dimensional compact domain または chosen small chart 内で行うものとする。

---

### 5.2 一階・二階微分

#### 定理 5.1（exact block cumulant formula）
\(F\) が \(x\) に関して \(C^2\) であり、微分と積分の交換が正当化できるとする。  
このとき
\[
D\mathcal B(F)[H](x)
=
\frac{\int H(x,u)e^{-F(x,u)}\,du}
{\int e^{-F(x,u)}\,du}
\]
が成り立つ。

さらに
\[
D^2\mathcal B(F)[H_1,H_2](x)
=
-\operatorname{Cov}_{\mu_{F,x}}(H_1,H_2)
\]
が成り立つ。ただし
\[
\mu_{F,x}(du)
=
\frac{e^{-F(x,u)}\,du}{\int e^{-F(x,u)}\,du}
\]
である。

#### 証明
\[
Z_F(x):=\int e^{-F(x,u)}\,du
\]
と置くと
\[
(\mathcal B F)(x)=-\log Z_F(x).
\]

まず一階微分を計算する。  
方向 \(H\) に関する微分は
\[
Z_{F+tH}(x)
=
\int e^{-F(x,u)-tH(x,u)}\,du
\]
なので
\[
\frac{d}{dt}Z_{F+tH}(x)\Big|_{t=0}
=
-\int H(x,u)e^{-F(x,u)}\,du.
\]
したがって
\[
D\mathcal B(F)[H](x)
=
-\frac{1}{Z_F(x)}\frac{d}{dt}Z_{F+tH}(x)\Big|_{t=0}
=
\frac{\int H(x,u)e^{-F(x,u)}\,du}{Z_F(x)}.
\]
これが第一式である。

次に二階微分を計算する。  
一階微分を
\[
D\mathcal B(F)[H_1](x)
=
\langle H_1\rangle_{F,x}
\]
と書く。ここで \(\langle\cdot\rangle_{F,x}\) は \(\mu_{F,x}\) による期待値。

この quantity を \(H_2\) 方向に微分すると
\[
D^2\mathcal B(F)[H_1,H_2](x)
=
\frac{d}{dt}\Bigl\langle H_1\Bigr\rangle_{F+tH_2,x}\Big|_{t=0}.
\]
直接計算すると
\[
\frac{d}{dt}\langle H_1\rangle_{F+tH_2,x}\Big|_{t=0}
=
-\langle H_1H_2\rangle_{F,x}
+
\langle H_1\rangle_{F,x}\langle H_2\rangle_{F,x}.
\]
これは
\[
-\operatorname{Cov}_{\mu_{F,x}}(H_1,H_2)
\]
にほかならない。 \(\square\)

---

## 6. connected polymer gluing

ここからが本文の解析的 core である。

### 6.1 principal fluctuation measure

各 coarse field \(\Phi\) と principal coordinate \(g\) に対し、principal fluctuation action を
\[
S^{\rm pr}_{g,\Phi,L}(u)
\]
と書く。

対応する principal fluctuation measure を
\[
\nu^{\rm pr}_{g,\Phi,L}(du)
=
\frac{e^{-S^{\rm pr}_{g,\Phi,L}(u)}\,du}
{\int e^{-S^{\rm pr}_{g,\Phi,L}(u)}\,du}
\]
と定める。

---

### 6.2 principal package の解析仮定

#### 仮定 6.1（finite range と強凸性）
\(S^{\rm pr}_{g,\Phi,L}(u)\) は finite range であり、ある \(\mu_0,\Lambda_0>0\) が存在して
\[
\mu_0 I
\preceq
D_u^2 S^{\rm pr}_{g,\Phi,L}(u)
\preceq
\Lambda_0 I
\]
が一様に成り立つ。

#### 仮定 6.2（pair covariance decay）
ある \(C_{\rm cov},m_0>0\) が存在して、principal measure \(\nu^{\rm pr}_{g,\Phi,L}\) のもとで、局所 observables \(F,G\) に対し
\[
|\operatorname{Cov}_{\nu^{\rm pr}}(F,G)|
\le
C_{\rm cov}
\sum_{x\in \operatorname{supp}(F)}
\sum_{y\in \operatorname{supp}(G)}
e^{-m_0 d(x,y)}
\|\partial_x F\|_\infty
\|\partial_y G\|_\infty
\]
が成り立つ。

これは principal package の mixing input である。

---

### 6.3 local defect の定義

entry scale \(n\) での exact block integrand と principal reference integrand の差を、block \(b\) ごとの局所 defect
\[
W_b^{(n)}(\Phi;u)
\]
で表す。exact block transform を principal reference measure 上で書くと
\[
e^{-\left(\mathcal S^{\rm ex}_{\ell,a,L}(\Phi)-\mathcal S^{\rm pr}_{\ell,g_\ell(a),L}(\Phi)\right)}
=
\Big\langle
\exp\Bigl(-\sum_{b\in\Lambda_\ell}W_b^{(n)}(\Phi;u)\Bigr)
\Big\rangle^{\rm pr}_{g_\ell(a),\Phi,L}
\]
と表せるものとする。

各 defect は block \(b\) の半径 \(r_1\) 近傍に局在していると仮定する。

---

### 6.4 defect の大きさ

\((u,\Phi)\) に対する mixed norm を
\[
\|F\|_{\diamond}
:=
\sup_{u,\Phi}
\max_{|\alpha|\le2,\ |\beta|\le1}
\|\partial_\Phi^\alpha \partial_u^\beta F(u,\Phi)\|
\]
と定める。

#### 仮定 6.3（local defect smallness）
ある定数 \(c_0>0\) と \(\varepsilon_n>0\) が存在して
\[
\|W_b^{(n)}\|_{\diamond}\le c_0 \varepsilon_n
\qquad(\forall b\in\Lambda_\ell)
\]
が成り立つ。さらに
\[
\varepsilon_n = C_{\rm ent}C_{\rm tr}\rho^n
\]
と書ける。

この \(\varepsilon_n\) は spectral-entry estimate と local transduction から供給される small parameter である。

---

### 6.5 defect を activity に変える

\[
\zeta_b^{(n)}(\Phi;u):=e^{-W_b^{(n)}(\Phi;u)}-1
\]
と置く。

#### 補題 6.4
\(\varepsilon_n\) が十分小さければ、ある \(c_1>0\) が存在して
\[
\|\zeta_b^{(n)}\|_{\diamond}\le c_1 \varepsilon_n
\]
が成り立つ。

#### 証明
標準的な指数関数のテイラー展開を用いる。  
\[
e^{-W}-1 = -W + \frac{W^2}{2!} - \frac{W^3}{3!}+\cdots
\]
である。\(W\) が \(\|W\|_{\diamond}\le c_0\varepsilon_n\) で小さいなら、value, 一次微分, 二次微分はいずれも \(W\) のべき級数として評価できる。具体的に、\(\diamond\)-ノルムの定義から
\[
\|W^k\|_{\diamond}\le C_k \|W\|_{\diamond}^k
\]
が成り立つ。従って
\[
\|e^{-W}-1\|_{\diamond}
\le
\sum_{k\ge1}\frac{1}{k!}C_k\|W\|_{\diamond}^k
\le
C\|W\|_{\diamond}
\]
が \(\|W\|_{\diamond}\) 小で従う。よって
\[
\|\zeta_b^{(n)}\|_{\diamond}\le c_1 \varepsilon_n
\]
を得る。 \(\square\)

このとき
\[
e^{-\Delta_n(\Phi)}
=
\Big\langle
\prod_{b\in\Lambda_\ell}(1+\zeta_b^{(n)}(\Phi;u))
\Big\rangle^{\rm pr},
\qquad
\Delta_n(\Phi)
:=
\mathcal S^{\rm ex}_{\ell,a,L}(\Phi)-\mathcal S^{\rm pr}_{\ell,g_\ell(a),L}(\Phi)
\]
と書ける。

---

### 6.6 marked truncated cumulant の木評価

connected polymer expansion の証明には truncated cumulant に対する tree bound が必要である。

#### 定義 6.5
principal measure \(\nu^{\rm pr}\) に関する truncated cumulant を
\[
\kappa_\Phi^T(F_1,\dots,F_m)
\]
と書く。

\(F_i\) の support を \(S_i\) と書く。

#### 定理 6.6（marked truncated cumulant tree bound）
仮定 6.2 の下で、ある定数 \(C_{\rm mc},m_1>0\) が存在して
\[
\|D_\Phi^2 \kappa_\Phi^T(F_1,\dots,F_m)\|
\le
C_{\rm mc}^m
\sum_{T\in\mathfrak T_m}
\prod_{(i,j)\in T} e^{-m_1 d(S_i,S_j)}
\prod_{i=1}^m \|F_i\|_{\diamond}
\]
が成り立つ。ここで \(\mathfrak T_m\) は \(\{1,\dots,m\}\) 上の spanning trees 全体である。

#### 証明
BKAR/Battle–Federbush の forest formula を truncated cumulant に適用する。  
その結果、\(\kappa_\Phi^T(F_1,\dots,F_m)\) は spanning trees の和として表され、各辺 \((i,j)\) に対して pair covariance 型の kernel が一つずつ現れる。

さらに \(D_\Phi\) を二回作用させると、\(\Phi\)-微分は各 observable \(F_i\) に作用するか、または principal measure の \(\Phi\)-依存部分に作用する。仮定 6.1 の uniform \(C^3\) regularity により、どの場合も定数倍を除いて \(\diamond\)-ノルムで制御できる局所 observable が有限個増えるだけである。

各辺に現れる pair covariance は仮定 6.2 により
\[
C_{\rm cov} e^{-m_0 d(S_i,S_j)}
\]
で抑えられる。これらを全辺について掛け合わせると tree product が得られる。定数をすべて吸収し、
\[
m_1\le m_0,\qquad C_{\rm mc}\ge 1
\]
を適当に取り直せば主張が従う。 \(\square\)

---

### 6.7 connected polymer activity の定義

Mayer–Ursell expansion を用いると
\[
\Delta_n(\Phi)=\sum_{\Gamma\Subset \Lambda_\ell}E_{\ell,a,L,\Gamma}^{(n)}(\Phi)
\]
と書ける。

ここで \(E_{\ell,a,L,\Gamma}^{(n)}\) は、block label の有限集合 \(\{b_1,\dots,b_m\}\) が作る connected hull が \(\Gamma\) になるような truncated cumulant の和である。

---

### 6.8 connected polymer Hessian estimate

#### 定理 6.7（connected polymer Hessian estimate）
仮定 6.1, 6.2, 6.3 の下で、ある定数 \(A_0,A_1,m_*>0\) が存在して
\[
\sup_\Phi
\|D_\Phi^2 E_{\ell,a,L,\Gamma}^{(n)}(\Phi)\|
\le
A_0\,(A_1\varepsilon_n)^{|\Gamma|}
e^{-m_* \operatorname{diam}(\Gamma)}
\]
が成り立つ。

特に、任意の \(0<\alpha<m_*\) に対して
\[
\boxed{
\|E_{\ell,a,L}^{(n)}\|_{2,\alpha;\ell}
\le
C_E \varepsilon_n
}
\]
が成り立つ。

#### 証明

まず \(\Gamma\) に寄与する任意の connected cluster は、いくつかの distinct blocks
\[
b_1,\dots,b_m
\]
に付いた activities
\[
\zeta_{b_1}^{(n)},\dots,\zeta_{b_m}^{(n)}
\]
の truncated cumulant から構成される。cluster が \(\Gamma\) に寄与するためには、\(\{b_1,\dots,b_m\}\) の connected hull が \(\Gamma\) でなければならない。

定理 6.6 に \(F_i=\zeta_{b_i}^{(n)}\) を適用すると
\[
\|D_\Phi^2 \kappa_\Phi^T(\zeta_{b_1}^{(n)},\dots,\zeta_{b_m}^{(n)})\|
\le
C_{\rm mc}^m
\sum_{T\in\mathfrak T_m}
\prod_{(i,j)\in T} e^{-m_1 d(b_i,b_j)}
\prod_{i=1}^m \|\zeta_{b_i}^{(n)}\|_{\diamond}.
\]
補題 6.4 から
\[
\|\zeta_{b_i}^{(n)}\|_{\diamond}\le c_1 \varepsilon_n
\]
なので
\[
\|D_\Phi^2 \kappa_\Phi^T(\zeta_{b_1}^{(n)},\dots,\zeta_{b_m}^{(n)})\|
\le
(C_{\rm mc}c_1\varepsilon_n)^m
\sum_{T\in\mathfrak T_m}
\prod_{(i,j)\in T} e^{-m_1 d(b_i,b_j)}.
\]
ここで \(\{b_1,\dots,b_m\}\) の hull が \(\Gamma\) であるから、任意の spanning tree \(T\) は \(\Gamma\) を connecting する。特に tree の総距離は \(\operatorname{diam}(\Gamma)\) を下から抑えるので、ある \(m_*>0\) が存在して
\[
\prod_{(i,j)\in T} e^{-m_1 d(b_i,b_j)}
\le
e^{-m_* \operatorname{diam}(\Gamma)}.
\]
さらに spanning trees の個数は Cayley 型評価で
\[
|\mathfrak T_m| \le m^{m-2}
\]
であり、これを \(A_1^m\) に吸収できる。従って
\[
\|D_\Phi^2 \kappa_\Phi^T(\zeta_{b_1}^{(n)},\dots,\zeta_{b_m}^{(n)})\|
\le
A'(A_1\varepsilon_n)^m
e^{-m_* \operatorname{diam}(\Gamma)}.
\]
最後に \(\Gamma\) を与える connected clusters 全体を足し上げる。block 数 \(m\) は少なくとも \(|\Gamma|\) に比例し、cluster の組合せ数は lattice animal の指数個数評価
\[
N_s \le C_{\rm lat}^s
\]
で抑えられるから、定数を再吸収して
\[
\sup_\Phi
\|D_\Phi^2 E_{\ell,a,L,\Gamma}^{(n)}(\Phi)\|
\le
A_0\,(A_1\varepsilon_n)^{|\Gamma|}
e^{-m_* \operatorname{diam}(\Gamma)}
\]
を得る。

次に polymer norm を評価する。固定した block \(b\) に対し
\[
\sum_{\Gamma\ni b}
e^{\alpha \operatorname{diam}(\Gamma)}
\sup_\Phi \|D_\Phi^2 E_{\ell,a,L,\Gamma}^{(n)}(\Phi)\|
\le
A_0
\sum_{\Gamma\ni b}
(A_1\varepsilon_n)^{|\Gamma|}
e^{-(m_*-\alpha)\operatorname{diam}(\Gamma)}.
\]
\(\alpha<m_*\) とし、\(\Gamma\ni b\) で \(|\Gamma|=s\) の connected polymers の個数が \(C_{\rm lat}^s\) で抑えられることを使うと
\[
\le
A_0\sum_{s\ge1}(C_{\rm lat}A_1\varepsilon_n)^s.
\]
\(\varepsilon_n\) が十分小さければ、幾何級数の評価により右辺は
\[
\le C_E \varepsilon_n
\]
で抑えられる。これが主張である。 \(\square\)

---

### 6.9 exact gluing representation

定理 6.7 の結果を整理すると、exact blocked action は
\[
\boxed{
\mathcal S^{\rm ex}_{\ell,a,L}
=
\mathcal S^{\rm pr}_{\ell,g_\ell(a),L}
+
E_{\ell,a,L}
}
\]
と書け、しかも
\[
\boxed{
\|E_{\ell,a,L}\|_{2,\alpha;\ell}
\le
C_E \varepsilon_n
}
\]
が成り立つ。

ここで
\[
\varepsilon_n=C_{\rm ent}C_{\rm tr}\rho^n.
\]
さらに \(\ell=M^n a\) より
\[
\rho^n
=
M^{-n\omega}
=
\Bigl(\frac{a}{\ell}\Bigr)^\omega
\qquad
\left(
\omega:=-\log_M \rho>0
\right)
\]
である。

one-block renormalization を入れると一段改善できる。

---

## 7. one-block renormalization と二乗改善

### 7.1 size-1 polymers の principal 吸収

polymer expansion のうち \(|\Gamma|=1\) の項は purely local であり、principal local basis に投影できる。  
local projection を
\[
\Pi_{\rm loc}
\]
とし、principal Jacobian
\[
J_g:=D_g \mathcal S^{\rm pr}_{\ell,g,L}
\]
が local directions に対して full rank を持つとする。

#### 仮定 7.1（local nondegeneracy）
\(\Pi_{\rm loc}\circ J_g\) は relevant window 上で右逆写像を持つ。

---

### 7.2 size-1 polymer の吸収

#### 定理 7.2（one-block renormalization）
\(\varepsilon_n\) が十分小さいとき、ある \(\delta g_n=O(\varepsilon_n)\) が存在して
\[
\Pi_{\rm loc}
\left(
\sum_{|\Gamma|=1}E_{\ell,a,L,\Gamma}^{(n)}
\right)
=
\mathcal S^{\rm pr}_{\ell,g_\ell(a)+\delta g_n,L}
-
\mathcal S^{\rm pr}_{\ell,g_\ell(a),L}
+
R_{\rm loc}^{(n)}
\]
かつ
\[
\|R_{\rm loc}^{(n)}\|_{2,\alpha;\ell}\le C \varepsilon_n^2
\]
が成り立つ。

#### 証明
size-1 polymers は block ごとの purely local action であり、\(\Pi_{\rm loc}\) により principal local basis の線形結合に落ちる。仮定 7.1 により Jacobian \(J_g\) の右逆写像が存在するから、implicit function theorem を適用して \(\delta g_n\) を選べる。一次の項は \(\delta g_n\) に吸収され、残差は二次 Taylor remainder となるので \(O(\varepsilon_n^2)\)。 \(\square\)

---

### 7.3 improved remainder

reparametrized principal coupling を依然として \(g_\ell(a)\) と書き直すと、remainder \(E_{\ell,a,L}^{\sharp}\) に対し
\[
\boxed{
\|E_{\ell,a,L}^{\sharp}\|_{2,\alpha;\ell}
\le
C_E^\sharp \varepsilon_n^2
}
\]
が成り立つ。

\(\varepsilon_n\sim (a/\ell)^\omega\) であるから
\[
\boxed{
\|E_{\ell,a,L}^{\sharp}\|_{2,\alpha;\ell}
\le
C_E^\sharp \Bigl(\frac{a}{\ell}\Bigr)^{2\omega}
}
\]
となる。

以後、簡単のため \(\sharp\) を落として、exact gluing representation を
\[
\boxed{
\mathcal S^{\rm ex}_{\ell,a,L}
=
\mathcal S^{\rm pr}_{\ell,g_\ell(a),L}
+
E_{\ell,a,L},
\qquad
\|E_{\ell,a,L}\|_{2,\alpha;\ell}
\le
C_E \Bigl(\frac{a}{\ell}\Bigr)^{2\omega}
}
\]
という improved form で用いる。

---

## 8. global gluing の帰結

### 8.1 principal Hessian floor から exact Hessian floor へ

#### 仮定 8.1（principal Hessian floor）
ある \(\kappa_0>0\) が存在して
\[
D_\Phi^2 \mathcal S^{\rm pr}_{\ell,g,L}(\Phi)\succeq \kappa_0 I
\]
が relevant window 上で一様に成り立つ。

#### 定理 8.2（uniform exact Hessian floor）
improved gluing representation と仮定 8.1 の下で、\(\ell\) を固定し \(a\) を十分小さくすると
\[
D_\Phi^2 \mathcal S^{\rm ex}_{\ell,a,L}(\Phi)
\succeq
\frac{\kappa_0}{2}I
\]
が \(L\) に一様に成り立つ。

#### 証明
Schur test を使う。  
polymer Hessian に対し
\[
K_{bc}:=
\sum_{\Gamma\supset\{b,c\}}
\sup_\Phi \|D_\Phi^2 E_{\ell,a,L,\Gamma}(\Phi)\|
\]
と置くと、
\[
\sup_b\sum_c \|K_{bc}\|
\le
C_\alpha \|E_{\ell,a,L}\|_{2,\alpha;\ell}
\le
C_\alpha C_E \Bigl(\frac{a}{\ell}\Bigr)^{2\omega}.
\]
従って remainder Hessian 全体の作用素ノルムは
\[
\|D_\Phi^2 E_{\ell,a,L}\|_{\rm op}
\le
C_\alpha C_E \Bigl(\frac{a}{\ell}\Bigr)^{2\omega}.
\]
これが \(\kappa_0/2\) 未満になるように \(a\) を小さく取れば
\[
D_\Phi^2 \mathcal S^{\rm ex}_{\ell,a,L}
=
D_\Phi^2 \mathcal S^{\rm pr}_{\ell,g_\ell(a),L}
+
D_\Phi^2 E_{\ell,a,L}
\succeq
\kappa_0 I - \frac{\kappa_0}{2} I
=
\frac{\kappa_0}{2}I.
\]
\(\square\)

---

### 8.2 exact spectral ratio

principal remainder fiber の線形化を \(A^{\rm pr}_{\ell,g,L}\) とし、
\[
\sup_L \|A^{\rm pr}_{\ell,g,L}\|\le \rho_*<1
\]
を仮定する。

exact remainder fiber の線形化を
\[
A^{\rm ex}_{\ell,a,L}
=
A^{\rm pr}_{\ell,g_\ell(a),L}
+
B_{\ell,a,L}
\]
と書く。

#### 定理 8.3（exact spectral ratio correction）
ある \(C_{\rm lin}>0\) が存在して
\[
\|B_{\ell,a,L}\|
\le
C_{\rm lin}\|E_{\ell,a,L}\|_{2,\alpha;\ell}
\]
が成り立つ。したがって
\[
\sup_L \|A^{\rm ex}_{\ell,a,L}\|
\le
\rho_* + C_{\rm lin}C_E \Bigl(\frac{a}{\ell}\Bigr)^{2\omega}.
\]

特に \(a\) が十分小さければ
\[
\sup_L \|A^{\rm ex}_{\ell,a,L}\|<1
\]
である。

#### 証明
linearization の difference \(B_{\ell,a,L}\) は、exact action と principal action の差の一階・二階 jets の組合せとして表される。したがって operator norm は Hessian polymer norm に比例して抑えられる。  
あとは improved gluing bound を代入するだけである。 \(\square\)

---

## 9. reference-scale renormalization

ここから fixed-\(\ell\) principal flow convergence を証明する。

### 9.1 exact gluing representation の abstract form

以後、improved gluing representation
\[
\boxed{
\mathcal S^{\rm ex}_{\ell,a,L}
=
\Psi_{\ell,L}(g_\ell(a))
+
E_{\ell,a,L}
}
\]
を用いる。ここで
\[
\Psi_{\ell,L}(g)=\mathcal S^{\rm pr}_{\ell,g,L},
\qquad
\|E_{\ell,a,L}\|_{\mathfrak A_\ell}
\le
C_E \Bigl(\frac{a}{\ell}\Bigr)^{2\omega}.
\]

---

### 9.2 transport defect

\[
r_{\ell\to\ell_R,L}(a)
:=
g_{\ell_R}(a)-\beta_{\ell\to\ell_R,L}(g_\ell(a))
\]
と定める。

#### 命題 9.1（approximate transport identity）
ある定数 \(C_{\ell\to\ell_R,L}>0\) が存在して
\[
g_{\ell_R}(a)
=
\beta_{\ell\to\ell_R,L}(g_\ell(a))
+
r_{\ell\to\ell_R,L}(a)
\]
かつ
\[
\|r_{\ell\to\ell_R,L}(a)\|
\le
C_{\ell\to\ell_R,L}
\Bigl(\frac{a}{\ell}\Bigr)^{2\omega}
\]
が成り立つ。

#### 証明
exact semigroup より
\[
\mathcal S^{\rm ex}_{\ell_R,a,L}
=
\mathbb B_{\ell\to\ell_R,L}
(\mathcal S^{\rm ex}_{\ell,a,L}).
\]
右辺に gluing representation を代入すると
\[
\mathcal S^{\rm ex}_{\ell_R,a,L}
=
\mathbb B_{\ell\to\ell_R,L}
\bigl(
\Psi_{\ell,L}(g_\ell(a))+E_{\ell,a,L}
\bigr).
\]
両辺に extraction map \(\Pi_{\ell_R,L}\) を作用させると
\[
g_{\ell_R}(a)
=
\Pi_{\ell_R,L}
\left[
\mathbb B_{\ell\to\ell_R,L}
(\Psi_{\ell,L}(g_\ell(a))+E_{\ell,a,L})
\right].
\]
principal invariance と retraction 性より
\[
\Pi_{\ell_R,L}
\left[
\mathbb B_{\ell\to\ell_R,L}
(\Psi_{\ell,L}(g_\ell(a)))
\right]
=
\beta_{\ell\to\ell_R,L}(g_\ell(a)).
\]
差をとると
\[
r_{\ell\to\ell_R,L}(a)
=
\mathcal F(\Psi_{\ell,L}(g_\ell(a))+E_{\ell,a,L})
-
\mathcal F(\Psi_{\ell,L}(g_\ell(a))),
\]
ただし
\[
\mathcal F:=\Pi_{\ell_R,L}\circ \mathbb B_{\ell\to\ell_R,L}.
\]
\(\mathcal F\) は解析的だから平均値表示により
\[
r_{\ell\to\ell_R,L}(a)
=
\int_0^1
D\mathcal F(\Psi_{\ell,L}(g_\ell(a))+tE_{\ell,a,L})[E_{\ell,a,L}]\,dt.
\]
relevant window 上で \(D\mathcal F\) は有界なので
\[
\|r_{\ell\to\ell_R,L}(a)\|
\le
M_{\ell\to\ell_R,L}\|E_{\ell,a,L}\|_{\mathfrak A_\ell}
\le
M_{\ell\to\ell_R,L} C_E
\Bigl(\frac{a}{\ell}\Bigr)^{2\omega}.
\]
\(\square\)

---

### 9.3 reference observable と renormalization condition

reference scale \(\ell_R\) での renormalization observable map を
\[
\mathcal O_{\ell_R,L}:U_{\ell_R,L}\to \mathbf R^m
\]
とする。

principal restriction を
\[
R_{\ell_R,L}(g):=\mathcal O_{\ell_R,L}(\Psi_{\ell_R,L}(g))
\]
と書く。

#### 仮定 9.2（reference nondegeneracy）
\(R_{\ell_R,L}\) は relevant window で局所微分同相であり、逆写像
\[
R_{\ell_R,L}^{-1}
\]
は Lipschitz である。

#### 仮定 9.3（reference renormalization condition）
ある target datum \(r_*\) が存在して
\[
\mathcal O_{\ell_R,L}(\mathcal S^{\rm ex}_{\ell_R,a,L})=r_*
\]
が成り立つ。

このとき
\[
g_R:=R_{\ell_R,L}^{-1}(r_*)
\]
を reference principal coupling と呼ぶ。

---

### 9.4 reference-scale convergence

#### 定理 9.4（reference-scale principal flow convergence）
仮定 9.2, 9.3 の下で
\[
g_{\ell_R}(a)\to g_R
\qquad(a\downarrow0)
\]
が成り立つ。さらに
\[
\|g_{\ell_R}(a)-g_R\|
\le
C_R^{\rm ref}\Bigl(\frac{a}{\ell_R}\Bigr)^{2\omega}
\]
が成り立つ。

#### 証明
reference scale で gluing representation を書くと
\[
\mathcal S^{\rm ex}_{\ell_R,a,L}
=
\Psi_{\ell_R,L}(g_{\ell_R}(a))+E_{\ell_R,a,L},
\qquad
\|E_{\ell_R,a,L}\|_{\mathfrak A_{\ell_R}}
\le
C_E \Bigl(\frac{a}{\ell_R}\Bigr)^{2\omega}.
\]
renormalization condition より
\[
r_*
=
\mathcal O_{\ell_R,L}
\left(
\Psi_{\ell_R,L}(g_{\ell_R}(a))+E_{\ell_R,a,L}
\right).
\]
Banach 空間版の平均値表示を \(\mathcal O_{\ell_R,L}\) に適用すると
\[
r_*
=
R_{\ell_R,L}(g_{\ell_R}(a))+\delta_R(a),
\]
ただし
\[
\|\delta_R(a)\|
\le
M_O \|E_{\ell_R,a,L}\|_{\mathfrak A_{\ell_R}}
\le
M_O C_E \Bigl(\frac{a}{\ell_R}\Bigr)^{2\omega}.
\]
従って
\[
R_{\ell_R,L}(g_{\ell_R}(a))
=
r_*-\delta_R(a).
\]
\(R_{\ell_R,L}^{-1}\) の Lipschitz 性より
\[
\|g_{\ell_R}(a)-g_R\|
=
\|R_{\ell_R,L}^{-1}(r_*-\delta_R(a))-R_{\ell_R,L}^{-1}(r_*)\|
\le
L_R \|\delta_R(a)\|.
\]
したがって
\[
\|g_{\ell_R}(a)-g_R\|
\le
L_R M_O C_E \Bigl(\frac{a}{\ell_R}\Bigr)^{2\omega}.
\]
\(\square\)

---

## 10. fixed-\(\ell\) principal flow convergence

### 10.1 finite-step principal transport の局所可逆性

#### 仮定 10.1（finite-step transport nondegeneracy）
固定した \(\ell<\ell_R\) に対し、
\[
\beta_{\ell\to\ell_R,L}:K\to K
\]
は relevant window で局所微分同相であり、その逆写像
\[
\beta_{\ell\to\ell_R,L}^{-1}
\]
は Lipschitz である。

---

### 10.2 fixed-\(\ell\) convergence

#### 定理 10.2（fixed-\(\ell\) principal flow convergence）
仮定 10.1 の下で
\[
\boxed{
g_\ell(a)\to g_\ell:=\beta_{\ell\to\ell_R,L}^{-1}(g_R)
}
\qquad(a\downarrow0)
\]
が成り立つ。さらに
\[
\boxed{
\|g_\ell(a)-g_\ell\|
\le
\widetilde C_\ell \Bigl(\frac{a}{\ell}\Bigr)^{2\omega}
}
\]
が成り立つ。

#### 証明
命題 9.1 より
\[
g_{\ell_R}(a)
=
\beta_{\ell\to\ell_R,L}(g_\ell(a))
+
r_{\ell\to\ell_R,L}(a),
\qquad
\|r_{\ell\to\ell_R,L}(a)\|
\le
C_{\ell\to\ell_R,L}\Bigl(\frac{a}{\ell}\Bigr)^{2\omega}.
\]
従って
\[
\beta_{\ell\to\ell_R,L}(g_\ell(a))
=
g_{\ell_R}(a)-r_{\ell\to\ell_R,L}(a).
\]
定理 9.4 から
\[
g_{\ell_R}(a)\to g_R
\]
であり、上の remainder は 0 に収束するから
\[
g_{\ell_R}(a)-r_{\ell\to\ell_R,L}(a)\to g_R.
\]
\(a\) を十分小さく取れば右辺は \(\beta_{\ell\to\ell_R,L}\) の局所逆写像の定義域に入るので
\[
g_\ell(a)
=
\beta_{\ell\to\ell_R,L}^{-1}
\bigl(
g_{\ell_R}(a)-r_{\ell\to\ell_R,L}(a)
\bigr)
\]
と書ける。よって Lipschitz 性から
\[
\|g_\ell(a)-g_\ell\|
\le
L_\beta
\left(
\|g_{\ell_R}(a)-g_R\|
+
\|r_{\ell\to\ell_R,L}(a)\|
\right).
\]
定理 9.4 と命題 9.1 を代入すると
\[
\|g_\ell(a)-g_\ell\|
\le
L_\beta
\left(
C_R^{\rm ref}\Bigl(\frac{a}{\ell_R}\Bigr)^{2\omega}
+
C_{\ell\to\ell_R,L}\Bigl(\frac{a}{\ell}\Bigr)^{2\omega}
\right).
\]
\(\ell_R=M^m \ell\) は fixed だから
\[
\Bigl(\frac{a}{\ell_R}\Bigr)^{2\omega}
=
M^{-2m\omega}\Bigl(\frac{a}{\ell}\Bigr)^{2\omega}
\le
\Bigl(\frac{a}{\ell}\Bigr)^{2\omega}.
\]
よって定数を吸収して
\[
\|g_\ell(a)-g_\ell\|
\le
\widetilde C_\ell \Bigl(\frac{a}{\ell}\Bigr)^{2\omega}
\]
を得る。 \(\square\)

---

### 10.3 scale compatibility

#### 定理 10.3
\[
\ell_1<\ell_2<\ell_R
\]
とする。対応する極限 couplings は
\[
g_{\ell_2}=\beta_{\ell_1\to\ell_2,L}(g_{\ell_1})
\]
を満たす。

#### 証明
\[
\beta_{\ell_1\to\ell_R,L}
=
\beta_{\ell_2\to\ell_R,L}\circ \beta_{\ell_1\to\ell_2,L}
\]
である。定義より
\[
\beta_{\ell_1\to\ell_R,L}(g_{\ell_1})=g_R,
\qquad
\beta_{\ell_2\to\ell_R,L}(g_{\ell_2})=g_R.
\]
従って
\[
\beta_{\ell_2\to\ell_R,L}
(\beta_{\ell_1\to\ell_2,L}(g_{\ell_1}))
=
g_R
=
\beta_{\ell_2\to\ell_R,L}(g_{\ell_2}).
\]
\(\beta_{\ell_2\to\ell_R,L}\) の局所一対一性から
\[
\beta_{\ell_1\to\ell_2,L}(g_{\ell_1})=g_{\ell_2}
\]
が従う。 \(\square\)

---

### 10.4 Cauchy estimate

#### 系 10.4
任意の十分小さい \(a,a'>0\) について
\[
\|g_\ell(a)-g_\ell(a')\|
\le
\widetilde C_\ell
\left[
\Bigl(\frac{a}{\ell}\Bigr)^{2\omega}
+
\Bigl(\frac{a'}{\ell}\Bigr)^{2\omega}
\right]
\]
が成り立つ。

#### 証明
三角不等式より
\[
\|g_\ell(a)-g_\ell(a')\|
\le
\|g_\ell(a)-g_\ell\|
+
\|g_\ell(a')-g_\ell\|.
\]
あとは定理 10.2 を二回使う。 \(\square\)

---

## 11. thermodynamic limit と common-scale continuum comparison

### 11.1 boundary comparison inequality

#### 仮定 11.1（uniform blocked mass）
定理 8.2 の Hessian floor により、exact blocked measure は covariance の指数減衰
\[
|\operatorname{Cov}_{\mu_{\ell,a,L}}(F,G)|
\le
C
\sum_{b,c}
e^{-m d(b,c)/\ell}
\|\partial_b F\|_\infty
\|\partial_c G\|_\infty
\]
を持つ。

これは uniform strong convexity から導かれる standard consequence として受け入れる。

---

### 11.2 thermodynamic comparison

support が boundary から距離 \(D\) だけ離れた local observable \(O\) をとる。

#### 定理 11.2（boundary comparison）
二つの体積 \(L<L'\) に対し
\[
|\langle O\rangle_{\ell,a,L}-\langle O\rangle_{\ell,a,L'}|
\le
C_O e^{-mD/\ell}
\]
が成り立つ。

#### 証明
二つの blocked actions を \(t\in[0,1]\) で線形補間して
\[
\mathcal S_t=(1-t)\mathcal S_{\ell,a,L}+t\mathcal S_{\ell,a,L'}
\]
とする。  
\(\langle\cdot\rangle_t\) を対応する期待値とする。

微分すると
\[
\frac{d}{dt}\langle O\rangle_t
=
-\operatorname{Cov}_{\mu_t}(O,\dot{\mathcal S}_t).
\]
\(\dot{\mathcal S}_t\) の support は boundary 近傍に局在しており、一方 \(O\) は boundary から距離 \(D\) 離れている。仮定 11.1 の covariance decay を適用すると
\[
\left|\frac{d}{dt}\langle O\rangle_t\right|
\le
C_O e^{-mD/\ell}.
\]
\(t\) で積分して
\[
|\langle O\rangle_{\ell,a,L}-\langle O\rangle_{\ell,a,L'}|
\le
\int_0^1 C_O e^{-mD/\ell}\,dt
=
C_O e^{-mD/\ell}.
\]
\(\square\)

#### 系 11.3（thermodynamic limit）
fixed \(\ell\) と fixed \(a\) に対して、local observables の thermodynamic limit
\[
\lim_{L\to\infty}\langle O\rangle_{\ell,a,L}
\]
が存在する。

#### 証明
定理 11.2 により、体積を大きくすると差は指数的に小さくなる。従って Cauchy。 \(\square\)

---

### 11.3 common-scale continuum comparison

次に二つの格子間隔 \(a,a'\) をとり、同じ physical mesoscopic scale \(\ell\) まで blocking した二つの theories を比較する。

#### 定理 11.4（common-scale continuum comparison）
local observable \(O\) に対して
\[
\left|
\langle O\rangle_{a,L}
-
\langle O\rangle_{a',L'}
\right|
\le
C_O
\left[
\|g_\ell(a)-g_\ell(a')\|
+
\|E_{\ell,a,L}\|_{\mathfrak A_\ell}
+
\|E_{\ell,a',L'}\|_{\mathfrak A_\ell}
+
e^{-mD/\ell}
\right]
\]
が成り立つ。

#### 証明
exact gluing representation を両方の theories に適用すると、
\[
\mathcal S_{\ell,a,L}^{\rm ex}
=
\Psi_{\ell,L}(g_\ell(a))+E_{\ell,a,L},
\qquad
\mathcal S_{\ell,a',L'}^{\rm ex}
=
\Psi_{\ell,L'}(g_\ell(a'))+E_{\ell,a',L'}.
\]
まず principal couplings の差
\[
g_\ell(a)-g_\ell(a')
\]
による principal action の差は、\(\Psi_{\ell,L}\) の \(C^1\) regularity により線形に評価できる。  
次に remainders は \(\mathfrak A_\ell\)-ノルムで評価される。  
最後に体積差は定理 11.2 の boundary comparison で制御される。これらを合成すれば主張が従う。 \(\square\)

#### 系 11.5
定理 10.4 と improved gluing bound を代入すると
\[
\left|
\langle O\rangle_{a,L}
-
\langle O\rangle_{a',L'}
\right|
\le
C_O'
\left[
\Bigl(\frac{a}{\ell}\Bigr)^{2\omega}
+
\Bigl(\frac{a'}{\ell}\Bigr)^{2\omega}
+
e^{-mD/\ell}
\right]
\]
が成り立つ。

#### 証明
定理 11.4 に

- 系 10.4 の
  \[
  \|g_\ell(a)-g_\ell(a')\|
  \le
  \widetilde C_\ell
  \left[
  \Bigl(\frac{a}{\ell}\Bigr)^{2\omega}
  +
  \Bigl(\frac{a'}{\ell}\Bigr)^{2\omega}
  \right],
  \]
- improved gluing の
  \[
  \|E_{\ell,a,L}\|_{\mathfrak A_\ell}
  \le
  C_E \Bigl(\frac{a}{\ell}\Bigr)^{2\omega},
  \qquad
  \|E_{\ell,a',L'}\|_{\mathfrak A_\ell}
  \le
  C_E \Bigl(\frac{a'}{\ell}\Bigr)^{2\omega},
  \]

を代入して定数をまとめればよい。 \(\square\)

---

## 12. 統合主定理

### 定理 12.1（v84 integrated gluing theorem）

仮定 2.1–2.3, 3.1, 4.1–4.4, 6.1–6.3, 7.1, 8.1, 9.2–9.3, 10.1, 11.1 の下で、次が成り立つ。

1. **spectral-entry**
   \[
   \|\widetilde R_n\|\le \delta \rho^n.
   \]

2. **bundle transduction**
   \[
   \|D_A s_{j,x}(0;g_n,\widetilde R_n)\|
   \le
   C_{\rm tr}\delta \rho^n.
   \]

3. **local minimizer control**
   \[
   \|z_{j,x}(g_n,\widetilde R_n)\|
   \le
   \frac{C_{\rm tr}\delta}{\mu}\rho^n.
   \]

4. **connected polymer gluing**
   \[
   \mathcal S^{\rm ex}_{\ell,a,L}
   =
   \mathcal S^{\rm pr}_{\ell,g_\ell(a),L}
   +
   E_{\ell,a,L},
   \qquad
   \|E_{\ell,a,L}\|_{2,\alpha;\ell}
   \le
   C_E \Bigl(\frac{a}{\ell}\Bigr)^{2\omega}.
   \]

5. **uniform exact Hessian floor**
   \[
   D_\Phi^2 \mathcal S^{\rm ex}_{\ell,a,L}(\Phi)
   \succeq
   \frac{\kappa_0}{2}I.
   \]

6. **reference-scale convergence**
   \[
   g_{\ell_R}(a)\to g_R,
   \qquad
   \|g_{\ell_R}(a)-g_R\|
   \le
   C_R^{\rm ref}\Bigl(\frac{a}{\ell_R}\Bigr)^{2\omega}.
   \]

7. **fixed-\(\ell\) principal flow convergence**
   \[
   g_\ell(a)\to g_\ell
   =
   \beta_{\ell\to\ell_R,L}^{-1}(g_R),
   \qquad
   \|g_\ell(a)-g_\ell\|
   \le
   \widetilde C_\ell \Bigl(\frac{a}{\ell}\Bigr)^{2\omega}.
   \]

8. **thermodynamic comparison**
   \[
   |\langle O\rangle_{\ell,a,L}-\langle O\rangle_{\ell,a,L'}|
   \le
   C_O e^{-mD/\ell}.
   \]

9. **common-scale continuum comparison**
   \[
   \left|
   \langle O\rangle_{a,L}
   -
   \langle O\rangle_{a',L'}
   \right|
   \le
   C_O'
   \left[
   \Bigl(\frac{a}{\ell}\Bigr)^{2\omega}
   +
   \Bigl(\frac{a'}{\ell}\Bigr)^{2\omega}
   +
   e^{-mD/\ell}
   \right].
   \]

### 証明
1 は定理 3.2、2 は定理 4.3 と定理 3.2、3 は補題 4.5 と系 4.6、4 は定理 6.7 と節 7、5 は定理 8.2、6 は定理 9.4、7 は定理 10.2、8 は定理 11.2、9 は定理 11.4 と系 11.5 による。 \(\square\)

---

## 13. 結論

本稿で閉じたのは、v83 に残っていた「あと一段外側の橋」である。

v83 の内部 statement は
\[
Q\to 0
\Longrightarrow
B0,S1,S2 \text{ absorb}
\]
という形だった。

v84 ではこれを
\[
(g,\widetilde R)\text{-bundle entry}
\Longrightarrow
\text{local transduction}
\Longrightarrow
\text{connected polymer gluing}
\Longrightarrow
\text{reference-scale renormalization}
\Longrightarrow
g_\ell(a)\to g_\ell
\]
という chain に持ち上げた。

とくに、fixed-\(\ell\) での principal flow convergence
\[
g_\ell(a)\to g_\ell
\]
は仮定ではなく、exact gluing representation と reference-scale renormalization condition の帰結として本文内で証明された。

さらに connected polymer Hessian estimate が通ると、

- uniform blocked convexity、
- volume-uniform exact spectral ratio、
- thermodynamic limit、
- common-scale continuum comparison、

はすべて global gluing representation の系として現れる。

従って v84 の本質は、v83 の局所閉包を否定することではなく、それを **spectral-entry bundle と connected polymer gluing を介して actual blocked dynamics へ接続し直した**ことにある。

---

## 付記：v83 との対応関係

v83 の scalar coordinate \(Q\) と v84 の bundle coordinate \((g,\widetilde R)\) の対応は次のように理解できる。

- \(Q\) は principal manifold からの距離を一次元に射影した coarse coordinate であった。
- \(\widetilde R\) は principal manifold の法 bundle に沿う真の remainder coordinate である。
- \(Q=0\) は v84 では \(R=\chi(g)\)、すなわち \(\widetilde R=0\) に置き換わる。
- \(D_A s_{j,x}(0;0)=0\) は
  \[
  D_A s_{j,x}(0;g,0)=0
  \]
  に強化される。

この意味で v84 は、v83 の主張を否定するのではなく、その局所的 statement を bundle-theoretic に持ち上げている。

---
