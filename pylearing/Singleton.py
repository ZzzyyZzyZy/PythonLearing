class Singleton(object):
    # 定义类属性记录单例对象引用
    instance = None

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否已经被赋值
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        # 2. 返回类属性的单例引用
        return cls.instance
