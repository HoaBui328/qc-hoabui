# UC60-61 — Chatbot Trợ lý Đầu Tư — UC Readiness Review (Re-audit)

**Tiêu đề:** UC60-61_chatbot_audited_20260518_v4.md
**Ngày tạo:** 18/05/2026
**Tác giả:** QC Agent
**Phiên bản:** v4

---

## 📊 Audit Summary

**Artefacts reviewed:** UC60-61_chatbot_srs_20260518_v1.4.md + Wireframes (7 ảnh) + CMR_Mobile v1.6

| # | Knowledge Area | Max Pts | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ Complete |
| 2 | Objective & Scope | 5 | 5/5 | ✅ Complete |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ Complete |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ Complete |
| 5 | UI Object Inventory & Mapping | 15 | 14/15 | ⚠️ Partial |
| 6 | Object Attributes & Behavior Definition | 20 | 18/20 | ⚠️ Partial |
| 7 | Functional Logic & Workflow Decomposition | 20 | 19/20 | ⚠️ Partial |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ Complete |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ Complete |
| 10 | Non-functional Requirements | 5 | 2/5 | ⚠️ Partial |
| **Total** | | **110** | **103/110** | **93.6/100** |

> **Verdict: ✅ READY** (93.6/100) — QA có thể bắt đầu thiết kế test case.

---

## 📋 Scoring Rationale

### 1. Feature Identity (5/5) ✅

- UC ID rõ ràng: UC60, UC61
- Tên chức năng: "Chatbot Trợ lý Đầu Tư trên Mobile"
- BA phụ trách: huyen.dinh2
- Phiên bản: v1.4
- Phân hệ: Ứng dụng Di động (Mobile App)

### 2. Objective & Scope (5/5) ✅

- Mô tả mục đích rõ ràng: tư vấn toàn diện về đầu tư tại Việt Nam qua hội thoại
- Exclusions được định nghĩa rõ: không quản lý model AI, không gọi điện/video call, không có màn hình quản lý riêng
- Phạm vi 6 nhóm năng lực được liệt kê cụ thể trong §1

### 3. Actors & User Roles (10/10) ✅

- Đối tượng: Cá nhân / Tổ chức (đã đăng nhập)
- Phân quyền: hai nhóm có cùng hành vi — không phân biệt
- Rõ ràng, không mơ hồ

### 4. Preconditions & Postconditions (10/10) ✅

- Preconditions: kết nối mạng ổn định + đã đăng nhập
- Postconditions: nhận phản hồi kèm trích dẫn pháp lý (nếu có), đánh giá là tuỳ chọn

### 5. UI Object Inventory & Mapping (14/15) ⚠️

- 32 UI objects được liệt kê chi tiết qua 4 section (Welcome, Hội thoại, Offline, Popup)
- Wireframe tham chiếu rõ ràng cho từng section
- Các element mới (trích dẫn collapsible, bubble câu hỏi bổ sung, bookmark, copy, Bottom Sheet lý do) được mô tả chi tiết trong spec

**Gap (-1 điểm):**
- **Field #5 (Nút Menu ⋮):** Element mới không có trong wireframe gốc. Wireframe hiện có chỉ hiển thị Header với nút Back + Avatar + Tiêu đề + Subtitle. Nút Menu (⋮) cần được bổ sung vào wireframe hoặc ghi nhận là element mới chưa có visual reference.

### 6. Object Attributes & Behavior Definition (18/20) ⚠️

- Tất cả 32 fields có quy tắc hiển thị và hành động chi tiết
- States rõ ràng (default, active, loading, error)
- Collapsible trích dẫn: mô tả đầy đủ (thu gọn/mở rộng, nội dung từng nguồn, badge hiệu lực, cảnh báo)
- Bottom Sheet lý do: checkbox multi-select, max 200 ký tự cho "Khác", nút Gửi/Bỏ qua

**Gap (-2 điểm):**
- **Q4 (Medium):** Field #19 Bookmark — "Nội dung đã bookmark được lưu trong phiên hiện tại" nhưng không mô tả: (a) Khi phiên hết hạn (>24h), bookmark có được giữ lại không? (b) Người dùng xem lại bookmark ở đâu? Không có entry point để xem danh sách bookmark.
- **Q5 (Low):** Field #16 Khối trích dẫn pháp lý — Không mô tả giới hạn số nguồn hiển thị khi mở rộng. Nếu có 20+ nguồn, vùng trích dẫn có scroll riêng hay chiếm toàn bộ bubble?

