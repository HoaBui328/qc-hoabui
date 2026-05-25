# Question Backlog

> Generated: 20/05/2026
> Source files: UC70_tra-cuu-tthc_audited_20260518_v2.md

---

## Open Questions

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q6 | 🟡 Medium | Mục 2.3, Row #2 — Khối Tên & Mã thủ tục | Nút Copy đã được mô tả nhưng còn thiếu chi tiết: (1) Vị trí chính xác của icon Copy so với mã thủ tục (bên phải, cùng dòng); (2) Trạng thái visual của icon (màu sắc, kích thước); (3) Thời gian hiển thị Toast "Đã sao chép" (bao lâu tự ẩn?). | Wireframe cho thấy icon Copy (□) nằm ngay bên phải mã "TT-001-2024", cùng dòng. Tester cần biết chính xác vị trí và hành vi feedback để verify. | Open |
| Q7 | 🟡 Medium | Mục 2.3, Row #1 — Header chi tiết | Tiêu đề header rút gọn — Tài liệu ghi "Tiêu đề hiển thị tên thủ tục rút gọn" nhưng không quy định: (1) Giới hạn bao nhiêu ký tự trước khi rút gọn? (2) Rút gọn bằng cách nào (cắt + "..." hay chỉ hiển thị 1 dòng)? | Wireframe cần xác nhận quy tắc truncate. | Open |
| Q8 | 🟡 Medium | Mục 2.3, Row #2 — Tag Cấp thực hiện | Vị trí Tag "Trung ương" — Wireframe cho thấy Tag badge nền đỏ đậm nằm bên trái mã thủ tục, cùng dòng. Tài liệu mô tả đúng nhưng chưa nêu rõ layout: Tag ở bên trái, Mã thủ tục ở giữa, Icon Copy ở bên phải. | Tester cần biết thứ tự hiển thị chính xác để verify UI. | Open |
| Q9 | 🟢 Low | Mục 1 — Mô tả chức năng | Mô tả chức năng còn high-level — chưa nêu rõ: (1) Danh sách mặc định sắp xếp theo tiêu chí gì? (mới nhất, theo tên A-Z, hay theo API trả về?); (2) Số lượng thủ tục tối đa hệ thống hỗ trợ hiển thị? | Ảnh hưởng đến test case verify thứ tự hiển thị mặc định và performance test. | Open |
| Q10 | 🟢 Low | Mục 2.3, Row #5 — Khối Tổng quan | Khối Tổng quan vs Khối Chi tiết — Cả 2 khối đều hiển thị "Cơ quan thực hiện". Không rõ vị trí hiển thị so với Khối Chi tiết (ở trên hay ở dưới?). | Wireframe cần xác nhận layout giữa các khối trong Tab Thông tin chung. | Open |
| Q11 | 🟢 Low | Mục 2.2 — Bottom Sheet | Bộ lọc chỉ còn 1 field (Lĩnh vực) — Sau khi bỏ Ngôn ngữ, Bottom Sheet chỉ còn 1 dropdown duy nhất. Cần xác nhận: có cần giữ dạng Bottom Sheet hay chuyển sang inline filter? | UX consideration: Bottom Sheet cho 1 field duy nhất có thể là over-engineering. Nếu tương lai thêm filter khác thì giữ Bottom Sheet là hợp lý. | Open |

Priority: H = High (blocks design), M = Medium (affects scope), L = Low (nice to know)
Status: Open | Answered | Deferred

---

## Answered Questions

| ID | Priority | Ref | Question | Answer | Answered By | Date | Status |
|----|----------|-----|----------|--------|-------------|------|--------|
