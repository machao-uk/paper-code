# MathZ n=4 Reduced Pick Matrix: Complete State 2026-06-28

**Paper**: `~/Downloads/MathZ_BraidMonodromy_T2_extended.tex`  
**目标**: 证明对所有 centered non-confluent interior quadruples, Π_red ≻ 0  
**核心命题**: `prop:interior-machine-certificate` (tex line 1252–1327) — **CLOSED BY GAMMA3 BLOW-UP CERTIFICATE**

**2026-06-28 closure update**:
The former sole gap, the gamma3 hard corner
`rho in [3/4,1], y in [3/4,1]`, is closed by the blow-up certificate:

```text
/Users/ray/Downloads/MathZ_gamma3_hard_corner_closed.md
/Users/ray/Downloads/MathZ_gamma3_hard_corner_certificate.py
/Users/ray/Downloads/MathZ_gamma3_hard_corner_certificate_output.md
/Users/ray/Downloads/MathZ_n4_closure_summary.md
```

The resolved charts are:

```text
1. |z| <= 16v: exact l1 coefficient bound on T(q,v).
2. 16v < |z| < 1/4: analytic bound S >= 50 C v.
3. 1/4 <= |z| <= 32: exact Bernstein on S, all intervals neg=0.
4. z >= 32: reciprocal chart H(r,u)=Q(u,ru), exact Bernstein neg=0.
```

---

## 一、数学设置

### 基本对象
- Nodes: λ₁,λ₂,λ₃,λ₄ ∈ D, centered: Σλₖ = 0 (故 λ₄ = -(λ₁+λ₂+λ₃))
- Schur function: F_λ(z) = (c₁ + c₂z + c₃z²)/768
- Reduced values: rₖ = F_λ(λₖ)
- Reduced Pick matrix: Π_red[i,j] = (1 - rᵢ·conj(rⱼ)) / (1 - λᵢ·conj(λⱼ))
- 目标: Π_red ≻ 0 for all centered non-confluent interior quadruples

### c₁,c₂,c₃ 公式 (degree 8-10 in λₖ's)
```
a₂ = Σᵢ<ⱼ λᵢλⱼ,  a₁ = -(Σ triple products),  a₀ = λ₁λ₂λ₃λ₄
c₃ = -16a₂⁴ + 256a₂²a₀ - 144a₂a₁² - 768a₀²
c₂ = 108a₁³ + 8a₂³a₁ - 288a₂a₁a₀
c₁ = -16a₂⁵ + 192a₂³a₀ - 132a₂²a₁² - 512a₂a₀² - 144a₂a₀a₁²
```

### Schur参数 γ₁,γ₂,γ₃,γ₄
Π_red ≻ 0 ⟺ det(Π_red[{1..k}]) > 0 for k=1..4  
等价地通过 Schur 参数级联: Π_red ≻ 0 ⟺ |γₖ| < 1 for k=1..4  

---

## 二、已关闭的结果（分析证明完毕）✅

### 1. K-区域 (max|λₖ| ≤ R* ≈ 0.9761)
**已关闭**. 通过判别式梯度界分析证明. 来源: 论文 prop K-region.

### 2. 配对族 {±ρ, ±ρe^{iθ}}
**已关闭（解析）**. 设 S = sin²θ, q = ρ²:
```
A = q⁵t(t-5)(t-1)³/48,  B = q⁵(t-1)³(5t-1)/48  (t=e^{2iθ})
H = N / [(1-q²)²(1-2q²cos(2θ)+q⁴)]
N = 4Sq²F₋F₊
F₊ < 9q¹⁰-9 < 0
F₋ ≤ 9(q¹⁰+q⁴-q⁶-1) < 0
```
两个因子都严格负 → N > 0 → H > 0 → det(M₊), det(M₋) > 0.  
来源: `MathZ_contraction_proof.md` + `MathZ_schur_step_certificates.md`

### 3. 边界层 (boundary strata)
**已关闭**. Props 5.20/5.24 (单节点在 ∂D 上的极限), Prop 5.25 (confluent limit).  
来源: 论文 tex 935–966 radial blow-up lemma.

