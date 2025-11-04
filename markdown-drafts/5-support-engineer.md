# 💻 Tech Operator 3rd Level Support Card

Highly focused on structured problem-solving and proactive context gathering.

## 🔎 PHASE 1: DIAGNOSIS STRATEGY (The Core)

This phase mandates a rapid, structured approach to defining the problem scope before escalation.

| Tool | Focus | Action / Instruction |
| :--- | :--- | :--- |
| **Is / Is Not Analysis** | **SCOPE DEFINITION** | **Mandate:** Create a table to establish boundaries. **What** is failing? **What** is *not* failing? **When** did it start? **When** did it *not* happen? **Where** is it happening? **Where** is it *not* happening? |
| **TRIAL-RUN Debugging** | **Hypothesis Testing** | Use a structured approach for technical investigation:<br>**T**est hypothesis. **R**eplicate the failure. **I**solate variables. **A**nalyze results. **L**og everything. **R**epeat. **U**pdate documentation. **N**otify customer. |
| **Modified 5 Whys** | **Cause Identification** | After defining the scope, ask **"Why?"** repeatedly. Focus on identifying the next logical dependency or team. |
| **KISS Rule** | **Solution Preference** | **Keep It Simple, Stupid.** When multiple solutions are found, **prefer the lowest-risk, simplest fix** that addresses the identified cause. |

## 🚨 PHASE 2: INCIDENT & RESOURCE MANAGEMENT (The Triage Limit)

This section now enforces a strict **triage-and-escalate** mindset.

| Rule | Action / Instruction |
| :--- | :--- |
| **The 30-Minute Rule** | **Limit investigation time:** If the root cause is **not found within 30 minutes**, STOP. **Escalate immediately** to the next tier, a Subject Matter Expert (SME), or initiate a formal incident bridge. |
| **The 3-Second Rule** | If you are *thinking* about calling for help, **do it now.** Escalate to the appropriate resource (SME, management) immediately. |
| **Documentation Mandate** | **Live-Document:** Record all **commands executed, logs analyzed, and hypotheses tested** in the ticket **as they happen.** This ensures efficient handoffs. |

## 📞 PHASE 3: CUSTOMER COMMUNICATION (SBAR-C & Context)

Use this structured format for status updates and ensure all necessary context is gathered upfront.

| Tool | Focus | Communication Action |
| :--- | :--- | :--- |
| **Context Protocol** | **Initial Data Gathering** | Before troubleshooting, ensure you have: 1. **User ID/Machine ID/Endpoint.** 2. **Exact Time** of failure. 3. **Exact Error Message/Screenshot.** 4. **Last Action** taken by user before failure. |
| **SBAR-C** | **Status Update** | Use this structure for any critical update to a customer or manager:<br>**S**ituation, **B**ackground, **A**ssessment, **R**ecommendation, **C**losing (Next Update Time). |
| **Clarity Check** | **Managing Expectations** | **Avoid jargon.** State what you are doing, why, and when you will provide the next update. **Always deliver on your stated update time.** |

## 🟢 PHASE 4: ESCALATION HANDOFF (Internal)

| Tool | Focus | Action / Instruction |
| :--- | :--- | :--- |
| **SME Handoff** | **Clarity** | When handing off to a Subject Matter Expert (SME), use the **SBAR** format (without the 'C') to brief them quickly and accurately. |
| **Final Check** | **Personal Readiness** | Before declaring the ticket **"Done,"** ensure the root cause found is addressed by the fix, not just the symptom. **Was the 30-Minute Rule triggered? Why?** |
