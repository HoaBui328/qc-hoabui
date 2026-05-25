# UC Readiness Review (Re-Audit)
**Functional / Black-box Test Readiness Template**
**File được audit:** `UC70_tra-cuu-tthc_srs_20260518_v5.md`
**Ngày audit:** 18/05/2026
**Phiên bản audit:** v2

---

## Feature Brief
Chức năng cho phép cá nhân, tổ chức (không yêu cầu đăng nhập) tìm kiếm, lọc và tra cứu thông tin chi tiết về các thủ tục hành chính trên ứng dụng di động. Hệ thống hiển thị danh sách thủ tục dưới dạng List Card (với thuộc tính: Tên thủ tục, Mã thủ tục, Lĩnh vực, Cơ quan thực hiện) và cung cấp màn hình chi tiết được phân rã thành 5 tab nội dung: Thông tin chung, Trình tự thực hiện, Thành phần hồ sơ, Cách thức thực hiện, và Căn cứ pháp lý. Bộ lọc chỉ gồm Lĩnh vực (đã bỏ bộ lọc Ngôn ngữ từ v5).

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `89.1 / 100` | ⚡ **CONDITIONALLY READY** |

---

## 📊 Audit Summary

| # | Knowledge Area | Max Pts | Score | Status | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 1 | Feature Identity | 5 | 5/5 | ✅ | Rõ ràng: UC70, Tra cứu TTHC trên Mobile |
| 2 | Objective & Scope | 5 | 5/5 | ✅ | Mô tả đầy đủ mục tiêu, phạm vi, exclusions |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ | Cá nhân/Tổ chức, public access |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ | Đầy đủ |
| 5 | UI Object Inventory & Mapping | 15 | 13/15 | ⚡ | Xem chi tiết bên dưới |
| 6 | Object Attributes & Behavior Definition | 20 | 17/20 | ⚡ | Một số mô tả còn high-level |
| 7 | Functional Logic & Workflow Decomposition | 20 | 18/20 | ⚡ | Luồng chính đầy đủ, thiếu một số chi tiết |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ | Tham chiếu CMR đầy đủ |
| 9 | Acceptance Criteria | 10 | 9/10 | ⚡ | Thiếu AC cho nút Copy |
| 10 | Non-functional Requirements | 5 | 5/5 | ✅ | Đa ngôn ngữ, timeout, retry |
| **Total** | | **110** | **102/110** | | **89.1/100** |

---

## 📋 Unified Gap & Question Report

### Phần A — Các vấn đề từ audit v1 đã được giải quyết trong v4/v5

| ID | Ref | Trạng thái | Ghi chú |
|----|-----|-----------|---------|
| Q1 (v1) | Active filter indicator | ✅ Resolved | v4 đã bổ sung: hiển thị chấm xanh khi Lĩnh vực khác mặc định (CMR-02) |
| Q2 (v1) | Tải mẫu đơn | ✅ Resolved | v4 đã làm rõ: tải file trực tiếp về bộ nhớ thiết bị (CMR-08) |
| Q3 (v1) | Swipe tab | ✅ Resolved | v4 đã bổ sung: hỗ trợ vuốt ngang (Swipe left/right) để chuyển tab |
| Q4 (v1) | Retry lazy load | ✅ Resolved | v4 đã bổ sung: retry 3 lần, cách nhau ~2s (CMR-04) |
| Q5 (v1) | Hotline behavior | ✅ Resolved | v4 đã làm rõ: push số ra dialer, không tự động gọi |

### Phần B — Các vấn đề mới phát hiện trong re-audit v5