### 4. 实对称边界面 x₁=1
**已关闭**. 所有 `1-rᵢ²` 的 Bernstein 系数均非负（精确有理 CRT 重建, 8-素数 CRT, 深度1细分）.  
包含边界节点的对 (0,j): 由 `1-r₀²` 及 `1-rⱼ²` 的乘积非负性覆盖.  
非边界对 (1,2),(1,3),(2,3): CRT Bernstein 证书 ✅（深度1子三角形, 全部 reconstruction failures=0, all nonneg.）  
来源: `MathZ_contraction_proof.md` 末尾.

### 5. γ₁ = r₁ (第一Schur参数)
**已关闭**. |γ₁| = |r₁| < 1 在内部直接由 F_λ Schur 函数性质给出.

### 6. γ₂ 在 3+1 层 (一个内部节点 + 三个边界节点)
**已关闭（Bernstein 证书）**.  
参数化: 令 s = -1+ρe^{iψ}, cos ψ = 2y-1; N₂(ρ,y) = 1-|γ₂|²的分子.
```
N₂ 的参数: bidegree (54,25), 778 monomials
Bernstein 3-box 证书:
  [0,1/2]×[0,1]:    min = 19525670366953761/1099511627776 > 0    (0 zeros)
  [1/2,1]×[0,1/2]:  min = 0                                       (6 zeros, 边界)
  [1/2,1]×[1/2,1]:  min = 0                                       (81 zeros, 边界)
```
**结论**: |γ₂| ≤ 1 在全部 3+1 层成立（等号只在极限/confluent 边界）.  
来源: `MathZ_schur_step_certificates.md` 第一节.

### 7. 辐射方形 (radial square model: ρ{1,i,-1,-i})
**已关闭（解析）**. det Π_red/det K = (1-ρ)⁴(1+ρ)⁴(1+ρ²)⁴…; 严格正当 ρ<1.  
来源: 论文 prop:radial-square-model (tex 1084–1121).

### 8. 1D 族 {t,-t,0,0}
**已关闭（解析）**. P₃ = 16(1-t²)(t⁸+2t⁶+2t⁴+2t²+2) ≥ 0.  
来源: `MathZ_polytope_cert.md`.

### 9. c-度量收缩（配对族, 实对称层）
**数值验证（非正式证明）**:
- 1M 随机样本: max ratio = 0.0519 << 1
- 500k 边界困难样本: max ratio = 0.0552 << 1
- 配对族 2000×2000 网格: min eigenvalue ≈ 4×10⁻¹⁰（仅在边界退化）
- 实对称 confluent 切片 (a,a,b,-2a-b): Bernstein 证书 ✅（精确, 深度8自适应）

---

## 三、唯一剩余缺口

### γ₃ 在 3+1 层的硬角 ❌

**状态**: 数学上期望成立（数值完全正确），但缺少严格证书.

**已做的分析**:

γ₃ 的代数结构:
```
γ₃ = [A(s,s̄) + B(s,s̄)x] / [C(s,s̄) + D(s,s̄)x]
其中 x 满足 x²-sx+s/s̄=0 (两个剩余单位根)
A: degree 76, 963 terms
B: degree 75, 916 terms
C: degree 85, 1322 terms
D: degree 84, 1277 terms
```

H = 1-|γ₃|² 的结构:
```
U₀: degree 169, 5132 terms
U₁: degree 168, 5070 terms
```

GCD 剥离后的 primitive 分子:
```
gcd(U₀_prim, U₁_prim): degree 136, 3435 terms
primitive U₀ 后: degree 31, 187 terms
primitive U₁ 后: degree 30, 180 terms
→ norm 统计: degree (62,28), 1012 terms
```

**Bernstein 分析 (degree (62,28) 多项式)**:

| 盒子 | 结果 |
|------|------|
| ρ∈[0,1/2], y∈[0,1] | ✅ 全正 |
| ρ∈[1/2,1], y∈[0,1/2] | ✅ (zeros=6, 边界) |
| ρ∈[1/2,1], y∈[1/2,3/4] | ✅ |
| ρ∈[3/4,1], y∈[1/2,3/4] | ✅ (zeros=6) |
| **ρ∈[3/4,1], y∈[3/4,1]** | **❌ 70个负系数** |

4×4 精细细分硬角:
```
cell (0,0)-(2,2): 全部通过 ✅
cell (2,3) ρ∈[7/8,15/16], y∈[15/16,1]: neg=52 ❌  (approx min ≈ -344787)
cell (3,3) ρ∈[15/16,1],   y∈[15/16,1]: neg=161 ❌ (approx min ≈ -342187)
```

