# Copilot Instructions (Submodule: sck-core-report)

- Tech: Python package.
- Precedence: Local first; fallback to root `../../.github/...`.
- Conventions: Reuse `../sck-core-ui/docs/backend-code-style.md` for AWS/S3/Lambda usage.

## Contradiction Detection
- Verify against backend style + root precedence.
- If conflict, warn + options + example.
- Example: "Returning raw data to UI without envelope conflicts with API rules; wrap in `{ status, code, data }`."

## Standalone clone note
If cloned standalone, see:
- UI/backend conventions: https://github.com/eitssg/simple-cloud-kit/tree/develop/sck-core-ui/docs
- Root Copilot guidance: https://github.com/eitssg/simple-cloud-kit/blob/develop/.github/copilot-instructions.md
 
