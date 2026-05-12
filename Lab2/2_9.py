from support2_9 import GraphVisual as GV
from klas_menu import Menu
from L2_10 import floyd_path as FP, dijkstra_path as DP

class Edge:
    def __init__(self, u: int, v: int, weight: float = 1.0):
        self.u = u
        self.v = v
        self.weight = weight

    def __repr__(self):
        return f"Edge( {self.u} -> {self.v} : {self.weight})"

class JGraph:
    def __init__(self,cnt:int = 1, directed:bool = False, weighted:bool = False,name:str = "noname"):
        if cnt<1 :
            print("count of nodes can't be less then 1. value set's by 1")
            cnt=1
        self.__cnt = cnt                  #count
        self.__rts : list[Edge] = [ ]     #routes
        self.__directed = directed        #isDirected?
        self.__weighted = weighted        #isWeighted?
        self.name = name

    def addedge(self,a:int,b:int, weight:int = 1):
        a=self.__cnv_int(a);b=self.__cnv_int(b);weight=self.__cnv_int(weight)
        if not (0<=a < self.__cnt and 0<= b < self.__cnt):
            raise IndexError(f"edge start,end must be between 0 and {self.__cnt-1}")
        self.__rts.append(Edge(a,b,weight))

    def rmedge(self,index):
        index=self.__cnv_int(index)
        if not (0 <= index < len(self.__rts)) and (-len(self.__rts)<=index<0):
            raise IndexError(f"edges got index between 0 and {len(self.__rts)-1}")
        self.__rts.pop(index)

    def changecnt(self,new_cnt:int):
        new_cnt=self.__cnv_int(new_cnt)
        if new_cnt<1:
            raise IndexError("cnt can't be less then 1")
        if new_cnt < self.__cnt:
            self.__rts = [e for e in self.__rts if e.u < new_cnt and e.v < new_cnt]
        self.__cnt=new_cnt

    def ret_gr(self):
        return [self.__cnt,self.ret_rts(),self.__weighted,self.__directed,self.name]

    def ret_rts(self):
        return [[eg.u,eg.v,eg.weight] for eg in self.__rts]

    def ret_cnt(self):
        return self.__cnt

    def isDir(self):
        return self.__directed

    def setDir(self,val:bool):
        val=self.__cnv_2b(val)
        self.__directed=val

    def isWe(self):
        return self.__weighted

    def setWe(self,val:bool):
        val=self.__cnv_2b(val)
        self.__weighted=val

    def smezh_matrix(self, isW:bool = None, isD:bool = None) -> list[list[int | float]]:
        mat = [[0] * self.__cnt for _ in range(self.__cnt)]

        if isW is None:
            isW = self.__weighted
        else:
            isW = self.__cnv_2b(isW)

        if isD is None:
            isD = self.__directed
        else:
            isD = self.__cnv_2b(isD)

        for e in self.__rts:
            val = e.weight if isW else 1
            mat[e.u][e.v] = val
            if not isD:
                mat[e.v][e.u] = val

        return mat

    def indent_matrix(self,isW:bool = None, isD:bool = None) -> list[list[int | float]]:

        if isW is None:
            isW = self.__weighted
        else:
            isW = self.__cnv_2b(isW)

        if isD is None:
            isD = self.__directed
        else:
            isD = self.__cnv_2b(isD)

        mat = [[0] * self.__cnt for _ in range(len(self.__rts))]

        for e in range(len(self.__rts)):
            mat[e][self.__rts[e].u]= (self.__rts[e].weight if isW else 1) * ((-1)if isD else 1)
            mat[e][self.__rts[e].v]= self.__rts[e].weight if isW else 1

        return mat

    def indent_matrix_v2(self,isW:bool = None, isD:bool = None) -> list[list[int | float]]:

        if isW is None:
            isW = self.__weighted
        else:
            isW = self.__cnv_2b(isW)

        if isD is None:
            isD = self.__directed
        else:
            isD = self.__cnv_2b(isD)

        mat = [[0] * (self.__cnt + (1 if isW else 0)) for _ in range(len(self.__rts))]

        for idx,e in enumerate(self.__rts):
            mat[idx][e.u]= (-1)if isD else 1
            mat[idx][e.v]= 1
            if isW:
                mat[idx][self.__cnt] = e.weight

        return mat

    def show_smatrix(self):
        lines="\n >> Smejnost (N x N) <<\n"
        adj = self.smezh_matrix()
        lines += " v\\v|" + "".join(f" v{v:<3}|" for v in range(self.__cnt))+'\n'
        for i, row in enumerate(adj):
            lines+=(f" v{i:<2}|" + "".join(f"{str(val):>5}|" for val in row))+'\n'
        return lines

    def show_imatrix(self):
        lines ="\n >> Incedence (M x N) <<\n"
        inc = self.indent_matrix()
        lines+=" e\\v|" + "".join(f" v{v:<3}|" for v in range(self.__cnt))+'\n'
        for i, row in enumerate(inc):
            lines+=f" e{i:<2}|" + "".join(f"{str(val):>5}|" for val in row)+"\n"
        return lines

    def show_imatrix_v2(self):
        lines = "\n >> Incedence (M x N + [w]) <<\n"

        inc = self.indent_matrix_v2()

        header = " e\\v|" + "".join(f" v{v:<3}|" for v in range(self.__cnt))
        if self.__weighted:
            header += "  w  |"
        lines+=header+'\n'

        for i, row in enumerate(inc):
            row_str = "".join(f"{str(val):>5}|" for val in row[:self.__cnt])
            if self.__weighted and len(row) > self.__cnt:
                row_str += f"{row[self.__cnt]:>5}|\n"
            lines+=f" e{i:<2}|{row_str}\n"

        return lines

    def svzyaz_components(self):
        mat = self.smezh_matrix()
        n = self.__cnt
        visited = [False]*n
        components =[]
        for v in range(n):
            if not visited[v]:
                comp = []
                stack = []
                stack.append(v)
                visited[v] = True

                while len(stack) > 0:
                    curr = stack.pop()
                    comp.append(curr)

                    for j in range(n):
                        if mat[curr][j] != 0 and not visited[j]:
                            visited[j] = True
                            stack.append(j)

                comp.sort()
                components.append(comp)
        return components

    def find_strong_components(self) -> list[list[int]]:
        if not self.__directed:
            return self.find_components_via_matrix()

        n = self.__cnt
        adj = self.smezh_matrix()
        adj_t = [[adj[j][i] for j in range(n)] for i in range(n)]

        visited = [False] * n
        finish_order = []

        for start in range(n):
            if not visited[start]:
                stack = [start]
                visited[start] = True
                while stack:
                    v = stack[-1]
                    next_v = -1
                    for j in range(n):
                        if adj[v][j] != 0 and not visited[j]:
                            next_v = j
                            break
                    if next_v != -1:
                        visited[next_v] = True
                        stack.append(next_v)
                    else:
                        finish_order.append(stack.pop())

        visited = [False] * n
        sccs = []

        for v in reversed(finish_order):
            if not visited[v]:
                comp = []
                stack = [v]
                visited[v] = True
                while stack:
                    curr = stack.pop()
                    comp.append(curr)
                    for j in range(n):
                        if adj_t[curr][j] != 0 and not visited[j]:
                            visited[j] = True
                            stack.append(j)
                sccs.append(sorted(comp))

        return sccs

    def __repr__(self):
        lines = [
            "JGraph:",
            f"  isWeighted? : {self.__weighted}, isDirected? : {self.__directed}",
            f"  cnt : {self.__cnt}",
            "  Edges:"
        ]
        for eg in self.__rts:
            lines.append(f"    {repr(eg)}")

        lines+=self.show_smatrix()
        lines+=self.show_imatrix()
        lines+=self.show_imatrix_v2()


        return lines

    def Graphic_Graph(self):
        GV(cnt=self.__cnt,rts=self.ret_rts(),is_naprav=self.__directed,vzves=self.__weighted, gr_label=self.name)

    @staticmethod
    def __cnv_2b(val) -> bool:
        if isinstance(val, bool):
            return val
        return str(val).strip().lower() in ('true', '1', 'yes', 'on', 'да', 't')

    @staticmethod
    def __cnv_int(val) -> int | float:
        if isinstance(val, int) or isinstance(val, float):
            return val
        if val.__contains__('.') or val.__contains__(','):
            return float(val)
        else:
            return int(val)

