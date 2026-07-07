# Uljas architecture package (`uljas.dediren`)

A mixed-notation [dediren](https://github.com/tommimarkus/dediren) architecture
package for the **Ulosottolaitos "Uljas"** information-system-applicant message
interface, built from `input/` (schemas + guide documents). ArchiMate® 3.2 frames
the enterprise/application/technology context; UML® 2.5 elaborates the message
data models and exchange sequences.

## Layout

| File | Role |
|------|------|
| `project.json` | Multi-model binding (`…project.v2`): `models[]` + 24 views |
| `model.json` | ArchiMate model (`semantic_profile: archimate`) — 5 views |
| `model-uml.json` | UML model (`semantic_profile: uml`) — 19 views |
| `render-policy.json` | ArchiMate SVG style (from the dediren `archimate-svg` fixture) |
| `render-policy-uml.json` | UML SVG style (from the dediren `uml-svg` fixture) |
| `generated/svg/*.svg` | Rendered diagrams (visual proof) |
| `generated/{layout,render-metadata}/` | Reproducible intermediates (git-ignored) |

Source of truth is the `*.json` under the package root. `generated/` is
reproducible output.

## Views (24)

**ArchiMate (5)** — `model.json`
- `context` — system context: applicant system ⇄ SFTP interface ⇄ Uljas
- `onboarding` — permit application → joint testing → production go-live
- `message-catalog` — the 12 message types by direction (in/out) and pairing
- `matter-lifecycle` — application → pending → collection → settlement → passive
- `deployment` — SFTP relay (VIA/Valtori) transport: `to_uljas` / `from_uljas`

**UML data models (15)** — `model-uml.json`, one per schema
`data-dt` Datatypes · `data-ct` Complex types · `data-co` Codes ·
`data-he` Hakemuserä · `data-hep` Hakemuseräpalaute · `data-me` Muutoserä ·
`data-mep` Muutoseräpalaute · `data-vt` Vireilletuloilmoitus · `data-st`
Saldotiedustelu · `data-stv` Saldotiedusteluvastaus · `data-ti` Tilityserittely ·
`data-mk` Maksukiellot · `data-mkp` Maksukiellon palauttaminen · `data-mkpp`
Palauttamisen palaute · `data-pp` Passiiviperinnän päättymisilmoitus

**UML sequences (4)** — `model-uml.json`
`seq-submission` · `seq-change` · `seq-balance` (alt fragment) · `seq-maksukielto`

Each UML message package carries a cross-notation
`properties.uml.architecture_context` link (`elaborates`) to its ArchiMate
`DataObject` in `model.json`.

## Regenerate

Requires Java 21+ and the dediren bundle (`2026.07.8`). From the repo root:

```bash
export DEDIREN_CACHE_DIR=<dir-with>/dediren-agent-bundle-2026.07.8/..  DEDIREN_VERSION=2026.07.8
export DEDIREN_CDS_DIR=<writable>/cds
DEDIREN=<bundle>/bin/dediren
PKG=docs/architecture/uljas.dediren

# IMPORTANT (UTF-8): dediren plugin children only inherit JAVA_HOME/PATH, so a
# non-UTF-8 locale makes them emit '?' for ä/ö. Point JAVA_HOME at a wrapper JDK
# whose bin/java forces UTF-8, e.g.:
#   mkdir -p /tmp/jdk-utf8/bin
#   printf '#!/bin/sh\nexec <real-jdk>/bin/java -Dstdout.encoding=UTF-8 -Dfile.encoding=UTF-8 "$@"\n' > /tmp/jdk-utf8/bin/java
#   chmod +x /tmp/jdk-utf8/bin/java
export JAVA_HOME=/tmp/jdk-utf8

# per view (see project.json): profile-validate, then
"$DEDIREN" validate --plugin generic-graph --profile archimate --input "$PKG/model.json"
"$DEDIREN" validate --plugin generic-graph --profile uml       --input "$PKG/model-uml.json"
# then project (layout-request + render-metadata) → layout → validate-layout → render,
# and the skill's svg-accessible-name.sh post-render step per view.
```

Known dediren tool issue: plugin children inherit only `JAVA_HOME`/`PATH`, so a
non-UTF-8 child locale makes them emit `?` for `ä`/`ö` in all output (incl. SVG)
while the pipeline reports `ok`. Full write-up + minimal repro:
[`DEDIREN-ISSUE-utf8-stdout.md`](DEDIREN-ISSUE-utf8-stdout.md). Workaround above.

Known finding: `data-ti` (Tilityserittely, 45 classes / 92 edges) is the largest
schema and renders dense (`ARCH-L-3`: residual route detours + label
dissociation after layout tuning). It is kept as a complete reference view;
recommended remediation is to split it into `lähete` (settlement summary) and the
five `erittely` families (raha / asia / este / peruutus / velallis).
