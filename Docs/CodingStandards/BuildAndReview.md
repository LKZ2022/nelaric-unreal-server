# Build Scripts, Tooling, and Review

## Unreal build scripts

- Apply CSharpier to `.Build.cs` and `.Target.cs`. It is as mandatory as clang-format for C++.
- Keep module dependencies minimal and classify them as public or private according to the headers that need them. Do not put vendor SDK dependencies in Core.
- Target UE 5.6 and later. When engine compilation CI is introduced, it should cover both the minimum supported release and the latest supported release. No UE compilation job or Runner is required at this stage.

## Local checks

Use the versions fixed by `.github/workflows/quality.yml` and `.config/dotnet-tools.json`:

1. `python Scripts/check_text.py` checks text encoding and line endings.
2. `python Scripts/check_format.py` checks C++ and UE build-script formatting. Install the pinned clang-format and restore the local .NET tool manifest first.
3. `python Scripts/check_public_docs.py` checks that every public header has a file comment.
4. `python Scripts/run_doxygen.py` builds the API site and fails on Doxygen warnings. Install the pinned Doxygen release first.

The format and documentation checks are CI requirements. They do not rewrite a PR. No clang-tidy, UE compilation, test coverage, or additional test gate is required now.

## Text-file exceptions

Human-written Markdown and LICENSE, C++ source and headers, and UE C# build scripts use UTF-8 BOM and CRLF. `.gitattributes`, `.editorconfig`, `.clang-format`, `.csharpierrc`, `.gitignore`, `.json`, `.yml`, `.yaml`, `Doxyfile`, and executable `.py` scripts use UTF-8 without BOM and LF for tool compatibility. The checker enforces these categories.

## Review

Review correctness, module boundaries, public API documentation, cancellation and failure behavior, ownership, performance, and secret handling. A PR seeking an exception must name the rule, reason, affected code, and alternatives. A maintainer must approve the exception. Current CI success is sufficient as an automated gate; tests may still be added for a concrete behavioral risk.
