# Báo cáo Re-Audit UC311-316: Báo cáo KCN/KKT
**Ngày thực hiện:** 2026-05-08
**Ngày cập nhật:** 2026-05-22
**Mức độ đánh giá:** ✅ **READY** (95.5/100)

## Đánh giá các Knowledge Areas

| # | Knowledge Area | Max Pts | Score | Ghi chú |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5 | Rõ ràng |
| 2 | Objective & Scope | 5 | 5 | Đã được xác định |
| 3 | Actors & User Roles | 10 | 10 | Phân quyền đầy đủ |
| 4 | Preconditions & Postconditions | 10 | 10 | Đã làm rõ |
| 5 | UI Object Inventory & Mapping | 15 | 15 | Đã bổ sung nút Xóa, Lập báo cáo, Import |
| 6 | Object Attributes & Behavior | 20 | 20 | Đã bổ sung logic Autofill và Check trùng lặp dự án |
| 7 | Functional Logic & Workflow | 20 | 20 | Đã bổ sung Exception Flow cho API lỗi |
| 8 | Functional Integration | 10 | 10 | Đồng bộ tính tổng real-time |
| 9 | Acceptance Criteria | 10 | 10 | Đã bổ sung AC-01 đến AC-03 |
| 10| Non-functional Requirements | 5 | 0 | (Bỏ qua NFR theo kế hoạch) |

**Raw Score:** 105/110  
**Final Score:** 95.5/100

---

## Báo cáo Gaps & Câu hỏi mở (Unified Gap & Question Report)

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | "Không cho phép chọn trùng dự án ở hai dòng khác nhau." | Cần bổ sung text lỗi (Toast/Inline) khi người dùng cố tình thêm dòng bị trùng dự án. | Đảm bảo Testability cho validation rules. | Resolved |
| Q2 | High | "Bắt buộc người dùng nhấn 'Thêm dòng'..." | Làm sao để xóa một dòng nếu người dùng thêm nhầm? Cần bổ sung nút và hành vi Xóa dòng. | Thiết kế UI/UX bị thiếu sót chức năng cơ bản. | Resolved |
| Q3 | Medium | Toàn tài liệu | Chưa có Acceptance Criteria rõ ràng. BA có thể duyệt các AC do QC generate không? | QA không có tiêu chuẩn để nghiệm thu test case. | Resolved |
| Q4 | Medium | "Gọi API hiển thị danh sách dự án..." | Cần bổ sung Exception flow khi API danh sách dự án bị timeout/error. | Giúp hoàn thiện kịch bản Edge Case. | Resolved |

## Summary & Recommendation
Các open gaps đã được resolve qua bản Implementation Plan. Hiện tại tài liệu đã đạt chuẩn để bắt đầu thiết kế Test Case / Scenario. **READY.**

---

## BỔ SUNG: CMR Alignment (2026-05-22)

### 1. Numeric Digit Precision
Áp dụng cho **TẤT CẢ** trường số trong UC311-316:
- Phần nguyên: tối đa **15 chữ số**
- Phần thập phân: tối đa **5 chữ số**
- Tổng tối đa: 21 ký tự (bao gồm dấu phân cách)
- Khi vượt giới hạn → block nhập thêm + hiển thị inline error: `"[Tên trường] chỉ được nhập tối đa 15 chữ số phần nguyên và 5 chữ số phần thập phân"`

### 2. CMR_18 — Tab Navigation
- Tất cả form nhập liệu (Lập báo cáo, Chỉnh sửa) phải hỗ trợ Tab Navigation giữa các trường. Tham chiếu: CMR_18.

### 3. Buttons — Luôn Enabled
- Tất cả các Button (Lưu nháp, Nộp báo cáo, Hủy, Xem trước, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Xóa) đều ở trạng thái **Luôn Enabled** khi hiển thị.

### 4. Placeholder Fix
- Trường "Trong nước" (nếu có): Placeholder chuẩn hóa theo CMR_06 STD-04a: `"Nhập [tên trường cụ thể]"` — VD: `"Nhập Trong nước"`.

### 5. Textbox Max Length
- Fields 18, 19 (textbox): Khai báo maxlength → **255 ký tự**. Error: `"[Tên trường] không được vượt quá 255 ký tự"`

### 6. Toast/Error Messages
- Tất cả message KHÔNG có dấu `.` ở cuối câu.

---

## Changelog
- **2026-05-22 (V3 — Align CMR):** Bổ sung section CMR Alignment: (1) Numeric precision 15+5 chữ số; (2) CMR_18 Tab Navigation; (3) Buttons "Luôn Enabled"; (4) Placeholder fix theo CMR_06 STD-04a; (5) Textbox max 255; (6) Xác nhận toast/error không trailing `.`. Tài liệu duy trì trạng thái READY.
- **2026-05-08 (V2):** Tích hợp tính năng thêm/xóa dòng. Tích hợp logic xử lý autofill và validate trùng lặp dữ liệu. Tích hợp Exception Flow khi gọi API lỗi. Bổ sung Acceptance Criteria.
