<!-- Copyright (c) 2026 Nelaric -->

English | [简体中文](NelaricCore.zh-CN.md)

# NelaricCore

`NelaricCore` is the runtime module in the `NelaricServer` plugin. It currently provides only the Unreal module startup and shutdown entry points. No server services or public C++ API are implemented yet.

The module will own gameplay-agnostic server control-plane mechanisms. Provider modules may depend on it; this module must not depend on a concrete Provider or vendor SDK.

Its only direct Unreal module dependency is `Core`, declared private in `NelaricCore.Build.cs`. There are no public module dependencies.
