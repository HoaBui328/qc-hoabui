---
title: "UC60-61 Chatbot — Biên bản giải đáp Q&A (QC ↔ BA)"
date: 2026-05-22
author: huyen.dinh2
version: v1
---

# UC60-61 Chatbot — Biên bản giải đáp Q&A

## Thông tin chung

| Mục | Nội dung |
|-----|----------|
| UC | UC60-61 — Chatbot Trợ lý Đầu Tư trên Mobile |
| SRS gốc | UC60-61_chatbot_srs_20260518_v1.4.md |
| Ngày giải đáp | 22/05/2026 |
| Người hỏi | QC Team |
| Người trả lời | BA (huyen.dinh2) |
| Kết quả | 12/12 câu hỏi đã được giải đáp |

---

## Tổng hợp Q&A

### Q1. Menu (⋮) header — Phiên mới + Chọn ngôn ngữ

| Mục | Nội dung |
|-----|----------|
| **Câu hỏi QC** | Chọn ngôn ngữ theo kiểu nào? Có function tạo phiên mới không? Bên họ support không? |
| **Trả lời BA** | Hệ thống tự nhận diện ngôn ngữ — user gửi tin nhắn theo ngôn ngữ nào thì AI phản hồi theo ngôn ngữ đó. Đóng Chatbot, mở lại = Phiên mới. |
| **Impact SRS** | **REMOVE** "Chọn ngôn ngữ" khỏi menu dropdown (Field #5). **MODIFY** logic phiên mới: đóng/mở lại chatbot = tạo phiên mới. |
| **Ref** | §2.1 Field #5, §3.10 item 1, §3.12 |

---

### Q2 & Q10. Bottom Sheet lý do 👎 — multi-select + Khác 200 ký tự + Gửi/Bỏ qua

| Mục | Nội dung |
|-----|----------|
| **Câu hỏi QC** | Process như thế nào? Hay logic là click like vs dislike thôi? Đã confirm với AI chatbot chưa? Cần BE xử lý lưu thêm lí do không, hay chỉ local FE? |
| **Trả lời BA** | Logic: Click like - dislike, theo QnA WBS. Bỏ bottom sheet, chỉ có like/dislike. |
| **Impact SRS** | **REMOVE** Khung #24 (Bottom Sheet lý do) toàn bộ. Tap 👎 = ghi nhận dislike trực tiếp, không thu thập lý do. |
| **Ref** | §2.2 Field #24, §3.2 |

---

### Q3 & Q8. Khối trích dẫn pháp lý collapsible (Khung #16)

| Mục | Nội dung |
|-----|----------|
| **Câu hỏi QC** | Chưa hiểu phần này, cần confirm với team AI vì họ làm gì mình làm nấy. BE trả về như message bình thường thôi đúng không? |
| **Trả lời BA** | Xóa bỏ hoàn toàn Khung số 16 trong SRS v1.4. Confirm: FE chỉ việc hiển thị text trả về từ BE/AI lên giao diện như wireframe. FE không cần gắp dữ liệu để làm UI collapsible hay badge xanh/đỏ gì cả. |
| **Impact SRS** | **REMOVE** Khung #16 toàn bộ. Mọi nội dung trích dẫn pháp lý (nếu có) nằm inline trong text bubble bot dạng plain text. |
| **Ref** | §2.2 Field #16, §3.4, §3.5 |

---

### Q4. Bubble câu hỏi bổ sung — viền đỏ nhạt, không rating (Khung #17)

| Mục | Nội dung |
|-----|----------|
| **Câu hỏi QC** | Chưa hiểu rõ phần này. |
| **Trả lời BA** | Follow theo wireframe. Với FE: Mọi phản hồi từ Bot (dù là câu trả lời hay câu hỏi ngược lại user) đều được vẽ chung 1 UI mặc định là Bubble Bot bình thường. Không cần check điều kiện viền đỏ hay ẩn thanh đánh giá. BA xóa/sửa nội dung Khung số 17 trong SRS v1.4 để đồng nhất với Wireframe. |
| **Impact SRS** | **REMOVE** Khung #17. Tất cả bot messages dùng chung 1 UI bubble mặc định, không phân biệt viền đỏ. |
| **Ref** | §2.2 Field #17, §3.1, §3.5 |

---

### Q5. Nút bookmark — toggle xám/vàng + Toast (Khung #19)

| Mục | Nội dung |
|-----|----------|
| **Câu hỏi QC** | Bookmark persistence — Lưu ở đâu? Mất khi phiên hết hạn? User xem lại ở đâu? Cần lưu phía BE không? Chức năng này là UC bao nhiêu trong AI chatbot? |
| **Trả lời BA** | UC: "Lưu lịch sử phiên tư vấn với Trợ lý AI". Ưu tiên follow theo wireframe, bỏ mục 19 SRS. |
| **Impact SRS** | **REMOVE** Khung #19 toàn bộ. Bookmark không thuộc scope UC60-61, thuộc UC riêng "Lưu lịch sử phiên tư vấn với Trợ lý AI". |
| **Ref** | §2.2 Field #19 |
| **Resolves** | Question Backlog Q4 |

---

### Q6. Nút copy — clipboard + Toast (Khung #20)

| Mục | Nội dung |
|-----|----------|
| **Câu hỏi QC** | Cái này có trong UC chức năng hay có bên nào yêu cầu không? |
| **Trả lời BA** | Không có => Bỏ. |
| **Impact SRS** | **REMOVE** Khung #20 toàn bộ. |
| **Ref** | §2.2 Field #20 |

---

### Q7 & Q11. Bubble cảnh báo thông tin nhạy cảm

| Mục | Nội dung |
|-----|----------|
| **Câu hỏi QC** | Bên họ định xử lý cảnh báo thông tin nhạy cảm như thế nào? AI detect ở BE trả flag, hay FE cần regex check trước khi gửi? |
| **Trả lời BA** | Hiển thị tin nhắn dạng bubble Bot bình thường, không dùng Bottom Sheet. Nội dung: *"Vì lý do bảo mật, tôi không thể xử lý yêu cầu này. Vui lòng không chia sẻ thông tin nhạy cảm qua chatbot."* Đề xuất team AI có FAQ để bot follow theo. AI/BE detect, FE chỉ hiển thị. |
| **Impact SRS** | **SIMPLIFY** §3.10 item 4. Bỏ mô tả UI đặc biệt. Chỉ là bubble bot bình thường với text cảnh báo do AI trả về. |
| **Ref** | §3.10 item 4 |

---

### Q9. "Kết nối cán bộ" format — Hotline số nào? "Kênh hỗ trợ" là gì?

| Mục | Nội dung |
|-----|----------|
| **Câu hỏi QC** | Hotline số nào? "Kênh hỗ trợ" là gì? Text cứng hay dynamic từ BE? |
| **Trả lời BA** | Giai đoạn này fix cứng thông tin hỗ trợ. Số: **+84 24 2220 2828** (từ chân trang cmcportal). Số này sẽ được AI tự sinh trong đoạn text chat trả về, chữ nằm trong bubble bot. |
| **Impact SRS** | **MODIFY** §3.10 item 2. Hotline fix cứng +84 24 2220 2828, nằm trong text bubble bot. Không cần UI đặc biệt. |
| **Ref** | §3.10 item 2 |
| **Resolves** | Question Backlog Q6 |

---

### Q12. Cho đánh giá lại max 3 lần — handle FE hay BE?

| Mục | Nội dung |
|-----|----------|
| **Câu hỏi QC** | Handle FE hay BE handle trả lỗi khi đánh giá quá 3 lần? Lưu local thì khi user đăng xuất ra vào lại hoặc đăng nhập trên máy khác thì lại được đánh giá lại. Có cần rule này không, hay kệ thích đánh giá bao nhiêu lần thì đánh giá? Team AI chatbot có giới hạn không? |
| **Trả lời BA** | "Max 3 lần" trong bảng xử lý lỗi = **retry API ngầm khi lỗi mạng** (Network Error / Timeout), KHÔNG phải giới hạn số lần user được phép bấm Đánh giá. Cụ thể: Gọi API gửi đánh giá mà bị lỗi mạng → app (FE) tự động gọi lại (retry) API đó ngầm tối đa 3 lần ở background. **Đối với User:** Được quyền bấm nút Đánh giá / Đánh giá lại bao nhiêu lần tùy thích (không giới hạn). **Đối với DEV:** Xử lý phần "max 3 lần" ở tầng Code Gọi Mạng (Axios/Fetch interceptor). Nếu API /rating bị lỗi thì cho retry 3 lần. |
| **Impact SRS** | **CLARIFY** bảng §3.11. Ghi rõ "max 3 lần" = retry API ngầm (network layer), không phải giới hạn user action. |
| **Ref** | §3.11 — Bảng xử lý lỗi, dòng "Gửi đánh giá thất bại" |

---

## Tổng hợp Impact lên SRS

| Loại thay đổi | Số lượng | Chi tiết |
|---------------|----------|----------|
| REMOVE (xóa section/field) | 6 fields | #16, #17, #19, #20, #24 + khung "Hành động trên Bubble Bot" |
| MODIFY (sửa nội dung) | ~12 chỗ | Fields #5, #15, #22, #23; Sections 3.1, 3.2, 3.4, 3.5, 3.10, 3.11, 3.12 |
| REMOVE AC | 4 ACs | AC12, AC13, AC15, AC16 |
| MODIFY AC | 2 ACs | AC4, AC17 |

## Question Backlog — Resolved

| ID | Trạng thái | Câu trả lời |
|----|------------|-------------|
| Q4 | Answered | Bookmark thuộc UC khác "Lưu lịch sử phiên tư vấn với Trợ lý AI". Bỏ khỏi UC60-61 |
| Q5 | Answered | Khối trích dẫn pháp lý bị xóa hoàn toàn → Không còn vấn đề overflow |
| Q6 | Answered | Hotline +84 24 2220 2828, fix cứng trong text bubble bot. AI tự sinh |

---

## Nguyên tắc chung rút ra

> **Triết lý thiết kế UC60-61 sau Q&A:**
> - FE chỉ hiển thị text trả về từ BE/AI lên giao diện — không tự xử lý logic UI phức tạp
> - Mọi phản hồi bot dùng chung 1 UI bubble mặc định
> - Đánh giá đơn giản: like/dislike, không thu thập lý do
> - Ngôn ngữ: AI tự detect, không cần UI chọn
> - Thông tin hỗ trợ: fix cứng trong text AI trả về
