
# 氧气液化
def liquid_oxygen_energy(nO2_vf, t1, t2):
    cp = 0.918  # 氧气的比热容(J/(g·K))
    M_O2 = 32   # 氧气的摩尔质量(g/mol)
    L = 213  # 氧气的液化潜热(J/g)

    nO2 = nO2_vf / 0.022414  # 氧气的摩尔
    m = nO2 * M_O2  # 氧气的质量(g)

    Q_cooling = m * cp * ()

