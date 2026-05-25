# UC059-064 — Question Backlog

| Thuộc tính | Giá trị |
|---|---|
| **UC** | UC059-064: Báo cáo tình hình thực hiện các dự án hợp tác với nước ngoài trong lĩnh vực dầu khí năm |
| **Nguồn** | UC059-064_dau-khi-dau-tu-nam_audited_20260514_v1.md |
| **Ngày tạo** | 2026-05-14 |
| **Tổng câu hỏi** | 9 |

---

## Câu hỏi mở (Open Questions)

| ID | Priority | Ref | Question | Why It Matters | Status | BA Answer |
|---|---|---|---|---|---|---|
| Q8 | Medium | UC059-064.1 — Nhập từ file | Nút [Nhập từ file] hiển thị trên danh sách nhưng SRS chưa specify CF_02 Case 1 hay Case 2. Phạm vi Import là gì? | QA cần biết scope Import để thiết kế test case. | Open | |
| Q9 | Low | UC059-064.2 — Trạng thái sau Nộp | SRS ghi "Đã tiếp nhận" nhưng CF_01 cho phép "Chờ duyệt" hoặc "Đã tiếp nhận" (theo CMR_03). Trạng thái chính xác sau Nộp cho UC này? | Ảnh hưởng đến expected state trong test case. | Open | |

---

## Câu hỏi đã trả lời (Answered Questions)

| ID | Priority | Ref | Question | Why It Matters | Status | BA Answer |
|---|---|---|---|---|---|---|
| Q1 | High | "Acceptance Criteria" — N/A (Missing) | UC gốc không có AC tường minh. BA có thể bổ sung? | AC là cơ sở pass/fail cho QA. | Resolved | AC được derive từ CF_01 + CMR_03 + validation rules đã mô tả trong SRS. QA sử dụng các tham chiếu CF/CMR làm AC. |
| Q2 | Medium | UC059-064.2 Mục 3 — Trigger đổi Năm BC ghi đè col(A) | Khi user đã sửa tay col(A) rồi đổi Năm BC → col(A) bị ghi đè không popup. Đây là intentional? Có nên có dirty-check warning? | Data loss risk. User có thể mất dữ liệu đã nhập mà không biết. | Resolved | Không còn áp dụng — Năm báo cáo đã chuyển thành Label/Disabled (xác định từ màn hình danh sách). Người dùng không thể đổi Năm trên form → không có trigger ghi đè. Đã xóa trigger (2) khỏi SRS v1.7. |
| Q3 | Medium | UC059-064.2 — Auto-fill col(A) "cột (B) năm T-1 đã phê duyệt" | Nếu BC năm T-1 tồn tại nhưng ở trạng thái "Lưu nháp" → có được dùng làm nguồn auto-fill không? Chỉ "Đã tiếp nhận" mới đủ điều kiện? | Ảnh hưởng đến test data setup và expected behavior. | Resolved | SRS ghi rõ: "cột (B) của báo cáo năm T-1 đã được phê duyệt thành công" → chỉ trạng thái "Đã tiếp nhận" mới đủ điều kiện. "Lưu nháp" không được dùng làm nguồn auto-fill. |
| Q4 | Medium | UC059-064.2 — V17 check trùng năm | V17 trigger khi nào? On blur Năm field, hay chỉ khi Lưu/Nộp? | Ảnh hưởng đến timing hiển thị lỗi. | Resolved | Không cần check V17 trên form — năm báo cáo được xác định từ màn hình danh sách. Hệ thống kiểm soát trùng kỳ tại listing level (nút "Lập báo cáo" chỉ hiện khi kỳ chưa có BC). Đã xóa V17 khỏi SRS v1.7. |
| Q5 | Medium | UC059-064.2 — RULE-03 validate on-blur | Viền đỏ inline khi vi phạm — có kèm inline error text message không? Hay chỉ viền đỏ? | QA cần biết exact UI feedback. | Resolved | Có kèm inline error text: *"Giá trị không được vượt quá dòng cha"*. Đã bổ sung vào SRS v1.7. |
| Q6 | Low | UC059-064.2 — Toast Success messages | Toast Success cho Lưu nháp/Nộp không được specify. Exact text? | QA cần verify exact message. | Resolved | Toast messages theo chuẩn CF_01: Lưu nháp → T01 "Lưu nháp thành công"; Nộp → T02 "Nộp báo cáo thành công". Tham chiếu CF_01 mục Toast. |
| Q7 | Low | UC059-064.2 — "Lao động" (Người) | Mục 1.9 và 2.9 ĐVT: Người. Đây là integer hay decimal? Decimal precision có áp dụng? | Ảnh hưởng đến test data và validation. | Resolved | Integer only — chỉ cho phép số nguyên. Chặn ký tự thập phân ngay khi gõ (block tại keystroke). Auto-round half-up KHÔNG áp dụng cho cột 1.9/2.9. Đã ghi rõ trong SRS v1.7. |

---

## Thống kê

| Priority | Số lượng | Resolved | Open |
|---|---|---|---|
| High | 1 | 1 | 0 |
| Medium | 5 | 4 | 1 |
| Low | 3 | 2 | 1 |
| **Tổng** | **9** | **7** | **2** |
