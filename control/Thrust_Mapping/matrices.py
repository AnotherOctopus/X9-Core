import Vectors


class Matrices(object):
    """Container Class """

    @staticmethod
    def dot6(a, b):
        """a and b should be vect6 objects"""
        return Matrices.dot(a.L, b.L) + Matrices.dot(a.R, b.R)

    @staticmethod
    def dot(a, b):
        """a and b should be vect3 objects"""
        return a.x * b.x + a.y * b.y + a.z * b.z

    @staticmethod
    def dot2(a, b):
        """a and b should be vect2 objects"""
        return a.a * b.a + a.b * b.b

    @staticmethod
    def cross(a, b):
        """returns the cross product of a and b"""
        x = a.y * b.z - a.z * b.y
        y = a.z * b.x - a.x * b.z
        z = a.x * b.y - a.y * b.x
        return Vectors.vect3(x, y, z)

    @staticmethod
    def add(a, b):
        """adds the sum of vectors a and b"""
        x = a.x + b.x
        y = a.y + b.y
        z = a.z + b.z
        return Vectors.vect3(x, y, z)

    @staticmethod
    def add6(a, b):
        """adds the sum of the vect6s a and b"""
        L = Matrices.add(a.L, b.L)
        R = Matrices.add(a.R, b.R)
        return Vectors.vect6(L.x, L.y, L.z, R.x, R.y, R.z)

    @staticmethod
    def sub(a, b):
        """subtract vector b from vector a"""
        x = a.x - b.x
        y = a.y - b.y
        z = a.z - b.z
        return Vectors.vect3(x, y, z)

    @staticmethod
    def sub6(a, b):
        """subtract b from a"""
        L = Matrices.sub(a.L, b.L)
        R = Matrices.sub(a.R, b.R)
        return Vectors.vect6(L.x, L.y, L.z, R.x, R.y, R.z)

    @staticmethod
    def mul(a, factor):
        """multiply vector a by factor"""
        x = a.x * factor
        y = a.y * factor
        z = a.z * factor
        return Vectors.vect3(x, y, z)

    @staticmethod
    def mul6(a, factor):
        """multiply vact6 a by factor"""
        L = Matrices.mul(a.L, factor)
        R = Matrices.mul(a.R, factor)
        return Vectors.vect6(L.x, L.y, L.z, R.x, R.y, R.z)

    @staticmethod
    def div(a, factor):
        """multiply vector a by factor"""
        x = a.x / factor
        y = a.y / factor
        z = a.z / factor
        return Vectors.vect3(x, y, z)

    @staticmethod
    def div6(a, factor):
        """multiply vact6 a by factor"""
        L = Matrices.div(a.L, factor)
        R = Matrices.div(a.R, factor)
        return Vectors.vect6(L.x, L.y, L.z, R.x, R.y, R.z)

    @staticmethod
    def max3(vect):
        """max value in vect3"""
        return max(vect.a.x, vect.a.y, vect.a.z)

    @staticmethod
    def max6(vect):
        """return the max value in vect6"""
        return max(vect.L.x, vect.L.y, vect.L.z, vect.R.x, vect.R.y, vect.R.z)

    @staticmethod
    def max8(vect):
        """return the max value in vect8"""
        return max(vect.a, vect.b, vect.c, vect.d, vect.e, vect.f, vect.g, vect.h)

    @staticmethod
    def matMul_86x61(mat, v):
        """return the resulting vect8 generated by multiplying a matrix8_6 by a vect6"""
        a = Matrices.dot6(mat.t1, v)
        b = Matrices.dot6(mat.t2, v)
        c = Matrices.dot6(mat.t3, v)
        d = Matrices.dot6(mat.t4, v)
        e = Matrices.dot6(mat.t5, v)
        f = Matrices.dot6(mat.t6, v)
        g = Matrices.dot6(mat.t7, v)
        h = Matrices.dot6(mat.t8, v)
        return Vectors.vect8(a, b, c, d, e, f, g, h)

    @staticmethod
    def matMul_33x31(m, v):
        """return the resulting vect3 generated by multiplying a matrix3_3 by a vect3"""
        x = Matrices.dot(m.a, v)
        y = Matrices.dot(m.b, v)
        z = Matrices.dot(m.c, v)
        return Vectors.vect3(x, y, z)

    @staticmethod
    def matMul_22x22(a, b):
        """both inputs are matrix2_2"""
        a1 = Matrices.dot2(a.one, Vectors.vect2(b.one.a, b.two.a))
        b1 = Matrices.dot2(a.one, Vectors.vect2(b.one.b, b.two.b))
        one = Vectors.vect2(a1, b1)
        a2 = Matrices.dot2(a.two, Vectors.vect2(b.one.a, b.two.a))
        b2 = Matrices.dot2(a.two, Vectors.vect2(b.one.b, b.two.b))
        two = Vectors.vect2(a2, b2)
        return Vectors.matrix2_2(one, two)

    @staticmethod
    def invert2_2(m):
        det = m.one.a * m.one.b - m.one.b * m.two.a
        a1 = m.two.b * 1024 / det
        b1 = -m.one.b * 1024 / det
        a2 = -m.two.a * 1024 / det
        b2 = m.one.a * 1024 / det
        one = Vectors.vect2(a1, b1)
        two = Vectors.vect2(a2, b2)
        return Vectors.matrix2_2(one, two)