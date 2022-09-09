# [DA217] - Metric and visualizations for happy path and deviations.

## 1. JIRA Ticket and Task Description

**_1.1 Description_**

Defining a formula to metricize deviation from the happy path that takes into account both
1. whether or not the new message type label transitioned to in the conversation sample matches a “happy path” transition, and
2. the number of turns before a state transition in terms of a message type label.

JIRA Ticket (https://wizardcommerce.atlassian.net/browse/DA-217)

**_1.2 Deliverables_**
- Metric Documentation/summary (https://docs.google.com/document/d/1A04RJvMe5gdd8cNCToVLPVDTWamnU_lDkv5-zzxyWW0/edit - Connect to preview )
- Github repo with 
  - classes for DAG deployment of metric code 
  - classes for `networkx` visualization of state transitions between message type labels. 
  - methods.ipynb detailing initial findings and methods

## 2. Log

#### 08.06.2022
- Created JIRA tickets
- Started project folder

#### 08.07.2022
- Finalized metric formula
  - https://docs.google.com/document/d/1A04RJvMe5gdd8cNCToVLPVDTWamnU_lDkv5-zzxyWW0/edit
- Finalized metric code/class

#### 08.08.2022
- Methods.ipynb finalized for reporting
- Finalized visualization tools for reporting `transitionsVisualizer.py`