## Challenge 2: Build Core Agents Using Microsoft Agent Framework

## Overview

In this challenge, you will build **multiple specialized AI agents** using the **Microsoft Agent Framework SDK**. Each agent performs a single responsibility and exposes a REST endpoint that can be invoked by an orchestrator in later challenges.

You will create each agent as a **separate Python file** inside Visual Studio Code. The actual implementation code will be provided separately and added into these files.

At the end of this challenge, all agents will run locally and be ready for containerization.

## Agent Design Guidelines

Follow these rules for all agents:

- Each agent handles **only one responsibility**
- Agents are **stateless**
- No agent controls workflow sequencing
- All agents expose a `POST /process` endpoint
- All inputs and outputs use JSON

## Agent 1 — Extraction Agent

### Purpose

The Extraction Agent is responsible for extracting structured information from unstructured text input.

### Example Input

```json
{
  "text": "John Doe is joining the company on 1st August as a Software Engineer in Bangalore."
}
```

### Example Output

```json
{
  "name": "John Doe",
  "role": "Software Engineer",
  "start_date": "1st August",
  "location": "Bangalore"
}
```

### Implementation Steps

1. Open **Visual Studio Code**
2. Inside your project folder, create a new file named:

```
extraction_agent.py
```

3. Open the newly created file
4. Add the provided Extraction Agent code into this file  
   *(Code will be provided separately)*
5. Save the file

## Agent 2 — Validation Agent

### Purpose

The Validation Agent validates structured data using simple business rules and determines whether the data is acceptable for further processing.

### Example Input

```json
{
  "name": "John Doe",
  "role": "Software Engineer",
  "start_date": "1st August",
  "location": "Bangalore"
}
```

### Example Output (Valid)

```json
{
  "status": "Valid",
  "message": "All required fields are present"
}
```

### Example Output (Invalid)

```json
{
  "status": "Invalid",
  "message": "Start date is missing"
}
```

### Implementation Steps

1. In **Visual Studio Code**, create a new file named:

```
validation_agent.py
```

2. Open the file
3. Paste the provided Validation Agent code into this file  
   *(Code will be provided separately)*
4. Save the file

## Agent 3 — Communication Agent

### Purpose

The Communication Agent generates human-readable messages such as emails or notifications based on structured input data.

### Example Input

```json
{
  "name": "John Doe",
  "role": "Software Engineer",
  "start_date": "1st August"
}
```

### Example Output

```json
{
  "message": "Welcome John Doe! We are excited to have you join as a Software Engineer starting on 1st August."
}
```

### Implementation Steps

1. In **Visual Studio Code**, create a new file named:

```
communication_agent.py
```

2. Open the file
3. Paste the provided Communication Agent code into this file  
   *(Code will be provided separately)*
4. Save the file

## Agent 4 — Reporting Agent

### Purpose

The Reporting Agent generates a concise summary of the completed workflow.

### Example Input

```json
{
  "name": "John Doe",
  "role": "Software Engineer",
  "status": "Validated"
}
```

### Example Output

```json
{
  "summary": "John Doe has been successfully onboarded as a Software Engineer."
}
```

### Implementation Steps

1. In **Visual Studio Code**, create a new file named:

```
reporting_agent.py
```

2. Open the file
3. Paste the provided Reporting Agent code into this file  
   *(Code will be provided separately)*
4. Save the file

## Validation Checklist

Ensure the following before proceeding:

- All four agent files are created
- Provided code is added to each file
- Files are saved successfully
- No orchestration logic is added yet

## Deliverables

By the end of this challenge, you should have:

- Four agent source files created
- Clear separation of responsibilities across agents
- Agents ready to be executed locally
- Agents prepared for containerization in the next challenge

---

### Proceed to Challenge 3 to containerize and deploy the agents using Azure Container Apps.
