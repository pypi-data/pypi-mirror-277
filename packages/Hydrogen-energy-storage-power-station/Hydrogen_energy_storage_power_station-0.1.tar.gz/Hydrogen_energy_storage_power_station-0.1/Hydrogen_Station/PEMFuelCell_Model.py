import math
import numpy as np
from matplotlib import pyplot as plt

# https://blog.csdn.net/weixin_45896923/article/details/130532262
# 输入参数中，氢气和空气的压力对V-I曲线影响不大，但温度对曲线影响较大


# PEM燃料电池电压计算
def fuelcell_voltage(i_in, Tk, P_H2, P_air):     # i_in是输入电流
                                                # Tk是燃料电池运行温度 (K)
                                                # P_H2是氢气的输入压力 (atm)
                                                # P_air是空气的输入压力 (atm)
    DELTA_G = 237.2  # Gibbs energy (kJ/mol)
    F = 96485  # F是法拉第常数
    z = 2  # z是电子数量(氢)
    R = 8.314  # 理想气体常数 j/(mol*K)
    n = 4  # 每mol的O2转移的电子摩尔数
    Alpha = 0.25  # 传输系数
    i0 = 10 ** (-6.912)  # 交换电流密度
    iL = 1.41  # 极限电流密度
    r = 0.19  # 内阻 Ω/cm2
    T_H2O = 60  # 水蒸气的温度 (摄氏度)
    RH = 0.9869 # 相对湿度
    Et = (DELTA_G * 1000) / (z * F)  # reversible cell voltage


    # 压力计算及能斯特电压计算
    # 饱和水蒸气压力(Bar)
    P_sat = 10 ** (-2.1794 + 0.02953 * T_H2O - 9.1837e-5 * (T_H2O ** 2) + 1.4454e-7 * (T_H2O ** 3))
    # 相对湿度RH非100%时，水蒸气压力
    P_H2O = P_sat * RH
    # 电流密度 A/cm2
    i = 0.001 * i_in
    # 燃料电池阳极氢气压力
    PP_H2 = 0.5 * P_H2 / math.exp(1.653 * i / (Tk ** 1.334)) - P_H2O
    # 燃料电池阴极氧气压力
    PP_O2 = P_air / math.exp(4.192 * i / (Tk ** 1.334)) - P_H2O

    # 计算三部分电压损失
    B = R * Tk / (n * F * Alpha)
    V_act = -1 * B * math.log(i / i0)  # 极化损失V
    V_ohmic = -(i * r)  # 欧姆损失V
    term = 1 - i / iL
    if term > 0:
        V_conc = (R * Tk / n / F) * (1 + 1 / Alpha) * math.log(1 - (i / iL))    # 浓差极化损失V
    else:
        V_conc = 0

    # 能斯特电压计算包括温度修正
    V_nerst = Et - R * Tk * math.log(P_H2O / (PP_H2 * (PP_O2 ** 0.5))) / (2 * F)

    # 燃料电池电压
    V_out = V_nerst + V_act + V_ohmic + V_conc
    return V_out, i


# 燃料电池的耗氢量
def fuelcell_consumption(i):   # i为电流，而不是电流密度
    MH2 = 1.008  # MH2是氢气的摩尔质量(g/mol)
    F = 96485  # F是法拉第常数
    nH2 = MH2 * i / (2 * F)     # 氢气的摩尔流速 (mol/s)
    nH2_vf = nH2 * 3600 * 0.022414   # 氢气的消耗量 (Nm3/h)
    return nH2_vf


# 燃料电池运行曲线
def power_to_current_curve(Tk, P_H2, P_air):       # Tk是燃料电池温度(K),P_H2是氢气的输入压力(atm),P_air是空气的输入压力(atm)
    # 数据准备
    x = np.array([])  # Current(A)
    y = np.array([])  # Voltage(V)
    z = np.array([])  # Power(W)

    for i in range(1, 1400):
        v, i_dens = fuelcell_voltage(i, Tk, P_H2, P_air)
        x = np.append(x, [i_dens])
        y = np.append(y, [v])
        z = np.append(z, [v * i_dens])  # W/cm2

    max_P = z.max()

    return x, y, z, max_P


# 通过输出功率计算燃料电池电流、电压（邻近拟合）
def power_to_current(p, current, voltage, power):     # p是燃料电池输出功率, current, voltage, power是电解槽的运行曲线数据
    index = np.abs(power - p).argmin()
    i = current[index]
    v = voltage[index]
    return i, v


# if __name__ == '__main__':
