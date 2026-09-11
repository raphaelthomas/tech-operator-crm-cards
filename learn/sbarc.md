# SBAR(C) 💬

## What it is

A four-part structure for handing over or escalating — **S**ituation · **B**ackground ·
**A**ssessment · **R**ecommendation — plus a **C**heck-back to confirm it landed.

It solves a specific failure: the person with the information tells a story, and the
person who needs it wants a conclusion and an ask. SBAR puts the headline first and forces
the sender to commit to a judgement rather than dumping raw data.

## Origin & evidence

SBAR comes from **US Navy nuclear submarines**, where officers briefed the captain in that
order. Doug Bonacum brought it to healthcare, and with Michael Leonard and Suzanne Graham
introduced it at Kaiser Permanente in Colorado around 2002. It is now standard in
hospitals worldwide.

> Leonard, M., Graham, S. & Bonacum, D. (2004). *The human factor: the critical importance
> of effective teamwork and communication in providing safe care.* Quality and Safety in
> Health Care 13(Suppl 1):i85–i90. https://doi.org/10.1136/qshc.2004.010033

The **check-back** is a separate technique, from AHRQ's TeamSTEPPS programme: the receiver
repeats the message and the sender confirms it. It is the same closed loop as nuclear
operations' three-way communication.

Note that the assessment step is deliberately a *judgement*, not data. Leonard and
colleagues' point is that juniors are often trained to report observations and leave
conclusions to seniors, which loses the information most worth having.

## How to run it

| Step | What you say |
| :--- | :--- |
| **S**ituation | What is happening now, and who it affects |
| **B**ackground | What changed, what you already tried |
| **A**ssessment | What you think it is, and how bad — your judgement, stated |
| **R**ecommendation | Exactly what you need from them |
| **C**heck-back | They repeat it; you confirm |

## Worked example

Handing an incident to a fresh commander:

1. **Situation** — "P1. The European API is at a 100% failure rate."
2. **Background** — "Started 45 minutes ago with the v3.1 EU deploy. Rollback is stuck;
   the old version won't clear."
3. **Assessment** — "I think this is the deployment system, not the code. We breach the
   SLA in fifteen minutes."
4. **Recommendation** — "Take command, and get the on-call platform engineer for manual
   cluster intervention."
5. **Check-back** — *"Taking command, calling platform for manual intervention. Correct?"*
   — "Correct."

## Limits

SBAR is built for one sender, one receiver, one ask. It does not structure a group
discussion, and it is a poor fit when the problem is genuinely not yet understood — an
honest "I don't know what this is" is better than an assessment invented to fill the slot.
