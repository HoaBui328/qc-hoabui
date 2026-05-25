# UC035-040 — Question Backlog

| Thuộc tính | Giá trị |
|---|---|
| **UC** | UC035-040: Báo cáo trước khi thực hiện dự án đầu tư |
| **Nguồn** | UC035-040_bao-cao-truoc-khi-thuc-hien-du-an-dt_audited_20260514_v1.md |
| **Ngày tạo** | 2026-05-14 |
| **Tổng câu hỏi** | 7 |

---

## Câu hỏi mở (Open Questions)

| ID | Priority | Ref | Question | Why It Matters | Status | BA Answer |
|---|---|---|---|---|---|---|
*(Không có câu hỏi mở nào)*

---

## Câu hỏi đã trả lời (Answered Questions)

| ID | Priority | Ref | Question | Why It Matters | Status | BA Answer |
|---|---|---|---|---|---|---|
| Q1 | High | UC035-040.1 #5 "Trạng thái kỳ" + Loại báo cáo = "Khai báo 1 lần, không định kỳ" | Báo cáo Ad-hoc khai báo 1 lần có "kỳ" không? Filter "Trạng thái kỳ" (#5) có ý nghĩa gì với loại báo cáo này? Nếu không có kỳ → nên xóa filter này. | Filter vô nghĩa gây nhầm lẫn cho user và tester. Cần xác nhận có nên giữ hay xóa. | Resolved | Đồng ý Phương án A: Xóa filter "Trạng thái kỳ" (#5) — báo cáo Ad-hoc 1 lần không có kỳ hạn, filter vô nghĩa. |
| Q2 | High | "Acceptance Criteria" — N/A (Missing) | UC gốc không có AC tường minh. BA có thể bổ sung? | AC là cơ sở pass/fail cho QA. | Resolved | Đồng ý. QA tự derive AC từ UC spec hiện tại. BA không bổ sung AC riêng. |
| Q3 | Medium | "Nguyên tắc trách nhiệm: cho phép chỉnh sửa tất cả trường API-sourced" vs #1-4 "API Label, Disabled" | Trường #1-4 (Tên TCKT, Loại hình, Địa chỉ, MST) có thực sự Disabled hay Enabled cho sửa? Mâu thuẫn giữa bảng UI và Mục 3. | Dev không biết implement Disabled hay Enabled. QA không biết expected behavior. | Resolved | Giữ #1-4 Disabled. Đây là thông tin hành chính/pháp lý — không cho phép sửa trên báo cáo. "Nguyên tắc trách nhiệm" chỉ áp dụng cho dữ liệu nghiệp vụ, không áp dụng cho dữ liệu định danh pháp lý. |
| Q4 | Medium | UC035-040.2 — Dynamic Block Giai đoạn + 008c | Khi xóa 1 giai đoạn từ block 003, block 008c (Phân kỳ ĐT) có tự động xóa Textarea tương ứng không? Dữ liệu đã nhập trong 008c có bị mất? | Ảnh hưởng đến data consistency và UX. Cần test hành vi cascade delete. | Resolved | Đồng ý cascade delete + warning: Xóa giai đoạn → tự động xóa Textarea 008c tương ứng. Nếu 008c đã có dữ liệu → popup cảnh báo trước khi xóa. |
| Q5 | Medium | UC035-040.3 #8 Import — Phân quyền: "Người dùng Admin" | Action Mapping ghi Import phân quyền cho "Người dùng Admin" nhưng UC này là User site (TCKT/NĐT). Ai thực sự có quyền Import? | Mâu thuẫn phân quyền. TCKT hay Admin? | Resolved | Đồng ý sửa phân quyền Import → "TCKT phụ trách dự án". UC này là User site, không phải Admin site. |
| Q6 | Low | UC035-040.2 #8 Vốn điều lệ — "Chuyển đổi số sang bằng chữ khi Export/In/Xem trước" | Logic chuyển đổi số sang chữ (VD: 1.000.000 → "Một triệu đồng") có hỗ trợ đa ngôn ngữ không? Chỉ tiếng Việt? | Ảnh hưởng đến test Export/Print output. | Resolved | Khách hàng không yêu cầu chuyển ngôn ngữ (chỉ hỗ trợ tiếng Việt). |
| Q7 | Low | UC035-040.1 #3 "Kỳ báo cáo" (strikethrough) | Trường #3 bị strikethrough — đã loại bỏ hoàn toàn hay chỉ ẩn? | Cần xác nhận trạng thái các trường strikethrough. | Resolved | Đồng ý loại bỏ hoàn toàn khỏi UI. Strikethrough = removed. Báo cáo Ad-hoc 1 lần không có "kỳ". |

---

## Thống kê

| Priority | Tổng | Open | Resolved |
|---|---|---|---|
| High | 2 | 0 | 2 |
| Medium | 3 | 0 | 3 |
| Low | 2 | 0 | 2 |
| **Tổng** | **7** | **0** | **7** |
