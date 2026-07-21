---
title: "Worklog Tuần 11"
date: 2026-06-29
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Mục tiêu tuần 11:

* Triển khai backend cho dự án Vertex IntervAI.
* Tích hợp S3, DynamoDB, Bedrock, API Gateway và frontend.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | ------------ | --------------- | -------------- |
| 1 | - Tham gia triển khai backend cho dự án Vertex IntervAI: phát triển các Lambda function chính (upload_cv, analyze_cv, create_interview, submit_answer). | 29/06/2026 | 29/06/2026 | AWS Lambda Documentation |
| 2 | - Tích hợp Amazon S3 để lưu trữ file CV và DynamoDB để quản lý metadata (bảng CVs, Users, Interviews). | 30/06/2026 | 30/06/2026 | AWS DynamoDB Documentation |
| 3 | - Triển khai logic phân tích CV sử dụng Amazon Bedrock (Claude 3.5 Sonnet) kết hợp fallback analyzer. | 01/07/2026 | 01/07/2026 | AWS Bedrock Documentation |
| 4 | - Hỗ trợ frontend React kết nối với API Gateway: upload CV, tạo phiên phỏng vấn AI và submit câu trả lời. | 02/07/2026 | 02/07/2026 | AWS API Gateway Documentation |
| 5 | - Thực hiện test tích hợp các luồng chính (Upload CV → Analyze → Interview). | 03/07/2026 | 03/07/2026 | AWS S3 Documentation |
| 6 | - Tham gia họp nhóm để review kiến trúc và phân công task. | 04/07/2026 | 04/07/2026 | FCAJ Workshop / Vertex IntervAI |
| 7 | - Cập nhật Worklog và tài liệu dự án. | 05/07/2026 | 05/07/2026 | FCAJ Workshop / Vertex IntervAI |

### Kết quả đạt được tuần 11:

* Hoàn thành phần backend core cho các chức năng chính của dự án.
* Hệ thống có thể xử lý end-to-end luồng Upload & Analyze CV thành công.
* Tích hợp thành công Amazon Bedrock vào quy trình phân tích CV và chấm điểm phỏng vấn.
* Frontend và Backend kết nối mượt mà qua API Gateway.
* Đội nhóm có phiên bản demo đầu tiên của dự án Vertex IntervAI.
