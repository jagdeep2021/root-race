# Root Race

A one-minute browser game about how roots find food, built for kids at the CAFNR Showcase (University of Missouri, 2026) by the Sidhu Lab.

**Play:** https://jagdeep2021.github.io/root-race/

You steer a corn root through the soil to collect water, nitrogen and phosphorus. The corn plant grows only as fast as its scarcest nutrient allows.

## What kids learn by playing

| In the game | The science |
|---|---|
| Phosphorus sits in patches near the surface and never moves | P is immobile in soil; topsoil foraging matters |
| Rain washes nitrogen deeper; a drought dries the topsoil | N leaching; deep roots reach water in drought |
| Touch a fungus and its threads pull in P from far away, for a little sugar | Arbuscular mycorrhizal symbiosis |
| Every bit of root costs sugar to keep alive | Root respiration / metabolic cost of soil exploration |
| **Key 1** Air channels: less energy lost, more sugar | Root cortical aerenchyma |
| **Key 2** Lignin armor: the rootworm can't chew it, and it pushes through hardpan | Multiseriate cortical sclerenchyma (MCS) |
| **Key 3** Root hairs: grab food from farther away | Root hairs |
| **Key 4** Exudates from the root tip scare nematodes away | Root exudates |
| **Key 5** Crown roots grow from the stem into the topsoil to find P | Shoot-borne (crown/nodal) roots, topsoil foraging |
| Roots can't grow up; worm tunnels are fast lanes; hardpan slows you | Gravitropism, biopores, soil compaction |
| After a round, replay as Deep Diver, Topsoil Forager, Fungus Friend or Iron Root | Root ideotypes suit different soils |

The side panel shows a live root cross-section that changes as traits are built. The title screen uses a real maize root cross-section from the lab.

## Controls

Mouse to steer · click for a side root · keys 1–5 for root traits · M for sound · F for fullscreen. Arrow keys also steer.

**Phones and tablets:** drag to steer, quick tap for a side root, buttons along the bottom for the traits. Scan the QR code on the title screen (print copy: `CAFNR_Showcase/RootRace/RootRace_QR.png` on OneDrive).

**Kiosk mode:** when nobody is playing, the title card alternates with a silent demo round and a zoom-out of the demo's root system. Any click or key starts a game.

## Running it

`index.html` is a single self-contained file (font and image inlined, no network needed). Double-click it to play offline. Scores are kept in the browser; Ctrl+Shift+X clears the leaderboard.

To change the game, edit `src/game.html`, then rebuild:

```
python3 src/build.py
```

Tunable numbers (round length, costs, speeds, event times) are in the `CFG` block at the top of the script.

## Credits

Game design: Jagdeep Sidhu (Sidhu Lab, University of Missouri). Font: Fredoka, SIL Open Font License 1.1 (`src/assets/OFL.txt`).
