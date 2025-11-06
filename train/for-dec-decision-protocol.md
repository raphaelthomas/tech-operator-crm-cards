# FOR-DEC Decision Protocol: High-Tempo Problem Solving 🚀

The **FOR-DEC** model (Fact, Option, Risk, Decision, Execution, Check) is a structured, six-step process for making logical, documented decisions under high stress and time pressure. It is designed to prevent "knee-jerk" reactions by systematically separating the analysis of the situation from the choice of action.

This is the primary decision-making tool for Incident Commanders and lead responders.

---

## The Six Steps of FOR-DEC

### 1. Fact 🔎
* **What is the objective reality?**
* **Goal:** Establish a shared, accurate mental model of the situation.
* **Action:** Synthesize all available data. Focus on **what is known** and **what is unknown**. State the core problem clearly.

### 2. Option 💡
* **What solutions are available?**
* **Goal:** Brainstorm a minimum of two distinct, viable courses of action (including the "Do Nothing" option).
* **Action:** List all possible, immediately actionable responses (e.g., Rollback, Scale up, Clear cache).

### 3. Risk ⚠️
* **What are the consequences of each option?**
* **Goal:** Evaluate the potential side effects (benefits and harm) associated with each option.
* **Action:** Articulate the risk of failure and the potential downstream impact for each listed option.

### 4. Decision 🎯
* **What is the chosen course of action?**
* **Goal:** Select the best option based on the risk/benefit analysis and communicate it clearly.
* **Action:** State the decision with a clear rationale and assign ownership.

### 5. Execution ⚙️
* **Action the decision.**
* **Goal:** Implement the chosen option and delegate tasks clearly.
* **Action:** Team members execute delegated tasks under the supervision of the Incident Commander.

### 6. Check ✅
* **Did the action achieve the desired result?**
* **Goal:** Close the loop and determine if the problem is solved or if a new FOR-DEC cycle is needed.
* **Action:** Validate the fix using the original data points. If the check fails, immediately start a new **FOR-DEC** cycle.



# FOR-DEC Decision Protocol: High-Tempo Problem Solving 🚀

## 1. Introduction: What It Is

The **FOR-DEC** model (Fact, Option, Risk, Decision, Execution, Check) is a six-step, structured process for making logical, documented decisions under high stress and time pressure. It is the core tool used by Incident Commanders to impose structure on chaotic situations and ensure that decisions are based on data, not impulse.

---

## 2. Theory and Background

FOR-DEC originated in the aviation industry (specifically by the German Air Force) to manage non-normal procedures and emergencies, where quick, accurate decisions are paramount. The model’s power lies in separating the **Analysis Phase (F-O-R)** from the **Action Phase (D-E-C)**. This separation prevents operators from jumping directly from observing a problem (**Fact**) to implementing the first solution they think of (**Execution**), which is a common stress-induced error.

| **Mnemonic** | **Phase** | **Core Question** |
| :--- | :--- | :--- |
| **F**act 🔎 | Analysis | What is the objective reality? |
| **O**ption 💡 | Analysis | What solutions are available? |
| **R**isk ⚠️ | Analysis | What are the consequences of each option? |
| **D**ecision 🎯 | Action | What is the chosen course of action? |
| **E**xecution ⚙️ | Action | Action the decision. |
| **C**heck ✅ | Action | Did the action achieve the desired result? |

---

## 3. Example: Database Saturation

| **Step** | **Incident Commander Statement** | **Rationale** |
| :--- | :--- | :--- |
| **Fact** | "DB CPU at 99%, latency spiking to 5 seconds. We see a new query flood from the analytics service." | Establishing a shared reality and identifying the likely source. |
| **Option** | "Option 1: Kill the top 10 running queries. Option 2: Initiate a temporary global rate limit for 5 minutes. Option 3: Failover to the cold replica." | Listing 2+ distinct, viable paths. |
| **Risk** | "Risk of Option 1: Losing non-critical customer transactions. Risk of Option 2: Temporary customer UX degradation. Risk of Option 3: 5 minutes of downtime due to DNS propagation." | Evaluating consequences before commitment. |
| **Decision** | "We are choosing Option 2: Apply a 5-minute global rate limit." | Stating the choice with conviction. |
| **Execution** | "Engineer X, apply the rate limit now and confirm activation in Slack." | Clear delegation and action. |
| **Check** | "CPU dropped to 45%. Latency back to 50ms. The rate limit worked." | Validating success against original metrics. |
