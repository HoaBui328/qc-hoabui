# Question Backlog

> Generated: 2026-05-11
> Source files: UC191-196_BaoCaoNamTaiChinhDTRNN.md

---

## Open Questions

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | H | Row 38 — cột Bắt buộc đánh 'x', Ghi chú ghi "Optional. Max 1000 ký tự" | Trường Kiến nghị là bắt buộc hay Optional? Hai nơi ghi mâu thuẫn nhau. | Validate sai khi submit → có thể block người dùng không cần thiết hoặc bỏ qua field thực sự bắt buộc. | Open |
| Q2 | H | "Cột Lũy kế ≥ Năm TC (dòng 1)", "Nếu (2) > 0 thì (2.1) ≤ (2)" | Hai rule validate chéo này là hard-block hay soft-warning? Error message hiển thị là gì? | Thiếu expected result → không thể viết test case negative cho các rule và tài chính quan trọng nhất. | Open |
| Q3 | M | "Tham chiếu: CMR_08" — CMR_08 hiện ghi chưa định nghĩa | Quy tắc định dạng, logic nhóm và hiển thị kỳ hạn theo năm cụ thể là gì? | Không thể test UI nhóm năm và các boundary của grouping logic. | Open |
| Q4 | M | Grid 2 cột (Năm TC / Luỹ kế) — "đơn vị USD trừ các ô ghi rõ VND" | Label đơn vị VND thể hiện cụ thể trên UI như thế nào? Cần wireframe. | Không kiểm tra được đúng đơn vị hiển thị trên Grid. | Open |
| Q5 | M | Section 8 AC — không có trong tài liệu gốc | Reviewer tự sinh AC. BA cần xác nhận AC có đúng nghiệp vụ không. | AC sai → QA viết test case sai hướng. | Open |
| Q6 | H | "Tham chiếu: CF_06" — CF_06 ghi "Chi tiết timeline chưa xác định" | Nội dung các loại hành động trong Audit Trail (Xem vòng đời) là gì? | QA không thể test nội dung timeline vòng đời. | Open |
| Q7 | M | "Năm tài chính báo cáo: Validate ngày hợp lệ, ngày kết thúc > ngày bắt đầu" | Error message khi vi phạm validate ngày là gì? | Thiếu expected result cho test case validate trường này. | Open |
| Q8 | M | "Ngày có BCTC: Validate ≤ ngày hiện tại" | Error message khi chọn ngày tương lai là gì? | Thiếu expected result cho test case boundary date. | Open |
| Q9 | L | "Nhà đầu tư cam kết chịu trách nhiệm hoàn toàn về tính chính xác..." (bị cắt ...) | Nội dung đầy đủ của label Checkbox cam kết là gì? | Cần text chính xác để verify UI — tránh sai nội dung pháp lý. | Open |
| Q10 | M | "Cho phép upload multi-file. Bắt buộc ít nhất 1 file" | Số lượng file tối đa được phép upload là bao nhiêu? | Thiếu upper boundary → không thể test vượt giới hạn số file. | Open |
| Q11 | M | "Xóa: Tham chiếu CF_08" — UC không mô tả popup xác nhận trong Section 2/3 | Hành động Xóa có popup xác nhận không? Nội dung popup P04 là gì? | Không có popup → xóa nhầm không recover được. | Open |
| Q12 | L | Placeholder: "Nghị định 103/2026/NĐ-CP" | Tên văn bản pháp lý này có chính xác không? Đã ban hành chưa? | Tham chiếu sai tên → rủi ro compliance. | Open |

Priority: H = High (blocks design), M = Medium (affects scope), L = Low (nice to know)
Status: Open | Answered | Deferred

---

## Answered Questions

| ID | Priority | Ref | Question | Answer | Answered By | Date | Status |
|----|----------|-----|----------|--------|-------------|------|--------|
