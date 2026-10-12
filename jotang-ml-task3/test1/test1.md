对于函数
取一组你自己选择的 x 和 y：

1. 把计算过程拆成若干个简单步骤，并画出计算图；
- \(\begin{align*}
a &= x\cdot y \\
b &= x^2 \\
c &= a + b \\
f &= c^2
\end{align*}\)
- 
x ──┬──→ a = x*y
    └──→ b = x²
y ─────→ a = x*y
a,b ───→ c = a + b
c  ───→ f = c²

2. 写一段 NumPy 代码，按照计算图从后向前计算梯度；
test1.ipynb
3. 使用 PyTorch 的 autograd 检查自己的结果是否一致。
test1.ipynb
