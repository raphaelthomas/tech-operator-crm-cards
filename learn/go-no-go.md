# Go / No-Go Poll 🚦

## What it is

Before committing, the person in charge polls each role **by name**, and each answers
aloud: go, or no-go. Any no-go stops it.

The design constraint is that **silence must not count as agreement.** A poll makes every
participant produce a positive statement, which is what separates it from "any objections?"
— a question whose most common answer is nothing, from people who had one.

## Origin & evidence

NASA's launch status check. In the final countdown the flight or launch director queries
each console — propulsion, guidance, life support, communications — by call sign, and each
controller declares the status of their system. The launch does not proceed until every
station has answered.

> NASA. *Launch status check.* https://en.wikipedia.org/wiki/Launch_status_check

Three features carry over. Each person is polled **individually by name**, so nobody can
hide in a group nod. Each is accountable for a **specific system**, not for a general
feeling about readiness. And the veto is **unilateral** — one no-go stops the count without
requiring the objector to win an argument.

## How to run it

- **Poll by name and by role.** "Database — go or no-go?" Not "everyone happy?"
- **Require the word.** A nod does not carry over a video call, and neither does silence.
- **Poll the person who owns the system**, not the most senior person present.
- **A no-go needs no justification** to be honoured. Ask afterwards, not as a condition of
  stopping.
- **Poll last**, immediately before the action, once the brief and checks are done.

## Worked example

Four roles: deploy, database, monitoring, comms. Monitoring answers "no-go — the
dashboard for the checkout service has been stale for ten minutes and I can't tell you
whether it's the dashboard or the service." Fifteen seconds, and the change is deferred
until the team can actually see what it is about to do. Under "any objections?" that
person says nothing, because what they have is a doubt rather than an argument.

## Limits

It only tests what each role can actually see; polling someone with no instrumentation
produces a confident go that means nothing. It is also vulnerable to seniority — if the
person running the change answers first and loudly, later answers converge on theirs. Poll
the most junior or most peripheral role first, and the answers stay independent.
