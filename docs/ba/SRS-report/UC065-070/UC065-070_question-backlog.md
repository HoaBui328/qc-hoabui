# UC065-070 — Question Backlog

| Thuộc tính | Giá trị |
|---|---|
| **UC** | UC065-070: Báo cáo tổng hợp tình hình ĐTNN trên địa bàn tỉnh/TP (Mẫu A.IV.1) |
| **Nguồn** | UC065-070_tong-hop-dtnn-dia-ban_audited_20260514_v1.md |
| **Ngày tạo** | 2026-05-14 |
| **Tổng câu hỏi** | 6 |

---

## Câu hỏi mở (Open Questions)

| ID | Priority | Ref | Question | Why It Matters | Status | BA Answer |
|---|---|---|---|---|---|---|
| Q1 | High | "Acceptance Criteria" — N/A (Missing) | UC gốc không có AC tường minh. BA có thể bổ sung? | AC là cơ sở pass/fail cho QA. | Open | |
| Q2 | Medium | UC065-070.2 — Col(9) override behavior | Khi user Lưu nháp rồi mở lại, col(5) thay đổi → col(9) có recalculate không? Hay giữ giá trị override? | Ảnh hưởng đến data consistency khi edit. | Open | |
| Q3 | Medium | UC065-070.2 — Auto-fill col(4) "cột (5) quý T-1" | Quý T-1 report phải ở trạng thái nào? Chỉ "Đã tiếp nhận"? Hay "Lưu nháp" cũng được? | Ảnh hưởng đến test data setup. | Open | |
| Q4 | Medium | UC065-070.2 — Section IV Optional | Nếu user nhập partial data Section IV (VD: chỉ nhập IV.1.a mà không nhập IV.1.b), có valid không? Hay phải all-or-nothing per row? | Ảnh hưởng đến validation logic. | Open | |
| Q5 | Low | UC065-070.2 — Toast Success messages | Toast Success cho Lưu nháp/Nộp không specify. Exact text? | QA cần verify. | Open | |
| Q6 | Low | UC065-070.2 — "Lao động" Integer vs Decimal | Mục 5 ghi "Nhập số nguyên" nhưng decimal precision rule áp dụng globally. Cái nào ưu tiên? | Ảnh hưởng đến test data. | Open | |

---

## Thống kê

| Priority | Số lượng |
|---|---|
| High | 1 |
| Medium | 3 |
| Low | 2 |
| **Tổng** | **6** |