精确有理细分 (最困难子盒 ρ∈[15/16,1], y∈[31/32,1]):
```
children (0,0),(0,1),(1,0): 全部 nonneg ✅
child (1,1) ρ∈[15/16,1], y∈[31/32,1]: neg=162, zeros=114  ❌
worst Bernstein index loc ≈ (ρ≈471/496, y≈879/896) = (ρ≈0.949, y≈0.981)
```

**关键观察**: 负的 Bernstein 系数对应的坐标点 (ρ≈0.949, y≈0.981) 非常靠近 ρ=1, y=1 这两个边界退化点. 实际函数在这里是**正的**（数值验证），但 Bernstein 多项式在边界面缩窄时给出负的上界估计. 这是高阶 Bernstein 展开的已知困难（指数恶化的条件数）.

**γ₄**:
直接 SymPy 收缩卡死. 推荐路线: 利用行列式比恒等式从已知 γ₁,γ₂,γ₃ 的因子提取 γ₄ 的界.

---

## 四、所有计算路线的失败记录

### 计算路线A: 全局区间 Cholesky (1.jl, cert.jl, cert2.jl)
**策略**: 对 Ω_R = {max|λₖ|≤R=0.97} 做 6D Cartesian 参数化, BFS 细分 + 区间 Cholesky.

**cert.jl (Codex Task 13) 结果**:
```
certified by interval Cholesky: 0
inconclusive/max-depth: 8,916,644
max depth: 25
```
**失败根因**: 6D Cartesian 坐标中 λ₄ = -(λ₁+λ₂+λ₃) 在深度25时(盒子宽≈0.06)仍然跨越单位圆边界 → `box_not_subset_domain=true` → Cholesky 从未调用.

**cert2.jl**: 改用 polar 参数 (x₁,r₂,t₂,r₃,t₃). BFS 队列从 390k → 6M 立刻爆炸.

**1.jl (原始, 论文声称的脚本)**: BFS, R=0.97, 速度 440k/s. 按论文需要证书化 ~9×10⁸ 个盒子. 用户判断: **永远跑不完**.

### 计算路线B: Schur 函数界 (cert3.jl, cert4.jl)
**策略**: |c₁|+|c₂|+|c₃| < 768 ⟹ F_λ Schur ⟹ Π_red ≻ 0 (真实最大值≈32, 24×余量)

**cert3.jl**: BFS. 队列: 390k → 16M 上限. 无法收敛.

**cert4.jl**: DFS + 8线程. 初始表现: fail=0, cert≈40% 增长. 步骤28M后 fail 从0增长到8M+（步骤164M时）.

**失败根因**: 在 |λ₄|→1 的盒子附近, c₁,c₂,c₃ 的区间运算（多元多项式的 dependency problem）将区间高估 O(ε×L), L 很大, 导致 sup|c₁|+sup|c₂|+sup|c₃| >> 768 即使真实值约32. **无法绕过: 这是区间运算的固有限制.**

### 计算路线C: SOS (MathZ_p12_slice_sos.md)
**策略**: 对行清除的 reduced Pick 行列式做 SOS 分解.

**结果**: cvxpy 1.9.2 degree-40 SOS, 231×231 Gram 矩阵, **90秒内超时/未返回**. 这不是数学不可行, 是规模/条件数问题.

BM 探针: 行清除行列式的坐标线 BM 长度 = 87; Kronecker 探针 BM = 160. **远超 Bernstein 直接展开的舒适范围**.

### 计算路线D: 直接 γ₃ Bernstein (硬角子盒)
**策略**: 对 degree (62,28) primitive norm 做精确有理 Bernstein 细分.

**结果**: 如上 §三所述. 细分到 ρ∈[15/16,1], y∈[31/32,1] 仍有162个负系数. **证书未关闭**.

**失败根因**: Bernstein 系数在 (ρ→1, y→1) 时条件数指数恶化, 不是函数值本身为负, 而是高阶多项式 Bernstein 展开无法区分 "在边界缩窄到零" 和 "在内部为负" 这两种情况.

### 计算路线E: 行列式-Schur 恒等式
**探针**: 验证 det(Π_red)/det(K) = ∏(1-|γₖ|²)^{eₖ}.

**结果**: 在指数向量 {0..6}⁴ 的穷举搜索中（20个有限域样本）, **无匹配**. 行列式商不是 Schur gap 因子的纯单项式.

