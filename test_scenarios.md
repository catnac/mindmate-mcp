# MindMate MCP – Test Scenarios

This document describes manual test scenarios for the three MCP tools exposed by the MindMate server.

## 1. Tool: getMotivationalQuote

**Description:**  
Returns a motivational quote based on the given emotion string.

### 1.1 Happy path

| ID  | Input                      | Expected Result                           |
|-----|----------------------------|-------------------------------------------|
| Q01 | emotion = "stressed"       | A stress-related motivational quote       |
| Q02 | emotion = "tired"          | A quote encouraging rest and self-care    |
| Q03 | emotion = "anxious"        | A calming / reassurance style message     |

### 1.2 Edge cases

| ID  | Input                        | Expected Result                                               |
|-----|------------------------------|---------------------------------------------------------------|
| Q10 | emotion = ""                 | Returns a generic default quote (no crash)                   |
| Q11 | emotion = "UNKNOWN_EMOTION"  | Returns a generic fallback quote from the JSON pool          |
| Q12 | emotion = None / missing     | Returns a safe error or fallback message, server still alive |

---

## 2. Tool: suggestMindfulnessActivity

**Description:**  
Suggests a short mindfulness or relaxation activity.

### 2.1 Happy path

| ID  | Input                | Expected Result                                         |
|-----|----------------------|---------------------------------------------------------|
| A01 | emotion = "stressed" | A breathing / grounding style instruction               |
| A02 | emotion = "tired"    | A gentle stretching or short break suggestion           |

### 2.2 Edge cases

| ID  | Input                        | Expected Result                                               |
|-----|------------------------------|---------------------------------------------------------------|
| A10 | emotion = ""                 | Generic activity suggestion (e.g., deep breathing)           |
| A11 | emotion = "random"           | Generic default activity without crashing                    |

---

## 3. Tool: dailyReflectionPrompt

**Description:**  
Returns a short reflection or gratitude question. Takes no input.

### 3.1 Happy path

| ID  | Input | Expected Result                                      |
|-----|-------|------------------------------------------------------|
| D01 | —     | A question about gratitude or daily reflection       |

### 3.2 Edge cases

| ID  | Situation                 | Expected Result                                                 |
|-----|---------------------------|-----------------------------------------------------------------|
| D10 | `prompts.json` is empty   | Default fallback question is returned, no crash                |
| D11 | `prompts.json` is missing | Server handles error gracefully or uses a built-in fallback    |

---

## 4. Test Execution Notes

- All scenarios were tested via the MCP client (Claude Desktop) and/or a local Python runner.
- Special attention was given to:
  - Empty or invalid emotion values
  - Missing / malformed JSON data
  - Stability of the MCP server (no unexpected crashes)