| ID | Priority | Ref | Vấn đề | Tại sao quan trọng | Đề xuất |
|----|----------|-----|---------|---------------------|---------|
| Q6 | 🟡 Medium | Mục 2.3, Row #2 — Khối Tên & Mã thủ tục | **Nút Copy đã được mô tả** nhưng còn thiếu chi tiết: (1) Vị trí chính xác của icon Copy so với mã thủ tục (bên phải, cùng dòng); (2) Trạng thái visual của icon (màu sắc, kích thước); (3) Thời gian hiển thị Toast "Đã sao chép" (bao lâu tự ẩn?). | Wireframe cho thấy icon Copy (□) nằm ngay bên phải mã "TT-001-2024", cùng dòng. Tester cần biết chính xác vị trí và hành vi feedback để verify. | Bổ sung: "Icon Copy (□) nằm bên phải mã thủ tục, cùng dòng, màu xám đậm. Tap → Toast 'Đã sao chép' hiển thị 2-3 giây rồi tự ẩn." |
| Q7 | 🟡 Medium | Mục 2.3, Row #1 — Header chi tiết | **Tiêu đề header rút gọn** — Tài liệu ghi "Tiêu đề hiển thị tên thủ tục rút gọn" nhưng không quy định: (1) Giới hạn bao nhiêu ký tự trước khi rút gọn? (2) Rút gọn bằng cách nào (cắt + "..." hay chỉ hiển thị 1 dòng)? | Wireframe cho thấy header hiển thị đầy đủ "Thủ tục đăng ký đầu tư dự án mới" — cần xác nhận quy tắc truncate. | Bổ sung quy tắc: "Tiêu đề header hiển thị tối đa 1 dòng, nếu vượt quá chiều rộng header thì cắt và hiển thị '...' ở cuối." |
| Q8 | 🟡 Medium | Mục 2.3, Row #2 — Tag Cấp thực hiện | **Vị trí Tag "Trung ương"** — Wireframe cho thấy Tag badge nền đỏ đậm "Trung ương" nằm bên trái mã thủ tục, cùng dòng. Tài liệu mô tả đúng nhưng chưa nêu rõ layout: Tag ở bên trái, Mã thủ tục ở giữa, Icon Copy ở bên phải. | Tester cần biết thứ tự hiển thị chính xác để verify UI. | Bổ sung mô tả layout: "[Tag Cấp thực hiện] [Mã thủ tục] [Icon Copy]" — hiển thị trên cùng 1 dòng, căn trái. |
| Q9 | 🟢 Low | Mục 1 — Mô tả chức năng | **Mô tả chức năng còn high-level** — Phần "Mô tả" chỉ liệt kê tổng quan các tính năng mà chưa nêu rõ: (1) Danh sách mặc định sắp xếp theo tiêu chí gì? (mới nhất, theo tên A-Z, hay theo API trả về?); (2) Số lượng thủ tục tối đa hệ thống hỗ trợ hiển thị? | Ảnh hưởng đến test case verify thứ tự hiển thị mặc định và performance test. | Bổ sung: "Danh sách mặc định hiển thị theo thứ tự [tiêu chí sắp xếp] từ API. Không giới hạn tổng số bản ghi (phụ thuộc dữ liệu hệ thống)." |
| Q10 | 🟢 Low | Mục 2.3, Row #5 — Khối Tổng quan | **Khối Tổng quan vs Khối Chi tiết** — Cả 2 khối đều hiển thị "Cơ quan thực hiện". Khối Tổng quan hiển thị 2 trường (Cơ quan thực hiện + Thời hạn) nhưng không rõ vị trí hiển thị so với Khối Chi tiết (ở trên hay ở dưới?). | Wireframe cần xác nhận layout giữa các khối trong Tab Thông tin chung. | Làm rõ thứ tự hiển thị: Khối Tổng quan (summary card) hiển thị ở đầu tab, Khối Chi tiết (full list) hiển thị bên dưới. |
| Q11 | 🟢 Low | Mục 2.2 — Bottom Sheet | **Bộ lọc chỉ còn 1 field (Lĩnh vực)** — Sau khi bỏ Ngôn ngữ, Bottom Sheet chỉ còn 1 dropdown duy nhất. Cần xác nhận: có cần giữ dạng Bottom Sheet hay chuyển sang inline filter (dropdown ngay trên màn hình danh sách) cho đơn giản hơn? | UX consideration: Bottom Sheet cho 1 field duy nhất có thể là over-engineering. Tuy nhiên nếu tương lai sẽ thêm filter khác thì giữ Bottom Sheet là hợp lý. | Xác nhận với PO/UX: giữ Bottom Sheet hay chuyển inline. Nếu giữ → document lý do (extensibility). |

---

## 🔍 Wireframe Cross-Check (So sánh Wireframe vs Tài liệu)

### Màn hình Chi tiết (Wireframe được cung cấp bởi user)

| Element trên Wireframe | Mô tả trong SRS v5 | Kết quả |
|---|---|---|
| Header đỏ đậm "Thủ tục đăng ký đầu tư dự án mới" | Row #1: Header nền đỏ đậm, chữ trắng, tên thủ tục rút gọn | ✅ Khớp |
| Icon chuông (thông báo) góc phải header | Row #1 (mục 2.1): Icon Thông báo góc phải | ✅ Khớp |
| Nút ← quay lại góc trái | Row #1: Nút Quay lại | ✅ Khớp |
| Tên thủ tục đậm "Thủ tục đăng ký đầu tư dự án mới" | Row #2: Tên thủ tục font đậm, chữ đen | ✅ Khớp |
| Tag đỏ "Trung ương" | Row #2: Tag Cấp thực hiện, badge nền đỏ đậm | ✅ Khớp |
| Mã "TT-001-2024" | Row #2: Mã thủ tục text xám | ✅ Khớp |
| **Icon Copy (□) bên phải mã thủ tục** | Row #2: "có icon Copy bên cạnh" | ⚡ Khớp nhưng mô tả chưa chi tiết vị trí/style |
| Tab bar: "Thông tin chung", "Trình tự thực hiện", "Thành phầ..." | Row #3: 5 tab đầy đủ | ✅ Khớp |
| Tab "Thông tin chung" đang active (gạch đỏ dưới) | Row #3: Mặc định "Thông tin chung" | ✅ Khớp |
| Đường kẻ phân cách dưới tab bar | Không mô tả | ⚠️ Minor — UI detail |

