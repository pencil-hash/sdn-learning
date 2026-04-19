# 导入拓扑基类，所有自定义拓扑都要继承这个类
from mininet.topo import Topo
# 导入Mininet核心网络类，用来创建、启动、管理整个虚拟网络
from mininet.net import Mininet
# 导入命令行交互接口，就是你之前敲 nodes、pingall 的 mininet> 终端界面
from mininet.cli import CLI
# 导入日志等级设置，用来控制终端输出的日志详细程度
from mininet.log import setLogLevel

# 定义自己的拓扑类 MyTopo，继承上面导入的 Topo 父类
# 继承之后，你就拥有了Mininet所有建主机、交换机、链路的内置方法
class MyTopo(Topo):
    # build() 构建函数，Mininet固定内置函数
    # 只要你写自定义拓扑，所有建网操作**必须全部写在这个函数里面**
    def build(self):

        # 添加一台主机，命名为 h1
        # self.addHost('主机名') → 创建虚拟主机节点
        h1 = self.addHost('h1')

        # 添加第二台主机，命名为 h2
        h2 = self.addHost('h2')

        # 添加一台交换机，命名为 s1
        s1 = self.addSwitch('s1')

        # 建立链路，把主机 h1 和交换机 s1 连接起来
        # self.addLink(节点A, 节点B) → 在两个网络节点之间通上网线
        self.addLink(h1, s1)

        # 建立第二条链路，把主机 h2 和交换机 s1 连接起来
        self.addLink(h2, s1)

# 脚本主入口
# Python程序固定入口判断
# 意思是：**只有直接运行这个py文件时，下面的代码才会执行**
# 如果别人导入这个文件当库用，下面代码不会跑
if __name__ == '__main__':

    # 设置日志输出等级为 info
    # 控制启动网络时，终端打印多少运行信息；选info是学习最舒服的等级，不多不少
    setLogLevel('info')

    # 实例化你上面写好的拓扑类，生成拓扑对象
    topo = MyTopo()

    # 创建Mininet网络实例，把你写好的拓扑传入进去
    # 默认使用Mininet自带的本地控制器，和你之前sudo mn默认启动完全一致
    # net = Mininet(topo=topo)
    net = Mininet(topo=topo, controller=None)

    # 启动整个虚拟网络！
    # 底层自动创建主机、交换机、链路，配置IP、网卡，完成网络初始化
    net.start()

    # 打开交互式命令行界面
    # 就是你之前熟悉的 mininet> 界面！
    # 你在这里依旧可以敲 nodes、net、h1 ping h2、pingall 所有命令
    CLI(net)

    # 第20行：退出命令行后，自动关闭、销毁整个虚拟网络，清理所有资源
    net.stop()
