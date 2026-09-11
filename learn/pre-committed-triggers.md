# Pre-Committed Triggers ✈️

## What it is

Deciding the abort criterion *before* entering the risky phase, and stating it aloud, so
that the moment of crisis contains execution rather than deliberation.

This is why no card here prints a rollback threshold or a time limit. What transfers is not
a value but the discipline of computing your own in advance and committing to it.

## Origin & evidence

Aviation's model case is **V1**, the takeoff decision speed. Below it there is runway
enough to stop; above it there is not, so the takeoff continues even with a failed engine.
V1 is not a constant: it is calculated fresh for every departure from weight, runway
length, surface and temperature, then briefed before the aircraft moves.

The FAA and industry Takeoff Safety Training Aid analysed 74 rejected-takeoff accidents
and incidents between 1959 and 1990:

- **58% were initiated at speeds in excess of V1** — the stop was begun after the point
  where stopping was still possible.
- **Approximately 80% were potentially avoidable** through appropriate operational
  practice.

Its first lesson is the one that transfers: *"the crew must always be prepared to make the
Go/No Go decision prior to the airplane reaching V1 speed."* The document is blunt about
why in-the-moment judgement fails here — the decision must be made "using rapidly
changing, often incomplete information in a dynamic environment in which the time
available decreases as the criticality of the decision increases."

> Federal Aviation Administration (1993). *Takeoff Safety Training Aid.* Advisory
> Circular 120-62.
> https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/23202

Crews also pre-commit the *ambiguous* case, not just the clear one. The Training Aid's
worked briefing includes: *"if we're not sure of an engine failure 5 knots before V1,
we'll continue the takeoff and I'll state 'CONTINUE TAKEOFF'."* The hardest call is made
while nothing is happening.

## How to use it

- **Compute the trigger for this change**, not for changes in general — error rate,
  latency, queue depth, whatever actually indicates this one failing.
- **State it as a number, aloud, in the brief**, and have someone read it back.
- **Pre-commit the ambiguous case too.** "If we cannot tell whether it is the deploy or
  the database by twenty minutes, we roll back anyway."
- **Two regimes, like the low- and high-speed abort.** Before traffic is cut over, roll
  back for anything. After, only for the severities you named.
- **When the trigger fires, execute.** Reopening the decision at the trigger is the
  failure mode, not a final safety check.

## Worked example

The brief sets rollback at an error rate above 2% sustained for five minutes. At minute
seven errors sit at 2.4%, and someone says they look like they are levelling off. That
sentence is the accident: the trigger has fired, and the decision is being reopened with
worse information than it was made with.

## Limits

A pre-committed trigger is only as good as the signal behind it — a threshold on a metric
that does not actually track user harm will fire late, or never. Triggers also need review
after the fact: if you routinely blow through one, it was wrong, and the fix is a better
number next time rather than a habit of ignoring it.
