# coding:utf-8

import sys, time, os, json, socket
import multiprocessing as mp
from multiprocessing import Pool



# 自定义异常，让外部指令问题更清楚
class ErrorException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

ARG_LIST = set(('-n', '-f', '-ip', '-w'))

def port_tcp(ip, l, w_arg):
    print(f"进程(ID:{os.getpid()})开始扫描" + ip)
    # 遍历1~1024的端口
    for i in range(1, 1025):
        try:
            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sk.settimeout(2)
            # 连接参数IP和遍历的端口
            result = sk.connect((ip, i))
            # 判断端口状态
            if result == 10035:
                print(f'端口没开！')
            else:
                print(f'端口：{i} 开启中！')
                # 定义json格式
                try:
                    response = {
                        'ip' : ip,
                        'port' : i
                    }
                    # 锁起来
                    l.acquire()
                    output = open(w_arg, 'a', encoding='utf-8')
                    json.dump(response, fp=output, ensure_ascii=False)
                    output.write("\n")
                    output.close()
                except Exception as e:
                    print(e)
                finally:
                    # 最后解锁
                    l.release()
        except Exception as e:
            print(e)


def ping_ip(ip, l):
    print(f"进程ID：{os.getpid()}开始ping" + ip)
    do = os.popen(f"ping {ip} -n 1").read()
    if '请求超时'in do or '无法访问'in do:
        print(f'ping {ip} 不通！')
    else:
        print(f'ping {ip} 成功！')

if __name__ == '__main__':
    # 给进程模块加锁
    l = mp.Manager().RLock()
    cpu =  mp.cpu_count()
    # 获取外部参数行 
    arg_list = sys.argv
    n_arg = cpu

    for i in arg_list:
        # 定义遍历开头是横杠，但要是不在大参列表里抛出异常
        if i.startswith('-') and i not in ARG_LIST:
            raise ErrorException("参数无效：" + i)
        # 取各参数的值
        elif i == '-n':
            n_arg = int(arg_list[arg_list.index('-n') + 1]) #实现取到参数值了
            if n_arg > cpu:
                raise ErrorException("进程设置不在CPU范围内。你最大可以设置为："+ str(cpu))
        elif i == '-f':
            f_arg = arg_list[arg_list.index('-f') + 1]
        elif i == '-ip':
            ip_arg = arg_list[arg_list.index('-ip') + 1]
            ip_list = ip_arg.split('-')
        elif i == '-w':
            w_arg = arg_list[arg_list.index('-w') + 1]
    #拿到了进程池的内存地址
    p = Pool(n_arg) 
    if f_arg == 'ping':
        ip_s = ip_list[0].split('.')
        ip_e = ip_list[1].split('.')
        ip3 = ip_list[0][:ip_list[0].rfind('.') + 1]
        if ip_s[0] != ip_e[0] or ip_s[1] != ip_e[1] or ip_s[2] != ip_e[2] or ip_s[3] == ip_e[3]:
            raise ErrorException('输入的IP范围有问题！')
        for i in range(int(ip_s[-1]), int(ip_e[-1]) + 1):
            ip = ip3 + str(i)
            p.apply_async(ping_ip, args=(ip, l))
    elif f_arg == 'tcp':
        ip = ip_arg     
        p.apply_async(port_tcp, args=(ip, l, w_arg))
    
    p.close()
    p.join()
