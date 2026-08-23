#!/usr/bin/env bash
# Offline preview of the docs, reproducing the "Pull from Armbian config" CI job
# locally: generate the software pages in configng, copy them into this repo,
# then serve with live reload.
#
#   ./serve-docs-local.sh            generate + stage + serve at http://127.0.0.1:8000
#   ./serve-docs-local.sh build      generate + stage + one-shot build into ./site
#   ./serve-docs-local.sh clean      revert the staged generated pages, leave tree clean
#
# Override repo locations with CONFIGNG=/path DOCS=/path if they aren't the
# defaults below.
set -euo pipefail

DOCS="${DOCS:-$(cd "$(dirname "$0")" && pwd)}"
CONFIGNG="${CONFIGNG:-$(cd "$DOCS/../configng" && pwd)}"
VENV="${VENV:-$DOCS/.venv-docs}"
cmd="${1:-serve}"

# Revert exactly what the staging block below writes: the generated hub/config
# pages and images (restore tracked ones, drop untracked ones), and the wholly
# generated docs/software tree. Only touches those paths.
stage_clean() {
	for d in docs/User-Guide_Armbian-Software docs/User-Guide_Armbian-Config docs/images; do
		git -C "$DOCS" checkout -- "$d" 2>/dev/null || true   # restore tracked files
		git -C "$DOCS" clean -fdq "$d" 2>/dev/null || true    # drop untracked generated files
	done
	rm -rf "$DOCS/docs/software"                              # wholly generated
	echo "reverted generated pages/images/software; check 'git status'"
}

if [[ "$cmd" == "clean" ]]; then stage_clean; exit 0; fi

# 1) pick a mkdocs that actually has this site's plugins. A bare PATH mkdocs may
#    lack mkdocs-material / mkdocs-redirects / mdx_truly_sane_lists and fail
#    confusingly, so use it only if those import; otherwise a local venv built
#    from requirements.txt (first run needs pip/network).
has_deps() { "$1" -c 'import material, mkdocs_redirects, mdx_truly_sane_lists' >/dev/null 2>&1; }
if command -v mkdocs >/dev/null 2>&1 && has_deps "$(command -v python3)"; then
	MK=mkdocs
else
	[[ -x "$VENV/bin/mkdocs" ]] && has_deps "$VENV/bin/python" || {
		echo ">> creating venv at $VENV and installing docs requirements (one-time, needs network)"
		python3 -m venv "$VENV"
		"$VENV/bin/pip" install -q --disable-pip-version-check -r "$DOCS/requirements.txt" \
			|| "$VENV/bin/pip" install -q mkdocs mkdocs-material mkdocs-redirects mdx_truly_sane_lists
	}
	MK="$VENV/bin/mkdocs"
fi

# 2) generate the markdown from configng (uses the committed config.jobs.json).
echo ">> generating software pages in $CONFIGNG"
( cd "$CONFIGNG" && python3 tools/config-markdown.py -u )

# 3) stage into the docs tree exactly like pull-from-armbian-config.yml.
echo ">> staging generated pages into $DOCS/docs"
mkdir -p "$DOCS/docs/images" "$DOCS/docs/User-Guide_Armbian-Config" \
         "$DOCS/docs/User-Guide_Armbian-Software" "$DOCS/docs/software"
rsync -a "$CONFIGNG/tools/include/images/." "$DOCS/docs/images/"
for p in Localisation Network System; do
	rsync -a "$CONFIGNG/docs/$p/$p.md" "$DOCS/docs/User-Guide_Armbian-Config/"
done
rsync -a --exclude="Software.user.md" "$CONFIGNG/docs/Software/"* "$DOCS/docs/User-Guide_Armbian-Software/"
rsync -a --delete "$CONFIGNG/docs/software/." "$DOCS/docs/software/"

# 3b) rebuild the ARMBIAN SOFTWARE nav from the staged app pages, exactly as the
#     pull-from-armbian-config workflow does, so the local preview matches CI.
echo ">> rebuilding software navigation"
python3 "$DOCS/tools/build-software-nav.py"

# 4) serve or build.
cd "$DOCS"
if [[ "$cmd" == "build" ]]; then
	"$MK" build --clean
	echo ">> built into $DOCS/site — open site/software/netdata/index.html"
else
	echo ">> serving at http://127.0.0.1:8000  (Ctrl-C to stop, then: ./serve-docs-local.sh clean)"
	"$MK" serve
fi
