import easylogger4dev_alpha as el
import pandas as pd

class A4csv:
    print("A")
    @el.log4csv("Test", "A的备注")
    def __init__(self):
        print("A被成功创建")

    @el.log4csv("Test","a有返回值")
    def a(self):
        print("a被输出")
        return "a"

    @el.log4csv("Test","b无返回值")
    def b(self):
        print("b被输出")
        return "b"

class B4excel:
    print("B")
    @el.log4excel("Test", "B的备注")
    def __init__(self):
        print("A被成功创建")

    @el.log4excel("Test","a有返回值")
    def a(self):
        df = pd.DataFrame([[1, 2, 3, 4, 5],
                           [1,2,3,4,5]], columns=["a", "b", "c", "d", "e"])
        print("a被输出")
        return df

    @el.log4excel("Test","b无返回值")
    def b(self):
        print("b被输出")

if __name__ == "__main__":
    print("start")
    el.logger_ini(True)
    app = A4csv()
    app.a()
    app.b()
    app1 = B4excel()
    app1.a()
    app1.b()
    el.log_del_cache()