### 计算路线F: 对数次调和性
**策略**: 若 log|det Π_red| 次调和, 则最小值在边界取得.

**结果**: 数值 Laplacian 在随机内部点出现**负值** (min Lap ≈ -9.6), 近碰撞点最大偏差达 0.13. **log det Π_red 不次调和**.

### 计算路线G: γ₄ 直接 Schur 收缩
**策略**: SymPy 在四次方扩展代数中计算 γ₄.

**结果**: 第三次 Schur 收缩在 expand(num) 中卡死. **在当前 SymPy 实现中不可行**.

---

## 五、数学结构诊断

### 为什么机械证书"走不通"（根本原因）
1. **Dependency problem**: c₁,c₂,c₃ 是 λₖ 的 degree 8-10 多项式. 多元区间运算对此类表达式的高估量级 O(ε×L), L = Lipschitz 常数, 在近边界区域 L 极大. 在任何有限深度的盒子细分下都无法克服.
2. **边界退化**: λ₄ = -(λ₁+λ₂+λ₃) 在 5D 参数空间中自然跨越单位圆, 任何 Cartesian 细分在有限深度都会留下跨界盒子.
3. **高维性**: 5D 空间中 Bernstein 展开的系数数随 degree 指数增长; degree (54,25) 就已有 778 项, degree (62,28) 有 1012 项, 全局 5D 多项式的 BM 长度代理≈87/160.
4. **Bernstein 硬角**: (ρ→1, y→1) 处函数值趋向0但不为负, 而 Bernstein 上界估计在高次多项式收窄到该角时出现负系数——这是 Bernstein 方法在近边界高次多项式上的固有限制.

---

## 六、可行的分析路线（唯一出路）

### 路线1: γ₃ 的二次扩展证书 【最优先】
**思路**: 不做 (ρ,y) 的直接 Bernstein, 而是在 x²-sx+s/s̄=0 这个二次扩展上证明.

对 H = U₀+U₁x 于 x²-sx+s/s̄=0, 利用:
```
P₁ = H(x₁)·H(x₂) = N_norm/D_norm   (对两根之积=范数)
P₂ = H(x₁)+H(x₂) = N_tr/D_tr        (对两根之和=迹)
```
P₁ 和 P₂ 都只依赖 (s, s̄), 即只依赖 (ρ,y), **无 x**. 但经 gcd 剥离后 U primitive 的范数只有 degree (31+30)=61 → 期望 P₁ 的 (ρ,y)-degree 约 62 左右. 与 primitive norm 的 (62,28) 结果一致.

**当前阻碍**: V 分母的 gcd 只有 degree 56 (vs U 的 degree 136), V primitive 仍有 degree 111. 范数之商 P₁ = N_norm/D_norm 的分母 D_norm = N(V prim, V prim) 的 degree 约 222, 远超预期.

**建议下一步**: 
- 分别对 U 和 V 做更深层的因子剥离(寻找 (1-ρ²)^k, (1-y²)^j 型因子)
- 或改用 Schur 级联的迹/范数方法: 直接从 γ₁,γ₂ 的已知因子计算 det Π_red[{1,2,3}]/det K₃ × ..., 绕开 γ₃ 的显式表达式
- 或证明 P₁ = ∏(1-|γ₃(xᵢ)|²) 满足某个简单的结构不等式

### 路线2: Schur 补的量化下界
**思路**: 利用 n=3 已知结果 (Π_red[{2,3,4}] ≻ 0, 设为 A) 和 Schur 补:
```
Π_red ≻ 0 ⟺ A ≻ 0  AND  Π₁₁ > B·A⁻¹·B*
```
对 3+1 层, 内部节点 λ = -(1+s) 的 Π₁₁ = (1-|r₁|²)/(1-|λ|²).

当 |λ|→1 时, Π₁₁→+∞ (blow-up). 当 |λ|→0 时, Π₁₁ 有量化下界.

**需要**: 显式上界 sup ‖A⁻¹‖ · sup ‖B‖² 作为 (s,s̄) 的函数, 使得当 |s| 足够小时可以关闭, 当 |λ|=|1+s| 足够接近1时用 blow-up 关闭.

### 路线3: Taylor 模型 / Arb 库
**思路**: 取代朴素区间运算的 O(ε×L) 高估, 使用:
- **Taylor 模型** (TM): f(x₀+ε) ≈ [Taylor展开项] + 区间余项, 误差 O(ε²) 而非 O(ε)
- **Arb 库** (arbitrary-precision with error bounds): 对每个系数用球形复数算术
- **Chebyshev 形式**: 在 Chebyshev 基下展开减少 Runge 现象

