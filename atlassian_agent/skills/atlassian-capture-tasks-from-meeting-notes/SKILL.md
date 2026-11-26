---
name: atlassian-capture-tasks-from-meeting-notes
skill_type: skill
description: >-
  Analyze meeting notes to find action items and create Jira tasks for assigned work. When an agent needs to: (1) Create Jira tasks or tickets from meeting notes, (2) Extract or find action items from notes or Confluence pages, (3) Parse meeting notes for assigned tasks, or (4) Analyze notes and generate tasks for team members.
---

# Capture Tasks from Meeting Notes

Scope: Analyze meeting notes to find action items and create Jira tasks for assigned work. When an agent needs to: (1) Create Jira tasks or tickets from meeting notes, (2) Extract or find action items from notes or Confluence pages, (3) Parse meeting notes for assigned tasks, or (4) Analyze notes and generate tasks for team members. Identifies assignees, looks up account IDs, and creates tasks with proper context.

## Keywords
meeting notes, action items, create tasks, create tickets, extract tasks, parse notes, analyze notes, assigned work, assignees, from meeting, post-meeting, capture tasks, generate tasks, turn into tasks, convert to tasks, action item, to-do, task list, follow-up, assigned to, create Jira tasks, create Jira tickets, meeting action items, extract action items, find action items, analyze meeting

## Overview

Automatically extract action items from meeting notes and create Jira tasks with proper assignees. This skill parses unstructured meeting notes (from Confluence or pasted text), identifies action items with assignees, looks up Jira account IDs, and creates tasks—eliminating the tedious post-meeting ticket creation process.

**Use this skill when:** Users have meeting notes with action items that need to become Jira tasks.

---

## Steps

1. Get the notes by calling `getConfluencePage` for a URL, or accept pasted text. Verify the body is non-empty before parsing.
2. Extract action items and their assignees from the notes using `references/action-item-patterns.md`. Verify each item has an action verb and a named owner or is marked unassigned.
3. Ask for the project key and check it with `getVisibleJiraProjects`. Verify the key is in the returned list.
4. Resolve each assignee with `lookupJiraAccountId`(searchString). Verify exactly one account matched, and ask the user when none or several matched.
5. Show the list to the user and create approved tasks with `createJiraIssue`. Verify each response returns an issue key and report all keys.

## Failure recovery

| Failure | Cause | Recovery |
|---|---|---|
| No action items found | The notes lack a recognizable pattern | Show the user what was scanned and apply the patterns in `references/action-item-patterns.md`, or ask for the items directly. |
| Assignee lookup returns none | The name differs from the Jira display name | Retry `lookupJiraAccountId` with the email or surname, or create the task unassigned and say so. |
| Task creation rejected | A required field or issue type is missing | Read `getJiraProjectIssueTypesMetadata` for the project and supply the missing field. |

## Workflow

Follow this 7-step process to turn meeting notes into actionable Jira tasks:

### Step 1: Get Meeting Notes

Obtain the meeting notes from the user.

#### Option A: Confluence Page URL

If user provides a Confluence URL:

```
getConfluencePage(
  cloudId="...",
  pageId="[extracted from URL]",
  contentFormat="markdown"
)
```

**URL patterns:**
- `https://[site].atlassian.net/wiki/spaces/[SPACE]/pages/[PAGE_ID]/[title]`
- Extract PAGE_ID from the numeric portion
- Get cloudId from site name or use `getAccessibleAtlassianResources`

#### Option B: Pasted Text

If user pastes meeting notes directly:
- Use the text as-is
- No fetching needed

#### If Unclear

Ask: "Do you have a Confluence link to the meeting notes, or would you like to paste them directly?"

---

### Step 2: Parse Action Items

Scan the notes for action items with assignees.

#### Common Patterns

**Pattern 1: @mention format** (highest priority)
```
@Sarah to create user stories for chat feature
@Mike will update architecture doc
```

**Pattern 2: Name + action verb**
```
Sarah to create user stories
Mike will update architecture doc
Lisa should review the mockups
```

**Pattern 3: Action: Name - Task**
```
Action: Sarah - create user stories
Action Item: Mike - update architecture
```

**Pattern 4: TODO with assignee**
```
TODO: Create user stories (Sarah)
TODO: Update docs - Mike
```

