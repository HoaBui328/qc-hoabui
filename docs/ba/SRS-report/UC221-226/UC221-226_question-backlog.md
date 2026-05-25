# UC221-226 — Question Backlog

| Thuộc tính | Giá trị |
|---|---|
| **UC ID** | UC221-226 |
| **Tên báo cáo** | Báo cáo tình hình thực hiện dự án đầu tư quý (Mẫu A.III.1) |
| **Ngày tạo** | 2026-05-21 |
| **Nguồn** | UC221-226_audited-v1.md |

---

## Danh sách câu hỏi

| ID | Priority | Ref | Question | Why It Matters | Status | Trả lời |
|----|----------|-----|----------|----------------|--------|---------|
| Q1 | Medium | UC221-226.2 Phần B — RULE-01 | RULE-01 nêu "Đối với dự án ĐTTN (được cấp GCNĐKĐT bằng VNĐ)" — nhưng UC221-226 thuộc phân hệ ĐTTN. Vậy RULE-01 có áp dụng mặc định cho TẤT CẢ dự án trong phân hệ này không? Hay vẫn có dự án ĐTTN được cấp bằng USD? Cần xác nhận logic xác định loại tiền tệ. | Ảnh hưởng đến đơn vị hiển thị toàn bộ Phần B. Nếu tất cả đều dùng "Triệu VNĐ" thì cột đơn vị trong eForm grid cần cập nhật. | Answered | ĐTTN luôn dùng VNĐ. Đã đổi toàn bộ đơn vị eForm Grid từ "USD" sang "Triệu VNĐ". RULE-01 cập nhật: đơn vị mặc định là "Triệu VNĐ" cho phân hệ ĐTTN. |
| Q2 | Medium | UC221-226.2 Mục 3 — Validation Trùng kỳ (V17) | Tài liệu ghi "Kiểm tra trùng (Năm + Quý + Dự án) khi Blur trường Năm/Quý hoặc khi nhấn [Lưu nháp]/[Nộp]". Tuy nhiên Quý và Năm đã chuyển thành Read-only (auto-fill từ kỳ hạn). Vậy validation V17 còn cần thiết không? Nếu hệ thống tự gán Quý/Năm từ kỳ hạn thì trùng kỳ chỉ xảy ra khi cùng Dự án — cần xác nhận logic. | Nếu V17 không còn áp dụng, cần xóa khỏi SRS để tránh nhầm lẫn khi implement. Nếu vẫn áp dụng, cần làm rõ trigger event (không còn Blur trên Quý/Năm). | Answered | Quý/Năm đã được xác định từ màn danh sách (Read-only). Trigger V17 đổi sang: chọn/đổi Dự án tại A-001 hoặc nhấn [Lưu nháp]/[Nộp]. |
| Q3 | Low | UC221-226.1 — Preconditions | Tài liệu không ghi rõ preconditions (VD: user đã đăng nhập, dự án đã tồn tại trên hệ thống, API khả dụng). Cần bổ sung để QC có thể setup test data chính xác. | Tester cần biết điều kiện tiên quyết để thiết lập môi trường test. | Answered | Đã bổ sung PRE-01→PRE-04 vào UC221-226.2 mục 1. |
| Q4 | Low | UC221-226.2 — Phần B NĐT blocks | Khi dự án ĐTTN không có "Nhà đầu tư nước ngoài" (chỉ có NĐT Việt Nam), mục 1.2 "Nhà đầu tư nước ngoài" hiển thị như thế nào? Ẩn hoàn toàn hay hiển thị với giá trị 0? | Ảnh hưởng đến UI rendering và auto-calc. Cần xác nhận empty state cho block NĐT NN khi không có NĐT nước ngoài. | Answered | eForm: ẩn block NĐT NN. Preview/In/Xuất: hiển thị đầy đủ cấu trúc bảng với giá trị trống. |
| Q5 | Low | UC221-226.2 — A-011, A-012, A-013 | Các trường A-011 (Địa chỉ), A-012 (SĐT), A-013 (Email) cho phép chỉnh sửa. Có validation format cho Email và SĐT không? (VD: email phải có @, SĐT chỉ chấp nhận số). | Thiếu validation format → không thể viết negative test cho các trường này. | Answered | Tuân thủ theo CMR_06 (common rule cho text field). Đã bổ sung tham chiếu CMR_06 vào A-012, A-013. |
