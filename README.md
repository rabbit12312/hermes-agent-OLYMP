# 🏛️ OLYMPUS — A Living Second Brain

> *Most AI assistants wait to be asked. OLYMPUS works while you sleep.*

OLYMPUS is a multi-agent Second Brain built on top of [Hermes Agent](https://nousresearch.com/hermes-agent). Five specialist agents — each named after a Greek god — share one persistent memory layer and work autonomously around the clock.

You don't manage the system. You just live. Olympus handles the rest.

---

## ⚡ How It Works

Every message you send is routed by **HERMES** — the orchestrator — to the right specialist. Gods work in parallel, share the same memory, and deliver results to your Telegram.

```
You speak → HERMES routes → Gods act → Memory persists → Telegram delivers
```

All 5 gods read and write to the same `MEMORY.md`. Perseus writes, Mnemosyne reads, Asclepius analyzes, Argus enriches alerts — one brain, five specializations.

---

## 🏛️ The Pantheon

### ⚡ HERMES — The Orchestrator
The central router. Every message passes through Hermes first. He decides which god (or gods) to wake, never answers from his own knowledge, and always shows which gods were consulted.

- Routes to multiple gods **in parallel** when needed
- Forbidden from touching memory or search directly
- Always shows: `⚔️ PERSEUS captured / 🌊 MNEMOSYNE found / 👁️ ARGUS watching`

---

### ⚔️ PERSEUS — The Memory Hunter
Captures **everything** you say and structures it into persistent, tagged memory.

```
[PERSON]   Anton Volkov — prefers directness, works in VC. Met 2026-03-10.
[EVENT]    Meeting with Anton, 2026-03-11 09:00 — goal: OLYMPUS demo.
[TASK]     Submit hackathon project — deadline: 2026-03-15 | priority: high
[IDEA]     AI job aggregator with candidate scoring — mentioned 3x, growing excitement
[DECISION] Chose Python over TypeScript — reason: hermes-agent ecosystem
```

**Pattern detection:** if a topic or person appears 3+ times, Perseus automatically creates a pattern file at `~/.hermes/olympus/patterns/[topic].md` — tracking all occurrences, dates, and emerging patterns.

---

### 🌊 MNEMOSYNE — The Goddess of Memory
Searches your entire history **by meaning**, not keywords. Finds what you forgot you knew.

Searches 3 layers simultaneously:
1. **Memory context** — instant scan of current `MEMORY.md`
2. **Past sessions** — deep search across all conversation history
3. **Olympus files** — notes and pattern files in `~/.hermes/olympus/`

Always returns: direct answer + related discoveries + pattern note.

> *"That startup idea" → finds first mention (Feb 12), all 6 occurrences, emotional trajectory, and flags it as high-recurrence.*

---

### 🌿 ASCLEPIUS — The Pattern Healer
Runs **every morning at 09:00** via cron. Reads 7 days of memory, finds non-obvious behavioral patterns, sends top 3 insights to Telegram.

Pattern categories:
- **Energy cycles** — days/times when fatigue appears
- **Procrastination signatures** — tasks appearing multiple times without `[DONE]`
- **High-frequency people** — relationships that need attention
- **Idea momentum** — ideas mentioned 6x are not casual thoughts
- **Emotional drift** — excitement → frustration = blocked project
- **Unresolved threads** — past events with no follow-up

```
🌿 ASCLEPIUS — Morning Diagnostics

PATTERN 1: Wednesday Fatigue Cycle
You mention low energy on Wednesdays 3 weeks in a row.
→ Consider moving one meeting to Tuesday.

PATTERN 2: Stalled task — "OLYMPUS README"
Appears in 3 sessions without [DONE] tag.
→ Schedule a focused 30-min block today.
```

---

### 👁️ ARGUS — The Hundred-Eyed Giant
Never sleeps. Checks your watch list **every 30 minutes**. When a condition triggers, fetches memory context about the subject and sends a rich Telegram alert.

Not just: *"Meeting in 2 minutes"*
But: *"Anton prefers directness. Your goal: demo OLYMPUS architecture. Last meeting went well."*

Watch types:
| Type | Example |
|------|--------|
| `time_before` | Alert 5 min before any event |
| `recurring_time` | Every morning at 08:00 |
| `deadline` | 3 hours before task deadline |
| `custom_check` | Any custom condition |

---

### 💪 HERACLES — The Weekly Synthesizer
Every **Sunday at 19:00**, reads the entire week, and delivers one structured digest to Telegram.

Sections:
- 🏆 **VICTORIES** — what actually got done
- 📅 **WEEK IN EVENTS** — people, meetings, decisions
- ⚡ **WHAT MOVED FORWARD** — projects and ideas with momentum
- 🔄 **STILL OPEN** — unresolved threads (most actionable section)
- 🌿 **ASCLEPIUS WISDOM** — top weekly pattern
- 📊 **NUMBERS** — sessions, memories captured, people engaged

---

## 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/rabbit12312/hermes-agent-OLYMP
cd hermes-agent-OLYMP

# 2. Install Hermes Agent
pip install hermes-agent
# or: curl -fsSL https://get.hermes.sh | sh

# 3. Copy config with OLYMPUS gods pre-loaded
cp cli-config.yaml.example ~/.hermes/cli-config.yaml

# 4. Add your API key to .env
cp .env.example .env
# edit .env: add ANTHROPIC_API_KEY or OPENAI_API_KEY

# 5. Run
hermes
```

All 5 gods are pre-loaded via `default_skills` in the config. Cron jobs for Asclepius, Argus, and Heracles start automatically.

---

## 📁 Project Structure

```
hermes-agent-OLYMP/
├── olympus/              # God skill files
│   ├── hermes.md         # Orchestrator — routing rules
│   ├── perseus.md        # Memory capture & tagging
│   ├── mnemosyne.md      # Semantic memory search
│   ├── asclepius.md      # Daily pattern analysis
│   ├── argus.md          # Monitoring & alerts
│   └── heracles.md       # Weekly digest
├── cli-config.yaml.example  # Ready config with default_skills
├── .env.example          # API keys template
└── cron/                 # Cron job schedulers
```

---

## 🛠️ Stack

- **[Hermes Agent](https://nousresearch.com/hermes-agent)** — multi-agent framework
- **Claude Sonnet** via Anthropic (or any supported LLM)
- **Cron jobs** — Asclepius daily, Argus every 30min, Heracles weekly
- **Telegram** — delivery channel for all proactive outputs
- **Markdown memory** — `MEMORY.md` + `USER.md` as persistent state

---

## 💡 The Core Insight

The difference between OLYMPUS and a regular AI assistant:

| Regular Assistant | OLYMPUS |
|---|---|
| Answers when asked | Acts autonomously on schedule |
| No memory between sessions | Persistent structured memory |
| One agent does everything | 5 specialists, each owns one domain |
| You manage the system | System manages itself |
| Forgets who you met yesterday | Remembers patterns across weeks |

---

Built with ❤️ for the Hermes Agent hackathon · Nous Research