**Pattern 5: Bullet with name**
```
- Sarah: create user stories
- Mike - update architecture
```

#### Extraction Logic

**For each action item, extract:**

1. **Assignee Name**
   - Text after @ symbol
   - Name before "to", "will", "should"
   - Name after "Action:" or in parentheses
   - First/last name or full name

2. **Task Description**
   - Text after "to", "will", "should", "-", ":"
   - Remove markers (@, Action:, TODO:)
   - Keep original wording
   - Include enough context

3. **Context** (optional but helpful)
   - Meeting title/date if available
   - Surrounding discussion context
   - Related decisions

#### Example Parsing

**Input:**
```
# Product Planning - Dec 3

Action Items:
- @Sarah to create user stories for chat feature
- Mike will update the architecture doc
- Lisa: review and approve design mockups
```

**Parsed:**
```
1. Assignee: Sarah
   Task: Create user stories for chat feature
   Context: Product Planning meeting - Dec 3

2. Assignee: Mike
   Task: Update the architecture doc
   Context: Product Planning meeting - Dec 3

3. Assignee: Lisa
   Task: Review and approve design mockups
   Context: Product Planning meeting - Dec 3
```

---

### Step 3: Ask for Project Key

Before looking up users or creating tasks, identify the Jira project.

**Ask:** "Which Jira project should I create these tasks in? (e.g., PROJ, PRODUCT, ENG)"

#### If User is Unsure

Call `getVisibleJiraProjects` to show options:

```
getVisibleJiraProjects(
  cloudId="...",
  action="create"
)
```

Present: "I found these projects you can create tasks in: PROJ (Project Alpha), PRODUCT (Product Team), ENG (Engineering)"

---

### Step 4: Lookup Account IDs

For each assignee name, find their Jira account ID.

#### Lookup Process

```
lookupJiraAccountId(
  cloudId="...",
  searchString="[assignee name]"
)
```

**The search string can be:**
- Full name: "Sarah Johnson"
- First name: "Sarah"
- Last name: "Johnson"
- Email: "sarah@company.com"

#### Handle Results

**Scenario A: Exact Match (1 result)**
```
✅ Found: Sarah Johnson (sarah.johnson@company.com)
→ Use accountId from result
```

**Scenario B: No Match (0 results)**
```
⚠️ Couldn't find user "Sarah" in Jira.

Options:
1. Create task unassigned (assign manually later)
2. Skip this task
3. Try different name format (e.g., "Sarah Johnson")

Which would you prefer?
```

**Scenario C: Multiple Matches (2+ results)**
```
⚠️ Found multiple users named "Sarah":
1. Sarah Johnson (sarah.johnson@company.com)
2. Sarah Smith (sarah.smith@company.com)

Which user should be assigned the task "Create user stories"?
```

#### Best Practices

