---
title: "Event 2"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

# Bài thu hoạch "FCAJ Meetup 06/06/2026"

### Mục Đích Của Sự Kiện

Mục đích của buổi meetup là tạo cơ hội để các thành viên trong cộng đồng công nghệ cùng lắng nghe những phần chia sẻ thực tế từ các diễn giả đã có kinh nghiệm làm việc trong nhiều môi trường khác nhau. Thông qua các chủ đề đa dạng như kết nối mạng, Docker, bảo mật ứng dụng web, Machine Learning và hành trình nghề nghiệp trong lĩnh vực hệ thống, sự kiện giúp người tham dự cập nhật thêm xu hướng công nghệ, hiểu rõ hơn các tình huống thực tế và mở rộng kết nối với những bạn có cùng định hướng.

### Danh Sách Diễn Giả

* **Nguyễn Quốc Bảo** - Đại học Công nghệ Swinburne
* **Bảo Huỳnh** - Junior Cloud Native Developer, Endava Vietnam
* **Lê Hoàng Gia Đại** - Đại học Công nghệ TP. Hồ Chí Minh
* **Vinh Trần** - System Administrator, Central Retail Group

### Nội Dung Nổi Bật

#### Kết nối Godot clients với AWS WebSockets

Phần trình bày này giúp tôi ôn lại các kiến thức nền tảng về mạng máy tính và cách các client kết nối với server trong một ứng dụng thời gian thực. Diễn giả giới thiệu thêm về ENet trong Godot và trình bày một demo game kéo búa bao có sử dụng một số dịch vụ AWS.

Điểm đáng chú ý là phần giải thích luồng tìm trận giữa hai người chơi, cách duy trì kết nối và xử lý khi người chơi bị ngắt kết nối. Qua đó, tôi hiểu rõ hơn cách WebSocket hỗ trợ giao tiếp hai chiều trong các ứng dụng cần phản hồi nhanh.

#### Docker và công nghệ ảo hóa

Diễn giả trình bày vai trò của Docker trong việc đóng gói và triển khai ứng dụng. Nội dung bắt đầu từ lợi ích của công nghệ ảo hóa, sau đó đi vào các khái niệm cơ bản của Docker, các câu lệnh thường dùng và cách tổ chức môi trường chạy ứng dụng.

Một nội dung hữu ích là cơ chế caching trong Docker, đặc biệt là Docker layer caching, giúp tối ưu thời gian build image. Các demo đơn giản trong phần này giúp tôi dễ hình dung hơn cách Docker được sử dụng trong quá trình phát triển phần mềm.

#### WAF và Machine Learning trong phát hiện tấn công mạng

Chủ đề này tập trung vào việc kết hợp AWS WAF với Machine Learning để cải thiện khả năng phát hiện các cuộc tấn công mạng. Thay vì chỉ dựa vào rule tĩnh, giải pháp có thể hỗ trợ phòng thủ chủ động hơn và thích ứng tốt hơn với các mối đe dọa mới.

Phần demo giúp tôi thấy rõ hơn cách một hệ thống bảo mật có thể thu thập tín hiệu, phân tích hành vi và đưa ra phản ứng phù hợp nhằm giảm thiểu rủi ro cho ứng dụng web.

#### Hành trình từ IT Helpdesk đến Senior Sysadmin

Phần chia sẻ của anh Vinh để lại nhiều ấn tượng vì đây là câu chuyện nghề nghiệp rất thực tế. Anh chia sẻ rằng bản thân không xuất phát từ một trường top, nhưng nhờ nỗ lực, kiên trì và tích lũy kinh nghiệm qua nhiều dự án, anh đã phát triển từ vị trí IT Helpdesk lên Senior Sysadmin.

Anh cũng kể về những buổi phỏng vấn ở nhiều công ty lớn, các tình huống sự cố trong hệ thống production như lỗi ổ cứng gây downtime, và cách bình tĩnh phân tích từng nguyên nhân để đưa ra nhiều hướng xử lý. Ngoài ra, phần chia sẻ cũng gợi ý một lộ trình học Cloud phù hợp cho người mới bắt đầu.

### Những Gì Học Được

* Ôn lại kiến thức về kết nối mạng, WebSocket và cách client giao tiếp với server trong ứng dụng thời gian thực.
* Hiểu rõ hơn vai trò của Docker trong phát triển và triển khai ứng dụng, đặc biệt là Docker layer caching để tăng tốc quá trình build image.
* Biết thêm cách AWS WAF có thể kết hợp với Machine Learning để nâng cao khả năng phát hiện và giảm thiểu tấn công mạng.
* Nhận ra kinh nghiệm thực tế, khả năng xử lý sự cố và tinh thần bình tĩnh khi troubleshooting là những yếu tố rất quan trọng trong công việc vận hành hệ thống.
* Hiểu rằng việc làm nhiều project thực tế giúp củng cố kiến thức tốt hơn so với chỉ học lý thuyết.

### Ứng Dụng Vào Công Việc

* Áp dụng Docker để xây dựng môi trường phát triển ổn định và đồng nhất hơn giữa các máy.
* Tối ưu Dockerfile và tận dụng layer caching để giảm thời gian build image trong các dự án cá nhân hoặc đồ án.
* Sử dụng Docker Compose để triển khai nhanh các service cần thiết trong môi trường development.
* Khi gặp lỗi hệ thống, cần phân tích nguyên nhân theo từng bước, kiểm tra giả thuyết rõ ràng và giữ bình tĩnh trước khi đưa ra kết luận.
* Chủ động thực hành thêm các mô hình sử dụng WebSocket hoặc các dịch vụ AWS để hiểu sâu hơn cách hệ thống hoạt động.

### Trải Nghiệm Trong Event

#### Học hỏi từ các diễn giả

Các diễn giả đều sử dụng nhiều ví dụ và câu chuyện thực tế thay vì chỉ trình bày lý thuyết. Cách chia sẻ này giúp tôi dễ hình dung hơn cách các công nghệ như Docker, WebSocket, WAF và Machine Learning được áp dụng trong môi trường doanh nghiệp.

Phần chia sẻ về hành trình nghề nghiệp của anh Vinh đặc biệt truyền cảm hứng, vì nó cho thấy xuất phát điểm không phải yếu tố quyết định duy nhất. Điều quan trọng hơn là sự kiên trì, tinh thần học hỏi và khả năng tích lũy kinh nghiệm qua từng công việc.

#### Bài học rút ra

Kiến thức nền tảng là cần thiết, nhưng kỹ năng thực hành và kinh nghiệm xử lý tình huống thực tế mới giúp bản thân tiến bộ rõ rệt. Tôi cũng nhận ra rằng khi làm việc với hệ thống, việc bình tĩnh phân tích vấn đề theo từng bước quan trọng hơn việc vội vàng tìm một câu trả lời nhanh.

Ngoài ra, các buổi meetup như thế này là cơ hội tốt để mở rộng kiến thức, cập nhật xu hướng công nghệ và học hỏi kinh nghiệm từ những người đang làm việc trong ngành.

#### Một số hình ảnh và video khi tham gia sự kiện

**Em đã check-in nhưng quên chụp ảnh cuối buổi.**
