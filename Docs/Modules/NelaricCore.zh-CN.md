<!-- Copyright (c) 2026 Nelaric -->

[English](NelaricCore.md) | 简体中文

# NelaricCore

`NelaricCore` 是 `NelaricServer` 插件中的运行时模块。目前仅提供 Unreal 模块的启动和关闭入口，尚未实现服务器服务或公开 C++ API。

该模块将承载与玩法无关的服务器控制面机制。Provider 模块可以依赖它；该模块不得依赖具体 Provider 或厂商 SDK。

模块当前唯一的直接 Unreal 模块依赖是 `Core`，在 `NelaricCore.Build.cs` 中声明为私有依赖。模块没有公开依赖。