### 7. Functional Logic & Workflow Decomposition (19/20) ⚠️

- §3.1 Luồng gửi/nhận: 10 bước chi tiết, bao gồm cả phản hồi dạng câu hỏi bổ sung
- §3.2 Luồng đánh giá: rõ ràng (👍 trực tiếp, 👎 qua Bottom Sheet)
- §3.3 Quy tắc phiên: lưu tự động, tiếp tục <24h, FIFO 50 phiên, phiên mới từ Menu
- §3.4–3.10 Logic xử lý ngầm: 7 section mô tả năng lực AI, đều ghi rõ "Xử lý ngầm" + output qua bubble chat

**Gap (-1 điểm):**
- **Q6 (Medium):** §3.10 item 2 "Kết nối cán bộ" — Mô tả "AI gợi ý NĐT liên hệ cán bộ qua hotline hoặc kênh hỗ trợ" nhưng không rõ: (a) Hotline hiển thị là số nào? Cùng (+84) 24 2220 2828 hay số khác? (b) "Kênh hỗ trợ" cụ thể là gì? Nếu chỉ là text trong bubble thì cần ghi rõ format output.

### 8. Functional Integration Analysis (10/10) ✅

- CMR references đầy đủ: CMR-06 (Header), CMR-07 (Error), CMR-13 (Pull-to-Refresh), CMR-17 (Đa ngôn ngữ), CMR-18 (Debounce)
- Entry points: Sidebar → "Chatbot hỗ trợ" / Floating Widget
- Timeout 30s override CMR-16 (10s) — có giải thích lý do hợp lý (AI processing time)
- Session management tích hợp với login/logout (401 → refresh token → redirect)
- Ngôn ngữ tích hợp CMR-17 + logic detect ngôn ngữ đầu vào

### 9. Acceptance Criteria (10/10) ✅

- 23 ACs (AC1–AC23): đầy đủ, measurable, testable
- AC1–AC11: giữ từ v1.3 (sửa AC7 cho logic phiên mới)
- AC12–AC23: cover toàn bộ tính năng mới v1.4
- Mỗi AC mô tả hành vi observable (bubble hiển thị, toast xuất hiện, icon đổi màu...)
- AC cho logic ngầm (AC21–AC23) test behavior output (AI trả về trong bubble) — phù hợp cho functional testing

### 10. Non-functional Requirements (2/5) ⚠️

**Có:**
- Timeout: 30 giây (giải thích lý do)
- Max phiên: 50 (FIFO)
- Max ký tự input: 500
- Đa ngôn ngữ: 5 ngôn ngữ
- Retry đánh giá: max 3 lần

**Thiếu (giữ từ audit v3 — Accepted):**
- Giới hạn số tin nhắn tối đa trong 1 phiên (Q3 — Accepted)
- Page size lazy load do API quyết định (Q2 — Accepted)
- Response time SLA cho non-AI operations
- Data retention policy (phiên lưu bao lâu trên server?)

---

## 📋 Unified Gap & Question Report

| ID | Priority | Ref | Câu hỏi / Gap | Why It Matters | Status |
|----|----------|-----|----------------|----------------|--------|
| Q2 | Low | §3.1 — Lazy load | Page size do API AI quyết định — không có fallback hay giới hạn tối thiểu. | QA không thể test boundary page size. | Accepted |
| Q3 | Low | N/A (Missing) | NFR còn thiếu: Giới hạn số tin nhắn tối đa, performance khi lịch sử dài. | QA ghi nhận không test performance. | Accepted |
| Q4 | Medium | §2.2 Field #19 | **Bookmark persistence & access:** (a) Bookmark có được giữ khi phiên hết hạn (>24h)? (b) Người dùng xem lại danh sách bookmark ở đâu? Hiện không có entry point. | QA cần biết để test: bookmark mất sau 24h hay giữ vĩnh viễn? Có cách nào xem lại bookmark không? | Open |
| Q5 | Low | §2.2 Field #16 | **Trích dẫn pháp lý overflow:** Khi có nhiều nguồn (>10), vùng trích dẫn mở rộng có scroll riêng hay chiếm toàn bộ? | QA cần test boundary cho số lượng nguồn lớn. | Open |
| Q6 | Medium | §3.10 item 2 | **Kết nối cán bộ — format output:** Hotline hiển thị là số nào? "Kênh hỗ trợ" cụ thể là gì? Cần ghi rõ format text trong bubble. | QA cần verify nội dung chính xác của bubble "kết nối cán bộ". | Open |

