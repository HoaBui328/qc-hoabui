# UC011-034 — Question Backlog

| Thuộc tính | Giá trị |
|---|---|
| **UC** | UC011-034: Bộ hồ sơ báo cáo xúc tiến đầu tư |
| **Nguồn** | UC011-034_bo-ho-so-xuc-tien-dau-tu_audited_20260514_v1.md |
| **Ngày tạo** | 2026-05-14 |
| **Tổng câu hỏi** | 9 |

---

## Câu hỏi mở (Open Questions)

| ID | Priority | Ref | Question | Why It Matters | Status | BA Answer |
|---|---|---|---|---|---|---|
| Q1 | High | "Đơn vị tiếp nhận sẽ thấy được các hồ sơ được gửi đến" (UC011-034.1 Mục 3) | Đơn vị tiếp nhận (Cục ĐTNN) có giao diện riêng không? Quyền hạn cụ thể là gì? Ai trigger "Yêu cầu chỉnh sửa"? Có notification cho Admin khi bị YCCS không? | Không thể test luồng YCCS end-to-end nếu không biết trigger từ phía tiếp nhận. Ảnh hưởng đến test integration. | Resolved | Luồng YCCS do đơn vị tiếp nhận trigger từ phía họ. Không thông báo qua người dùng (Admin không nhận notification riêng — chỉ thấy trạng thái đổi khi truy cập danh sách). |
| Q2 | High | "Acceptance Criteria" — N/A (Missing) | UC gốc không có Acceptance Criteria tường minh. BA có thể bổ sung AC chính thức cho các luồng chính không? | AC là cơ sở để QA xác định pass/fail. Thiếu AC → test case dựa trên suy luận, có thể sai lệch với kỳ vọng BA. | Resolved | Đồng ý. QA tự derive AC từ UC spec hiện tại (đã đủ chi tiết). BA không bổ sung AC riêng. |
| Q3 | Medium | Tab B.IV.3 & B.IV.4 — Phần I Header (strikethrough ~~) | Các trường Header (Năm, Tên Bộ/UBND, Ngày lập, Số công văn, Đơn vị tính) bị strikethrough. Chúng đã bị loại bỏ hoàn toàn khỏi UI hay chỉ ẩn (hidden) và vẫn tồn tại ở backend? | Ảnh hưởng đến test data setup và verify dữ liệu export/print. Nếu vẫn tồn tại ở backend → cần test auto-fill logic. | Resolved | Đồng ý loại bỏ khỏi UI form nhập liệu. Dữ liệu Phần I không hiển thị trong form, nhưng sẽ được lấy sẵn từ báo cáo B.IV.2 (Năm, Số công văn) và tài khoản đăng nhập (Tên Bộ/UBND) để phục vụ Export/Print. |
| Q4 | Medium | CF_06.1: "⏳ [PENDING — CHL-09]: Chi tiết các loại hành động trong timeline Báo cáo gộp..." | Khi nào chi tiết Audit Trail (CF_06.1) sẽ được cập nhật? Các event nào được ghi nhận (Tạo, Lưu nháp biểu X, Nộp, YCCS, Xóa)? | Không thể test chức năng Xem vòng đời nếu không biết expected events. | Open | |
| Q5 | Medium | "Nguyên tắc trách nhiệm (API-sourced fields): ...hệ thống cho phép chỉnh sửa tất cả trường API-sourced trước khi Nộp" (UC011-034.2 Mục 3) | Nguyên tắc này mâu thuẫn với CMR_12 (API trả về data → Disabled). Cụ thể trường nào được phép sửa? Có nút "Unlock" hay tự động Enabled? | Mâu thuẫn giữa UC và CMR_12 → dev có thể implement sai. QA không biết expected behavior chính xác. | Resolved | Tất cả trường lấy qua API đều Enabled cho sửa (Phương án B). UI hiển thị warning icon cho ô dữ liệu API-sourced đã bị user chỉnh sửa. Không cần nút Unlock — trường luôn Enabled. CMR_12 được reinterpret: API pre-fill giá trị nhưng không lock field. |
| Q6 | Medium | UC011-034.3 #2 Import — Điều kiện: "Chờ duyệt" | Import cho phép khi hồ sơ ở trạng thái "Chờ duyệt". Nhưng CMR_03 quy định "Chờ duyệt" khóa quyền Sửa/Nộp. Import khi đã Chờ duyệt sẽ tạo bản ghi mới hay ghi đè? | Logic mâu thuẫn tiềm ẩn. Cần xác nhận hành vi Import khi đã có hồ sơ Chờ duyệt. | Resolved | Đồng ý loại bỏ "Chờ duyệt" khỏi điều kiện Import. Import chỉ khả dụng khi: trạng thái kỳ = "Trong thời hạn" VÀ (chưa có hồ sơ hoặc hồ sơ ở trạng thái Lưu nháp / Yêu cầu chỉnh sửa). |
| Q7 | Low | UC011-034.2 Mục 3 — "Decimal precision: auto-round half-up khi blur" | Khi auto-round, hệ thống có hiển thị thông báo/indicator cho người dùng biết giá trị đã bị làm tròn không? | UX concern: người dùng có thể không nhận ra giá trị đã thay đổi sau blur. | Resolved | Không cần hiển thị thông báo/indicator khi auto-round. Chỉ auto-round im lặng. |
| Q8 | Low | UC011-034.1 — Phân trang | CMR_10 quy định phân trang theo Kỳ (10 kỳ/trang). Nhưng UC011-034.1 Mục 3 chỉ nói "Phân trang danh sách. Tham chiếu: CMR_10." Với báo cáo Annual, số kỳ thường ít (< 10). Phân trang có thực sự cần thiết? | Nếu số kỳ < 10 thì pagination không bao giờ kích hoạt → có thể bỏ qua test pagination hoặc cần test với data lớn (nhiều năm). | Resolved | Đồng ý giữ nguyên phân trang theo CMR_10. Dữ liệu có thể nhiều năm (từ 1987) nên pagination vẫn cần thiết. |
| Q9 | Low | Tab A.IV.4 — "(8) Diện tích đất ≤ Tổng DT quỹ đất dự án" | Thông báo lỗi cụ thể khi vi phạm là gì? UC chỉ ghi "Cảnh báo inline" mà không nêu text message. | QA cần biết exact error message để verify. | Resolved | Đồng ý bổ sung text cảnh báo inline: *"Diện tích đất không được vượt quá tổng diện tích quỹ đất của dự án."* |

---

## Thống kê

| Priority | Tổng | Open | Resolved |
|---|---|---|---|
| High | 2 | 0 | 2 |
| Medium | 4 | 1 | 3 |
| Low | 3 | 0 | 3 |
| **Tổng** | **9** | **1** | **8** |
