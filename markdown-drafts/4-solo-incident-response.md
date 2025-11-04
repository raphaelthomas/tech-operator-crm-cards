# 🛑 Tech Operator Solo Operations Card

Focus **Self-Regulation, Structured Thinking, and Efficient Escalation** as highest-value approach for a solo operator.

## 🧠 FOCUS & STABILITY (Internal Check)

| 🎯 **CRITICAL ACTION** | **ACTION / REMINDER** |
| :--- | :--- |
| **1. Stop Fixation** | **"STOP & BREATHE":** If you feel panic, frustration, or tunnel vision, **physically stand up and step away for 60 seconds.** Force a cognitive reset before touching the keyboard again. |
| **2. Self-Assessment** | **Check IMSAFE:** Am I fit to operate? *Illness, Medication, Stress, Alcohol/Fatigue, Emotion*. **If any are "Red," call for immediate relief.** |
| **3. Risk Tolerance** | **KISS Rule (Keep It Simple, Stupid):** When selecting an option, **prefer the simplest, lowest-risk action** that solves the immediate problem. Avoid complex, multi-step solutions during high stress. |
| **4. Call for Help** | **The 3-Second Rule:** If you are *thinking* about calling for help, **do it now.** Don't wait until the situation is catastrophic. |

## 🟢 SBAR: ESCALATION & HANDOFF FRAMEWORK

Use this framework when calling a specialist, handing off the incident, or providing a critical update to a stakeholder.

| Mnemonic | What to State Clearly | Solo Operator Application |
| :--- | :--- | :--- |
| **S**ituation | **What is the current problem?** (The specific, immediate issue.) | *“The Primary Service is down and has been for 15 minutes.”* |
| **B**ackground | **What is the context leading up to this?** (History, recent changes, attempts made.) | *“A config deployment failed. I tried a rollback, but logs show the DB is now unresponsive.”* |
| **A**ssessment | **What is your conclusion or analysis?** (What you think is happening, severity, risk.) | *“I suspect a resource exhaustion issue. We are at risk of data loss if not resolved quickly.”* |
| **R**ecommendation | **What action do you need from them?** (Specific request for next step/help.) | *“I need you to join the bridge and take the lead on DB diagnostics.”* |

## 🛠️ FOR-DEC: STRUCTURED PROBLEM SOLVING

| FRAMEWORK | **SOLO ENGINEER ACTIONS** |
| :--- | :--- |
| **1. F**acts | **Gather Data:** What are the hard facts? System logs, metrics, status codes. **Ignore assumptions and noise.** |
| **2. O**ptions | **Brainstorm:** What are the possible solutions? (List 2-3 simple actions: Restart service, Revert change, Failover.) |
| **3. R**isks & Benefits | **Weigh Options:** What is the risk of *this* action? What is the risk of *no* action? **(Use KISS Rule here.)** |
| **4. D**ecision | **Commit:** Choose the best course of action. **Do not hesitate** once data supports it. |
| **5. E**xecution | **Verify & Act:** Execute the change **slowly and deliberately**. Verbalize the command before hitting Enter. |
| **6. C**heck & Control | **Verify:** Check metrics/logs to confirm the action worked. If not, **return to Step 1 (Facts).** |

## 📝 ERROR PREVENTION PROTOCOL

| RULE | ACTION / INSTRUCTION |
| :--- | :--- |
| **"Write It Down"** | **Live-Document:** Record every single command, action, and timestamp in the incident journal/chat **as you execute it.** |
| **Communication Clarity** | **Close the Loop:** When receiving instructions from a specialist, **repeat the instruction back** to ensure mutual understanding. |
| **The 3-WAY Rule** | **Critical Command Check:** For *any* irreversible command (e.g., delete, purge): **1. Say It** (out loud or into the mic). **2. Type It.** **3. Review It** (read it back) before executing. |
| **Checklist Discipline** | **Use the Runbook:** For any known procedure, **use the official checklist**. Do not rely on memory in a high-stress environment. |
| **Fatigue Awareness** | **Know Your Limit:** If you have been working for more than 4 hours on a critical incident, you are at high risk of error. **Mandate a relief team or take a 10-minute break.** |
