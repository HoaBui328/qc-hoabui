# UC60-61 — Chatbot Trợ lý Đầu Tư — UC Readiness Review (Re-audit)

**Tiêu đề:** UC60-61_chatbot_audited_20260514_v3.md
**Ngày tạo:** 14/05/2026
**Tác giả:** QC Agent
**Phiên bản:** v3 

---

## 📊 Audit Summary

**Artefacts reviewed:** UC60-61_Chatbot.md (v1.3) + Wireframes (7 ảnh)

| # | Knowledge Area | Max Pts | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ Complete |
| 2 | Objective & Scope | 5 | 5/5 | ✅ Complete |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ Complete |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ Complete |
| 5 | UI Object Inventory & Mapping | 15 | 15/15 | ✅ Complete |
| 6 | Object Attributes & Behavior Definition | 20 | 20/20 | ✅ Complete |
| 7 | Functional Logic & Workflow Decomposition | 20 | 20/20 | ✅ Complete |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ Complete |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ Complete |
| 10 | Non-functional Requirements | 5 | 2/5 | ⚡ Partial |
| **Total** | | **110** | **107/110** | **97.3/100** |

> **Verdict: ✅ READY** (97.3/100) — QA có thể bắt đầu thiết kế test case.

---

## 📋 Unified Gap & Question Report (Remaining)

| ID | Priority | Ref | Câu hỏi / Gap | Why It Matters | Status |
|----|----------|-----|----------------|----------------|--------|
| Q2 | Low | Section 3.1 — Lazy load | **Page size do API AI quyết định** — không có fallback hay giới hạn tối thiểu để QA test được. | QA không thể test boundary page size. | Accepted |
| Q3 | Low | N/A (Missing) | **NFR còn thiếu:** Giới hạn số tin nhắn tối đa, performance khi lịch sử dài. | QA ghi nhận không test performance. | Accepted |

---

## 🟢 What's Good

- Đã update chuẩn theo Q&A v1.3: Bỏ chip gợi ý, bỏ đính kèm file (bot chỉ phản hồi plain text/list).
- Bổ sung Disclaimer miễn trừ trách nhiệm (AC11).
- Xử lý case câu hỏi "Ngoài phạm vi" logic rõ ràng.
- Logic đa ngôn ngữ (bot detect theo ngôn ngữ input) đã được confirm.

---

## 🧪 Testability Outlook

**CÓ THỂ test ngay:**
- Luồng Welcome → hội thoại.
- Input bar: max 500 ký tự, max 5 dòng.
- Send button: 3 trạng thái (ẩn / paper plane / spinner).
- Rating: 3 animation states + "Đánh giá lại?" + API reset.
- Back popup xác nhận rời chatbot.
- Error flow chuẩn CMR-07: lỗi mạng, HTTP 500, timeout 30s.
- Offline screen.
- Xử lý fallback & câu hỏi "Ngoài phạm vi".
- Lazy load khi scroll lên.
- Đa ngôn ngữ tự nhận diện đầu vào.

**Accepted dependencies (không test):**
- Page size lazy load, Performance/load test.

**Suggested test focus:**
- Boundary: 500 ký tự / 5 dòng.
- Concurrent: gửi tin → đang loading → thêm nội dung vào ô.
- Edge: "Đánh giá lại?" liên tục.
- Input khác ngôn ngữ hệ thống.

---

## 📝 Changelog

- **v3 (14/05/2026):**
  - Cập nhật điểm Readiness do BA đã hoàn thiện thiết kế UI/Object ở v1.3.
  - Xóa "Chip gợi ý" và "File đính kèm" khỏi scope test theo cập nhật v1.3.
  - Xóa Q1 khỏi báo cáo sau khi đã được dọn dẹp format `---`.