if __name__ == "__main__":
    new_gr = JGraph(cnt=4, name = "TestGraph")
    funcs = [
            lambda *args:new_gr.addedge(args[0],args[1],args[2]) if len(args)>=3 else new_gr.addedge(args[0],args[1]),

            lambda *args:new_gr.rmedge(args[0]),
            lambda *args:new_gr.changecnt(args[0]),

            lambda :print(new_gr.ret_gr()),
            lambda :print(new_gr.ret_rts()),
            lambda :print(new_gr.ret_cnt()),

            lambda :print(new_gr.isDir()),
            lambda :print(new_gr.isWe()),

            lambda *args:new_gr.setDir(args[0]),
            lambda *args:new_gr.setWe(args[0]),

            lambda *args:   new_gr.smezh_matrix(args[0],args[1])if len(args)>=2 else new_gr.smezh_matrix(),
            lambda *args:   new_gr.indent_matrix(args[0],(args[1]))if len(args)>=2 else new_gr.indent_matrix(),
            lambda *args:   new_gr.indent_matrix_v2((args[0]),(args[1]))if len(args)>=2 else new_gr.indent_matrix_v2(),

            lambda :print(new_gr.show_smatrix()),
            lambda :print(new_gr.show_imatrix()),
            lambda :print(new_gr.show_imatrix_v2()),

            lambda :print(new_gr.svzyaz_components()),
            lambda :print(new_gr.find_strong_components()),

            lambda :print(new_gr.__repr__()),
            lambda :new_gr.Graphic_Graph(),

            lambda *args:print(FP(new_gr.ret_cnt(),new_gr.ret_rts(),args[0],args[1],directed=new_gr.isDir())),
            lambda *args:print(DP(new_gr.ret_cnt(),new_gr.ret_rts(),args[0],args[1],directed=new_gr.isDir()))
    ]
    descriptions = ("1)addedge *u *v *w         добавляет ребро из \'u\' в \'v\' с весом \'w\'\n"
                    "2)rmedge *i                удаляет ребро с индексом \'i\'\n"
                    "3)changecnt *n             устанавливает количество вершин на \'n\'(Рёбра из/в несуществующие вершины будут удалены)\n"
                    "4)ret_gr                   возвращает граф в виде списка: [вершины, рёбра, взвешеный?, направленый?, имя графа] \n"
                    "5)ret_rts                  возвращает рёбра в виде списка: [вершина откуда, вершина куда, вес]\n"
                    "6)ret_cnt                  возвращает количество вершин\n"
                    "7)isDir                    возвращает значение показывающее направленный ли граф\n"
                    "8)isWe                     возвращает значение показывающее взвешенный ли граф\n"
                    "9)setDir *b                устанавливает направленность графа как True или False\n"
                    "10)setWe *b                устанавливает взвешенность графа как True или False\n"
                    "11)smezh_matix *d *w       возвращает матрицу смежности в виде списка списков, со значением \'d\' - направленности и \'w\' - взвешенности\n"
                    "12)indent_matrix *d *w     возвращает матрицу инценденций в виде списка списков, со значением \'d\' - направленности и \'w\' - взвешенности\n"
                    "13)indent_matrix_v2 *d *w  то же что и 12, но в случае если граф взвешен, веса будут указаны отдельной колонкой\n"
                    "14)show_smatrix            красивый вывод в консоль 11 матрицы\n"
                    "15)show_imatrix            красивый вывод в консоль 12 матрицы\n"
                    "16)show_imatrix_v2         красивый вывод в консоль 13 матрицы\n"
                    "17)components              компоненты связности\n"
                    "18)strong components       компоненты сильной связности\n"
                    "19)                        самый полный вывод информации о графе(для отладки)\n"
                    "20)Graphic_Graph           графический вывод графа\n"
                    "21)Floyd-W Path *a *b      поиск кратчайшего пути в графе из вершины \'a\' в \'b\' алгоритмом Флойда-Уоршелла\n"
                    "22)DijkstraPath *a *b      поиск кратчайшего пути в графе из вершины \'a\' в \'b\' алгоритмом Дийкстры"
                    )

    men = Menu(funcs=funcs,desc=descriptions,numolabo=2.9)
    men.start()