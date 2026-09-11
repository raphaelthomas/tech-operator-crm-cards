# FOR-DEC 🚀

## What it is

A six-step structure for deciding under time pressure: **F**acts · **O**ptions ·
**R**isks & benefits · **D**ecision · **E**xecution · **C**heck.

Its whole value is the break between **FOR** and **DEC** - analysis and action. Under
stress the default path runs straight from noticing a problem to executing the first
plausible fix. FOR-DEC forces a shared picture and at least two options to exist before
anyone commits.

## Origin & evidence

Developed jointly by **Lufthansa and the German Aerospace Center (DLR)**, following the
Lufthansa CRM working group set up in autumn 1992, and described by Hörmann as a
prescriptive model for aeronautical decision-making. It is taught in German commercial
aviation and has since spread to medicine and emergency services.

> Hörmann, H.-J. (1995). *FOR-DEC: A prescriptive model for aeronautical decision making.*
> In Fuller, R., Johnston, N. & McDonald, N. (eds), Human Factors in Aviation Operations.
> Aldershot: Avebury Aviation.

> Soll, H., Proske, S., Hofinger, G. & Steinhardt, G. (2016). *Decision-Making Tools for
> Aeronautical Teams: FOR-DEC and Beyond.* Aviation Psychology and Applied Human Factors
> 6(2):101–112. https://doi.org/10.1027/2192-0923/a000099

Soll and colleagues' review is also the source of its main caveat: the model is useful
"for structured decision-making in complex situations **when there is enough time**."

## How to run it

| Step | Question | What good looks like |
| :--- | :--- | :--- |
| **F**acts | What is objectively true? | What is known *and* what is unknown, said aloud |
| **O**ptions | What could we do? | At least two, one of which is doing nothing |
| **R**isks | What does each cost? | Including the risk of *not* acting |
| **D**ecision | What are we doing? | One option, named owner |
| **E**xecution | Do it | Delegated explicitly, not assumed |
| **C**heck | Did it work? | Against the facts from step one - or start again |

## Worked example

| Step | Incident commander |
| :--- | :--- |
| **F**acts | "Database CPU 99%, latency 5s, query flood from the analytics service. We don't know why it started." |
| **O**ptions | "One: kill the top queries. Two: rate-limit analytics. Three: fail over to the replica. Four: nothing." |
| **R**isks | "One loses transactions. Two degrades reporting. Three costs five minutes of downtime. Nothing means we stay down." |
| **D**ecision | "Two. Rate-limit analytics. I own it." |
| **E**xecution | "Sam, apply the limit now and confirm in channel." |
| **C**heck | "CPU 45%, latency 50ms. Holding. Root cause still unknown - that's the next cycle." |

## Limits

FOR-DEC needs time you may not have. For genuinely time-critical actions, a pre-committed
trigger is the right tool, not a decision cycle. It also produces nothing useful from bad
facts: if step one is guesswork, the structure will lend false confidence to whatever
follows.
