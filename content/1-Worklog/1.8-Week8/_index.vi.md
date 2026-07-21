---
title: "Worklog Tuần 8"
date: 2026-06-08
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Mục tiêu tuần 8:

* Triển khai xác thực Cognito và chức năng upload CV.
* Kết nối API Gateway với Lambda và DynamoDB.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | ------------ | --------------- | -------------- |
| 1 | - Cấu hình Cognito Hosted UI, App Client, group user/admin | 19/06/2026 | 19/06/2026 | AWS Cognito Documentation |
| 2 | - Viết Lambda upload_cv: validate file, upload S3, lưu metadata DynamoDB | 20/06/2026 | 21/06/2026 | AWS Lambda Documentation |
| 3 | - Tạo route API Gateway POST /upload_cv | 22/06/2026 | 23/06/2026 | AWS API Gateway Documentation |
| 4 | - Test login/logout cơ bản | 24/06/2026 | 25/06/2026 | FCAJ Workshop / Vertex IntervAI |
| 5 | - Rà soát bảo mật cơ bản cho file CV | 27/06/2026 | 27/06/2026 | AWS S3 Documentation |

### Kết quả đạt được tuần 8:

* Hoàn thiện auth với Cognito.
* Triển khai chức năng upload CV thành công.
* Bảo mật cơ bản cho file CV.
