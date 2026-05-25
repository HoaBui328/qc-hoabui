# Backlog Câu hỏi: UC203-208_QLNNBoDTRNN

- **UC:** UC203-208 — Báo cáo QLNN về HĐĐTRNN các Bộ, ngành (Mẫu II.4)
- **Ngày tạo:** 2026-05-11
- **Nguồn:** UC203-208_QLNNBoDTRNN_audited_20260511_v1.md

---

## Open Questions

| ID | Priority | Ref | Question | Why It Matters | Status | BA Answer |
|----|----------|-----|----------|----------------|--------|-----------|
| Q1 | High | N/A (Missing) | Bổ sung file Mockup/Wireframe cho UC203-208 (Danh sách, Lập báo cáo, Xem chi tiết). | Không thể map UI components — Section 4/5 bị chặn hoàn toàn (score 0). | Open | |
| Q2 | High | UC203-208.2 mục 3: "Nộp thành công → 'Đã tiếp nhận' hoặc 'Chờ duyệt'" | Quy trình duyệt Mẫu II.4 là 2 bước hay >2 bước? Xác nhận chính xác 1 giá trị trạng thái đầu ra. | Tester không thể viết expected result cho luồng Nộp. | Open | |
| Q3 | High | UC203-208.2 mục 12: Nút "Xem" | CF_01 gọi là [Xem chi tiết], UC gọi là [Xem]. Tên chính thức? CF_07.1 cũng có nút [Xem] trên View — 2 nút cùng tên gây nhầm. | Tester cần đúng label để viết test step và báo bug. | Open | |
| Q4 | Medium | UC203-208.2 mục 2: "Số văn bản — Placeholder 'VD: 123/2026/VB-BTC'" | Có áp dụng CMR_13 (Số công văn) không? Placeholder có năm 2026 — không khớp pattern CMR_13. Nếu không, validate format cụ thể là gì? | Xác định auto-uppercase, block ký tự, validate `/` `-` theo CMR_13 hay chỉ max 50 chars. | Open | |
| Q5 | Medium | UC203-208.2 mục 1: "Tên cơ quan — CMR_12" | Trường lấy data từ API call (áp dụng 4 case CMR_12: null → Enabled, lỗi → Toast T05) hay từ session/token (luôn Disabled)? | Test case cần biết có mock API, có case Enabled, có Toast T05 không. | Open | |
| Q6 | Medium | UC203-208.1 mục 4: "Placeholder 'Nhập dữ liệu'" | CS_01 Mục 3 chuẩn: "Tìm kiếm theo Mã báo cáo". UC ghi "Nhập dữ liệu". Placeholder chính thức? | Sai placeholder → lỗi UI khi test. | Open | |
| Q7 | Medium | UC203-208.1 mục 4: "Live Search" | CS_01 yêu cầu Debounce 300–500ms. UC không đề cập. Có áp dụng? | Không debounce → mỗi keystroke gọi API → performance. | Open | |
| Q8 | Medium | UC203-208.1 mục 4: "Không tìm thấy kết quả" | CS_01 chuẩn: "Không tìm thấy dữ liệu phù hợp" kèm hình ảnh placeholder. UC ghi "Không tìm thấy kết quả" (không nhắc hình ảnh). Text và ảnh chính thức? | Expected text sai → fail test. | Open | |
| Q9 | Medium | UC203-208.1 mục 3: "Phân trang — CMR_10" | CS_01 Mục 4: max 10 bản ghi/kỳ + scroll dọc. UC tham chiếu CMR_10 (phân trang 10/20/50/100). Mâu thuẫn — áp dụng rule nào? | 2 rule xung đột, tester không biết test scroll hay pagination. | Open | |
| Q10 | Medium | UC203-208.2: Không đề cập CMR_14 | CF_01 nút [Hủy] → dirty check → popup P02. UC không nhắc CMR_14. Có áp dụng Dirty Form Guard cho Lập + Chỉnh sửa? | Popup cảnh báo khi navigate khỏi form dirty — cần test hay không. | Open | |
| Q11 | Medium | UC203-208.2 mục 9: "Cho phép upload nhiều file" | Max bao nhiêu file? Giới hạn tổng dung lượng? Cho phép upload file trùng tên? | Boundary test: max count, total size, duplicate name. | Open | |
| Q12 | Medium | UC203-208.2 mục 9: Lỗi file upload | UC mô tả inline error. CF_02 dùng Alert trên popup (A03). Lỗi hiển thị inline hay Alert popup? | Vị trí lỗi khác nhau → test step khác nhau. | Open | |
| Q13 | Medium | UC203-208.1 mục 8: "Import — CF_02" | UC không mô tả luồng Import chi tiết. Xác nhận: (a) Áp dụng CF_02 Case 2? (b) Template format .xlsx hay .docx? (c) Tên file: Mau_ODI_II4_[YYYYMMDD]_[HHMM]? | Tester cần spec luồng Import end-to-end. | Open | |
| Q14 | Medium | UC203-208.3 mục 1: "Nộp — CF_09" | CF_09 Step 3b: validate FAIL → mở màn hình Lập + hiển thị lỗi + scroll/focus. UC không mô tả. Có áp dụng? | Test behavior Nộp từ Danh sách khi fail. | Open | |
| Q15 | Medium | UC203-208.1 mục 1: Yearpicker filter | CS_01 Mục 2: chỉ Enable năm có data hoặc năm hiện tại, còn lại Disabled. UC không đề cập. Có áp dụng? | Test Enable/Disable năm trong Yearpicker. | Open | |
| Q16 | Medium | UC203-208.3: Export file naming | CF_04: tên file = `[Mã-Báo-Cáo]_[Kỳ-Báo-Cáo]_[Mã-cơ-quan-nộp]`. Mã cơ quan nộp lấy từ đâu? Format cụ thể? | Verify tên file export chính xác. | Open | |
| Q17 | Low | UC203-208.1 mục 5: "CMR_08" | CMR_08 "Chưa định nghĩa". Bao giờ có quy tắc hiển thị kỳ hạn? | Test header kỳ hạn bị chặn. | Open | |

---

## Answered Questions

| ID | Ref | Question | BA Answer | Status |
|----|-----|----------|-----------|--------|
|    |     |          |           |        |
