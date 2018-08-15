# 面向对象的三大特征
- 封装
- 继承
- 多态
## 封装
- 封装就是对对象成员进行访问限制
- 封装的三个级别
    - 公开，public
    - 受保护的，protected
    - 私有的，private
    - public， protected， private不是关键字
- 判别对象的位置
    - 对象内部
    - 对象外部
    - 子类中
- 私有
    - 私有成员是最高级别的封装，只能在当前类或对象中访问
    - 在成员面前添加两个下划线即可
                class  Person():
                    # name是共有成员
                    name = "zhangsan"
                    # __age就是私有成员
                    __age = 14
                    
    - python中私有不是真私有，是一种称为name mangling改名策略，可以使用对象
    ._classname_attributename访问
- 受保护的封装 protected
    - 受保护的封装是将对象成员进行一定级别的封装，然后，在类中或子类中可以进行
    访问，在外部不行
    - 封装方法： 在成员名称前添加一个下划线即可 _age
- 公开的，公共的 public
    - 对成员无任何操作，任何地方都可以访问
## 继承
- 一个类可以获得另外一个类的成员属性和成员方法
- 所有的类都继承自object类，即所有的类都是object类的子类
- 子类一旦继承父类，则可以使用父类中除私有成员外的所有内容
- 子类中定义的成员和父类成员相同，优先使用子类成员
## 多态
- 多态就是同一个对象在不同情况下有不同的状态出现
- 多态不是语法，是一种设计思想
- 多态性：一种调用方式，不同执行效果

- MiXin设计模式
    - 主要采用多继承方式对类的功能进行扩展
    - 使用多继承的方法来实现MiXin
    - 使用MiXin可以不对类进行任何修改的情况下，扩充功能
## 类的函数
- issubclass 检查一个类是否是另一个类的子类
- isinstance 检测一个对象是否是一个类的实例
- hasattr    检测一个对象是否有成员xxx
- getattr
- setattr
- delattr
- dir 获取对象成员列表
## 类的成员描述符（属性）
- 类的成员描述符是为了在类中对类的成员属性进行相关操作而创建的一种方式
    - get：获取属性的操作
    - set：修改或者添加属性的操作
    - delete：删除属性的操作
- 如果想使用类的成员描述符，大概有三种方法
    - 使用类实现描述器
    - 使用属性修饰符
    - 使用property函数
        - property（fget， fset， fdel， doc）
        - 两种方法
            - 1、装饰器实现
            
                    class Goods(object):
                    
                        def __init__(self):
                            # 原价
                            self.original_price = 100
                            # 折扣
                            self.discount = 0.8

                        @property
                        def price(self):
                            # 实际价格 = 原价 * 折扣
                            new_price = self.original_price * self.discount
                            return new_price

                        @price.setter
                        def price(self, value):
                            self.original_price = value

                        @price.deleter
                        def price(self):
                            del self.original_price

                    obj = Goods()
                    obj.price         # 获取商品价格
                    obj.price = 200   # 修改商品原价
                    del obj.price     # 删除商品原价
            - 2、类属性实现
            
                    class Foo(object):
                        def get_bar(self):
                            print("getter...")
                            return 'wang'

                        def set_bar(self, value): 
                        """必须两个参数"""
                            print("setter...")
                            return 'set value' + value

                        def del_bar(self):
                            print("deleter...")
                            return 'wang'

                        BAR = property(get_bar, set_bar, del_bar, "description...")

                    obj = Foo()
                    obj.BAR  # 自动调用第一个参数中定义的方法：get_bar
                    obj.BAR = "jack"  # 自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当作参数传入
                    desc = Foo.BAR.__doc__  # 自动获取第四个参数中设置的值：description...
                    print(desc)
                    del obj.BAR  # 自动调用第三个参数中定义的方法：del_bar方法
            - 3、在私有属性中的使用
            
                    class Money(object):
                        def __init__(self):
                        self.__money = 0

                        @property
                        def money(self):
                            return self.__money

                        @money.setter
                        def money(self, value):
                            self.__money = value

                    salary = Money()
                    print(salary.money)
                    salary.money = 20000
                    print(salary.money)
## 类的内置属性
    
        __dict__：以字典的方式显示类的成员组成
        __module__：查看当前操作的对象在哪个模块中，不带括号调用
        __doc__：获取类的文档信息
        __name__：获取类的名称，如果在模块中使用，获取模块的名称
        __bases__：获取某个类的所有父类，以元祖的方式显示
                    
                    calss Person():
                    ''' 
                    这里是__doc__的文档信息
                    '''
                        pass
                    print(Person.__dict__)
                    ptint(Person.__doc__)
## 类的常用魔术方法
- 魔术方法就是不需要人为调用的方法，基本是在特定时刻自动触发
- 魔术方法的统一特征，方法名被前后各两个下划线包裹
- 操作类
    - __init__()：构造函数
    - __new__()：对象实例化方法，此函数较特殊，一般不需要使用
    - __call__()：对象当函数使用的时候触发

                    class A():
                        def __init__(self):
                            pass
                        def __call__(self):
                            print('我被调用了')
                    a = A()
                    a() ---------> 调用A()中的call函数
    - __str__()：当对象被当做字符串使用的时候返回一个描述性信息，必须是字符串，当创建对象时，
    此方法就存在返回值了，在外界可以使用print(obj)查看，也可以使用格式化字符串来查看。

                    class A():
                        def __init__(self):
                            pass
                        def __str__(self):
                            return  '我被调用了'
                    a = A()
                    print(a) ---------> a被当做字符串调用str函数
    - __repr__()：返回字符串
- 描述符相关
    - __set__
    - __get__
    - __delete__
- 属性操作相关
    - __getattr__：访问一个不存在的属性时触发
    - __setattr__：对成员属性进行设置的时候触发
        - 参数： 
            - self用来获取当前对象
            - 被设置的属性名称，以字符串的形式出现
            - 需要对属性名称设置的值
        - 作用：进行属性设置的时候进行验证或者修改
        - 注意：在该方法中不能对属性直接进行赋值操作，否则死循环
        
                    