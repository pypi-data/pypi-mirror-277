import numpy as np
import re

class Space:
    
    def __init__(self, p1 = None, p2 = None, points = None, p3 = None, line = None, circle = None):
        """
        line is like -> [ P, P] or -> [(i,j), (i,j)] -> it is two points!
        p is (i, j) -> is two axis atleast -> (i, j ,k) for 3 dim
        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.points = points
        self.line = line
        self.circle = circle
        self.__check_points__()
    
    def __check_points__(self):
        if self.p1 is not None and not isinstance(self.p1, tuple) or not isinstance(self.p1, float) or not isinstance(self.p1, int):
            if self.points is None:
                self.points = self.p1
                self.p1 = None
            else:
                if isinstance(self.p1 , list) :
                    self.p1_arr = np.asarray(self.p1)
                    self.p1 = None
                elif isinstance(self.p1, np.ndarray):
                    self.p1_arr =self.p1
                    self.p1 = None
                else:
                    raise TypeError(" 'p' should be of type int or float or tuple represented a single point. ")
        if self.p2 is not None and not isinstance(self.p2, tuple) and not isinstance(self.p2, float) and not isinstance(self.p2, int):
            if self.points is None:
                self.points = self.p2
                self.p2 = None
            else:
                if hasattr(self, 'p1_arr'):
                    raise TypeError(" 'p' should be of type int or float or tuple represented a single point. ")
                elif isinstance(self.p2 , list) :
                    self.p1_arr = np.asarray(self.p2)
                    self.p2 = None
                elif isinstance(self.p2, np.ndarray):
                    self.p1_arr = self.p2
                    self.p2 = None
                else:
                    raise TypeError(" 'p' should be of type int or float or tuple represented a single point. ")
        if self.p3 is not None and not isinstance(self.p3, tuple) and not isinstance(self.p3, float) and not isinstance(self.p3, int):
            if self.points is None:
                self.points = self.p3
            else:
                raise TypeError(" 'p' should be of type int or float or tuple represented a single point. ")
        if isinstance(self.points , list) :
            if not hasattr(self, 'points_arr'):
                self.points_arr = np.asarray(self.points)
            else:
                if hasattr(self, 'p1_arr'):
                    raise ProcessLookupError("There is no space left for this points. please use a fresh class! ")
                else:
                    self.p1_arr = np.asarray(self.points)
        elif isinstance(self.points, np.ndarray):
            if not hasattr(self, 'points_arr'):
                self.points_arr = self.points
            else:
                if hasattr(self, 'p1_arr'):
                    raise ProcessLookupError("There is no space left for this points. please use a fresh class! ")
                else:
                    self.p1_arr = self.points
        else:
            raise TypeError(" 'points' should be of type list or numpy.ndarray represented a series of points. ")
        self.__handle_points__()
    
    def __handle_points__(self):
        
        points_z = None
        self.points_x = self.points_arr[:,0]
        self.points_y = self.points_arr[:,1]
        try:
            points_z = self.points_arr[:,2]
        except:
            pass
        if points_z is not None:
            self.points_z = points_z
            points_z = None
        if hasattr(self, 'p1_arr'):
            p1_z = None
            self.p1_x = self.p1_arr[:,0]
            self.p1_y = self.p1_arr[:,1]
            try:
                p1_z = self.p1_arr[:,2]
            except:
                pass
            if p1_z is not None:
                self.p1_z = p1_z
        self.__find_min__()
        self.__find_max__()
    
    def __find_min__(self):
        self.points_x_sorted = np.sort(self.points_x, axis=0)  #  np.min(self.points_x)
        points_x_min_i = self.points_x_sorted[0]  #  np.min(self.points_x)
        points_x = list(self.points_x)
        points_x_min_i_where = points_x.index(points_x_min_i)
        points_x_min_j = self.points_y[points_x_min_i_where]
        self.points_y_sorted = np.sort(self.points_y, axis=0)
        points_y_min_j =  self.points_y_sorted[0]  #np.min(self.points_y)
        points_y = list(self.points_y)
        points_y_min_j_where = points_y.index(points_y_min_j)
        points_y_min_i = self.points_x[points_y_min_j_where]
        if hasattr(self, 'points_z'):
            self.points_z_sorted = np.sort(self.points_z, axis=0)
            points_z_min_k = self.points_z_sorted[0]     #np.min(self.points_z)
            points_z = list(self.points_z)
            points_z_min_k_where = points_z.index(points_z_min_k)
            points_z_min_i = self.points_x[points_z_min_k_where]
            points_z_min_j = self.points_y[points_z_min_k_where]
            points_x_min_k = self.points_z[points_x_min_i_where]
            points_y_min_k = self.points_z[points_y_min_j_where]
            self.points_z_min = (points_z_min_i, points_z_min_j,points_z_min_k)
            self.points_x_min = (points_x_min_i, points_x_min_j, points_x_min_k)
            self.points_y_min = (points_y_min_i, points_y_min_j, points_y_min_k)
        else:
            self.points_x_min = (points_x_min_i, points_x_min_j)
            self.points_y_min = (points_y_min_i, points_y_min_j)
        if hasattr(self, 'p1_arr'):
            self.p1_x_sorted = np.sort(self.p1_x, axis=0)
            p1_x_min_i = self.p1_x_sorted[0] #np.min(self.p1_x)
            p1_x = list(self.p1_x)
            p1_x_min_i_where = p1_x.index(p1_x_min_i)
            p1_x_min_j = self.p1_y[p1_x_min_i_where]
            self.p1_y_sorted = np.sort(self.p1_y, axis=0)
            p1_y_min_j = self.p1_y_sorted[0] #np.min(self.p1_y)
            p1_y = list(self.p1_y)
            p1_y_min_j_where = p1_y.index(p1_y_min_j)
            p1_y_min_i = self.p1_x[p1_y_min_j_where]
            if hasattr(self, 'p1_z'):
                self.p1_z_sorted = np.sort(self.p1_z, axis=0)
                p1_z_min_k = self.p1_z_sorted[0]
                p1_z = list(self.p1_z)
                p1_z_min_k_where = p1_z.index(p1_z_min_k)
                p1_z_min_i = self.p1_x[p1_z_min_k_where]
                p1_z_min_j = self.p1_y[p1_z_min_k_where]
                p1_x_min_k = self.p1_z[p1_x_min_i_where]
                p1_y_min_k = self.p1_z[p1_y_min_j_where]
                self.p1_z_min = (p1_z_min_i, p1_z_min_j,p1_z_min_k)
                self.p1_x_min = (p1_x_min_i, p1_x_min_j, p1_x_min_k)
                self.p1_y_min = (p1_y_min_i, p1_y_min_j, p1_y_min_k)
            else:
                self.p1_x_min = (p1_x_min_i, p1_x_min_j)
                self.p1_y_min = (p1_y_min_i, p1_y_min_j)
    
    def __find_max__(self):
        self.positive_sorted_x = self.points_x_sorted[::-1]
        self.positive_sorted_y = self.points_y_sorted[::-1]
        points_x_max_i = self.positive_sorted_x[0]
        points_x = list(self.points_x)
        points_x_max_i_where = points_x.index(points_x_max_i)
        points_x_max_j = self.points_y[points_x_max_i_where]
        points_y_max_j = self.positive_sorted_y[0]
        points_y = list(self.points_y)
        points_y_max_j_where = points_y.index(points_y_max_j)
        points_y_max_i = self.points_x[points_y_max_j_where]
        if hasattr(self, 'points_z'):
            self.positive_sorted_z = self.points_z_sorted[::-1]
            points_z_max_k = self.positive_sorted_z[0]
            points_z = list(self.points_z)
            points_z_max_k_where = points_z.index(points_z_max_k)
            points_z_max_i = self.points_x[points_z_max_k_where]
            points_z_max_j = self.points_y[points_z_max_k_where]
            points_x_max_k = self.points_z[points_x_max_i_where]
            points_y_max_k = self.points_z[points_y_max_j_where]
            self.points_z_max = (points_z_max_i, points_z_max_j,points_z_max_k)
            self.points_x_max = (points_x_max_i, points_x_max_j, points_x_max_k)
            self.points_y_max = (points_y_max_i, points_y_max_j, points_y_max_k)
        else:
            self.points_x_max = (points_x_max_i, points_x_max_j)
            self.points_y_max = (points_y_max_i, points_y_max_j)
        if hasattr(self, 'p1_arr'):
            self.positive_sorted_p1_x = self.p1_x_sorted[::-1]
            self.positive_sorted_p1_y = self.p1_y_sorted[::-1]
            p1_x_max_i = self.positive_sorted_p1_x[0]
            p1_x = list(self.p1_x)
            p1_x_max_i_where = p1_x.index(p1_x_max_i)
            p1_x_max_j = self.p1_y[p1_x_max_i_where]
            p1_y_max_j =  self.positive_sorted_p1_y[0]
            p1_y = list(self.p1_y)
            p1_y_max_j_where = p1_y.index(p1_y_max_j)
            p1_y_max_i = self.p1_x[p1_y_max_j_where]
            if hasattr(self, 'p1_z'):
                self.positive_sorted_p1_z = self.p1_z_sorted[::-1]
                p1_z_max_k = self.positive_sorted_p1_z[0]
                p1_z = list(self.p1_z)
                p1_z_max_k_where = p1_z.index(p1_z_max_k)
                p1_z_max_i = self.p1_x[p1_z_max_k_where]
                p1_z_max_j = self.p1_y[p1_z_max_k_where]
                p1_x_max_k = self.p1_z[p1_x_max_i_where]
                p1_y_max_k = self.p1_z[p1_y_max_j_where]
                self.p1_z_max = (p1_z_max_i, p1_z_max_j,p1_z_max_k)
                self.p1_x_max = (p1_x_max_i, p1_x_max_j, p1_x_max_k)
                self.p1_y_max = (p1_y_max_i, p1_y_max_j, p1_y_max_k)
            else:
                self.p1_x_max = (p1_x_max_i, p1_x_max_j)
                self.p1_y_max = (p1_y_max_i, p1_y_max_j)
    
    def find_edges(self, n = 50, m = 50 , rotate = 0):
        edges = []
        points_x = list(self.points_x)
        points_y = list(self.points_y)
        change_map = [ ('positive_sorted_x','positive_sorted_y'), ('positive_sorted_x', 'points_y_sorted') , ('points_x_sorted','positive_sorted_y' ), ('points_x_sorted','points_y_sorted') ]
        for changes in change_map:
            first_arr = getattr(self, changes[0])
            second_arr = getattr(self, changes[1])
            first_arr_reRule = getattr(self, changes[1])
            second_arr_reRule = getattr(self, changes[0])
            first_arr_i = first_arr[:n]
            first_arr_reRule_i = first_arr_reRule[:m]
            first_arr_j = []
            first_arr_reRule_j = []
            if n != m :
                raise NotImplementedError()
            for i in range(len(first_arr_i)):
                temp_1 = first_arr_i[i]
                temp_2 = first_arr_reRule_i[i]
                tempx1 = re.search(r'_x' , changes[0])
                tempy1 = re.search(r'_y' , changes[0])
                tempx2 = re.search(r'_x' , changes[1])
                tempy2 = re.search(r'_y' , changes[1])
                if tempx1 is not None:
                    first_arr_i_where = points_x.index(temp_1)
                    first_arr_j.append(self.points_y[first_arr_i_where])
                elif tempy1 is not None:
                    first_arr_i_where = points_y.index(temp_1)
                    first_arr_j.append(self.points_x[first_arr_i_where])
                
                if tempx2 is not None:
                    first_arr_reRule_i_where = points_x.index(temp_2)
                    first_arr_reRule_j.append(self.points_y[first_arr_reRule_i_where])
                elif tempy2 is not None:
                    first_arr_reRule_i_where = points_y.index(temp_2)
                    first_arr_reRule_j.append(self.points_x[first_arr_reRule_i_where])
            second_arr_list = list(second_arr)
            second_arr_reRule_list = list(second_arr_reRule)
            second_where = second_arr_list.index(first_arr_j[0])
            second_reRule_where = second_arr_reRule_list.index(first_arr_reRule_j[0])
            second_max = second_arr[second_where:]
            second_reRule_max = second_arr_reRule[second_reRule_where:]
            second_max = list(second_max)
            second_reRule_max = list(second_reRule_max)
            for a, b in zip(first_arr_i,first_arr_j):
                if b in second_max:
                    if rotate == 0 or rotate == 2 :
                        edges.append((a,b))
                    elif rotate == 1 or rotate == 4:
                        edges.append((b,a))
            for p, q in zip(first_arr_reRule_i,first_arr_reRule_j):
                if q in second_reRule_max:
                    if rotate == 0 or 1:
                        edges.append((q,p))
                    elif rotate == 2 or rotate == 4:
                        edges.append((p,q))
        return np.asarray(edges)
    
#end#