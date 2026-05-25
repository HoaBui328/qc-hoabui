# BÁO CÁO KIỂM TRA ĐỘ SẴN SÀNG CỦA YÊU CẦU (READINESS AUDIT REPORT)

**Tài liệu:** UC257 — Đăng xuất ứng dụng Mobile
**Phiên bản đánh giá:** v2.7
**Ngày đánh giá:** 13/05/2026
**Ghi chú:** Tất cả 8 câu hỏi từ audit v2 đã được BA phản hồi và remediated vào v2.7. Đây là bản audit cuối cùng trước khi chuyển sang giai đoạn test design.

---

## 📊 Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 13/15 | ⚡ |
| 6 | Object Attributes & Behavior Definition | 20 | 18/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 19/20 | ⚡ |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | Non-functional Requirements | 5 | 5/5 | ✅ |
| **Total** | | **110** | **105/110** | **95.5/100** |

**Kết luận: ✅ READY** — QA có thể bắt đầu thiết kế test case. Các gap còn lại là Low priority, không block test design.

---

## 📋 Unified Gap & Question Report (Còn mở)

| ID | Priority | Ref | Question / Vấn đề | Why It Matters | Status |
|---|---|---|---|---|---|
| Q1 | Medium | Mục 2.1 Row 9 "Đổi mật khẩu" | Khi điều hướng từ Settings → UC253 (Đặt lại mật khẩu), người dùng **đã đang đăng nhập**. UC253 có bỏ qua bước xác thực OTP/Email hay không? Hay vẫn đi qua toàn bộ luồng quên mật khẩu (OTP → mật khẩu mới)? | Nếu bỏ qua OTP, QA cần test entry point khác với luồng quên mật khẩu thông thường. Nếu không bỏ qua, UX có vẻ bất hợp lý với người dùng đã đăng nhập. | Open |
| Q2 | Medium | Mục 2.1 Row 9 — Post-success auto-logout | Khi Đổi MK thành công → auto-logout: luồng này có gọi **SDK unregister** (FCM/APNS) và **API logout** không? Hay chỉ clear local data (Token, User Info, Cache)? | Nếu không gọi API logout, server token không bị revoke → các thiết bị khác vẫn còn phiên hoạt động. Cần làm rõ để QA thiết kế test case cho idempotent behavior. | Open |
| Q3 | Low | Mục 3.2 — Android Back button | Sau khi Đổi MK thành công và auto-logout (từ UC253), Android Back button có hành vi giống luồng logout thường không (không có hành động)? Cần ghi rõ vào section 3.2 để tránh bất ngờ khi test. | Nhất quán tài liệu; tránh tranh cãi khi kiểm thử Back button sau auto-logout từ Đổi MK. | Open |

---

## ✅ Gaps đã được đóng (từ audit v1 & v2)

| ID | Vấn đề ban đầu | Giải pháp | Phiên bản |
|---|---|---|---|
| v1-Q1 | Thiếu menu "Đổi mật khẩu" | Thêm row 9 "Đổi mật khẩu" → UC253 | v2.6 |
| v1-Q2 | Thứ tự menu sai so với wireframe | Reorder rows 7-10 theo wireframe | v2.6 |
| v1-Q3 | Dialog button sai (Danger thay vì Primary), thiếu focus mặc định | Đổi sang Button (Primary) "Xác nhận" + focus mặc định "Hủy" (CMR-10) | v2.6 |
| v1-Q4 | Thiếu mô tả Header (CMR-06) | Thêm ghi chú kiểu App Header vào row 1 | v2.6 |
| v2-Q1+Q2 | Thiếu post-success flow sau Đổi MK | Mô tả chi tiết: Toast → auto-logout → Login | v2.7 |
| v2-Q3 | Màu nền Avatar chưa định nghĩa | Bổ sung: Cố định màu brand (đỏ), follow Design System | v2.7 |
| v2-Q4 | SDK call fail behavior không rõ | Xác nhận silent fail, không log | v2.7 |
| v2-Q5 | Loading type sai (Overlay vs Button Loading) | Sửa thành Button Loading (spinner + disabled trên nút Xác nhận) | v2.7 |
| v2-Q6 | Toast duration chưa định nghĩa; 2 toast khác nhau | Thống nhất 1 toast "Đăng xuất thành công." (3 giây) cho mọi trường hợp | v2.7 |
| v2-Q7 | AC3 mâu thuẫn với logic 3.1 | Viết lại AC3: "gọi SDK không block logout" | v2.7 |
| v2-Q8 | Section 3.5 trùng lặp với bảng 2.1 | Xóa section 3.5 (DRY) | v2.7 |