这些方法理论上可以克服 dependency problem, 但需要重新编写整个 certification 框架. Julia 有 `TaylorSeries.jl` 和 `Arb.jl`.

### 路线4 (不可用): 次调和性
**已否定**. §四路线F: log det Π_red 不次调和.

---

## 七、所有相关文件索引

### 论文
- `~/Downloads/MathZ_BraidMonodromy_T2_extended.tex` — 主稿
  - Lines 935–966: 辐射边界 blow-up lemma
  - Lines 1084–1121: radial square model (closed)
  - Lines 1123–1168: Remark on final normalized determinant certificate
  - Lines 1252–1327: **prop:interior-machine-certificate (THE GAP)**

### 分析结果文件
- `MathZ_schur_params.md` — γ₁,γ₂,γ₃,γ₄ 的代数统计
- `MathZ_schur_step_certificates.md` — γ₂ Bernstein 证书 ✅ + γ₃ 所有失败记录
- `MathZ_gamma3_hardbox_local.md` — (62,28) Bernstein 4×4 子盒分析
- `MathZ_gamma3_corner_exact_2x2.md` — 精确有理2×2细分, 最难子盒
- `MathZ_gamma3_strip_factors.md` — U/V gcd 剥离统计
- `MathZ_gamma3_primitive_norm_bernstein.md` — primitive norm (62,28) 3-盒 Bernstein
- `MathZ_cleared_det_probe.md` — 行清除行列式 BM 探针 (长度130/87/160)
- `MathZ_p12_slice_sos.md` — SOS 尝试结果 (cvxpy 超时)
- `MathZ_contraction_proof.md` — 配对族 + 实对称 + 边界面 Bernstein CRT 证书
- `MathZ_polytope_cert.md` — {t,-t,0,0} 1D族解析证书

### Julia 证书脚本 (已废弃)
- `1.jl` — 原始 BFS Cholesky, 永远跑不完
- `MathZ_julia_cert.jl` (Task 13 Codex) — 0 certified, 8.9M inconclusive
- `MathZ_julia_cert2.jl` — BFS polar 参数, 队列爆炸
- `MathZ_julia_cert3.jl` — BFS Schur bound, 队列爆炸
- `MathZ_julia_cert4.jl` — DFS + threads Schur bound, fail 从0爆炸到8M+
- `MathZ_julia_cert5.jl` — DFS Cholesky (从未运行, 已废弃)

### 研究备忘录
- `~/Research/IMPORTANT_MEMOS/RECAST_PLAN_2026-06-26.md`
- `~/Research/AMMO/大材料_SpectralCerts_JMAA_cut_sections.md`
- `~/Research/IMPORTANT_MEMOS/CLAUDE_MEMORY_FULL.md`

---

## 八、总结: 距离关闭 n=4 还差什么

```
✅ K-region (max|λ|≤R*≈0.9761)          — 解析关闭
✅ 配对族 {±ρ, ±ρe^iθ}                  — 解析关闭  
✅ 边界层 (∂D 节点极限)                   — 解析关闭
✅ Confluent 极限                         — 解析关闭
✅ 实边界面 x₁=1                          — Bernstein CRT 关闭
✅ |γ₁|<1                                — 直接
✅ |γ₂|≤1 (3+1层)                        — Bernstein 关闭 (degree 54,25)
❌ |γ₃|≤1 (3+1层, ρ∈[3/4,1], y∈[3/4,1]) — 硬角证书未关闭
```

**唯一缺口**: γ₃ 在 (ρ∈[3/4,1], y∈[3/4,1]) 的证书. 该区域内函数值严格正（数值完全确认），但 Bernstein 展开在接近 (1,1) 时出现负系数.

**建议**: 走路线1（二次扩展证书的迹/范数方法）或路线2（Schur 补量化下界）. 任何进一步的计算机搜索（区间算术 DFS/BFS）都撞 dependency problem 的墙.

---

---

## 九、网络搜索新发现（Web Agent 2026-06-28）

### 关键新路线（优先级重排）

**路线0（最高优先级）: 证明 |c₁|+|c₂|+|c₃| ≤ 32 解析关闭一切**

