#!/usr/local/python

#该测试可能导致较大的网络开销
def test_network():
    print("正在测试网络")

#该测试可能导致较大的CPU消耗
def test_cpu():
    print("正在测试CPU")

#分别设置属性
test_network.cost_network = 1
test_cpu.cost_cpu = 1


