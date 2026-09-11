# SHELL Model 🐚

## What it is

A checklist of *interfaces* to examine when something went wrong, with the human at the
centre:

| | Component | In an incident review |
| :--- | :--- | :--- |
| **S** | Software | Code, config, runbooks, procedures, documentation |
| **H** | Hardware | Machines, network, tooling, the interfaces people operate |
| **E** | Environment | Time of day, on-call load, noise, deadline pressure |
| **L** | Liveware | The person - training, fatigue, expectations |
| **L** | Liveware–Liveware | Between people - handovers, comms, hierarchy |

The claim is that failures live in the **interfaces**, not the boxes. The person was not
defective and the tool was not defective; the fit between them was.

## Origin & evidence

Proposed by Edwards in 1972 as SHEL, given its familiar diagram by Hawkins in 1975, and
adopted by ICAO as a standard human-factors framework.

> International Civil Aviation Organization. *Safety Management Manual*, Doc 9859.
> https://skybrary.aero/articles/icao-shell-model

The diagram matters more than the letters: Liveware sits in the middle with **ragged
edges**, and the surrounding blocks must be shaped to match it. A mismatch at any edge is a
latent condition waiting for a bad day. ICAO's summary of the perspective is the useful
one - the human is rarely, if ever, the sole cause of an accident.

## How to use it

Use it as a sweep at the end of an analysis, to catch the dimension nobody looked at. Most
software reviews cover S and H thoroughly, glance at the second L, and skip E entirely.

- **S** - Was the runbook current? Did the config mean what it looked like it meant?
- **H** - Did the interface make the dangerous action look like the safe one?
- **E** - What time was it? How long had they been on? Who was waiting?
- **L** - Had they done this before? Trained on it? Were they fit for duty?
- **L–L** - Was there a handover? Could a junior person have objected?

## Worked example

A review concludes that an engineer applied config to the wrong cluster. Sweeping SHELL:
**S**, the runbook named an environment that had been renamed. **H**, both clusters'
prompts are identical. **E**, 02:40, the fourth night of an on-call week. **L**, the
engineer had never run this procedure unsupervised. **L–L**, the handover was a one-line
message and the person who knew the rename was asleep.

The finding "used the wrong cluster" was true and worth almost nothing. Five interfaces
were misshapen, and each is fixable.

## Limits

It is a prompt, not an analysis - it tells you where to look and nothing about what you
will find, and its categories overlap enough to argue about. Use it to check coverage after
a [5 Whys](./5-whys.md) or a latent-condition search, not as a substitute for either.