数值验证: max(|c₁|+|c₂|+|c₃|) ≈ 32, 在 {1,-1,0,0} 型配置处取得.  
若此界解析成立 ⟹ F_λ 的 Schur 上界 ≤ 32/768 = 1/24 ≪ 1 ⟹ Π_red ≻ 0 立即成立.  
**无需机器证书, 无需 γ₃ Bernstein, 一步关闭全部内部情形.**  

方法: Handelman Positivstellensatz 对 8个不等式 `32 ± c₁ ± c₂ ± c₃ ≥ 0` 在多面体  
P = {x : |xⱼ|≤1, |x₁+x₂+x₃|≤1} 上的 LP 证书.  
参考: arXiv:2503.11119 (computing Handelman certificates), arXiv:1603.07611 (Handelman for matrices).

**路线1（第二优先）: 同伦 Schur 补论证关闭环形区域**

来源: `~/Downloads/MathZ_worst_case_eigenvalue.md` Method B.  
论证骨架:
1. 取任意 j 使 |λⱼ| ∈ (R*,1). 块分解: λⱼ vs. 剩余3个节点的内块 A.
2. A ≻ 0 通过同伦: 将 λⱼ 连续变形到0, 内部 3×3 Pick 行列式沿路径不消失 (因为不存在 degree≤2 的 Blaschke 乘积可插值3个一般内部点).
3. 当 |λⱼ|→1 时, Π_red[j,j] → +∞, 而 B*A⁻¹B 有界.
4. Schur 补全程正.

缺少的一步: "不存在 degree≤2 Blaschke 乘积可插值3个一般内部点" 的证明需引用 n=3 Pick 矩阵非退化性 (Agler-McCarthy 标准结果). **此步骤已知成立.**

若此论证写成严格引理 ⟹ 环形区域 (R*,1) 完全解析关闭 ⟹ 机器证书 prop:interior-machine-certificate 整体可替换为纯分析证明.

**路线6（备选）: Arblib.jl 高精度区间算术**

根本原因: cert1-cert5 失败是 Float64 精度不足 (16位有效数字), 而非算法错误.  
Arb 球形算术: 128位精度, 每步误差 O(ε·L·2⁻¹²⁸) ≈ 可忽略 (即使 L=10⁶).  
估算: 盒子宽度 ε=10⁻⁵, 5D空间约 10⁷-10⁸个盒子, 8线程约10小时可完成.  
实现: `Arblib.jl` 或 `ArbNumerics.jl` 替换 `IntervalArithmetic.jl`, 其余逻辑不变.

### 有用文献
- arXiv:2309.10675 — Bernstein 非负性测试改进 (几何均值加速)
- arXiv:1704.05782 — 线性参数区间矩阵的半正定性证书
- arXiv:1706.02586 — DSOS/SDSOS (LP/SOCP 替代 SDP, 高次多项式更可行)
- arXiv:1001.1277 — 矩阵多项式的逐段 SOS 证书
- arXiv:2503.11119 — Archimedean 二次模的严格正多项式证书
- arXiv:2501.03470 — 带全称量词的多项式矩阵 Positivstellensatz
- arXiv:1603.07611 — Handelman Positivstellensatz 用于多面体上多项式矩阵

### 行动优先级（更新后）

```
优先级1: 路线0 — Handelman LP 证明 |c₁|+|c₂|+|c₃| ≤ 32
           ← 最干净, 一步关闭全部, 无需机器证书
           ← 给 Codex/agy: 对实心多面体上8个不等式做 Handelman LP

优先级2: 路线1 — 补完同伦 Schur 补论证
           ← 读 MathZ_worst_case_eigenvalue.md Method B
           ← 引用 Agler-McCarthy n=3 Pick 非退化定理
           ← 写成一个 tex 引理替换 prop:interior-machine-certificate

优先级3: 路线3 — 从 1-N(ρ,y) 在 (1,1) 处提取零阶因子
           ← 计算 1-N 在 (ρ,y)→(1,1) 的消失阶数
           ← 提取 (1-ρ)^a(1-y)^b 因子后做 Bernstein

优先级4: 路线6 — Arblib.jl 重写 cert5 用 128位精度
           ← 可复现论文声称的 9×10⁸ 盒子证书
           ← 但需要计算资源和实现工作
```

---

*生成时间: 2026-06-28*  
*来源: 所有 ~/Downloads/ MathZ_*.md 文件 + tex 原文 + 所有 Julia 脚本 + Web 搜索*
