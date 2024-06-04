import math
import numpy


class Math:
    @staticmethod
    def x2y_by_polynomial_regression(x, x_list, y_list, degree: int = 2):
        """
        :param x: 获取y需要对应的x
        :param x_list: 基础x数组
        :param y_list: 基础y数组
        :param degree: 幂
        :return: 返回 x对应的y
        """
        cs = numpy.polyfit(x_list, y_list, degree)
        r = 0.0
        for i in range(degree, 0, -1):
            r += pow(x, i) * cs[degree - i]
        r += cs[-1]
        return r

    @staticmethod
    def ring_volume_weight(diameter: float, height: float, inner_diameter: float = 0, margin: float = 0,
                           density: float = 1):
        diameter += 2 * margin
        height += 2 * margin
        if inner_diameter < 2 * margin:
            inner_diameter = 0
        else:
            inner_diameter -= 2 * margin
        vol = math.pi * (pow(diameter / 2, 2) - pow(inner_diameter / 2, 2)) * height
        return vol * density

    @staticmethod
    def ring_min_diameter_by_pressure(inner_diameter: float = 0, weight: float = 1000000,
                                      safety_ratio: float = 5, yield_strength: float = 27.6):
        """
        :param inner_diameter: mm
        :param weight: kgs 默认按1000吨硫化机压力
        :param safety_ratio: num 安全系数 默认 5 倍
        :param yield_strength: kgs/mm^2 默认ZG 270-500 铸钢的 屈服强度 YIELD STRENGTH (/Mpa) 270 N/mm2 (27.6 kgf/mm2)
        :return: minimal_diameter: mm
        """
        area = weight / yield_strength * safety_ratio
        return pow(area / math.pi + pow(inner_diameter / 2, 2), 0.5) * 2