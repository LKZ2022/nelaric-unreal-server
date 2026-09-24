<!-- Copyright (c) 2026 Nelaric -->

English | [简体中文](README.zh-CN.md)

# Nelaric Unreal Server

A gameplay-agnostic, provider-agnostic dedicated server framework for Unreal Engine.

This repository has a UE 5.6 plugin scaffold at `Unreal-Plugins/NelaricServer/`. Its `NelaricCore` module loads but does not yet provide server services or a public API. The local validation project under `Development/` is excluded from Git.

See the [NelaricCore module description](Docs/Modules/NelaricCore.md) for its current responsibility and dependencies.

## Contributing

All developers contributing to this project must follow both [Epic Games' Unreal Engine Coding Standard](https://dev.epicgames.com/documentation/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine) and the [project coding standards](Docs/CodingStandards/). The project standards define our module boundaries, API contracts, review rules, and required automated checks.

See the [contribution guide](CONTRIBUTING.md) for issue and pull request guidance, and the [development and CI workflow](Docs/DevelopmentWorkflow.md) for automated checks and the Linux plugin build.

## API Documentation

The [API documentation site](https://nelaric.github.io/nelaric-unreal-server/) publishes the coding standards now and will include the public C++ API when public headers are added.

## Star History

<a href="https://www.star-history.com/?repos=Nelaric%2Fnelaric-unreal-server&type=date&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=Nelaric/nelaric-unreal-server&type=date&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=Nelaric/nelaric-unreal-server&type=date&legend=top-left" />
    <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=Nelaric/nelaric-unreal-server&type=date&legend=top-left" />
  </picture>
</a>

## Thanks

Thanks to everyone contributing to Nelaric Unreal Server, to Epic Games for Unreal Engine, and to CircleCI for the Linux plugin build service.
<!-- Temporary fork PR CI verification. -->
