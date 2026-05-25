# Question Backlog

> Generated: 2026-05-11 (Updated after re-check round)
> Source files: UC197-202_audited_v1.md

---

## Open Questions

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | N/A (Missing) | Khi báo cáo Mẫu I.19 được nộp, trạng thái tiếp theo là "Chờ duyệt" hay "Đã tiếp nhận"? Quy trình phê duyệt nội bộ gồm 2 hay nhiều bước (per CMR_03)? | Không thể viết expected result chính xác cho luồng Submit. Mọi test case Submit sẽ bị block. | Open |
| Q2 | High | UC197-202.1 mục 3: "Phân trang theo bản ghi. Tham chiếu: CMR_10" vs CS_02 (2026-05-11): "Scroll dọc nếu >10 bản ghi" | **Mâu thuẫn:** UC tham chiếu CMR_10 (phân trang), nhưng CS_02 cập nhật 2026-05-11 quy định báo cáo không định kỳ dùng Scroll dọc. Tài liệu nào đúng? | Phân trang và scroll là 2 hành vi hoàn toàn khác nhau — QA không thể verify UI. | Open |
| Q3 | High | UC197-202.1 mục 2: Placeholder Search = `"Nhập dữ liệu"` vs CS_01 (2026-05-11): `"Tìm kiếm theo Mã báo cáo"` | **Mâu thuẫn:** Placeholder ô tìm kiếm trong UC khác chuẩn CS_01 mới nhất. Tài liệu nào đúng? | QA không thể xác định expected text chính xác khi verify UI. | Open |
| Q4 | High | UC197-202.1 mục 2: Empty state = `"Không tìm thấy kết quả"` (màn hình trắng) vs CS_02: `"Không tìm thấy dữ liệu phù hợp"` kèm hình minh họa | **Mâu thuẫn:** Cả text lẫn UI (màn hình trắng vs có hình) đều khác. Tài liệu nào đúng? | QA không thể xác định expected result đúng cho test case empty state. | Open |
| Q5 | High | UC197-202.2 mục 2: Trường "Mã số thuế" — "Lỗi inline nếu sai định dạng" | Thiếu nội dung text lỗi inline khi MST sai định dạng. BA cần bổ sung text cụ thể. | Không có expected message → không thể verify thông báo lỗi. | Open |
| Q6 | Medium | UC197-202.2 mục 2: Trường "Tổng số tiền cho vay (USD)" | Có giới hạn max value không? CMR_05 cho phép dấu trừ mặc định nhưng UC ghi "> 0" — hành vi chặn ký tự `-` có block ngay khi gõ không? | Cần xác định để viết test case boundary và negative cho trường số tiền. | Open |
| Q7 | Medium | UC197-202.2 mục 2: Trường "Tên nhà đầu tư" — Tham chiếu CMR_06, không ghi max length | Xác nhận max length áp dụng là 500 ký tự (CMR_06 default) không? | QA không có giá trị boundary để test. | Open |
| Q8 | Medium | UC197-202.2 mục 3: Trường "Ngày cấp CCCD/CNĐKDN" — Validate ≤ ngày hôm nay | Có validate ngày tối thiểu không (VD: 01/01/1900 có bị reject không)? Định dạng hiển thị trong field: dd/MM/yyyy hay MM/dd/yyyy? | Thiếu boundary tối thiểu và format → không thể viết test case boundary cho trường ngày. | Open |
| Q9 | Medium | UC197-202.3 mục 2: Nút [Nộp] từ Danh sách — Tham chiếu CF_09 | Theo CF_09, khi validate FAIL từ Danh sách, hệ thống redirect sang màn hình Chỉnh sửa và hiển thị lỗi inline. UC không đề cập — xác nhận áp dụng đúng CF_09? | QA cần biết expected redirect để viết test case Nộp-thất bại từ danh sách. | Open |
| Q10 | Medium | UC197-202.2 mục 3 — Màn hình Chỉnh sửa (CF_03) | Khi mở Chỉnh sửa, các field ICR đang Disabled (API đã trả dữ liệu trước đó) — NĐT có thể unlock/override để chỉnh không? Hay luôn Disabled suốt vòng đời? | Ảnh hưởng trực tiếp đến test case chỉnh sửa sau khi tạo. | Open |
| Q11 | Low | N/A (Missing) | Có giới hạn số lượng báo cáo I.19 tối đa một NĐT có thể tạo không? | Cần xác định để test edge case tạo nhiều bản ghi. | Open |
| Q12 | Low | UC197-202.2: Nhóm trường max length (mục 10–20) | Hành vi khi nhập vượt max length: block ký tự ngay khi gõ (hard limit) hay hiển thị warning sau submit? | CMR_06 không mô tả hành vi vượt max length → không thể verify UX tại boundary. | Open |
| Q13 | Low | N/A (Missing) | Metadata "Cơ quan nhận: Bộ Tài chính / Ngân hàng Nhà nước" — người dùng có cần chọn hay là thông tin cố định hệ thống tự gắn? | Nếu cần chọn thì phải có UI element, nếu cố định thì không cần test. | Open |
| Q14 | Low | UC197-202.2 — Trường "Đại diện theo pháp luật" và "Chức vụ" | Đối với tài khoản Cá nhân: ICR có thể trả dữ liệu cho 2 trường này không? Nếu Disabled (có data ICR) thì trường 7 có tự động Required không? | Hành vi conditional required + Disabled/Enabled phức tạp cần rõ để test đúng. | Open |

Priority: H = High (blocks design), M = Medium (affects scope), L = Low (nice to know)
Status: Open | Answered | Deferred

---

## Answered Questions

| ID | Priority | Ref | Question | Answer | Answered By | Date | Status |
|----|----------|-----|----------|--------|-------------|------|--------|
