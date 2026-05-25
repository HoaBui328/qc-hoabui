# UC053-058 — Question Backlog

| Thuộc tính | Giá trị |
|---|---|
| **UC** | UC053-058: Báo cáo tình hình thực hiện dự án đầu tư trong lĩnh vực dầu khí |
| **Nguồn** | UC053-058_dau-khi-du-an-dau-tu_audited_20260514_v1.md |
| **Ngày tạo** | 2026-05-14 |
| **Tổng câu hỏi** | 8 |

---

## Câu hỏi mở (Open Questions)

| ID | Priority | Ref | Question | Why It Matters | Status | BA Answer |
|---|---|---|---|---|---|---|
| Q1 | High | "Acceptance Criteria" — N/A (Missing) | UC gốc không có AC tường minh. BA có thể bổ sung Acceptance Criteria cho từng luồng chính? | AC là cơ sở pass/fail cho QA. Không có AC → QA phải tự suy luận expected behavior. | Resolved | AC được derive từ CF_01 + CMR_03 + validation rules đã mô tả trong SRS. QA sử dụng các tham chiếu CF/CMR làm AC. |
| Q2 | High | "Nguyên tắc trách nhiệm: cho phép chỉnh sửa tất cả trường API-sourced" vs Cột (3)-(6) "API Label / Read-only khi chọn từ API" | Mâu thuẫn: Mục "Nguyên tắc trách nhiệm" nói ALL API-sourced fields Editable, nhưng bảng UI ghi (3)-(6) là Read-only khi chọn từ API. Hành vi thực tế là gì? | Dev/QA không biết expected behavior. Recurring issue across all UCs. Cần BA xác nhận dứt khoát. | Resolved | Đã sửa SRS v1.9: "Nguyên tắc trách nhiệm" chỉ áp dụng khi API null/fail (CMR_12 Enabled). Khi API trả data → cột (3)-(6) Disabled (API Label). Không còn mâu thuẫn. |
| Q3 | Medium | UC053-058.2 — Nộp 2-step process | Nộp → "Đã tiếp nhận" (2-step process). Cụ thể 2 step là gì? Có confirmation popup không? Giữa 2 step có trạng thái trung gian không? | QA cần biết exact flow để thiết kế test case cho Nộp. Khác biệt so với các UC khác (1-step → "Chờ duyệt"). | Resolved | Có quy trình duyệt nội bộ. Flow: Validate → Popup xác nhận → Nộp → "Chờ duyệt" (CF_01, CMR_03). Không phải 2-step đặc biệt — giống các UC khác. |
| Q4 | Medium | UC053-058.2 — Cột (7) Tỷ lệ góp vốn "auto-fill nếu có" | Khi API trả về null cho Cột (7), trường này là Required hay Optional? PVN có bắt buộc nhập không? | Ảnh hưởng đến validation khi Submit. Nếu Required + API null → PVN phải nhập tay. | Resolved | Cột (7) là Optional. Khi API null → trường Enabled, PVN có thể nhập hoặc để trống. Validate chỉ kiểm tra range 0–100 nếu có giá trị. |
| Q5 | Medium | UC053-058.2 — "Thêm nhanh" mode | Khi PVN tạo dự án mới qua "Thêm nhanh" tại Cột (2), dự án này có được lưu vào DB hệ thống không? Hay chỉ tồn tại trong phạm vi báo cáo này? | Ảnh hưởng đến data persistence và khả năng reuse dự án ở BC sau. | Open | |
| Q6 | Medium | UC053-058.1 — Import (CF_02) | UC đề cập nút Import nhưng không specify CF_02 Case 1 hay Case 2. Phạm vi Import là gì? Template Excel format? | QA cần biết scope Import để thiết kế test case. | Resolved | Import theo CF_02 Case 1 (Import by report scope). Đã bổ sung tham chiếu CF_02 Case 1 vào SRS v1.9. Template Excel theo format chuẩn CF_02. |
| Q7 | Low | UC053-058.2 — Toast Success messages | UC không ghi rõ Toast Success cho Lưu nháp/Nộp. Exact text message? | QA cần verify exact message hiển thị. | Resolved | Toast messages theo chuẩn CF_01: Lưu nháp → T01 "Lưu nháp thành công"; Nộp → T02 "Nộp báo cáo thành công". Tham chiếu CF_01 mục Toast. |
| Q8 | Low | UC053-058.2 — Decimal precision cho Cột (14)(15) Lao động | Cột (14)(15) là Integer only (block decimal). Vậy auto-round half-up có áp dụng cho 2 cột này không? Hay chỉ block input? | Cần xác nhận behavior: block tại keystroke hay validate sau blur? | Resolved | Block tại keystroke (chỉ cho phép digit 0–9). Auto-round half-up KHÔNG áp dụng cho cột (14)(15) vì đã chặn input ở UI level. Đã ghi rõ trong SRS: "Chặn ngay khi gõ". |

---

## Thống kê

| Priority | Số lượng | Resolved | Open |
|---|---|---|---|
| High | 2 | 2 | 0 |
| Medium | 4 | 3 | 1 |
| Low | 2 | 2 | 0 |
| **Tổng** | **8** | **7** | **1** |
