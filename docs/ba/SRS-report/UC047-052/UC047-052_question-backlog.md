# UC047-052 — Question Backlog

| Thuộc tính | Giá trị |
|---|---|
| **UC** | UC047-052: Báo cáo tình hình thực hiện dự án đầu tư năm |
| **Nguồn** | UC047-052_thuc-hien-du-an-dau-tu-nam_audited_20260514_v1.md |
| **Ngày tạo** | 2026-05-14 |
| **Tổng câu hỏi** | 8 |

---

## Câu hỏi mở (Open Questions)

| ID | Priority | Ref | Question | Why It Matters | Status | BA Answer |
|---|---|---|---|---|---|---|

---

## Câu hỏi đã giải quyết (Resolved Questions)

| ID | Priority | Ref | Question | Why It Matters | Status | BA Answer |
|---|---|---|---|---|---|---|
| Q1 | High | "Acceptance Criteria" — N/A (Missing) | UC gốc không có AC tường minh. BA có thể bổ sung? | AC là cơ sở pass/fail cho QA. | Resolved | Áp dụng precedent UC041-046: QA tự derive AC từ Rule và ràng buộc. |
| Q2 | High | "Nguyên tắc trách nhiệm" vs #3→#11 "Label, Read-only" | Trường #3→#11 có thực sự Read-only hay Enabled cho sửa? | Dev/QA không biết expected behavior. | Resolved | Giữ nguyên Read-only như UI. (Đã chốt) |
| Q3 | Medium | UC047-052.2 — Block NĐT "tự động render" + "[+ Thêm NĐT]" | Khi thêm thủ công, row 1 (Tên NĐT) và row 2 (MST) có phải nhập tay không? | Ảnh hưởng đến UI behavior của block thêm mới. | Resolved | Đã xóa chức năng [+ Thêm NĐT] khỏi tài liệu. NĐT tự động lấy từ API (read-only). |
| Q4 | Medium | UC047-052.2 — Rule 04 "kiểm tra trùng MST" | Rule 04 chỉ check trùng MST trong cùng BC hay cross-check? Trigger khi nào? | Ảnh hưởng đến validation. | Resolved | Đã xóa Rule 04 do chức năng thêm NĐT thủ công đã bị hủy bỏ. |
| Q5 | Medium | UC047-052.1 — Phân quyền "TCKT" | NĐT thành viên có quyền xem BC này không? | Ảnh hưởng phân quyền. | Resolved | Đã cập nhật tài liệu: Tổ chức kinh tế (toàn quyền), NĐT thành viên (có quyền Xem). |
| Q6 | Medium | UC047-052.2 — Validation số "≥ 0" vs "cho phép âm" | Khi nhập số âm vào mục không cho phép, hệ thống hiển thị lỗi gì? | QA cần exact error message. | Resolved | Theo Common Function (chỉ validate bắt buộc khi nộp, định dạng thì chặn bởi input HTML hoặc báo lỗi theo CS). |
| Q7 | Low | UC047-052.2 — Toast messages | UC không ghi rõ Toast Success. Exact text? | QA cần verify exact message. | Resolved | Tuân thủ Toast chuẩn từ CF_01. |
| Q8 | Low | UC047-052.2 — Decimal precision + RULE-01 | Khi đơn vị là Triệu VNĐ, decimal precision có thay đổi? | Ảnh hưởng test data. | Resolved | Áp dụng precedent UC041-046: Max 5 chữ số thập phân cho mọi trường số. |

---

## Thống kê

| Priority | Số lượng |
|---|---|
| High | 0 |
| Medium | 0 |
| Low | 0 |
| **Tổng** | **0** |
