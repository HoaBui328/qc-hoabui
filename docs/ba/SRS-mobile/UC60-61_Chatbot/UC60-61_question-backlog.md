# Question Backlog

> Generated: 2026-05-14
> Updated: 2026-05-22 (Q&A resolution — QC ↔ BA, cập nhật SRS v1.5)
> Source files: UC60-61_chatbot_audited_20260518_v4.md, UC60-61_chatbot_qa-resolution_20260522_v1.md

---

## Open Questions

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q2 | Low | §3.1 — Lazy load | Page size do API AI quyết định — không có fallback hay giới hạn tối thiểu để QA test được. Ghi nhận là dependency của BE/AI team. | QA không thể test boundary page size, chỉ test behavior (loading indicator xuất hiện/ẩn đúng lúc). | Accepted |
| Q3 | Low | N/A (Missing) | NFR còn thiếu: Giới hạn số tin nhắn tối đa trong 1 phiên, performance khi lịch sử dài. Đây là dependency của BE/AI team. | QA ghi nhận không test performance; chỉ test functional flow. | Accepted |

Priority: H = High (blocks design), M = Medium (affects scope), L = Low (nice to know)
Status: Open | Answered | Accepted | Deferred

---

## Answered Questions

| ID | Priority | Ref | Question | Answer | Answered By | Date | Status |
|----|----------|-----|----------|--------|-------------|------|--------|
| Q1 | Low | Section 2.1 mô tả giao diện | Dòng `---` thừa xuất hiện trước "#### 2.2" do edit kỹ thuật — cần dọn dẹp để markdown không bị vỡ. | Đã xóa dòng --- thừa. | huyen.dinh2 | 2026-05-14 | Answered |
| Q4 | Medium | §2.2 Field #19 | **Bookmark persistence & access:** (a) Bookmark có được giữ khi phiên hết hạn (>24h)? (b) Người dùng xem lại danh sách bookmark ở đâu? | Bookmark không thuộc scope UC60-61. Thuộc UC riêng "Lưu lịch sử phiên tư vấn với Trợ lý AI". Đã xóa Field #19 khỏi SRS v1.5. | huyen.dinh2 | 2026-05-22 | Answered |
| Q5 | Low | §2.2 Field #16 | **Trích dẫn pháp lý overflow:** Khi có nhiều nguồn (>10), vùng trích dẫn mở rộng có scroll riêng hay chiếm toàn bộ? | Khối trích dẫn pháp lý collapsible (Field #16) đã bị xóa hoàn toàn khỏi SRS v1.5. FE chỉ hiển thị text trả về từ BE/AI dạng plain text inline trong bubble. Không còn vấn đề overflow. | huyen.dinh2 | 2026-05-22 | Answered |
| Q6 | Medium | §3.10 item 2 | **Kết nối cán bộ — format output:** Hotline hiển thị là số nào? "Kênh hỗ trợ" cụ thể là gì? | Hotline fix cứng: +84 24 2220 2828 (từ chân trang cmcportal). Số này được AI tự sinh trong đoạn text chat trả về, nằm trong bubble bot bình thường. Không cần UI đặc biệt. | huyen.dinh2 | 2026-05-22 | Answered |