---

## 🟢 What's Good

- Tài liệu v2.7 là bản **cực kỳ hoàn chỉnh** — một trong những UC được documented tốt nhất trong toàn bộ suite Mobile.
- Xử lý đầy đủ: SDK unregister song song, idempotent logout, CJK Avatar fallback, Outside Tap deliberate design, iOS gesture navigation.
- i18n 5 ngôn ngữ đầy đủ cho tất cả text cứng, bao gồm cả toast Đổi MK thành công.
- AC đã nhất quán với logic xử lý sau khi remediate AC3.
- Thống nhất 1 toast duy nhất cho mọi luồng logout (success + fallback) — đơn giản và nhất quán UX.

---

## 🧪 Testability Outlook

**What CAN be tested now (ngay lập tức):**
- Happy path: Dialog xác nhận → Button Loading → API logout → clear data → Toast 3s → Login screen.
- Fallback paths: Timeout 10s, lỗi mạng → cùng toast "Đăng xuất thành công." và hành vi dọn dẹp.
- Dialog behavior: Outside Tap không đóng, Android Back đóng, focus mặc định trên "Hủy" (CMR-10).
- Menu blur rules: Cá nhân ↔ Tổ chức (rows 7-8), "Đổi mật khẩu" không blur (row 9).
- Đổi MK post-success: Toast 3s "Đổi mật khẩu thành công..." → auto-logout → Login.
- Back button: Tại Cài đặt (→ Home), Dialog mở (→ đóng Dialog), sau logout (→ không action).
- Avatar: initial + màu brand đỏ; CJK/Emoji/null → icon mặc định.
- Tên truncate (>25 ký tự), Email truncate/null.
- i18n: chuyển ngôn ngữ → text toàn màn hình cập nhật (CMR-17).
- Debounce: double-tap "Đăng xuất" và "Xác nhận" (CMR-18).

**What CANNOT be tested yet (pending):**
- Entry point vào UC253 từ Settings: có bỏ qua OTP không (Q1).
- SDK/API call behavior trong Đổi MK auto-logout (Q2).

**Suggested test focus areas:**
- **CMR compliance:** CMR-10 (Dialog focus), CMR-17 (i18n), CMR-18 (debounce), CMR-16 (10s timeout).
- **Security tests:** Verify all local data is cleared after logout; verify token is revoked on other devices.
- **Partial failure tests:** SDK call fail → logout still completes; API 401 during logout → fallback behavior.
- **Multi-device tests:** Logout on device A → verify device B gets forced to Login.
- **Đổi MK flow:** Full flow from Settings → UC253 → success → auto-logout → Login.

---

## 📌 Summary & Recommendation

UC257 v2.7 đạt **95.5/100** — ✅ **READY**. Sau 3 vòng audit và remediation, tài liệu đã được nâng cấp đáng kể từ v2.5 (chưa có menu Đổi MK, Dialog sai CMR) lên v2.7 với đầy đủ logic cho tất cả các luồng. Còn 3 câu hỏi nhỏ (Q1-Q3) ở mức Medium/Low — không block test design nhưng nên được BA bổ sung trong sprint tiếp theo để hoàn thiện documentation.

**Đề xuất:** QA bắt đầu thiết kế test case ngay. Tập trung trước vào luồng logout chính, fallback flows, và menu blur rules. Chờ BA trả lời Q1-Q2 trước khi thiết kế test case cho tính năng Đổi MK từ Settings.
