# Is / Is-Not 🔲

## What it is

Before hunting a cause, draw the boundary of the problem. For each dimension, record what
the problem **is** - and, just as deliberately, what it **is not** but plausibly could
have been.

The second column is the technique. "Checkout is failing" narrows nothing. "Checkout is
failing *and signup, on the same service and database, is not*" eliminates most of the
candidate causes before you touch a single log.

## Origin & evidence

Kepner-Tregoe Problem Analysis, developed by Charles Kepner and Benjamin Tregoe in the
late 1950s and published in *The Rational Manager*. A problem is defined as a deviation
from expected performance whose cause is not yet known, and the method exists to stop the
characteristic managerial failure of jumping from symptom to presumed cause.

> Kepner, C. H. & Tregoe, B. B. (1965). *The Rational Manager: A Systematic Approach to
> Problem Solving and Decision-Making.* New York: McGraw-Hill.

Their chart asks what, where, when and to what extent - each against a contrasting case
where the problem is absent - and then looks for what is **distinctive** about the problem
case. A cause that cannot explain both the is and the is-not is not the cause.

## How to run it

| | Is | Is not |
| :--- | :--- | :--- |
| **What** is affected | | but could plausibly have been |
| **Where** | | |
| **When** did it start / recur | | |
| **How much** / how many | | |

Then: what distinguishes the left column from the right? Test candidate causes against
*both* columns, and discard any that would also have broken the right-hand side.

Fill it in from evidence, not memory, and leave cells blank when you genuinely do not
know - a guessed is-not is worse than an empty one, because it eliminates the truth.

## Worked example

Checkout is returning 500s. Is-not: signup, which uses the same service and database, is
fine. Is: only EU customers. Is-not: US customers on the same build. Is: began 14:10.
Is-not: nothing deployed since 09:00.

What is distinctive about EU checkout at 14:10 that does not apply to EU signup or US
checkout? Not the release - that is eliminated by the timing. The answer was a payment
provider's regional certificate expiring, which only checkout calls. No logs were read to
get this far.

## Limits

It needs enough observability to answer the questions honestly; on a poorly instrumented
system the is-not column fills with assumption and misleads confidently. It is also built
for a deviation with a clear before-and-after - for slow degradations, or systems that were
never right, there is no contrasting case to compare against.
