# 11_root_race: kids' root game (CAFNR Showcase 2026)

Static game on GitHub Pages: `jagdeep2021/root-race`
→ https://jagdeep2021.github.io/root-race/

Its own public repo, nested in ~/lab-code and ignored by the parent SidhuLab repo (same pattern as 10_teaching_4320).

## Layout
| path | what |
|---|---|
| `src/game.html` | the source. Contains `__AER__` and `__FONT__` placeholders |
| `src/assets/` | lab cross-section image, Fredoka woff2, its OFL license |
| `src/build.py` | inlines assets, writes `index.html` (optional extra path = offline copy) |
| `index.html` | built, single file, what Pages serves. Never edit by hand |

Offline showcase copy: `python3 src/build.py "<OneDrive>/1_Sidhu Lab/10_Outreach_news/2026/CAFNR_Showcase/RootRace.html"`

## Test hooks (URL params)
- `?endtest=1&auto=1` plays a full round with the AI and logs `SCORE <cm> <root> {...}` to the console
- `?ff=30&auto=1` fast-forwards 30 s of AI play (for screenshots)
- `&hero=diver|forager|fungus|armored` picks the root type
Headless check: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --window-size=1440,900 --enable-logging=stderr --v=0 --virtual-time-budget=6000 --dump-dom "file://$PWD/index.html?endtest=1&auto=1" 2>&1 | grep SCORE`
The AI scores roughly 90–200 cm; one run in ~10 fails low (AI noise).

## Decisions the user made; do not undo
- **Roots can never grow upward** (`downAngle`). Pointing above the tip means "go sideways that way".
- **Nothing gets stuck at the bottom or in corners.** At the floor, a downward heading turns sideways and a heading into a wall flips.
- **Soil depth is tied to the clock** (`diveFraction`): a nonstop dive takes ~85% of the round, so nobody runs out of soil early.
- **Title screen does one job** (press Play). Teaching happens in play: first-encounter labels pinned to objects (`scanCallouts`), event banners, the trait panel.
- **No root choice before the first play.** It broke the flow. Root types (ideotypes) are offered only on the end screen ("try again as").
- **Air channels read as sugar gained** ("+X saved by air channels" plus gold sparkles), not only as a lower cost.
- **Exudates come from the root tip**: puffs released at tips that diffuse and fade; nematodes flee them.
- **Rootworm must be seen**: it spawns near the tip, is large, shows CHOMP, and has an off-screen arrow.
- Science framing is reviewed by the PI: MCS = lignified outer cortex that helps penetrate hard soil; its pest resistance is game licence.
