# Copilot Instructions (Submodule: sck-core-report)

## Plan → Approval → Execute (Mandatory)
All non-trivial actions must follow the plan/approval workflow defined at the root. Trivial Q&A may bypass; otherwise wait for explicit approval.

- Tech: Python package.
- Precedence: Local first; fallback to root `../../.github/...`.
- Conventions: Reuse `../sck-core-ui/docs/backend-code-style.md` for AWS/S3/Lambda usage.

## Google Docstring Requirements
**MANDATORY**: All docstrings must use Google-style format for Sphinx documentation generation:
- Use Google-style docstrings with proper Args/Returns/Example sections
- Napoleon extension will convert Google format to RST for Sphinx processing
- Avoid direct RST syntax (`::`, `:param:`, etc.) in docstrings - use Google format instead
- Example sections should use `>>>` for doctests or simple code examples
- This ensures proper IDE interpretation while maintaining clean Sphinx documentation

## Contradiction Detection
- Verify against backend style + root precedence.
- If conflict, warn + options + example.
- Example: "Returning raw data to UI without envelope conflicts with API rules; wrap in `{ status, code, data }`."

## Standalone clone note
If cloned standalone, see:
- UI/backend conventions: https://github.com/eitssg/simple-cloud-kit/tree/develop/sck-core-ui/docs
- Root Copilot guidance: https://github.com/eitssg/simple-cloud-kit/blob/develop/.github/copilot-instructions.md
 
