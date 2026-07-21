---
title: "Week 11 Worklog"
date: 2026-06-29
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Week 11 Objectives:

* Implement backend features for Vertex IntervAI.
* Integrate S3, DynamoDB, Bedrock, API Gateway, and frontend flows.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | ------------ | --------------- | -------------- |
| 1 | - Implement backend Lambda functions for Vertex IntervAI: upload_cv, analyze_cv, create_interview, and submit_answer | 29/06/2026 | 29/06/2026 | AWS Lambda Documentation |
| 2 | - Integrate Amazon S3 for CV storage and DynamoDB for metadata management (CVs, Users, Interviews) | 30/06/2026 | 30/06/2026 | AWS DynamoDB Documentation |
| 3 | - Implement CV analysis logic using Amazon Bedrock (Claude 3.5 Sonnet) with fallback analyzer | 01/07/2026 | 01/07/2026 | AWS Bedrock Documentation |
| 4 | - Support React frontend integration with API Gateway: upload CV, create AI interview, and submit answers | 02/07/2026 | 02/07/2026 | AWS API Gateway Documentation |
| 5 | - Run integration tests for the main flow: Upload CV -> Analyze -> Interview | 03/07/2026 | 03/07/2026 | AWS S3 Documentation |
| 6 | - Join team meetings to review architecture and divide tasks | 04/07/2026 | 04/07/2026 | FCAJ Workshop / Vertex IntervAI |
| 7 | - Update the Worklog and project documentation | 05/07/2026 | 05/07/2026 | FCAJ Workshop / Vertex IntervAI |

### Week 11 Achievements:

* Completed the backend core for the main project features.
* The system can process the end-to-end Upload and Analyze CV flow successfully.
* Successfully integrated Amazon Bedrock into CV analysis and interview scoring.
* Frontend and backend communicate smoothly through API Gateway.
* The team has the first demo version of Vertex IntervAI.