- Try full name first ("Sarah Johnson")
- If no match, try first name only ("Sarah")
- If still no match, ask user
- Cache results (don't lookup same person twice)

---

### Step 5: Present Action Items

**CRITICAL:** Always show the parsed action items to the user BEFORE creating any tasks.

#### Presentation Format

```
I found [N] action items from the meeting notes. Should I create these Jira tasks in [PROJECT]?

1. [TASK] [Task description]
   Assigned to: [Name] ([email if found])
   Context: [Meeting title/date]

2. [TASK] [Task description]
   Assigned to: [Name] ([email if found])
   Context: [Meeting title/date]

[...continue for all tasks...]

Would you like me to:
1. Create all tasks
2. Skip some tasks (which ones?)
3. Modify any descriptions or assignees
```

#### Wait for Confirmation

Do NOT create tasks until user confirms. Options:
- "Yes, create all" → proceed
- "Skip task 3" → create all except #3
- "Change assignee for task 2" → ask for new assignee
- "Edit description" → ask for changes

---

### Step 6: Create Tasks

Once confirmed, create each Jira task.

#### Determine Issue Type

Before creating tasks, check what issue types are available in the project:

```
getJiraProjectIssueTypesMetadata(
  cloudId="...",
  projectIdOrKey="PROJ"
)
```

**Choose the appropriate issue type:**
- Use "Task" if available (most common)
- Use "Story" for user-facing features
- Use "Bug" if it's a defect
- If "Task" doesn't exist, use the first available issue type or ask the user

#### For Each Action Item

```
createJiraIssue(
  cloudId="...",
  projectKey="PROJ",
  issueTypeName="[Task or available type]",
  summary="[Task description]",
  description="[Full description with context]",
  assignee_account_id="[looked up account ID]"
)
```

#### Task Summary Format

Use action verbs and be specific:
- ✅ "Create user stories for chat feature"
- ✅ "Update architecture documentation"
- ✅ "Review and approve design mockups"
- ❌ "Do the thing" (too vague)

#### Task Description Format

```markdown
**Action Item from Meeting Notes**

**Task:** [Original action item text]

**Context:**
[Meeting title/date]
[Relevant discussion points or decisions]

**Source:** [Link to Confluence meeting notes if available]

**Original Note:**
> [Exact quote from meeting notes]
```

**Example:**
```markdown
**Action Item from Meeting Notes**

**Task:** Create user stories for chat feature

**Context:**
Product Planning Meeting - December 3, 2025
Discussed Q1 roadmap priorities and new feature requirements

**Source:** https://yoursite.atlassian.net/wiki/spaces/TEAM/pages/12345

**Original Note:**
> @Sarah to create user stories for chat feature
```

---

### Step 7: Provide Summary

After all tasks are created, present a comprehensive summary.

**Format:**
```
✅ Created [N] tasks in [PROJECT]:

1. [PROJ-123] - [Task summary]
   Assigned to: [Name]
   https://yoursite.atlassian.net/browse/PROJ-123

2. [PROJ-124] - [Task summary]
   Assigned to: [Name]
   https://yoursite.atlassian.net/browse/PROJ-124

[...continue for all created tasks...]

**Source:** [Link to meeting notes]

**Next Steps:**
- Review tasks in Jira for accuracy
- Add any additional details or attachments
- Adjust priorities if needed
- Link related tickets if applicable
```

---

## Action Item Pattern Examples

### Pattern 1: @Mentions (Most Explicit)

```
@john to update documentation
@sarah will create the report
@mike should review PR #123
```

**Parsed:**
- Assignee: john/sarah/mike
- Task: update documentation / create the report / review PR #123

---

### Pattern 2: Name + Action Verb

```
John to update documentation
Sarah will create the report
Mike should review PR #123
Lisa needs to test the feature
```

**Parsed:**
- Assignee: name before action verb
- Task: text after "to/will/should/needs to"

---

### Pattern 3: Structured Action Format

```
Action: John - update documentation
Action Item: Sarah - create the report
AI: Mike - review PR #123
```

**Parsed:**
- Assignee: name after "Action:" and before "-"
- Task: text after "-"

---

### Pattern 4: TODO Format

```
TODO: Update documentation (John)
TODO: Create report - Sarah
[ ] Mike: review PR #123
```

**Parsed:**
- Assignee: name in parentheses or after ":"
- Task: text between TODO and assignee

---

### Pattern 5: Bullet Lists

```
- John: update documentation
- Sarah - create the report
* Mike will review PR #123
```

**Parsed:**
- Assignee: name before ":" or "-" or action verb
- Task: remaining text

---

## Additional reference

Edge cases, quality tips and worked examples (moved verbatim). See [edge-cases-and-examples](references/edge-cases-and-examples.md).

## When NOT to Use This Skill

This skill is for **converting meeting action items to Jira tasks only**.

**Don't use for:**
❌ Summarizing meetings (no task creation)
❌ Finding meeting notes (use search skill)
❌ Creating calendar events
❌ Sending meeting notes via email
❌ General note-taking

**Use only when:** Meeting notes exist and action items need to become Jira tasks.

---

## Quick Reference

**Primary tool:** `getConfluencePage` (if URL) or use pasted text
**Account lookup:** `lookupJiraAccountId(searchString)`
**Task creation:** `createJiraIssue` with `assignee_account_id`

**Action patterns to look for:**
- `@Name to/will/should X`
- `Name to/will/should X`
- `Action: Name - X`
- `TODO: X (Name)`
- `Name: X`

**Always:**
- Present parsed tasks before creating
- Handle name lookup failures gracefully
- Include context in task descriptions
- Provide summary with links

**Remember:**
- Human-in-loop is critical (show before creating)
- Name lookup can fail (have fallback)
- Be flexible with pattern matching
- Context preservation is important