### Kết luận Wireframe Cross-Check
- **Nút Copy**: ĐÃ được mô tả trong SRS v5 (Row #2, mục 2.3) với hành vi "Tap icon Copy → Sao chép mã thủ tục vào clipboard, hiển thị Toast 'Đã sao chép'". Tuy nhiên mô tả vị trí chỉ ghi "có icon Copy bên cạnh" — nên bổ sung chi tiết hơn (xem Q6).
- **Layout tổng thể**: Wireframe khớp với mô tả SRS. Thứ tự hiển thị: [Tên thủ tục] → [Tag Cấp thực hiện] [Mã thủ tục] [Icon Copy] → [Tab Bar].

---

## 🟢 What's Good (Điểm mạnh)
- Tài liệu v5 đã giải quyết toàn bộ 5 câu hỏi từ audit v1 (indicator bộ lọc, swipe tab, retry lazy load, tải file trực tiếp, dialer behavior).
- Cập nhật nhãn "Cơ quan" → "Cơ quan thực hiện" đồng bộ giữa card danh sách và tab chi tiết.
- Bỏ bộ lọc Ngôn ngữ được phản ánh nhất quán xuyên suốt tài liệu (mô tả, Bottom Sheet, luồng xử lý, AC).
- Tham chiếu CMR đầy đủ và chính xác.
- Nút Copy đã được mô tả với hành vi rõ ràng (copy to clipboard + toast).

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- Luồng tìm kiếm (Search) theo debounce 3 giây, auto-trim whitespace, state persistence.
- Luồng lọc danh sách qua Bottom Sheet (chỉ Lĩnh vực) + active filter indicator.
- Lazy load 20 item + retry 3 lần khi lỗi mạng + Pull to Refresh.
- Hiển thị UI màn hình Chi tiết: 5 tab, swipe ngang, tap tab.
- Nút Copy: sao chép mã thủ tục + toast "Đã sao chép".
- Nút Hotline: mở dialer với số điện thoại.
- Tab Thành phần hồ sơ: tải file trực tiếp về thiết bị.
- Partial API failure: block lỗi hiển thị riêng, block khác bình thường.
- Empty state, null value display ("-").

**What CANNOT be tested yet (blocked by gaps):**
- Thời gian hiển thị Toast (Q6) — cần xác nhận duration.
- Quy tắc truncate tiêu đề header (Q7) — cần xác nhận max chars/lines.
- Thứ tự sắp xếp mặc định danh sách (Q9) — cần xác nhận sort criteria.

**Suggested test focus areas:**
- Happy path: Tìm kiếm → Lọc → Xem chi tiết → Copy mã → Tải biểu mẫu.
- UI verification: Vị trí icon Copy, Tag Cấp thực hiện, layout header chi tiết.
- Edge cases: Tên thủ tục rất dài (truncate), mã thủ tục null, tất cả field null.
- Regression: Đảm bảo bỏ bộ lọc Ngôn ngữ không ảnh hưởng luồng lọc còn lại.

---

## 📌 Summary & Recommendation
Tài liệu SRS UC70 v5 đạt **89.1/100 (CONDITIONALLY READY)**. So với audit v1 (85.5/100), tài liệu đã cải thiện đáng kể nhờ giải quyết toàn bộ 5 câu hỏi trước đó. Nút Copy bên cạnh mã thủ tục **ĐÃ được mô tả** trong tài liệu (mục 2.3, Row #2) với hành vi đầy đủ. Các vấn đề còn lại chủ yếu là bổ sung chi tiết UI (vị trí chính xác, duration toast, quy tắc truncate) — không block việc thiết kế test case cho luồng chính.

**Khuyến nghị:** QA có thể bắt đầu thiết kế test case ngay. BA nên bổ sung các chi tiết Q6-Q11 trong phiên bản tiếp theo để hoàn thiện 100%.

---

## Changelog (So với audit v1)

| Mục | Thay đổi |
|-----|----------|
| SRS version | v3 → v5 |
| Q1-Q5 (audit v1) | Tất cả đã Resolved trong SRS v4/v5 |
| Score | 85.5 → 89.1 (+3.6) |
| Bộ lọc Ngôn ngữ | Đã bỏ khỏi Bottom Sheet (v5) |
| Nhãn "Cơ quan" | Đổi thành "Cơ quan thực hiện" (v5) |
| New questions | Q6-Q11 (chủ yếu Low-Medium, không block test design) |
