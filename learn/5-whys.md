# 5 Whys 🔍

## What it is

Ask "why?" repeatedly, treating each answer as the symptom of something further back,
until you reach a cause worth fixing.

In incident review one rule governs it: **never accept human error as the final answer.**
"The engineer forgot the step" is where the investigation gets interesting, not where it
stops. Each answer should move outward — from the action, to the condition that allowed
it, to the decision that created the condition.

| Depth | Moves from | To |
| :--- | :--- | :--- |
| Why 1–2 | Symptom | The action taken |
| Why 3–4 | The action | The missing safeguard that let it through |
| Why 5+ | The safeguard | The policy, budget or priority behind its absence |

Five is a rule of thumb, not a quota. Stop when the answer names something you can change.

## Origin & evidence

Developed by **Sakichi Toyoda** at Toyota in the early twentieth century and formalised by
**Taiichi Ohno** as part of the Toyota Production System, where he described repeating
"why" five times as the basis of Toyota's scientific approach.

> Ohno, T. (1988). *Toyota Production System: Beyond Large-Scale Production.*
> Cambridge, MA: Productivity Press.

The blameless framing is a later addition from software incident practice, where the
technique is paired with Reason's latent conditions — see [Safety-II and
Work-as-Done](./safety-ii-wad-wai.md) for the strongest version of that argument.

## How to run it

- Start from a fact, not a characterisation. "The rollback took 45 minutes", not "the
  rollback was botched."
- Write each answer down. The chain is the output, not the last line.
- If an answer names a person, ask what made that the reasonable choice at the time.
- Stop at something actionable and owned. "Human nature" and "the org is like that" mean
  you have gone one step too far.

## Worked example

**A deployment failed and the manual rollback took 45 minutes longer than expected.**

| | Question | Answer |
| :--- | :--- | :--- |
| 1 | Why did the rollback take 45 minutes? | The engineer had to look up credentials and commands for the legacy load balancer by hand. |
| 2 | Why were those not automated? | The central secret manager does not support that load balancer's API. |
| 3 | Why is the load balancer still in production? | Its deprecation project was halted six months ago. |
| 4 | Why was it halted? | Its budget went to a customer-facing feature. |
| 5 | Why did that trade look correct? | Resilience risk was never quantified, so it could not compete with revenue in planning. |

The fix is not "automate the rollback." It is that the planning process cannot see
resilience risk — which would also have produced the next three incidents.

## Limits

The 5 Whys is widely criticised, and fairly. It follows a *single* causal chain when real
incidents have several; different facilitators reliably reach different "root causes" from
the same evidence; and the framing of "root cause" itself suggests failure has one origin,
which complex systems rarely oblige. Use it to open up an investigation, not to close one,
and pair it with a method that spreads sideways.
