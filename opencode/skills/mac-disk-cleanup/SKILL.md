---
name: mac-disk-cleanup
description: Audit and clean up disk space on macOS. Use when the user says 'clean up disk', 'free up space', 'disk is full', 'check disk usage', 'disk cleanup', or 'storage is running out'.
---

# Disk Cleanup

## Prerequisites

- macOS with standard Unix tools (`df`, `du`, `rm`, `find`, etc.)
- Homebrew (optional, for `brew cleanup`)
- `python3` (for Kiro CLI orphaned KB cleanup)

## Run

Ensure dependencies are available:

```bash
command -v brew >/dev/null 2>&1 || echo "Warning: Homebrew not installed. Skip brew cleanup steps."
python3 --version >/dev/null 2>&1 || echo "Warning: python3 not installed. Skip Kiro CLI KB cleanup."
```

## Steps

### 1. Audit

Run `df -h /` to get overall disk usage, then check all known bloat locations in parallel:

| Location | Command |
|---|---|
| `~/Downloads` | `du -sh ~/Downloads` |
| `~/.Trash` | `du -sh ~/.Trash` |
| `/tmp/` | `du -sh /tmp/` |
| CoreSimulator | `du -sh ~/Library/Developer/CoreSimulator` |
| Xcode Archives | `du -sh ~/Library/Developer/Xcode/Archives` |
| iOS DeviceSupport | `du -sh ~/Library/Developer/Xcode/iOS\ DeviceSupport` |
| DerivedData | `du -sh ~/Library/Developer/Xcode/DerivedData` |
| Library Caches | `du -sh ~/Library/Caches` |
| Library Containers | `du -sh ~/Library/Containers` |
| Docker | `du -sh ~/Library/Application\ Support/Docker` |
| Kiro CLI KB | `du -sh ~/Library/Application\ Support/kiro-cli/knowledge_bases 2>/dev/null || echo "0B"` |

For locations over 1 GB, drill down with `du -sh <path>/*/ | sort -rh | head -10` to identify the largest subdirectories or files.

For `~/Downloads`, also run `ls -lhS ~/Downloads/ | head -20` to list the largest individual files and identify stale installers (.dmg, .pkg, .xip), databases (.sqlite), archives (.zip), binaries (.apk, .ipa), and videos (.mp4, .mov, .mkv).

### 2. Report

Present findings as a monospaced padded code block sorted by size (largest first) with columns: `#`, `Location`, `Size`, `Verdict`.

Use verdict indicators:
- 🔴 for items > 10 GB or clearly stale
- 🟡 for items 1–10 GB worth reviewing
- 🟢 for items < 1 GB or already clean

Example:

```
#   Location              Size     Verdict
1   CoreSimulator         44 GB    🔴 93 shutdown simulators, many unavailable
2   iOS DeviceSupport     21 GB    🔴 Old device symbols still present
3   Library/Caches        18 GB    🟡 Spotify 7.8G, Google 1.9G
4   Xcode Archives        14 GB    🔴 Archives dating back to 2025
5   Downloads              4.8 GB  🟡 Xcode xip 2.8G, old installers
6   Trash                  958 MB  🟢 Easy win
7   /tmp/                   59 MB  🟢 Clean
```

### 3. Plan

Create a todo list of cleanup actions with numbered task descriptions, ordered by reclaim potential (largest first). Each task should include the size and the command to run.

Wait for user confirmation before proceeding. The user may exclude specific items.

### 4. Execute

For each approved task, run the cleanup command and verify the result with `du -sh` afterward. Mark each todo item complete with the before/after sizes.

### 5. Summarize

Present a final monospaced padded code block with columns: `#`, `Task`, `Before`, `After`, `Reclaimed`. Include a total row.

Example:

```
#   Task                    Before    After     Reclaimed
1   CoreSimulator           44 GB     18 GB     ~26 GB
2   iOS DeviceSupport       21 GB     10 GB     ~11 GB
3   Homebrew cache          894 MB    ~0        ~1.3 GB
4   Xcode Archives          14 GB     0 GB      ~14 GB
5   Downloads               4.8 GB    1.2 GB    ~3.6 GB
6   Trash                   958 MB    ~0        ~1 GB
                                        Total:  ~56.9 GB
```

## Common Cleanup Commands

| Target | Command | Notes |
|---|---|---|
| Unavailable simulators | `xcrun simctl delete unavailable` | Safe — removes simulators for uninstalled runtimes |
| Old iOS DeviceSupport | `rm -rf ~/Library/Developer/Xcode/iOS\ DeviceSupport/<version>/` | Xcode re-downloads on device reconnect |
| Xcode Archives | `rm -rf ~/Library/Developer/Xcode/Archives/*` | Local-only artifacts |
| DerivedData | `rm -rf ~/Library/Developer/Xcode/DerivedData/*` | Rebuilds on next Xcode build |
| Downloads (videos) | `find ~/Downloads -maxdepth 1 -type f \( -name "*.mp4" -o -name "*.mov" -o -name "*.mkv" -o -name "*.avi" \) -delete` | Only top-level, not subfolders |
| Downloads (stale files) | List with `ls -lhS ~/Downloads/ \| head -20`, then delete individually by name | Covers .dmg, .pkg, .xip, .sqlite, .apk, .ipa, .zip |
| Homebrew cache | `brew cleanup --prune=all` | Removes old bottles and cask installers |
| Kiro CLI orphaned KB indexes | See below | Removes orphaned BM25 index directories |
| Trash | `rm -rf ~/.Trash/*` | Permanent deletion |

## Rules

- Always audit before deleting — never assume what is safe to remove.
- Always confirm with the user before deleting anything.
- Do not delete Spotify cache, browser profiles, or app containers unless explicitly requested.
- For iOS DeviceSupport, prefer keeping the latest version per device and removing older ones.
- After all deletions, empty Trash as a final step to actually reclaim the space.

## Kiro CLI Knowledge Base Cleanup

Re-indexing creates orphaned BM25 index directories that are never cleaned up. Each orphaned directory contains a `data.bm25.json` (~285MB).

To identify orphaned directories:

1. For each agent folder in `~/Library/Application Support/kiro-cli/knowledge_bases/`:
2. Read `contexts.json` to get active context IDs.
3. List all UUID directories in the folder.
4. Any directory not in `contexts.json` is orphaned.

To clean:

```bash
# List orphaned directories
python3 <skill-dir>/scripts/list-orphaned-kb.py
```

After confirming the list, delete with `rm -rf` on each orphaned path.
