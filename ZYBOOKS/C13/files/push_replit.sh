#!/bin/bash
# 🚀 push_replit.sh — safely push to GitHub/Replit without getting stuck
# Usage: bash push_replit.sh
# Optional message: bash push_replit.sh "my commit message"

REMOTE="replit"
BRANCH="main"
MSG="${1:-📤 manual push @ $(date +"%H:%M:%S")}"

# Prefer a dedicated replit remote; fall back to origin if missing.
if ! git remote get-url "$REMOTE" >/dev/null 2>&1; then
    REMOTE="origin"
fi

echo "📦 Staging all changes..."
git add .

# Only commit if there's something to commit
if ! git diff --cached --quiet; then
    git commit -m "$MSG"
fi

echo "🔄 Syncing with remote (rebase)..."
if ! git pull --rebase "$REMOTE" "$BRANCH"; then
    echo "⚠️  Conflict detected — accepting local version of conflicted files..."
    # Accept our version for any conflicted files
    git diff --name-only --diff-filter=U | xargs -r git checkout --theirs
    git diff --name-only --diff-filter=U | xargs -r git add
    GIT_EDITOR=true git rebase --continue
fi

echo "🚀 Pushing to $REMOTE/$BRANCH..."
if git push "$REMOTE" "$BRANCH"; then
    echo "✅ Done! Code is live on GitHub/Replit."
else
    echo "❌ Push failed. Try running: bash push_replit.sh"
fi
