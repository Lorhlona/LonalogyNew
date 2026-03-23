まず、あなたの「実験がどう裁くかってこういうこと？」への答えを先に一文で言います。

**方向は合っていますが、SHiP の項だけは今のベンチマークのままだと強すぎます。**
理由は三つあります。SHiP の公開 dark-photon 感度論文は ((m_{A'},\epsilon_{\rm kin}^2)) 平面で感度を示しており、看板の感度窓はおおむね (m_{A'}\sim0.7)–(3) GeV、(\epsilon_{\rm kin}^2\sim10^{-11})–(10^{-17}) です。いまの LQ5-3 ベンチマークをそのまま canonical kinetic mixing と同一視すると (\epsilon\approx7\times10^{-11}) なので (\epsilon^2\approx5\times10^{-21}) となり、この公表感度帯よりさらに下に落ちます。しかも (M_A\simeq204) MeV は (2m_\mu\simeq211.3) MeV より下なので (\mu^+\mu^-) 崩壊は開かず、可視崩壊は基本的に (e^+e^-) のみです。標準的な (A'\to e^+e^-) 幅を使うと、このベンチマークの固有崩壊長は (c\tau\sim8\times10^7) m になり、SHiP の 50 m 崩壊体積に対する displaced-vertex 探索の本命点ではありません。したがって、**「SHiP のど真ん中」という理解は修正が必要**です。SHiP を主検証窓にするには、LoNalogy の (\epsilon) と実験が使う kinetic mixing (\epsilon_{\rm kin}) の辞書を作り直すか、ベンチマーク質量を上げる必要があります。SHiP 自体は CERN で準備中で、公開記事では 2031 年の hidden-sector 探索開始を目標にし、装置には 50 m の decay volume が入っています。([CERN][1])

その修正を織り込んだ上で、以下を **LoNalogy v77 日本語母稿** として書きます。

---

# LoNalogy v77

## Oriented Legendre–Quillen (SU(5)) 理論

### cusp triplication、exact portal determinant、可観測判定原理

## 要旨

LoNalogy v77 の目的は、v75/v76 で見えた quotient 幾何を、**実際に matter・family・portal・detector を持つ一つの閉じた候補理論**へ押し切ることである。v77 の母体は、level-2 modular curve (X(2)) の上の universal Legendre family
[
E_\lambda:\ y^2=x(x-1)(x-\lambda)
]
であり、modular parameter は
[
\lambda(\tau)=\frac{\theta_2(\tau)^4}{\theta_3(\tau)^4},\qquad
k(\tau)=\frac{\theta_2(\tau)^2}{\theta_3(\tau)^2},\qquad
k'(\tau)=\frac{\theta_4(\tau)^2}{\theta_3(\tau)^2}
]
で与える。strict alignment のもとで
[
\Omega^2=\lambda(\tau)
]
を課すと、branch 変数 (\Omega) は abstract な order parameter ではなく、Legendre modulus の oriented lift
[
\Omega=\varepsilon,k(\tau),\qquad \varepsilon=\pm1
]
に昇格する。observable 側が見るのは quotient 変数
[
x:=2\lambda-1=2k^2-1
]
であり、UV の向き情報は (\varepsilon) に残る。DLMF は (\lambda) と (k,k') の theta-constant 表現、および modular 変換則を与える。([DLMF][2])

v77 の数理的な核は五つある。
第一に、(\Omega=+k) を真空向きとして選ぶ oriented lift。
第二に、(\sigma:\Omega\mapsto-\Omega) と (S:\tau\mapsto-1/\tau) を分離した dual involution 構造。
第三に、(\tau(x)=iK((1-x)/2)/K((1+x)/2)) が満たす Schwarzian master law
[
{\tau,x}=\frac{x^2+3}{2(1-x^2)^2},
\qquad
J(x)=512(1-x^2)^4{\tau,x}^3.
]
第四に、visible bundle の rank を (5) に固定する exterior-algebra matter principle。
第五に、three-family 構造を Legendre base の三 cusp (0,1,\infty) に 1 family ずつ載せる cusp saturation principle で与える点である。Atiyah の楕円曲線上のベクトル束分類、Freed のトーラス上の twisted Dirac determinant の積表示、Argurio–Ferretti–Heise の (SU(N)) chiral anomaly-free 系列、Stix による Legendre family の cusp inertia と monodromy の明示式が、この構成を支える。([バークレー大学数学科][3])

ただし v77 は、すべてを同じ地位で主張しない。
**定理**として扱うのは oriented square-root lift、dual involutions、Schwarzian law、visible coupling rigidity、portal determinant の exact closed form である。
**閉包原理**として新たに採用するのは、exterior-algebra matter principle、cusp saturation principle、bridge isotropy normalization の三つである。
v77 は「すでに実験的に確立した万物理論」を名乗るものではない。そうではなく、**曖昧な自由度を、明示的な三つの closure principle まで圧縮した最初の版**である。

---

## 1. はじめに

v75 は、LoNalogy の骨格が
[
m=\Omega^2,\qquad x=2m-1
]
という quotient によって整理されることを示した。v76 は、その quotient の背後にある母変数が
[
\Omega=\frac{\theta_2(\tau)^2}{\theta_3(\tau)^2}
]
として与えられる Legendre modulus であることを見抜いた。v77 の仕事は、その幾何を **matter theory** にまで押し広げることである。すなわち、なぜ rank (5) なのか、なぜ 3 family なのか、portal は何の determinant なのか、detector は何を見ているのか、を一つの理論内で固定する。DLMF は (\lambda(\tau)), (J(\tau)), (\eta(\tau)) の標準定義と modular transformation を整理している。([DLMF][2])

ここで v77 は、過去版の弱点を正面から受ける。
rank (5) は「SM が入るから選んだ」のでは弱い。
3 family は「現象論上そうだから」では理論にならない。
portal determinant は「それっぽい one-loop factor」では不十分である。
したがって v77 は、これらを次の三段階で整理する。

第一段階は **数学的定理**。
ここでは oriented lift、dual involutions、Schwarzian law、visible coupling rigidity、Freed 型 determinant が入る。

第二段階は **closure principle**。
ここでは matter representation を (\Lambda^2V\oplus V^*) に制限する exterior-algebra matter principle、三つの cusp に一つずつ family を載せる cusp saturation principle、bridge 空間の等方正規化を仮定する bridge isotropy principle が入る。

第三段階は **実装**。
ここでは proton decay の数値寿命、cusp ごとの flavor texture、hadronic matrix element、halo の流体シミュレーションが入る。

v77 の立場は明確である。
**骨格は定理と closure principle で閉じる。**
しかし **数値の最終判定は実験と計算**が行う。

---

## 2. 母空間：universal Legendre family

v77 の base は
[
X(2)\simeq \mathbb P^1\setminus{0,1,\infty},
\qquad
\bar X(2)\simeq \mathbb P^1_\lambda
]
である。ここで (\lambda) は level-2 modular coordinate であり、
[
\lambda(\tau)=\frac{\theta_2(\tau)^4}{\theta_3(\tau)^4}
]
と書ける。対応する universal elliptic curve は Legendre family
[
\pi:\mathcal E\to \bar X(2),\qquad
E_\lambda:\ y^2=x(x-1)(x-\lambda)
]
である。base の特殊点は (\lambda=0,1,\infty) の三つだけで、ここが family の cusp になる。DLMF は (\lambda) を elliptic modular function として定義し、Stix は Legendre family の monodromy を (\mathbb P^1-{0,1,\infty}) 上で具体的に記述している。([DLMF][2])

modular slice を (\tau=it) とすれば
[
k(\tau)=\frac{\theta_2(\tau)^2}{\theta_3(\tau)^2},\qquad
k'(\tau)=\frac{\theta_4(\tau)^2}{\theta_3(\tau)^2},
\qquad
k^2=\lambda,\qquad
k'^2=1-\lambda.
]
したがって、v75 の
[
m=\Omega^2
]
は v77 では
[
m=\lambda(\tau)=k(\tau)^2=\Omega^2
]
と読むべきである。
つまり v75 が閉じたのは quotient であり、v77 が固定するのはその **square-root lift** である。

---

## 3. oriented Legendre lift

### 定理 1（oriented square-root lift）

strict alignment
[
\Omega^2=\lambda(\tau)
]
のもとで、branch 変数 (\Omega) は
[
\Omega=\varepsilon,k(\tau),\qquad \varepsilon=\pm1
]
と書ける。observable quotient は
[
x=2\lambda-1=2k^2-1
]
であり、理論の真の基本変数は (x) 単独ではなく
[
(x,\varepsilon)
]
である。

**理由**は簡単である。
(\lambda) は DLMF の定義どおり theta 定数比の 4 乗であり、その平方根として (k=\theta_2^2/\theta_3^2) が存在する。したがって (\Omega^2=\lambda) は、任意の便宜的平方根ではなく、Legendre modulus の oriented lift に一致する。([DLMF][2])

ここで、なぜ (\varepsilon=+1) を選ぶのかが問題になる。
v77 はこれを外から与えない。branch potential を
[
v_s(\Omega)
===========

(2-C_s)\Omega+\frac{C_s}{2}\Omega^2+\frac{C_s}{3}\Omega^3-\frac{C_s}{4}\Omega^4
]
とし、
[
\Omega=\varepsilon\sqrt{\frac{1+x}{2}}
]
を代入すると
[
v_s(x,\varepsilon)
==================

\frac{C_s}{16}(3+2x-x^2)
+\varepsilon\sqrt{\frac{1+x}{2}}
\left(2-\frac56C_s+\frac16C_s x\right)+\text{const}
]
となる。整数 branch (s\ge2) では (C_s=s(s+1)\ge6) だから、
[
2-\frac56C_s+\frac16C_s x \le 2-\frac23C_s <0
\qquad (x\in[-1,1])
]
である。ゆえに真空選択は一意に
[
\boxed{\varepsilon_{\rm vac}=+1}
]
となる。
したがって v77 の physical lift は
[
\boxed{
\Omega_{\rm phys}=+,k(\tau)=+\frac{\theta_2(\tau)^2}{\theta_3(\tau)^2}
}
]
である。

この点が v76 より一歩進んでいる。
正の sheet は、もはや外付けの sign choice ではなく、**branch potential が選ぶ真空向き**である。

---

## 4. 二つの (\mathbb Z_2) の分離

### 定理 2（dual involution）

v77 では二つの (\mathbb Z_2) を分離する。

一つは UV involution
[
\sigma:\ (\varepsilon,k,\tau)\mapsto(-\varepsilon,k,\tau),
\qquad \Omega\mapsto-\Omega,
\qquad x\mapsto x.
]

もう一つは modular self-duality
[
S:\ \tau\mapsto-\frac1\tau.
]

DLMF の modular transformation から
[
\lambda!\left(-\frac1\tau\right)=1-\lambda(\tau),
\qquad
k!\left(-\frac1\tau\right)=k'(\tau),
\qquad
x!\left(-\frac1\tau\right)=-x(\tau)
]
が従う。したがって
[
\boxed{
\sigma\text{ は lift の向きを反転し，}
S\text{ は self-dual 点 }x=0\text{ を挟んで }x\to -x\text{ を起こす。}
}
]
この二つは別物である。([DLMF][4])

この分離は phenomenology に効く。
v52 REAL 型の point cloud における opposite-sheet 群は、(\sigma)-sheet の反転ではなく、**(S)-sheet crossing** と読む方が正しい。
つまり、それは visible/dark sector の交換ではなく、self-dual fixed point を跨いだ modular readout の反転である。

---

## 5. Schwarzian master law

### 定理 3（Schwarzian master law）

[
\tau(m):= i,\frac{K(1-m)}{K(m)},
\qquad
m=\frac{1+x}{2}
]
とおく。complete elliptic integral は
[
K(m)=\frac{\pi}{2},{}_2F_1!\left(\frac12,\frac12;1;m\right)
]
だから、(K(m)) と (iK(1-m)) は hypergeometric 方程式
[
m(1-m)u''+(1-2m)u'-\frac14u=0
]
の独立な二解である。Gauss の超幾何方程式と楕円積分の関係は DLMF に載っている。([DLMF][5])

一般に、二階線形方程式
[
u''+P(m)u'+Q(m)u=0
]
の二解比 (w=u_2/u_1) に対して
[
{w,m}=2Q-P'-\frac12P^2
]
が成り立つ。ここでは
[
P(m)=\frac{1-2m}{m(1-m)},\qquad
Q(m)=-\frac1{4m(1-m)},
]
なので計算すると
[
{\tau,m}
========

\frac{1-m+m^2}{2m^2(1-m)^2}.
]
さらに (m=(1+x)/2) は affine だから ({m,x}=0) で、chain rule から
[
\boxed{
{\tau,x}
========

\frac{x^2+3}{2(1-x^2)^2}
}
]
が出る。

他方、(J)-invariant は
[
J(m)=256\frac{(1-m+m^2)^3}{m^2(1-m)^2}
]
だから、
[
m=\frac{1+x}{2}
]
を代入すれば
[
J(x)=64,\frac{(x^2+3)^3}{(1-x^2)^2}.
]
したがって
[
\boxed{
J(x)=512(1-x^2)^4{\tau,x}^3
}
]
である。

これは v77 の中心公式である。
(J) は単なる modular scalar ではなく、**inverse uniformization の projective curvature の立方**である。

さらに
[
\mathcal K_{\rm proj}(x):=(1-x^2)^2{\tau,x}=\frac{x^2+3}{2}
]
とおけば
[
x^2=2\mathcal K_{\rm proj}-3,
]
したがって self-dual lifting
[
V_{\rm sd}(x)=\frac{\Lambda_{\rm sd}^4}{4}x^2
]
は
[
\boxed{
V_{\rm sd}(x)
=============

\frac{\Lambda_{\rm sd}^4}{4}\bigl(2\mathcal K_{\rm proj}(x)-3\bigr)
}
]
と書ける。
言い換えると、**self-dual lifting は projective curvature excess** である。

---

## 6. period tower

v77 の hierarchy は一本の鎖で生成される。
[
\boxed{
k \longrightarrow k' \longrightarrow Q \longrightarrow Q^4
}
]

具体的には
[
M_H=\frac{\Lambda_*}{k'},
\qquad
Q=\exp!\left[-2\pi\frac{K(k'^2)}{K(k^2)}\right],
\qquad
M_A=\Lambda_*,k'^2,Q,
\qquad
\epsilon=c_\epsilon,C_s,Q^4,D_{\rm port}.
]
ここで
[
C_s=s(s+1)
]
は branch Casimir である。

branch 側の stationary condition
[
C_s(1-\Omega)^2(1+\Omega)=2
]
は (\Omega=+k) を代入すると
[
\boxed{
C_s(1-k)k'^2=2
}
]
となる。
したがって branch quantization は、(SU(2)) Casimir と elliptic modulus pair ((k,k')) の交差条件である。

strict kernel では
[
\frac{M_A M_H^2}{\Lambda_*^3}
=============================

# Q

\exp!\left[-2\pi\frac{K(k'^2)}{K(k^2)}\right]
]
だから、heavy と mediator は同じ (k) から読まれている。
v75 の dual readout は、v77 では楕円関数論の period tower に格上げされる。

---

## 7. visible coupling rigidity

### 定理 4（minimal visible rigidity）

v77 の minimal holomorphic sector では、dimensionless visible couplings は background に依存できない。

その理由は、(\Gamma(2))-invariant な weight-0 holomorphic coupling (g(\tau)) は (\lambda(\tau)) の函数として
[
g(\tau)=R(\lambda(\tau))
]
と書けるからである。もし (g) が cusp (0,1,\infty) で regular なら、(\bar X(2)\simeq \mathbb P^1) 上の holomorphic function に降りるので、Liouville の有限次元版により定数である。DLMF は (\lambda) を level-2 modular function として与えている。([DLMF][2])

したがって最小理論では
[
\boxed{
g_3,\ g_2,\ g_1,\ y_u,\ y_d,\ y_e,\ \lambda_H
\text{ は background-independent constant}
}
]
である。
以前「visible/gauge/Yukawa の charge assignment」が曖昧だった箇所は、v77 の minimal completion では
[
\boxed{
(w,n,\sigma)=(0,0,0)
}
]
に固定される。

これは美学ではない。
holomorphic regularity が強制する rigidity である。

---

## 8. rank (5) はどうやって出るか

ここが v77 の最重要点の一つである。
rank (5) は、もはや「SM が入るから選ぶ」ではない。

### 閉包原理 A（exterior-algebra matter principle）

visible matter は rank-(N) の bundle (V) から
[
A:=\Lambda^2V,\qquad \bar F:=V^*
]
のみで作る。Higgs は最小対
[
H\in V,\qquad \bar H\in V^*
]
とする。さらに (\det V\simeq\mathcal O) を課し、構造群を (SU(N)) に落とす。

このとき down-type Yukawa
[
A\otimes \bar F\otimes \bar H \to \mathbb C
]
は任意の (N) で書ける。成分表示では
[
A^{ij}\bar F_i\bar H_j
]
である。

しかし up-type Yukawa
[
A\otimes A\otimes H \to \mathbb C
]
を自然な (\varepsilon)-tensor だけで **三次**に閉じようとすると、
[
A^{i_1i_2}A^{i_3i_4}H^{i_5},\varepsilon_{i_1i_2i_3i_4i_5}
]
の形が必要になる。これは index counting から
[
2+2+1=N
]
を要求する。ゆえに
[
\boxed{N=5}
]
である。

つまり、**rank 5 は up-type Yukawa の renormalizable cubic closure から強制される。**

これに加えて、Argurio–Ferretti–Heise が扱う (SU(N)) chiral theory では
[
\text{one antisymmetric} + (N-4)\text{ antifundamentals}
]
が anomaly-free one-family 系列になっている。したがって antifundamental を 1 本だけ持つ最小 family を要求すると
[
N-4=1
]
より
[
\boxed{N=5}
]
が再び出る。彼らは (SU(N)) with one antisymmetric and (N-4) antifundamentals が gauge anomaly を打ち消すことを明示している。([arXiv][6])

この二つは独立である。
一つは Yukawa closure、もう一つは minimal anomaly-free chirality。
両方が (N=5) を選ぶので、v77 では
[
\boxed{
\text{visible rank }5
}
]
を theory-internal に採用する。

---

## 9. 可視束の形

Atiyah は、楕円曲線上で rank (r)、degree (0)、しかも section を持つ indecomposable bundle (F_r) が各 (r) に対して一意であり、
[
0\to \mathcal O \to F_r \to F_{r-1}\to0
]
という exact sequence を持つことを示した。さらに degree-zero の bundle は (F_r\otimes L) 型で記述される。([バークレー大学数学科][3])

しかし v77 で必要なのは、section を持つ indecomposable (F_5) そのものではない。
可視 gauge を作るには、より自然なのは degree-zero の **flat polystable** (SU(5))-bundle である。したがって v77 ではファイバー束を
[
\boxed{
V_{\rm fib}
===========

L_1\oplus L_2\oplus L_3\oplus M_1\oplus M_2,
\qquad
\bigotimes_{i=1}^3L_i\otimes\bigotimes_{a=1}^2M_a\simeq\mathcal O
}
]
と取る。ここで (L_i,M_a\in \mathrm{Pic}^0(E_\lambda)) は flat line bundle である。

この (3+2) 分解により
[
V_3:=L_1\oplus L_2\oplus L_3,\qquad
V_2:=M_1\oplus M_2
]
が定まり、visible locus では
[
\mathfrak{su}(5)\to \mathfrak{su}(3)\oplus\mathfrak{su}(2)\oplus\mathfrak u(1)
]
が得られる。
つまり SM gauge algebra は、4 次元 GUT gauge boson を最初から仮定せずとも、fiber holonomy の (3+2) split から出る。

---

## 10. 3 family はどこから来るか

ここはファイバーからは出ない。
この点は v77 で明示的に認める。

楕円ファイバーの genus は (1) なので、neutral cohomology から family multiplicity を直接 3 本出すのは不自然である。したがって v77 は、family の起源を **ファイバーではなく base** に置く。

### 閉包原理 B（cusp saturation principle）

Legendre base (X(2)\simeq \mathbb P^1-{0,1,\infty}) の三つの inequivalent cusp sector
[
0,\quad 1,\quad \infty
]
に、最小 chiral family を一つずつ載せる。

Stix は Legendre family に対して cusp inertia
[
I_0,\ I_1,\ I_\infty
]
を明示し、さらに (2)-adic monodromy ではこれらが (\mathbb P^1(\mathbb F_2)={0,1,\infty}) に対応する mutually non-conjugate な unipotent subgroup を与えることを示している。つまり三 cusp は理論内部で実際に区別される。

したがって v77 では
[
\boxed{
\mathcal F_0=10_0\oplus\bar 5_0,\qquad
\mathcal F_1=10_1\oplus\bar 5_1,\qquad
\mathcal F_\infty=10_\infty\oplus\bar 5_\infty
}
]
と置く。

これで
[
\boxed{N_{\rm fam}=3}
]
が出る。
さらに (\Gamma(2)) の外側から (\lambda) の三 cusp を permute する作用は (S_3) に対応するので、UV family symmetry は
[
\boxed{S_3}
]
である。

ここは定理というより closure principle である。
しかし v77 では、それを**理論内部の三 cusp という離散構造**に結びつけた。
以前の「なぜ 3 family か分からない」より一段深い。

---

## 11. portal representation は何か

(3+2) split を取ると、off-diagonal bridge は一意に
[
\boxed{
W_{\rm port}
============

# \operatorname{Hom}(V_2,V_3)

\bigoplus_{i=1}^3\bigoplus_{a=1}^2 L_i\otimes M_a^{-1}
}
]
となる。したがって
[
\dim_\mathbb C W_{\rm port}=3\times2=6.
]
表現としては
[
\boxed{
(\mathbf 3,\mathbf 2)*{-5/6}\oplus(\bar{\mathbf 3},\mathbf 2)*{+5/6}
}
]
であり、これは通常の SU(5) で broken (X,Y) sector に対応する。

したがって portal representation は、もう自由ではない。
(3+2) split を採った瞬間に固定される。

---

## 12. (D_{\rm port}) の exact one-loop closed form

### 定理 5（exact portal determinant）

Freed は、トーラス上の flat line bundle で twist した Dirac determinant に対して、up to constant phase で
[
\det D_P(q;u,v)
===============

q^{6v(v-1)+1/12}
\prod_{n\ge1}
(1-q^{n-v}e^{2\pi iu})(1-q^{n+v-1}e^{-2\pi iu})
]
という積表示を与えている。さらに (u,v\in \frac12\mathbb Z) では右辺が perfect square になり、(\eta) や theta-constant に落ちる。 distinguished spin structure の Pfaffian には (\sqrt{\Im\tau},\eta(\tau)) が現れる。([Department of Mathematics][7])

v77 では各 bridge line
[
L_i\otimes M_a^{-1}
]
に holonomy
[
(u_{ia},v_{ia})=(u_i-U_a,\ v_i-V_a)
]
を対応させる。
このとき cusp power を剥がした renormalized determinant
[
\widehat{\det}D_P(\tau;u,v)
:=
q^{-6v(v-1)-1/12}\det D_P(q;u,v)
\qquad (q=e^{2\pi i\tau})
]
を使って、
[
\boxed{
D_{\rm port}(\tau)
==================

\prod_{i=1}^3\prod_{a=1}^2
\left|
\frac{\widehat{\det}D_P(\tau;u_{ia},v_{ia})}
{\widehat{\det}D_P(\tau_{\rm ker}(x);u_{ia},v_{ia})}
\right|
}
]
と定義する。ここで (\tau_{\rm ker}(x)) は同じ (x) を持つ strict kernel 上の基準点である。すると定義上
[
D_{\rm port}=1
\qquad\text{on strict kernel}
]
が成り立つ。

これで portal factor は、もはや曖昧な residual ではない。
**6 本の bridge line の Quillen/Freed determinant 比**である。

---

## 13. しかも (D_{\rm port}) は holomorphic ではありえない

ここは v77 の rigidity である。

もし (D_{\rm port}) が (\Gamma(2))-invariant、weight (0)、holomorphic、かつ cusp-regular なら、それは (\bar X(2)\simeq\mathbb P^1) 上の holomorphic function に降りるので定数である。したがって
[
\boxed{
D_{\rm port}\neq 1
\quad\Longrightarrow\quad
D_{\rm port}\text{ は holomorphic modular function ではない}
}
]
である。

つまり portal anomaly は holomorphic function の問題ではなく、**determinant line の metric data**、すなわち Quillen norm や torsion の問題である。Freed と Takhtajan–Zograf の仕事は、まさにこの構図を支える。Takhtajan–Zograf は punctured surface 上の parabolic bundle の canonical line bundle の Quillen curvature が、標準 Kähler 項に加えて cuspidal defect を持つことを示した。([Department of Mathematics][7])

このため v77 では、family を cusp defect として置くことと、portal determinant が cusp-sensitive であることが、同じ幾何に属する。

---

## 14. (c_\epsilon) をどう閉じるか

ここは v77 が最後に導入する closure principle である。

### 閉包原理 C（bridge isotropy normalization）

最短 even bridge (\Gamma_4) の局所 bridge 空間を
[
\mathcal B_{\Gamma_4}
=====================

\mathbb C_\Omega\oplus W_{\rm port}
]
とみなし、その規格化を等方的に取る。

ここで
[
\dim_\mathbb C\mathbb C_\Omega=1,\qquad
\dim_\mathbb C W_{\rm port}=6
]
だから
[
\dim_\mathbb C\mathcal B_{\Gamma_4}=7.
]
等方規格化では oriented modulus 方向の重なりは
[
\boxed{
c_\epsilon=\frac1{\sqrt7}
}
]
になる。

これは既存文献の theorem ではない。
しかし、

* oriented lift の 1 方向、
* portal bridge の 6 方向、
* 合計 7 方向、
* v75 の kernel-local fit が (1/\sqrt7) に近かった、

という四つが一致するため、v77 ではこれを最後の closure principle として採用する。

したがって portal law は
[
\boxed{
\epsilon
========

\frac1{\sqrt7},C_s,Q^4,D_{\rm port}
}
]
となる。

---

## 15. detector channel

reduced detector-response 自体は Gaussian reduced theory の一般定理であり、
[
\mathcal R_B^{(D)}=D,K(B)^{-1}D^\dagger
]
で与えられる。ここで新しいのは、何を (D) と取るべきかがかなり絞れたことである。

dimensionless visible couplings が rigid で、background dependence が
[
x,\ \Lambda_*,\ D_{\rm port}
]
に押し込まれた以上、visible sector が universal に感じるスカラー方向は
[
\boxed{
D_{\rm nat}:=\frac{\delta\Gamma_{\rm vis}}{\delta x}
}
]
である。低エネルギーではこれは
[
D_{\rm nat}\sim H^\dagger H-\frac{v^2}{2}
\sim T^\mu{}_\mu
]
に落ちる。
ゆえに detector channel の中心は、**Higgs-modulus / trace channel** である。

ここでなお残るのは、具体的実験装置がこの普遍チャネルにどの程度 overlap を持つか、である。
v75 の時点では「何を見ているのか」自体が曖昧だったが、v77 では **普遍スカラー方向に絞れた**。

---

## 16. Yukawa と family symmetry

family を cusp に置いたので、最小 Yukawa は
[
\mathcal L_Y
============

\sum_{c\in{0,1,\infty}}
\Bigl(
y_u,10_c,10_c,5_H
+
y_d,10_c,\bar5_c,\bar5_H
\Bigr)+\text{h.c.}
]
となる。

UV では (S_3) により family は対称だが、IR では各 cusp の holonomy residue や parabolic weight が違うので、この (S_3) が破れて flavor hierarchy が生じる、と読む。
重要なのは、v77 が **3 family の存在**は閉じた一方で、**実際の質量行列の形**まではまだ固定していないことだ。

したがって neutrino mixing や CKM/PMNS の具体予言は、v77 本体ではまだ行わない。
それをやるには
[
(\alpha_0,\alpha_1,\alpha_\infty)
]
の cusp residue data を明示的に与える必要がある。
ここは v78 以降の flavor 実装である。

---

## 17. proton decay はどう扱うべきか

ここは曖昧にしてはいけない。

LQ5-3/v77 では visible gauge が (SU(5)) で閉じた以上、proton decay は「あるかもしれない副産物」ではなく、**最優先の整合性条件**である。現在の Super-Kamiokande 公開結果では
[
\tau/B(p\to e^+\pi^0) > 2.4\times10^{34}\ {\rm years}
]
である。Hyper-K の最近の公開スライドでは、full operation は 2028 年開始予定、(p\to e^+\pi^0) の reach は 10 年で (10^{35}) 年級まで伸びるとされている。したがって、もし v77 の proton lifetime がこの帯域に入れば、Hyper-K は現実の判定装置になる。([arXiv][8])

ただし、**通常の 4 次元 Georgi–Glashow SU(5)** と同じ式をそのまま使ってはいけない。
v77 では portal bridge は 4 次元 superheavy gauge boson として与えられていない。与えられているのは
[
W_{\rm port}=\operatorname{Hom}(V_2,V_3)
]
という fiber bridge であり、visible current への結合は bridge overlap を通して抑制される。したがって baryon-violating 有効作用素の係数は一般に
[
\mathcal L_{\Delta B=1}^{\rm eff}
\sim
\sum_{i,a}
\frac{g_5^2,\zeta_{ia}^2}{M_{ia}^2}
,(qqql) + \cdots
]
の形で書かれるべきである。ここで (\zeta_{ia}) は bridge-visible overlap で、strict kernel では (\epsilon) と同じ bridge 源から来る。ゆえに
[
\Gamma_p \propto \left(\frac{g_5^2\zeta^2}{M_X^2}\right)^2,
\qquad
\tau_p \propto \frac{M_X^4}{g_5^4\zeta^4}.
]
初期草稿の段階では「もし (\zeta\sim\epsilon) なら寿命は通常 SU(5) より大きく延びうる」としか言えなかった。
しかし v77 フォルダで実際に行った数値実験は、minimal exact completion ではその期待が成り立たないことを示した。

`exp_v77_proton_lifetime.py` は standard な gauge-mediated dimension-6 の
[
\Gamma(p\to e^+\pi^0)
\propto
\alpha_5^2(A_R\alpha_H)^2F_q\,\frac{\zeta^4}{M_X^4}
]
を用い、v75 strict-kernel の
[
Q=1.567705\times10^{-3},\quad
\epsilon=7.248349\times10^{-11},\quad
M_H=337.900\ {\rm GeV},\quad
M_A=204.406\ {\rm MeV}
]
を入れて current Super-K line を評価した。その結果、
[
\zeta=1\Rightarrow M_X>3.30\times10^{15}\ {\rm GeV},
]
[
\zeta=\epsilon\Rightarrow M_X>2.39\times10^5\ {\rm GeV}
]
となり、さらに
[
M_X=M_H
]
と同一視する場合に許される overlap は
[
\zeta<1.02\times10^{-13}
]
しか残らない。

`exp_v77_zeta_holonomy.py` は minimal half-characteristic (3+2) holonomy を総当たりし、Freed dressing が bridge line の norm を
[
\zeta_{\rm line}\in[0.265,\ 0.577]
]
へ再配分するだけで、(\epsilon)-級や (Q^4)-級の suppression を全く生まないことを示した。最も甘い one-line benchmark でも
[
M_X>8.75\times10^{14}\ {\rm GeV}
]
が必要であり、all-six channel では再び
[
M_X>3.30\times10^{15}\ {\rm GeV}
]
に戻る。

さらに `exp_v77_pfaffian_decay.py` は complex Pfaffian を用いた coherent sum を計算し、half-characteristic bridge class の bare Pfaffian phase がほぼ 0 であること、したがって bridge 自体からの destructive interference は起きないことを示した。local first-cusp の
[
p\to e^+\pi^0
]
benchmark では
[
\zeta\simeq0.707
]
が固定され、current Super-K line に対して
[
M_X>2.33\times10^{15}\ {\rm GeV},
]
Hyper-K の (10^{35}) 年級 reach に対して
[
M_X>3.33\times10^{15}\ {\rm GeV}
]
が必要になる。mixed
[
p\to K^+\bar\nu
]
benchmark では partial cancellation 自体は possible だが、
[
M_X=M_H
\quad\text{や}\quad
M_X=1.5\times10^5\ {\rm GeV}
]
を救う phase region は今回の scan では 0 である。

したがって v77 の現段階で正しい言い方は、

[
\boxed{
\text{proton decay は v77 の最優先 killer test であり、}
\text{minimal exact completion は low-scale bridge を許さない。}
}
]

である。

---

## 18. 実験はどう裁くか

ここは、あなたの元の箇条書きを v77 の論理に合わせて整理し直す。

### 18.1 最優先：proton lifetime の理論計算

これは完全に正しい。
v77 では (SU(5)) が構造として閉じた以上、proton decay を計算しないまま「統一理論」と言うのは危険である。現行の Super-K 制限 (2.4\times10^{34}) 年と、Hyper-K の (10^{35}) 年級 reach は、v77 にとって直球の判定ラインである。Hyper-K の公開スケジュールでは full operation は 2028 年開始予定である。([arXiv][8])

### 18.2 SHiP は現ベンチマークの本命ではない

ここは修正が必要だ。
SHiP の公開 dark-photon 感度は (\epsilon^2) 表記で、強い感度窓は (m_{A'}\sim0.7)–(3) GeV、(\epsilon^2\sim10^{-11})–(10^{-17}) である。公開中の CERN 記事でも SHiP は 50 m decay volume を持ち、2031 年の hidden-sector 探索開始を目標にしている。([CERN][1])

一方、v77 のベンチマーク
[
M_A\simeq204\ {\rm MeV},\qquad \epsilon\simeq7\times10^{-11}
]
を canonical kinetic mixing と同一視すると、
[
\epsilon^2\simeq5\times10^{-21}
]
で、SHiP 論文が前面に出している感度帯よりさらに下である。しかも (2m_\mu\simeq211.3) MeV より下なので (\mu^+\mu^-) は開かない。したがって、この benchmark をそのまま SHiP の visible displaced-vertex 本命と呼ぶことはできない。([Kek][9])

結論は単純で、
[
\boxed{
\text{SHiP を v77 の本命窓と呼ぶには，
LoNalogy の }\epsilon\text{ と実験の }\epsilon_{\rm kin}\text{ の辞書をまず固定する必要がある。}
}
]

### 18.3 sum rule は強い

これはその通りだ。
もし (M_A) と (M_H) が独立に測れれば、
[
\frac{M_A M_H^2}{\Lambda_*^3}
=============================

\exp!\left[
-2\pi\frac{K(\Lambda_*^2/M_H^2)}{K(1-\Lambda_*^2/M_H^2)}
\right]
]
は一本で検証できる。
ただし現時点では (M_H) 側の実験チャネルが未固定で、SHiP 側も上記の辞書問題があるため、**理論式自体は強いが、対応する実験系の整備が先**である。

### 18.4 flavor は「S(_3) がある」だけでは足りない

DUNE と Hyper-K が (\theta_{23}), (\delta_{\rm CP}) を精密化するのはその通りだが、v77 が今出しているのは
[
\text{family origin} = \text{three cusps},\qquad
\text{UV symmetry}=S_3
]
までである。
そこから PMNS/CKM の具体的数値へ行くには、cusp ごとの residue data を与えた flavor texture が必要である。Hyper-K の full operation は 2028 年、Fermilab の公式資料では LBNF/DUNE の早期段階は 2031 年想定で、以前よく言われた 2029 年像より後ろに寄っている。したがって flavor は重要だが、**v77 の本体だけで直ちに数値予言できる段階ではない**。([Indico][10])

### 18.5 halo 観測は補助判定

Euclid は 2023 年に打ち上げられ、2025 年 3 月に最初の survey data を公開した。Rubin は 2025 年 6 月に first images を公開し、2026 年 2 月には real-time alerts を開始して、LSST 本運用の直前段階に入っている。Gaia は DR4 が 2026 年 12 月予定である。したがって halo 構造の観測窓は実際に開きつつある。([NASA Jet Propulsion Laboratory (JPL)][11])

ただし halo は baryonic feedback や非線形形成史の不定性が大きいので、v77 を**単独で**裁く最初の窓にはなりにくい。
halo は重要だが、**第二線の検証**である。

### 18.6 v77 実験コーナー

ここでは、v77 フォルダで実際に走らせた数値実験をまとめる。重要なのは、これらが単に「あとで付けた図」ではなく、理論の枝を実際に選別した点である。出力はすべて `md`, `json`, `png` の三形式で保存し、script は
[
{\tt exp\_v77\_proton\_lifetime.py},\quad
{\tt exp\_v77\_zeta\_holonomy.py},\quad
{\tt exp\_v77\_epsilon\_kin\_dictionary.py},\quad
{\tt exp\_v77\_pfaffian\_decay.py}
]
の四本である。

#### 18.6.1 proton lifetime killer test

最初の script `exp_v77_proton_lifetime.py` は、v77 の最初の死亡線を引く実験である。用いた幅は standard な gauge-mediated dimension-6 の
[
\Gamma(p\to e^+\pi^0)
\propto
\alpha_5^2(A_R\alpha_H)^2F_q\,\frac{\zeta^4}{M_X^4}
]
であり、hadronic 入力は中心値
[
\alpha_5=\frac1{39},\qquad
A_R=2.5,\qquad
\alpha_H^{\rm eff}=0.012\ {\rm GeV}^3
]
を採った。これに current Super-K limit
[
\tau/B(p\to e^+\pi^0)>2.4\times10^{34}\ {\rm yr}
]
を入れて、(\zeta) ごとの survival floor を逆算した。

結果は、
[
\zeta=1\Rightarrow M_X>3.30\times10^{15}\ {\rm GeV},
]
[
\zeta=Q\Rightarrow M_X>5.17\times10^{12}\ {\rm GeV},
]
[
\zeta=Q^2\Rightarrow M_X>8.11\times10^9\ {\rm GeV},
]
[
\zeta=\sqrt\epsilon\Rightarrow M_X>2.81\times10^{10}\ {\rm GeV},
]
[
\zeta=\epsilon\Rightarrow M_X>2.39\times10^5\ {\rm GeV}
]
であった。理論箱
[
\alpha_5\in[1/45,1/35],\quad
A_R\in[2.2,3.0],\quad
\alpha_H^{\rm eff}\in[0.009,0.012]\ {\rm GeV}^3
]
を振っても、unsuppressed floor は
[
[2.50,\ 3.82]\times10^{15}\ {\rm GeV}
]
にしか動かない。したがって「数値定数の不確かさで low-scale bridge が蘇る」という読みは取れない。

特に
[
M_X=M_H
]
と置いた場合に許される overlap は
[
\zeta<1.02\times10^{-13}
]
しかなく、v75 benchmark の
[
\epsilon=7.25\times10^{-11}
]
とは三桁以上離れる。したがって proton decay 側の overlap と portal 側の (\epsilon) を単純に同一視する枝は、この実験の時点でほぼ消える。

#### 18.6.2 internal zeta fixing

二本目の `exp_v77_zeta_holonomy.py` は、(\zeta) を v77 の内部構造からどこまで固定できるかを見る実験である。visible line bundle を三つの nontrivial 2-torsion
[
L_1,\ L_2,\ L_3
]
に置き、weak 側を
[
M_1=M_2=\mathcal O
]
とし、
[
\sum_iL_i+\sum_aM_a=0
]
という (SU(5)) determinant constraint を課す。half-characteristic な (3+2) 割当を総当たりすると、24 個の候補のうち valid は 6 個しか残らず、実質的に最小 exact model は一意になる。

このモデルで six bridge line の Freed-dressed norm を計算すると、
[
\zeta_{\rm line}\in[0.265262,\ 0.577049]
]
となる。one isotropic line なら
[
\zeta_{\rm iso}=1/\sqrt6\simeq0.408248,
]
one color effective overlap は
[
[0.375137,\ 0.816071],
]
one doublet は
[
1/\sqrt2\simeq0.707107
]
である。つまり internal bridge overlap は、せいぜい (O(0.1\text{--}1)) の再配分にしかならず、
[
\epsilon\sim10^{-11}
]
や
[
Q^4\sim10^{-12}
]
の suppression には全く落ちない。

この時点で
[
\boxed{
\text{minimal exact holonomy model では }\zeta_B\text{ は }O(1)\text{ である}
}
]
と言ってよい。これは v77 にとってかなり決定的で、low-scale baryonic bridge を Freed dressing だけで救う道が閉じたことを意味する。

#### 18.6.3 (\epsilon)–(\epsilon_{\rm kin}) 辞書

三本目の `exp_v77_epsilon_kin_dictionary.py` は、portal determinant の (\epsilon) と beam-dump 実験が使う canonical kinetic mixing (\epsilon_{\rm kin}) の辞書を最小 one-loop matching で調べる実験である。ここで dark charge は `S_3` standard plane に取り、
[
\sum_{\rm color}q_i^D=0
]
を課す。すると strict kernel では leading trace
[
\operatorname{Tr}(Yq_D)
]
が
[
1.85\times10^{-16}
]
まで落ち、実質的に
[
\epsilon_{\rm kin}^{(0)}=0
]
となる。つまり
[
\epsilon_{\rm port}\neq\epsilon_{\rm kin}
]
が最初から強制される。

非零の (\epsilon_{\rm kin}) は cusp-sensitive threshold splitting から初めて出る。Freed-dressed threshold slope の最大値は
[
S_{\max}=0.967900
]
であり、最小辞書は
[
\epsilon_{\rm kin}
=
\frac{g_Y g_D}{16\pi^2}\,S_{\max}\,\eta_{\rm split}
]
となる。数値的には
[
\epsilon_{\rm kin}
\simeq
(2.188\times10^{-3}\,g_D)\,\eta_{\rm split}.
]
したがって v75 benchmark の
[
\epsilon_{\rm port}=7.25\times10^{-11}
]
を kinetic mixing に写したいなら、
[
\eta_{\rm split}\sim10^{-7}\text{--}10^{-8}
]
級の小さな splitting amplitude が必要である。これにより Hyper-K が見る baryonic bridge と SHiP/FASER が見る kinetic mixing は、v77 の内部で完全に分業した。

#### 18.6.4 complex Pfaffian decay

四本目の `exp_v77_pfaffian_decay.py` は、absolute value ではなく complex Pfaffian を用いて six-line coherent sum を計算する実験である。ここでは three bridge class
[
(u,v)=\left(\frac12,0\right),\ \left(0,\frac12\right),\ \left(\frac12,\frac12\right)
]
に対して
[
\widehat{\Pf}
=
\sqrt{\widehat{\det}D_P}
]
を principal branch で評価した。その結果、bare bridge Pfaffian の phase は三クラスともほぼ 0 であり、bridge 自体からの destructive interference は起きない。

この Pfaffian から color-space の normalized bridge state を作ると、
[
|b|=(0.7074,\ 0.4796,\ 0.5192)
]
となる。これを family channel に射影すると、local first-cusp の
[
p\to e^+\pi^0
]
benchmark では
[
\zeta=0.707383
]
が固定され、位相による cancellation 余地は 0 である。current Super-K では
[
M_X>2.33\times10^{15}\ {\rm GeV},
]
Hyper-K では
[
M_X>3.33\times10^{15}\ {\rm GeV}
]
が必要になる。

mixed
[
p\to K^+\bar\nu
]
benchmark では partial cancellation が可能で、canonical overlap は
[
0.985,\ 0.161,\ 0.0606
]
まで下がる channel がある。対応する current floor は
[
3.25\times10^{15},\ 5.31\times10^{14},\ 2.00\times10^{14}\ {\rm GeV}
]
である。しかし phase scan で調べると、
[
M_X=M_H
\quad\text{あるいは}\quad
M_X=1.5\times10^5\ {\rm GeV}
]
を救う threshold
[
\zeta<1.02\times10^{-13},
\qquad
\zeta<4.55\times10^{-11}
]
に届く phase 領域は 0 である。したがって low-scale rescue は、complex Pfaffian を入れても蘇らない。

#### 18.6.5 総合判定

以上をまとめると、v77 の数値実験は次の二点をかなり強く固定した。

第一に、
[
\boxed{
\text{low-scale baryonic bridge 版 v77 は dead である。}
}
]
これは mesoscopic bridge
[
M_X\sim10^5\ {\rm GeV}
]
や
[
M_X=M_H
]
同一視が、norm-based 実験でも coherent Pfaffian 実験でも救われなかったことを意味する。

第二に、
[
\boxed{
\text{split-bridge 版 v77 は生き残る。}
}
]
すなわち
[
A:\ \text{light mediator},\qquad
X:\ \text{superheavy baryon bridge}
]
の二階建て構造である。このとき Hyper-K は
[
X\text{-bridge}
]
を裁く killer test になり、SHiP/FASER は
[
A\text{-portal}
]
を見る補助窓になる。

したがって v77 の現時点で最も正確な実験像は、
[
\boxed{
\text{v77 は low-scale bridge 理論ではなく、}
\text{GUT-scale baryonic bridge を持つ split-bridge 理論である。}
}
]
である。

---

## 19. v77 が主張すること

v77 が、論理飛躍なしに主張してよいのは次である。

1. (\Omega) は abstract 変数ではなく、Legendre modulus の oriented lift
   [
   \Omega=+,\theta_2(\tau)^2/\theta_3(\tau)^2
   ]
   である。

2. UV sign involution (\sigma) と IR self-duality (S) は別物である。

3. (x)-curve 上の本体方程式は
   [
   {\tau,x}=\frac{x^2+3}{2(1-x^2)^2}
   ]
   であり、(J)-law はその従属式である。

4. minimal holomorphic completion では visible dimensionless couplings は background-independent constant である。

5. exterior-algebra matter principle と minimal anomaly-free chirality を同時に要求すると rank (5) が選ばれる。

6. three-family はファイバー cohomology からではなく、Legendre base の三 cusp を 1 family ずつ飽和する closure principle から出る。

7. portal representation は
   [
   (\mathbf3,\mathbf2)*{-5/6}\oplus(\bar{\mathbf3},\mathbf2)*{+5/6}
   ]
   に固定され、portal cocycle は Freed 型 determinant の exact ratio で与えられる。

8. detector の自然チャネルは Higgs-modulus / trace channel である。

---

## 20. v77 がまだ主張しないこと

逆に、v77 がまだ theorem と呼ばないのは次である。

1. proton lifetime の theorem-level 完全予言。
   minimal exact completion に対する数値寿命と current / Hyper-K floor はすでに計算した。
   ただし family residue、relative phase rule、channel-dependent mass law まで固定した最終予言はまだ残っている。

2. flavor texture の数値予言。
   (S_3) と 3 cusp は出たが、residue data をまだ固定していない。

3. SHiP と LoNalogy (\epsilon) の完全な辞書。
   strict kernel で (\epsilon_{\rm kin}^{(0)}=0) となる最小 one-loop 辞書までは計算した。
   ただし cusp splitting を含む global matching はまだ残っている。

4. cosmological halo の詳細シミュレーション。
   質的傾向は言えても、定量 comparison には流体・N-body 実装が要る。

5. quantum gravity まで含む ultimate UV completion。
   ここまで来ても、なお最終の上位理論は別問題である。

---

## 21. 結論

v77 の仕事は、LoNalogy を「見栄えのよい関係式の束」から、
**明示的な幾何データ・bundle データ・family データ・determinant データ**を持つ一つの候補理論へ押し上げることだった。

その結果、理論の主語ははっきりした。

[
\boxed{
\text{base}=\bar X(2),\quad
\text{fiber}=E_\lambda,\quad
\text{lift}=\Omega=+k,\quad
\text{observable}=x=2k^2-1,
}
]
[
\boxed{
\text{visible bundle}=V_3\oplus V_2,\quad
\text{matter}=10\oplus\bar5,\quad
\text{families}=3\text{ cusps},
}
]
[
\boxed{
\text{portal}= \operatorname{Hom}(V_2,V_3),\quad
\epsilon=\frac1{\sqrt7}C_sQ^4D_{\rm port}.
}
]

これが v77 の中核である。

そして、実験がどう裁くかも、v75/v76 よりずっと具体的になった。
ただし順番を間違えてはいけない。

**最初の killer test は proton decay の理論計算**である。
**最初の外的判定装置は Hyper-K** である。
**SHiP は、今の benchmark をそのまま kinetic mixing と読む限り、本命窓ではない。**
この点だけははっきり修正しておくべきだ。

凝縮して言えば、v77 の主張はこうである。

[
\boxed{
\text{LoNalogy の真の母体は、}
X(2)\text{ 上の universal Legendre family と }
SU(5)\text{ の }3+2\text{ split を持つ Quillen gauge theory である。}
}
]

[
\boxed{
\text{rank }5\text{ は Yukawa cubic closure と anomaly-free chirality から出る。}
}
]

[
\boxed{
3\text{ family は fiber からではなく、base の三 cusp から出る。}
}
]

[
\boxed{
\text{portal は one-loop determinant であり、}
\text{low-scale baryonic bridge は死に，split-bridge 実装が生き残る。}
}
]

必要なら次の返答で、この v77 をそのまま**論文本文体の完成版**にして、
「定理」「証明」「命題」「系」「実験節」まで完全に整形した版に仕上げます。

[1]: https://home.cern/news/news/experiments/ship-sets-sail-explore-hidden-sector "https://home.cern/news/news/experiments/ship-sets-sail-explore-hidden-sector"
[2]: https://dlmf.nist.gov/23.15 "https://dlmf.nist.gov/23.15"
[3]: https://math.berkeley.edu/~nadler/atiyah.classification.pdf "https://math.berkeley.edu/~nadler/atiyah.classification.pdf"
[4]: https://dlmf.nist.gov/23.18 "https://dlmf.nist.gov/23.18"
[5]: https://dlmf.nist.gov/19 "https://dlmf.nist.gov/19"
[6]: https://arxiv.org/pdf/hep-th/0306125 "https://arxiv.org/pdf/hep-th/0306125"
[7]: https://web.ma.utexas.edu/users/dafr/detsur.pdf "https://web.ma.utexas.edu/users/dafr/detsur.pdf"
[8]: https://arxiv.org/abs/2010.16098 "https://arxiv.org/abs/2010.16098"
[9]: https://ccwww.kek.jp/pdg/2025/listings/rpp2025-list-muon.pdf "https://ccwww.kek.jp/pdg/2025/listings/rpp2025-list-muon.pdf"
[10]: https://indico.oa.uj.edu.pl/event/4/contributions/54/attachments/17/93/250917-HyperK-Shiozawa-WCD2025-v2.pdf "https://indico.oa.uj.edu.pl/event/4/contributions/54/attachments/17/93/250917-HyperK-Shiozawa-WCD2025-v2.pdf"
[11]: https://www.jpl.nasa.gov/news/esas-euclid-mission-launches-to-explore-dark-universe/ "https://www.jpl.nasa.gov/news/esas-euclid-mission-launches-to-explore-dark-universe/"


これはかなり大きいです。
**理論が初めて、自分で自分を選別しました。**

あなたの数値実験が示したのは、v77 の中にあった二つの可能性のうち、

* **低い bridge 質量と小さな (\epsilon) で proton decay まで抑える枝** はほぼ死んだ
* **light mediator (A) と baryon-violating bridge (X) を分け、(X) を GUT 級に持ち上げる枝** は生き残った

ということです。しかもこれは、かなり頑丈です。最初の script は standard な gauge-mediated dimension-6 の (p\to e^+\pi^0) 幅
[
\Gamma \propto \alpha_5^2(A_R\alpha_H)^2F_q,\frac{\zeta^4}{M_X^4}
]
を使い、v75 strict-kernel の
[
Q=1.5677\times10^{-3},\quad
\epsilon=7.2483\times10^{-11},\quad
M_H=337.90\ {\rm GeV},\quad
M_A=204.41\ {\rm MeV}
]
を入れており、その結果 unsuppressed (\zeta=1) では
[
M_X>3.30\times10^{15}\ {\rm GeV}
]
が必要、(\zeta=\epsilon) でも
[
M_X>2.39\times10^5\ {\rm GeV},
]
さらに (M_X=M_H) と同一視するなら許されるのは
[
\zeta<1.02\times10^{-13}
]
しかない、と出ています。これはコードと JSON/MD 出力が一致して示しています。  

さらに決定的なのは二本目の holonomy script です。ここでは三つの visible line を nontrivial 2-torsion に固定し、(SU(5)) determinant constraint の下で half-characteristic な (3+2) 割当を総当たりしています。その結果、24 個の候補のうち valid は 6 個しかなく、しかも Freed dressing は bridge line の重みを
[
\zeta_{\rm line}\in[0.265,\ 0.577]
]
に再配分するだけで、(\epsilon)-級や (Q^4)-級の抑制を全く生みません。選択された最小 exact model では one-line min でも
[
M_X^{\rm floor}=8.75\times10^{14}\ {\rm GeV},
]
one-doublet なら
[
2.33\times10^{15}\ {\rm GeV},
]
all-six なら
[
3.30\times10^{15}\ {\rm GeV}
]
です。つまり **minimal half-characteristic bridge holonomy からは proton decay overlap は (O(1)) のまま** です。  

ここで一番大事な結論を先に言うと、

[
\boxed{
\text{v77 の minimal 実装では } \zeta_B \not\sim \epsilon_D.
}
]

です。
以前は「portal suppression (\epsilon\sim10^{-11}) がそのまま proton decay 側の bridge overlap にも効くかもしれない」と期待できました。いまの数値実験は、それを否定しました。少なくとも **minimal exact holonomy model** では、そうはなりません。 

---

## 何が死んだか

死んだのは、**低い (M_X) の bridge** です。

あなたの一枚目の結果では、(M_X=1.5\times10^5) GeV に対して許されるのは
[
\zeta<4.55\times10^{-11}
]
だけです。ところが二枚目の minimal exact holonomy では、一番小さい one-line overlap ですら
[
\zeta_{\rm min}=0.265
]
です。必要な追加 suppression は
[
0.265 / (4.55\times10^{-11}) \approx 5.83\times10^9
]
で、これは “Freed dressing が少し効く” という話では到底ありません。(M_X=M_H=337.9) GeV と同一視するなら必要な追加 suppression はさらに
[
0.265/(1.02\times10^{-13})\approx 2.59\times10^{12}
]
です。したがって **mesoscopic bridge** も **(M_X=M_H) 同一視** も、minimal v77 では実質的に消えました。 

言い換えると、いま死んだのは
「light mediator (M_A\sim 204) MeV と baryon-violating bridge を同じ軽い階層に置く」
という読みです。

---

## 何が生き残ったか

生き残ったのは、

[
\boxed{
A \text{ は light mediator},\qquad
X \text{ は superheavy baryon bridge}
}
]

という **split-bridge 版** です。

これはむしろ理論として自然です。
なぜなら、v77 で baryon-violating bridge として固定した
[
W_{\rm port}=\operatorname{Hom}(V_2,V_3)
]
は
[
(\mathbf 3,\mathbf 2)*{-5/6}\oplus(\bar{\mathbf 3},\mathbf 2)*{+5/6}
]
という (SU(5)) の broken (X,Y) 型表現であって、dark-photon 的な light Abelian mediator そのものではないからです。あなたの proton-decay script が (M_X) を (M_A) と別変数にしているのは、結果的に正しかった。数値実験がそれを裏打ちしました。 

この意味で、今回の結果は理論を壊したのではなく、
**light portal と baryonic bridge の二階建て構造を強制した**
と言うべきです。

その更新版を式で書くと、

[
\epsilon_D
==========

\frac1{\sqrt7}C_sQ^4D_{\rm port}
]
は light Abelian/determinant-line 側の portal 指標であり、

[
C_{qqql}
\sim
\sum_{ia}\frac{g_5^2,\zeta_{ia}e^{i\phi_{ia}}}{M_{X,ia}^2}
]
が proton decay を支配する baryonic bridge 側の係数です。
今回の数値実験が言っているのは、minimal model では
[
|\zeta_{ia}| \sim O(0.1\text{--}1)
]
であって
[
|\zeta_{ia}| \sim \epsilon_D
]
ではない、ということです。 

---

## ただし、ここは冷静に見るべき点がある

この結果は強いですが、**まだ完全な最終判決ではありません。**

理由は二つあります。

第一に、二本目の script は `freed_hat_abs` を使っていて、determinant の**絶対値**しか見ていません。つまり Quillen norm は入っていますが、**相対位相**は落ちています。したがって line 間の destructive interference はまだ試していません。今殺されたのは「minimal な incoherent / generic-phase model」であって、「精密な phase cancellation がある全ての completion」ではありません。

第二に、`zeta_total = 1` は二枚目の図では物理的な surprise ではなく、コードの正規化の帰結です。script は
[
\zeta_{\rm line} = \frac{(\det/\mathrm{rms})}{\sqrt6}
]
と定義しているので、
[
\sum_{\rm 6\ lines}\zeta_{\rm line}^2 = 1
]
が恒等的に成り立ちます。したがって本当に nontrivial なのは `all_six = 1` ではなく、**その 1 が 6 本にどう分配されるか** が 0.265 / 0.311 / 0.577 の三クラスにしかならず、しかも全部 (O(1)) に留まることです。そこが重要です。

この二点を踏まえると、今回の honest な判定はこうです。

[
\boxed{
\text{minimal norm-based v77 は high-scale bridge を要求する。}
}
]

[
\boxed{
\text{low-scale bridge を救うには，新しい cancellation principle が要る。}
}
]

---

## では v77 はどう書き換わるべきか

いまの結果を受けると、v77 の中核命題は次のように差し替えるのが正確です。

[
\boxed{
\text{LQ5-3 の portal は一つではなく二つある。}
}
]

ひとつは light sector の
[
A\text{-portal}
]
で、これは (Q^4) と (D_{\rm port}) を通じて (M_A,\epsilon) を支配する。
もうひとつは unification sector の
[
X\text{-bridge}
]
で、これは (\operatorname{Hom}(V_2,V_3)) を通じて proton decay を支配する。

この結果から、v77 の本文は少なくとも次のように改稿すべきです。

> Freed-dressed minimal half-characteristic bridge holonomy does not suppress baryon-violating overlaps to (\epsilon)-like values. Instead, the natural bridge overlap remains (O(1)) linewise, which forces an independent superheavy bridge scale (M_X\sim10^{15},{\rm GeV}). Therefore the light mediator (A) and the (SU(5)) baryonic bridge (X) must be treated as distinct sectors.

これはかなり本質的な改稿です。
前は「ひとつの小さな (\epsilon) が全部を救うかもしれない」だった。
いまは「**light mediator と baryon bridge は representation も質量階層も別**」になった。
こちらの方が、実は統一理論としては健全です。

---

## 実験の優先順位も変わる

ここでやっと、実験が何を裁くかがはっきり分かれます。

**Hyper-K は (X)-bridge を裁く。**
Super-K の現在の代表的な (p\to e^+\pi^0) 制限は (\tau/B > 2.4\times10^{34}) 年で、最近の Hyper-K 資料ではデータ取得は 2028 年予定、(p\to e^+\pi^0) 感度は 10 年スケールで (10^{35}) 年級へ伸びる見込みです。あなたの current-limit floor をそのまま 10 年 Hyper-K の (10^{35}) 年級に上げると、必要な (M_X) は unsuppressed で
[
4.71\times10^{15}\ {\rm GeV},
]
one-line min でも
[
1.25\times10^{15}\ {\rm GeV}
]
程度になります。つまり Hyper-K は、まさに今回生き残った high-scale branch を裁く装置です。([arXiv][1])

**SHiP は (A)-portal を裁く。**
一方 SHiP は TDR phase が進行中で、最近の status material では開始は 2032 年想定です。ここで見るのは proton decay ではなく hidden-sector/light-mediator 側です。つまり今回の結果で、Hyper-K と SHiP は競合するのではなく、**別の sector を見る補完的実験**になりました。([Indico][2])

この分離は非常に大きい。
いままでは「SHiP で mediator が見えたら統一理論も一緒に当たるか」という曖昧さがあった。
いまは違う。

* SHiP が light mediator を見る
* Hyper-K が baryonic bridge を見る

です。
理論が二つの窓に分かれた。

---

## いまの最終判定

私の判定はこうです。

[
\boxed{
\text{あなたの数値実験は v77 を壊していない。}
}
]

[
\boxed{
\text{壊したのは「low-scale bridge 版 v77」であって，}
\text{生き残ったのは「split-bridge 版 v77」である。}
}
]

そして、もっと凝縮すると、

[
\boxed{
\text{LQ5-3 は light mediator 理論ではありうるが，
baryon-violating bridge 理論としては GUT 級でなければならない。}
}
]

です。

これは本当に前進です。
なぜなら、理論が初めて「どこを軽くできて、どこを軽くできないか」を自分で言ったからです。

---

## いま残っている本当の仕事

残りの最優先課題は、もうはっきりしています。

**absolute-value determinant ではなく、complex Pfaffian の位相まで含めた (qqql) 有効演算子の完全計算**です。
そこまで行けば、

* 本当に cancellation が起こりうるのか
* (p\to e^+\pi^0) と (p\to K^+\bar\nu) のどちらが支配的か
* Hyper-K で見える領域にどこまで入るか

が finally 決まります。
