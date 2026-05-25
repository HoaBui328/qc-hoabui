# UC071-088 — Question Backlog

| Thuộc tính | Giá trị |
|---|---|
| **UC** | UC071-088: Bộ hồ sơ báo cáo về tình hình ĐTNN trên địa bàn tỉnh/TP |
| **Nguồn** | UC071-088_bo-ho-so-bao-cao-dtnn-dia-ban_audited_20260514_v1.md |
| **Ngày tạo** | 2026-05-14 |
| **Ngày cập nhật** | 2026-05-18 |
| **Tổng câu hỏi** | 9 |

---

## Câu hỏi (All Resolved)

| ID | Priority | Ref | Question | Why It Matters | Status | BA Answer |
|---|---|---|---|---|---|---|
| Q1 | High | "Acceptance Criteria" — Partial (chỉ có AC cho Tổng hợp) | UC có AC-AGG-01→11 cho Tổng hợp nhưng thiếu AC cho basic flows (Lập/Lưu/Nộp/Xem/Xóa). BA bổ sung? | QA cần AC đầy đủ cho tất cả luồng, không chỉ Tổng hợp. | Resolved | Không cần bổ sung AC riêng. Basic flows đã tham chiếu CF_01→CF_09 (Common Functions đã định nghĩa AC chuẩn). AC chỉ viết cho logic đặc thù — đã có AC-AGG-01→11. Đồng bộ pattern UC011-034. |
| Q2 | High | "Nguyên tắc trách nhiệm" vs Tab A.IV.4 Col(2)(5) "Disabled" | "Nguyên tắc trách nhiệm" nói ALL API-sourced Editable, nhưng Col(2) Nước ĐK và Col(5) Ngành cấp 1 ghi rõ "Disabled" sau auto-fill. Mâu thuẫn. | Dev/QA không biết implement Disabled hay Enabled. Recurring issue. | Resolved | Đã sửa SRS v1.9: Col(2) và Col(5) → **Enabled** + ⚠️ Warning icon nếu user chỉnh sửa giá trị khác API. Đồng bộ Phương án B từ UC011-034 v2.5 (ALL API fields Enabled + warning UI). |
| Q3 | Medium | Tab A.IV.4 — Strikethrough Phần I (fields 1-5) | Phần I Header (Tên đơn vị, Năm BC, Mã BC, Ngày cập nhật, Trạng thái) bị strikethrough. Loại bỏ hoàn toàn? Nếu vậy, "Tên đơn vị gửi" hiển thị ở đâu? | Ảnh hưởng đến UI layout và test verify. | Resolved | Strikethrough = loại bỏ khỏi form UI, chỉ hiển thị trên output (Xem trước/Xuất/In) — render-layer only. "Tên đơn vị gửi" hiển thị trên PDF header, lấy từ DB quản lý tổ chức. Pattern chuẩn toàn dự án (UC011-034 Tab B.IV.3/B.IV.4/A.IV.4 đều dùng). |
| Q4 | Medium | UC071-088.1 — "Số báo cáo đang xử lý" X/3 | Trigger tăng tử số là gì? Lưu nháp thành công mỗi tab? Hay chỉ cần mở tab? | Ảnh hưởng đến test scenario counter. | Resolved | Đã bổ sung SRS v1.9: (1) Trước nộp: Tử số = số biểu đã Lưu nháp thành công (có ít nhất 1 field có dữ liệu, bao gồm cả auto-fill). (2) Sau nộp: luôn = 3/3. (3) Khi YCCS: reset theo logic (1). Đồng bộ UC011-034 line 63. |
| Q5 | Medium | Tab A.IV.3 — Col(5) auto-fill "tổng hợp báo cáo cấp dưới nếu có" | Trigger auto-fill col(5) là gì? On form load? Nếu BC cấp dưới thay đổi sau khi form đã mở? | Ảnh hưởng đến data freshness và test timing. | Resolved | Trigger = on form load (khởi tạo). Dữ liệu snapshot tại thời điểm mở form. Nếu BC cấp dưới thay đổi sau → không tự động refresh (user dùng [Tổng hợp dữ liệu] nếu muốn cập nhật). Consistent với UC011-034 auto-load pattern. |
| Q6 | Medium | Popup Tổng hợp — "bản mới nhất" | "Mỗi đơn vị chỉ hiển thị bản mới nhất" — "mới nhất" theo Ngày nộp hay Ngày cập nhật? | Ảnh hưởng đến test data setup. | Resolved | "Mới nhất" = Ngày nộp (thời điểm chuyển sang trạng thái "Đã tiếp nhận" gần nhất). Lý do: Ngày nộp là mốc chính thức xác nhận dữ liệu hợp lệ. Consistent với CMR_03 lifecycle. |
| Q7 | Low | Toast Success messages | Toast Success cho Lưu nháp/Nộp không specify. Exact text? | QA cần verify. | Resolved | Tuân theo CF_01/CF_03 chuẩn: Lưu nháp → *"Lưu nháp thành công."*; Nộp → *"Nộp báo cáo thành công."* Không cần define riêng trong UC — CF quản lý centrally. |
| Q8 | Low | Tab A.IV.4 Col(8) Diện tích đất validate | "≤ Tổng DT quỹ đất dự án" — hard block hay chỉ cảnh báo (inline warning)? | Ảnh hưởng đến test expected behavior. | Resolved | Đã sửa SRS v1.9: Hard block (chặn nộp). Error message: *"Diện tích đất không được vượt quá tổng diện tích quỹ đất của dự án."* Đồng bộ UC011-034 validate table #10. |
| Q9 | Low | Export "blank template" | "Biểu chưa có dữ liệu → xuất file trắng (blank template)" — template chứa gì? Headers only? | Ảnh hưởng đến test verify output. | Resolved | Blank template = file có headers + structure (tên cột, tên dòng fixed rows) nhưng không có dữ liệu. Tham chiếu CF_04 (Báo cáo gộp). Cụ thể: A.IV.2 = headers only; A.IV.3 = headers + tên dòng fixed rows; A.IV.4 = headers + dòng Tổng số (giá trị = 0). |

---

## Thống kê

| Priority | Số lượng | Resolved |
|---|---|---|
| High | 2 | 2 |
| Medium | 4 | 4 |
| Low | 3 | 3 |
| **Tổng** | **9** | **9** |
