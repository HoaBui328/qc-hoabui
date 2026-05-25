# Question Backlog — UC256: Đăng nhập ứng dụng Mobile

> **Document title:** UC256 Question Backlog
> **Date created:** 2026-05-19
> **Author:** QC Agent (qc-qna)
> **Version:** v1
>
> Generated: 2026-05-19
> Source files: docs/QC/uc-read/UC256/UC256_dang-nhap-mobile_audited_20260519_v1.md

---

## Open Questions

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | H | project-context-master §7.1: "Không giới hạn số lần nhập sai mật khẩu (BS-03)" vs UC256 §3.1: "5 lần sai liên tiếp → khóa 15 phút" | **Conflict BS-03 vs Account Lockout:** Project-level rule BS-03 nói không giới hạn nhập sai, nhưng UC256 mô tả lockout 5 lần. Cái nào đúng? UC256 đã override BS-03 hay BS-03 đã bị cập nhật? | QC không biết test lockout hay không. Nếu không có lockout → bỏ toàn bộ AC-21/AC-22 + security test. Nếu có → cần test chi tiết counter logic. | Open |
| Q2 | H | UC256 §2.2: "min 10, max 13 số" vs project-context §7.1: "CMND/CCCD 9 hoặc 12 số (BS-09)" | **Conflict format Mã định danh:** Spec yêu cầu min 10 số nhưng CMND cũ có 9 số. User có CMND 9 số có đăng nhập được không? Hay UC256 chỉ chấp nhận CCCD (12 số) + MST (10/13 số)? | Ảnh hưởng trực tiếp validation test cases. Nếu 9 số valid → min phải là 9, không phải 10. | Open |
| Q3 | M | UC256 §3.1 "Khóa tài khoản" | **Lockout scope:** Counter đếm sai là per-device hay per-account (cross-device)? User sai 3 lần trên device A, 2 lần trên device B → khóa hay không? | Ảnh hưởng test scenario multi-device. | Open |
| Q4 | M | UC256 §3.2 "Điều kiện hiển thị" | **Biometric điều kiện (a):** "đã đăng nhập thành công bằng mật khẩu trên thiết bị này ít nhất một lần" — nếu user clear app data hoặc reinstall app, điều kiện (a) reset? | Ảnh hưởng test data setup cho biometric scenarios. | Open |
| Q5 | M | UC256 §3.3 "Auto-create Account" | **VNeID auto-create:** Sau redirect UC252 với Mã ĐD auto-fill, user có bắt buộc hoàn tất đăng ký ngay không? Nếu user cancel UC252 → quay về đâu? | Ảnh hưởng test flow VNeID → UC252 → cancel. | Open |
| Q6 | M | UC256 §3.3 "Xử lý trùng" | **VNeID trùng số ĐD:** Lỗi hiển thị ở đâu? Toast hay popup? User có thể retry hay phải liên hệ hỗ trợ (dead-end)? | Ảnh hưởng test UX error recovery. | Open |
| Q7 | M | UC256 §2.2 Item 8 + §3.1 | **Loading overlay dismiss:** Khi API trả lỗi (401/5xx/timeout), loading overlay tự dismiss trước khi hiển thị toast? Hay toast hiển thị trên loading? | Ảnh hưởng test UI state transitions. | Open |
| Q8 | M | UC256 header table: "Tổ chức: MST" | **Phân biệt CN vs DN sau login:** Trang chủ DN có menu "Quản lý doanh nghiệp" — redirect logic dựa trên gì? Loại tài khoản lưu ở đâu? | Ảnh hưởng test navigation sau login cho 2 loại user. | Open |
| Q9 | M | N/A (Missing) | **Postcondition khi login fail:** Sau khi API trả 401, form state như thế nào? MĐD giữ nguyên? MK bị clear? Nút Đăng nhập vẫn Enabled? | Ảnh hưởng test form state sau error. | Open |
| Q10 | M | N/A (Missing) | **Platform-specific gap (mobile-native): App lifecycle** — User đang nhập MĐD/MK, app vào background (incoming call, switch app), quay lại foreground. Form data có giữ không? | Ảnh hưởng test mobile-specific scenario. Nếu data mất → UX issue. | Open |
| Q11 | M | N/A (Missing) | **Platform-specific gap (mobile-native): Hardware back (Android)** — Tại §2.2, nhấn hardware back button (Android) = tap nút Back trong header (quay §2.1)? Hay behavior khác? | Ảnh hưởng test Android-specific navigation. | Open |
| Q12 | M | N/A (Missing) | **Platform-specific gap (mobile-native): Biometric OS permission** — Nếu user chưa grant biometric permission cho app (hoặc đã revoke), Row Biometric hiển thị hay ẩn? Có thông báo hướng dẫn bật permission không? | Ảnh hưởng test biometric edge case. | Open |
| Q13 | L | N/A (Missing) | **Platform-specific gap (mobile-native): Safe-area insets** — Sticky bottom button "Đăng nhập" có respect safe-area (notch, home indicator) không? | Ảnh hưởng test UI trên thiết bị có notch/dynamic island. | Open |
| Q14 | L | N/A (Missing) | **Platform-specific gap (mobile-native): Accessibility** — Form fields có accessibility labels cho VoiceOver/TalkBack không? Dynamic Type support? | Ảnh hưởng accessibility testing. | Open |
| Q15 | L | N/A (Missing) | **Platform-specific gap (mobile-native): Offline startup** — Mở app khi không có mạng → hiển thị gì? Có cache login screen không? | Ảnh hưởng test offline scenario. | Open |
| Q16 | L | N/A (Missing) | **Platform-specific gap (mobile-native): Deep-link cold start** — Push notification khi chưa login → app mở → redirect login → sau login có redirect về target của push không? | Ảnh hưởng test push notification + login integration. | Open |
| Q17 | L | CMR-07, CMR-09, CMR-16, CMR-17, CMR-18 | **Common rules file BLOCKED:** CMR_Mobile.md không tồn tại trên disk. Không thể verify exact rule text. Spec inline đủ chi tiết nhưng có thể sai lệch. | Cần BA cung cấp lại CMR_Mobile.md để cross-check. | Open |

Priority: H = High (blocks design), M = Medium (affects scope), L = Low (nice to know)
Status: Open | Answered | Deferred

---

## Answered Questions

| ID | Priority | Ref | Question | Answer | Answered By | Date | Status |
|----|----------|-----|----------|--------|-------------|------|--------|

---

## Deferred Questions

| ID | Priority | Ref | Question | Reason | Deferred By | Date | Status |
|----|----------|-----|----------|--------|-------------|------|--------|
