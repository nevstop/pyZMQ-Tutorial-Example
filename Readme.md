python examples of ZeroMQ for Guide:
https://github.com/anjuke/zguide-cn

LabVIEW examples of ZeroMQ for Guide:
https://github.com/nevstop/lvZMQ-Tutorial-Example


## ZMQ 简介

ZMQ（ØMQ、ZeroMQ, 0MQ）
 - 看起来像是一套嵌入式的网络链接库，但工作起来更像是一个并发式的框架。
 - 提供的套接字可以在多种协议中传输消息，如线程间、进程间、TCP、广播等。
 - 可以使用套接字构建多对多的连接模式，如扇出、发布-订阅、任务分发、请求-应答等。
 - ZMQ的快速足以胜任集群应用产品。
 - 异步I/O机制能够支持构建多核应用程序，完成异步消息处理任务。
 - ZMQ有着多语言支持，并能在几乎所有的操作系统上运行。
 - ZMQ是iMatix公司的产品，以LGPL开源协议发布。
 
## Example 列表

 1. "Hello world": 使用 REQ-REP 模式，演示 ZMQ 如何工作。
 2. "Weather Station": 使用气象站范例，演示如何使用 Publish-Subscribe 模式，建立单向数据分发。
 3. "REQ-REP": 使用 REQ-REP 模式，演示 1-N ZMQ 模型
 4. "Distributed Calc": 使用 PUSH-Pull 模式，演示分布式负载均衡计算
