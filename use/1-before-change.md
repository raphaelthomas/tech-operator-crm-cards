# 🚦 Before a Change

## Time-Out - stop, out loud, everyone

| | |
| :--- | :--- |
| **Who** | Ops on the keys · Monitor watching · who can call the stop |
| **What** | The change, and the exact system it lands on |
| **Rollback** | Tested, and how long it takes to run |
| **Trigger** | The exact condition that means roll back. State it as a number, now. |
| **Time-box** | When we stop and reassess regardless of progress |
| **Gotchas** | Anything known about this system that is not in the runbook? Ask each person by name. |

## Pre-mortem

The change has failed. **Why?** Name three. Mitigate or accept each, aloud.

## Go / No-Go

Each role answers by name, aloud. Any No-Go stops it. **Silence is not a Go.**

## On the keys

| | |
| :--- | :--- |
| **Irreversible action** | Two-person rule - Monitor confirms before you commit it. |
| **Every command** | Point and call: read it aloud, Monitor confirms, then execute. |
| **Trigger hit** | Roll back. Do not reopen the decision. |

### Solo
- Irreversible action: there is no solo two-person rule. Defer it, or wake someone.
- No Monitor: read the command aloud to yourself, and name the three failures anyway.
