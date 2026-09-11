# Swiss Cheese and Latent Conditions 🧀

## What it is

Defences against failure are layered, and every layer has holes. An accident happens when
holes in successive layers line up and let a hazard through.

The holes come from two sources. **Active failures** are the unsafe acts at the sharp end
— the wrong command, the missed alarm. **Latent conditions** are decisions taken long
before, often far away, that sat dormant in the system: a staffing choice, a deferred
upgrade, a default that was convenient at the time.

## Origin & evidence

James Reason's model of organisational accidents, which reframed investigation away from
the last person to touch the system.

> Reason, J. (1990). *Human Error.* Cambridge: Cambridge University Press.
>
> Reason, J. (2000). *Human error: models and management.* BMJ 320:768–770.
> https://doi.org/10.1136/bmj.320.7237.768

Reason's central argument is that active failures are hard to foresee and largely
unpreventable by exhortation, while latent conditions can be **identified and repaired
before an accident** — which makes them the better target. His distinction between the
*person approach* and the *system approach* is the intellectual ancestor of the blameless
postmortem.

The holes move. Layers are not static barriers but shift with load, staffing and time of
day, which is why the same system survives on Tuesday and fails on Friday.

## How to use it

In a review, do not stop when you have found the act that broke it:

- **List every layer that should have caught this** — tests, review, monitoring, alerting,
  canary, rate limits, the runbook, the reviewer — and for each, why it did not.
- **Ask when each hole was made.** The latent condition usually predates the incident by
  months.
- **Fix holes, not people.** The active failure is rarely repeatable; the latent condition
  is waiting for the next person.
- **Count the layers that held.** If only one stood between you and disaster, you were
  lucky, and luck is not a control.

## Worked example

An engineer runs a migration against production. The active failure is obvious. The layers:
the tool defaults to the last-used context (hole made two years ago); staging and prod
prompts are visually identical (a design decision); the reviewer approved a diff that did
not show the target; there is no confirmation step for destructive statements; the alert
fired but into a channel nobody watches at 19:00.

Five holes, one of them a person, four of them decisions made calmly, in daylight, by
people who were not present that evening.

## Limits

The metaphor is popular partly because it is comforting — it implies a tidy stack of
independent barriers, where real systems have couplings, and it can encourage endless
layering rather than simplification. It also says little about how *success* is normally
produced; for that see [Safety-II and Work-as-Done](./safety-ii-wad-wai.md).
