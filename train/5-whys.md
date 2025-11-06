# Modified 5 Whys: Uncovering Systemic Flaws 🔍

## 1. Introduction: What It Is

The **Modified 5 Whys** is a root cause analysis technique designed to drill down from an observed symptom to a deep, organizational failure. The "Modified" aspect ensures that the investigation focuses strictly on **systemic and process failures**, deliberately bypassing the tendency to stop the inquiry at human error (the "Why did the engineer forget the step?").

This method, popularized by Toyota, uses a simple iterative questioning process to uncover the chain of causality.

## 2. Theory and Background

The original **5 Whys** technique was developed at Toyota in the 1930s to troubleshoot production line issues. The theory holds that by asking "Why?" five times, you can reliably move past surface symptoms to the root cause.

In incident response, the 5 Whys is modified to adhere to **Blameless Culture** principles. The key rule is: **Never accept a human error as the final answer.** Every human error is treated as a symptom of a deeper systemic failure in Policy, Procedures, or Training (the 4 Ps).

| 

| **Goal of Questioning** | **Focus Shift** | **Target Outcome** | 
| **Surface Level** (Why 1-2) | Symptom to **Active Error** | The immediate action that caused the failure. | 
| **Mid Level** (Why 3-4) | Active Error to **Precondition** | The lack of a safeguard or procedural failure that enabled the error. | 
| **Deep Level** (Why 5) | Precondition to **Latent Flaw** | The management, budget, or policy decision that created the precondition. | 

## 3. Example: The Delayed Rollback ⏱️

**Initial Problem:** A critical deployment failed, and the manual rollback took 45 minutes longer than expected, extending the outage.

| **#** | **Question** | **Answer** | **Systemic Flaw Identified** | 
| **Why 1** | Why did the rollback take 45 minutes? | Because the engineer had to manually look up the secure credentials and commands for the legacy load balancer. | Inefficient Procedure | 
| **Why 2** | Why weren't the credentials and commands automated? | Because the new centralized secret management system doesn't support the legacy load balancer API. | Technical Debt / Tooling Gap | 
| **Why 3** | Why is that legacy load balancer still in production? | Because the project to deprecate it was halted and its budget reallocated six months ago. | Policy / Resource Allocation | 
| **Why 4** | Why was the budget reallocated? | Because management prioritized a new customer-facing feature over infrastructure resilience work. | Policy / Prioritization Mismatch | 
| **Why 5** | Why did the product goal outweigh the clear security/resilience risk of the legacy load balancer? | Because the internal resilience risks were not quantified and prioritized against new revenue generation in the planning process. | **Systemic Flaw:** Inadequate risk-quantification methodology. |
