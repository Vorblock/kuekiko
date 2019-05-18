---
title: "Frida从入门到放弃_1"
date: 2019-01-22T20:39:26+08:00
draft: false
tags: [
    "android安全","HOOK","Frida"
]
categories : ["HOOK","Android安全"]
description : ""
banner : "http://md.kangsiji.cn/frida.png"
images : []
---


### 0x00 Frida

Frida 官网：https://www.frida.re/

github: https://github.com/frida/frida

Dynamic instrumentation toolkit for developers, reverse-engineers, and security
researchers.

### 0x01 安装

用python

`pip install frida-tools` 就一个命令搞定



> Failed to load the Frida native extension: DLL load failed: 找不到指定的模块 
>
> 报了这个错 查了大半天 原来我用的版本是基于python3.7编译的。我现在用的3.6.。。。。
>
> 作者真的是脑子一根筋。。。 所以只好升级成3.7.。。。



### 0x02 Android环境

设备：小米mix2 运行Android8.0 MIUI10开发版已解锁root

frida-server: 用的arm64版本

下载号frida-server  然后adb push 进去

`adb push frida-server /data/local/tmp`

然后`chomd 755 frida-server`

运行`./frida-server`

![frida-server](https://my-md-1253484710.file.myqcloud.com/20190112133452.png)

命令行运行`frida-ps -U`

![frida-ps](https://my-md-1253484710.file.myqcloud.com/20190112133604.png)

安装成功