---

## 🟢 What's Good (v1.4)

- **Thiết kế đúng triết lý:** Toàn bộ năng lực AI mới được mô tả là "xử lý ngầm" — không sinh thêm màn hình, giữ nguyên wireframe. Rất rõ ràng cho dev và QA.
- **Trích dẫn pháp lý:** Collapsible container với badge hiệu lực + cảnh báo hết hiệu lực — thiết kế UX tốt.
- **Bubble câu hỏi bổ sung:** Phân biệt rõ với bubble phản hồi (viền đỏ nhạt, không có thanh đánh giá) — testable.
- **Session management:** Logic phiên rõ ràng (auto-save, 24h rule, 50 max FIFO, "Phiên mới" từ Menu).
- **Bottom Sheet lý do đánh giá thấp:** Multi-select + "Khác" (max 200 ký tự) — nâng cao chất lượng feedback.
- **Disclaimer mở rộng:** Text đầy đủ hơn v1.3, bao gồm "không thay thế kết luận chính thức của cơ quan có thẩm quyền".
- **Popup rời chatbot:** Cập nhật text phù hợp logic lưu phiên mới ("sẽ được lưu tự động").

---

## 🧪 Testability Outlook

**CÓ THỂ test ngay:**
- Luồng Welcome → Hội thoại (giữ từ v1.3)
- Input bar: max 500 ký tự, max 5 dòng, bàn phím behavior
- Send button: 3 trạng thái (ẩn / paper plane / spinner)
- Rating: 👍 trực tiếp, 👎 qua Bottom Sheet lý do, "Đánh giá lại?" reset
- Back popup xác nhận (text mới: "lưu tự động")
- Error flows chuẩn CMR-07
- Offline screen + nút "Thử lại"
- Fallback & câu hỏi "Ngoài phạm vi"
- Lazy load khi scroll lên
- Đa ngôn ngữ tự nhận diện đầu vào
- **[MỚI]** Khối trích dẫn pháp lý: collapsible, tap mở/đóng, badge hiệu lực, cảnh báo
- **[MỚI]** Bubble câu hỏi bổ sung: viền đỏ nhạt, không có thanh đánh giá
- **[MỚI]** Nút Bookmark: toggle icon xám↔vàng, Toast
- **[MỚI]** Nút Copy: copy to clipboard, Toast
- **[MỚI]** Bottom Sheet lý do: checkbox multi-select, "Khác" max 200 ký tự, Gửi/Bỏ qua
- **[MỚI]** Menu (⋮): "Phiên mới" (lưu + reset Welcome), "Chọn ngôn ngữ"
- **[MỚI]** Phiên tự động: lưu khi ≥1 cặp hỏi-đáp, tiếp tục <24h, Welcome >24h
- **[MỚI]** FIFO 50 phiên
- **[MỚI]** Phát hiện thông tin nhạy cảm → bubble cảnh báo + không lưu

**Accepted dependencies (không test):**
- Page size lazy load (Q2)
- Performance/load test (Q3)
- Độ chính xác nội dung AI (thuộc AI team)

**Chờ clarification (Q4, Q5, Q6):**
- Bookmark persistence & access point
- Trích dẫn overflow behavior
- Format output "Kết nối cán bộ"

---

## 📝 Changelog

- **v4 (18/05/2026):**
  - Re-audit trên SRS v1.4 (thay đổi lớn từ v1.3: bổ sung 7 section logic xử lý ngầm, 11 UI elements mới trong bubble, session management redesign, 12 AC mới)
  - Giữ Q2, Q3 (Accepted từ v3)
  - Bổ sung Q4 (Bookmark persistence), Q5 (Trích dẫn overflow), Q6 (Kết nối cán bộ format)
  - Điểm giảm từ 97.3 (v3 trên v1.3) xuống 93.6 (v4 trên v1.4) do scope mở rộng đáng kể với một số gap mới
  - Verdict vẫn READY — các gap mới không block test design
