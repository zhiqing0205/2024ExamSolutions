n, m = map(int, input().split())
mod = 10 ** 9 + 7
m_n = pow(m, n, mod)
# print((m_n + (m - 1) / m * m_n * (n - 1) % mod) % mod)
print((m_n + (m - 1) * pow(m, n - 1, mod) * (n - 1) % mod) % mod)