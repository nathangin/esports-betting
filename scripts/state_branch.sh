#!/usr/bin/env bash
# Keeps the paper-trading state (ledger, scans, fitted parameters, reports) on its own
# branch so scheduled runs never touch the code on main.
#
#   scripts/state_branch.sh checkout          -> worktree of the state branch in ./state-branch
#   scripts/state_branch.sh commit "message"  -> commit and push whatever changed there
set -euo pipefail

BRANCH="${STATE_BRANCH:-paper-trading}"
DIR="${STATE_DIR:-state-branch}"

case "${1:-}" in
  checkout)
    git config --global user.name "esalpha-bot"
    git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"
    if git ls-remote --exit-code --heads origin "$BRANCH" >/dev/null 2>&1; then
      git fetch --depth=1 origin "$BRANCH:refs/remotes/origin/$BRANCH"
      git worktree add -B "$BRANCH" "$DIR" "origin/$BRANCH"
    else
      git worktree add --detach "$DIR"
      (cd "$DIR" && git checkout -q --orphan "$BRANCH" && git rm -rfq . && git clean -fdxq)
      printf '# Paper-trading state\n\nWritten by the GitHub Actions workflows on the default branch. See state/reports/summary.md.\n' > "$DIR/README.md"
    fi
    mkdir -p "$DIR/state"
    ;;
  commit)
    cd "$DIR"
    git add -A
    if git diff --cached --quiet; then
      echo "state: nothing to commit"
      exit 0
    fi
    git commit -qm "${2:-update state}"
    for i in 1 2 3 4 5; do
      if git push -q origin "HEAD:$BRANCH"; then
        echo "state: pushed"
        exit 0
      fi
      echo "state: push rejected, rebasing (attempt $i)"
      git fetch -q --depth=50 origin "$BRANCH"
      git rebase -q FETCH_HEAD || { git rebase --abort || true; }
      sleep $((i * 3))
    done
    echo "state: could not push" >&2
    exit 1
    ;;
  *)
    echo "usage: $0 checkout|commit [message]" >&2
    exit 2
    ;;
esac
