# UC Readiness Review — UC256: Đăng nhập ứng dụng Mobile
**Functional / Black-box Test Readiness Report**

**Document title:** UC256 Readiness Review Report
**Date created:** 2026-05-19
**Author:** QC Agent (qc-uc-read)
**Version:** v1

---

## Feature Brief

UC256 mô tả chức năng đăng nhập ứng dụng Mobile của Cổng một cửa đầu tư Quốc gia, cho phép người dùng (cá nhân hoặc tổ chức) xác thực bằng 3 phương thức: (1) Mã định danh + Mật khẩu, (2) Sinh trắc học (FaceID/Vân tay), (3) VNeID (deep-link sang app bên thứ ba). Spec v2.5 bao gồm 2 màn hình (Chọn phương thức + Form đăng nhập), validation chi tiết, account lockout 5 lần, biometric exception handling, VNeID auto-create account, và đa ngôn ngữ. Spec chất lượng cao về mặt UI behavior và error flows, nhưng có conflict với project-level rule BS-03 về lockout policy và thiếu một số platform-specific behaviors cho mobile-native.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| **77.7 / 100** | ⚠️ **CONDITIONALLY READY** |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC256 | Đăng nhập ứng dụng Mobile | v2.5 | In Review |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| huy.lai2 | - | 2026-04-29 | 2026-05-14 |

---

## 1. Objective & Scope

### 1.1 Objective
Cho phép người dùng (NĐT cá nhân hoặc tổ chức) đăng nhập vào ứng dụng di động Cổng một cửa đầu tư Quốc gia để truy cập các dịch vụ yêu cầu xác thực (quản lý hồ sơ, đặt lịch, phản ánh, thông báo).

### 1.2 In Scope
- Đăng nhập bằng Mã định danh (CMND/CCCD/MST) + Mật khẩu
- Đăng nhập bằng Sinh trắc học (FaceID/Vân tay)
- Đăng nhập qua VNeID (deep-link sang app VNeID)
- Validation on-blur cho form fields
- Account lockout (5 lần sai → khóa 15 phút)
- Đa ngôn ngữ (VI/EN/ZH/JA/KO)
- Error handling (401, 5xx, timeout, mất mạng)

### 1.3 Out of Scope
- Đăng ký tài khoản (UC252)
- Quên mật khẩu (UC253)
- Cấu hình sinh trắc học (UC254)
- Đăng xuất (UC257)

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| NĐT Cá nhân (CN) | Primary | Đăng nhập bằng CMND/CCCD (9/12 số) hoặc VNeID. Sau login → Trang chủ NĐT CN. |
| NĐT Doanh nghiệp (DN) | Primary | Đăng nhập bằng MST (10/13 số). VNeID không áp dụng. Sau login → Trang chủ có menu "Quản lý doanh nghiệp". |
| Guest (chưa đăng nhập) | Trigger | Mở app → màn hình đăng nhập hiển thị mặc định. |
| VNeID App | System (External) | Xác thực danh tính qua deep-link, trả callback token. |
| Backend API | System | Xử lý xác thực, trả token, quản lý lockout counter. |

⚡ **Partial:** Thiếu chi tiết redirect logic phân biệt CN vs DN sau đăng nhập thành công. Không rõ NĐT nước ngoài có phải actor riêng không.

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Thiết bị đã cài đặt ứng dụng.
- Thiết bị có kết nối mạng ổn định.
- *(inferred)* Tài khoản người dùng đã được tạo và ở trạng thái active (không bị khóa vĩnh viễn).

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Login thành công (MĐD/MK hoặc Biometric hoặc VNeID) | Token lưu Secure Storage. Session active. Điều hướng Trang chủ. Ngôn ngữ server override local. |
| Login thất bại (401) | ⚠️ **Missing** — spec không mô tả rõ system state sau fail (token cũ có bị xóa? form reset?) |
| Account lockout | Tài khoản khóa 15 phút. Counter reset về 0 sau 15 phút. |

⚡ **Partial:** Thiếu postcondition khi thất bại. Thiếu precondition về trạng thái tài khoản (active/suspended/locked).

---

## 4. UI Object Inventory & Mapping

### §2.1 — Màn hình Chọn phương thức đăng nhập

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | §2.1 Header | Language Switcher (icon quả địa cầu + "VI") | Button (Icon) | - | "VI" | - | VI, EN, ZH, JA, KO | Góc phải trên cùng. Tap → Bottom Sheet chọn ngôn ngữ. | Chọn cách đăng nhập (1).png [BLOCKED] |
| 2 | §2.1 Header | Logo hệ thống | Image | - | - | - | - | Không tương tác. | Chọn cách đăng nhập (1).png [BLOCKED] |
| 3 | §2.1 Header | "Cổng một cửa đầu tư Quốc gia" | Label | - | - | - | - | Không tương tác. Wrap xuống dòng. | Chọn cách đăng nhập (1).png [BLOCKED] |
| 4 | §2.1 Header | "Đăng nhập" | Label (Title) | - | - | - | - | Font to, đậm, màu trắng. | Chọn cách đăng nhập (1).png [BLOCKED] |
| 5 | §2.1 Header | "Chọn phương thức đăng nhập" | Label (Subtitle) | - | - | - | - | Font nhỏ hơn, màu trắng. | Chọn cách đăng nhập (1).png [BLOCKED] |
| 6 | §2.1 Body | Card "Đăng nhập" | Card | - | - | - | - | Icon user hồng + "Đăng nhập" + "Sử dụng mã định danh và mật khẩu". Tap → §2.2. | Chọn cách đăng nhập (1).png [BLOCKED] |
| 7 | §2.1 Body | Card "Đăng nhập với VNeID" | Card | - | - | - | - | Logo VNeID + tiêu đề + phụ đề dịch vụ công. Tap → deep-link/Store. | Chọn cách đăng nhập (1).png [BLOCKED] |
| 8 | §2.1 Footer | "Đăng ký tài khoản" | Link (Red) | - | - | - | - | Dưới divider "hoặc". Tap → UC252. | Chọn cách đăng nhập (1).png [BLOCKED] |
| 9 | §2.1 Footer | "Quên mật khẩu" | Link (Grey) | - | - | - | - | Cạnh link Đăng ký. Tap → UC253. | Chọn cách đăng nhập (1).png [BLOCKED] |
| 10 | §2.1 Footer | Banner bảo mật | Container | - | - | - | - | Icon bảo mật + text cam kết. Không tương tác. | Chọn cách đăng nhập (1).png [BLOCKED] |

### §2.2 — Màn hình Đăng nhập Mã định danh

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|---|---|---|---|---|---|---|---|---|
| 11 | §2.2 Header | Nút Back (←) + "Đăng nhập Nhà đầu tư" | Component (Header) | - | - | - | - | Nền đỏ. Tap Back → §2.1. | Đăng nhập bằng mã định danh, faceID.png [BLOCKED] |
| 12 | §2.2 Form | "Mã định danh*" | Textbox (Numeric) | Yes | - | "Nhập mã định danh của bạn" | - | Icon thẻ. Bàn phím numeric. Max 13 ký tự số. Auto-trim (CMR-09). | Đăng nhập bằng mã định danh, faceID.png [BLOCKED] |
| 13 | §2.2 Form | "Mật khẩu*" | Password Input | Yes | - | "Nhập mật khẩu" | - | Icon mắt toggle. Max 50 ký tự. KHÔNG trim (CMR-09 loại trừ). | Đăng nhập bằng mã định danh, faceID.png [BLOCKED] |
| 14 | §2.2 Form | "Quên mật khẩu?" | Link (Red) | - | - | - | - | Dưới trường Mật khẩu. Tap → UC253. | Đăng nhập bằng mã định danh, faceID.png [BLOCKED] |
| 15 | §2.2 Form | Row Biometric ("Đăng nhập bằng Face ID" / "Đăng nhập bằng Vân tay") | Row (Icon+Text) | - | - | - | - | Conditional display: (a) + (b). Tap → OS Biometric Prompt. | Đăng nhập bằng mã định danh, faceID.png [BLOCKED] |
| 16 | §2.2 Footer | "Chưa có tài khoản?" | Label (Divider) | - | - | - | - | Đường gạch ngang + text xám. Không tương tác. | Đăng nhập bằng mã định danh, faceID.png [BLOCKED] |
| 17 | §2.2 Footer | "Đăng ký tài khoản mới" | Button (Outline) | - | - | - | - | Viền xám, nền trắng. Luôn enabled. Debounce (CMR-18). Tap → UC252. | Đăng nhập bằng mã định danh, faceID.png [BLOCKED] |
| 18 | §2.2 Sticky Bottom | "Đăng nhập" | Button (Primary) | - | - | - | - | Nền đỏ/xám. Sticky bottom. Disabled/Enabled theo CMR-09. Debounce (CMR-18). | Đăng nhập bằng mã định danh, faceID.png [BLOCKED] |

⚡ **Partial:** Wireframe BLOCKED. Có thể thiếu: Bottom Sheet ngôn ngữ (UI chi tiết), Loading overlay component, Toast component, Popup biometric khóa.

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|---------------------------------------------|
| Language Switcher | Enabled (luôn hiển thị) | Tap → Mở Bottom Sheet | Chọn ngôn ngữ → đóng Bottom Sheet, cập nhật tức thì toàn bộ nhãn/placeholder/thông báo lỗi trên màn hình. |
| Logo hệ thống | Enabled (static) | N/A | Không thay đổi. |
| Tên hệ thống | Enabled (static) | N/A | Cập nhật theo ngôn ngữ đã chọn. |
| Tiêu đề "Đăng nhập" | Enabled (static) | N/A | Cập nhật theo ngôn ngữ. |
| Phụ đề | Enabled (static) | N/A | Cập nhật theo ngôn ngữ. |
| Card "Đăng nhập" | Enabled | Tap → Navigate §2.2 | Không thay đổi state. |
| Card "Đăng nhập với VNeID" | Enabled | Tap → Deep-link VNeID / Store | Nếu VNeID đã cài → mở app. Chưa cài → Store. Sau VNeID callback: token → login hoặc redirect UC252 (auto-create) hoặc lỗi trùng. |
| Link "Đăng ký tài khoản" | Enabled | Tap → Navigate UC252 | Không thay đổi state. |
| Link "Quên mật khẩu" | Enabled | Tap → Navigate UC253 | Không thay đổi state. |
| Banner bảo mật | Enabled (static) | N/A | Không thay đổi. |
| Header Back button | Enabled | Tap → Navigate §2.1 | Không thay đổi state. |
| Mã định danh (Textbox) | Enabled. Auto-trim khoảng trắng đầu/cuối (CMR-09). | Tap → bàn phím numeric. On-blur → validate. | Trống/chỉ khoảng trắng → inline error "Vui lòng nhập Mã định danh". <10 số → "Sai định dạng." >13 số → block nhập. Ký tự không phải số → "Mã định danh chỉ gồm các số 0-9." Khi valid → clear error, re-evaluate nút Đăng nhập state. |
| Mật khẩu (Password) | Enabled. KHÔNG trim (CMR-09 loại trừ). Max 50 ký tự (block >50). | Tap → nhập. On-blur → validate. Tap icon mắt → toggle show/hide. | Trống → inline error "Vui lòng nhập Mật khẩu". Khi valid → clear error, re-evaluate nút Đăng nhập state. |
| Link "Quên mật khẩu?" (§2.2) | Enabled | Tap → Navigate UC253 | Không thay đổi state. |
| Row Biometric | Hidden (default). Visible khi: (a) user đã login thành công bằng MK ≥1 lần trên thiết bị VÀ (b) đã bật sinh trắc trong UC254. Disabled khi OS khóa biometric (5 lần fail OS). | Tap (khi Visible + Enabled) → OS Biometric Prompt | Thành công → auto login. Fail → toast. Cancel → focus Mã định danh. OS khóa → popup + Disabled. Reset: login bằng MK thành công → Enabled lại. |
| Divider "Chưa có tài khoản?" | Enabled (static) | N/A | Không thay đổi. |
| Nút "Đăng ký tài khoản mới" | Enabled (luôn) | Tap → Navigate UC252. Debounce (CMR-18). | Không thay đổi state. |
| Nút "Đăng nhập" | **Disabled** (nền xám) khi ≥1 trường bắt buộc trống hoặc có lỗi validation. **Enabled** (nền đỏ) khi tất cả trường hợp lệ (CMR-09). Sticky bottom. | Tap (khi Enabled) → Loading overlay → API call. Debounce (CMR-18). | API 200 → lưu token → Trang chủ. API 401 → toast lỗi. 5xx → toast "Hệ thống đang bận". Timeout >10s → toast + "Thử lại". Mất mạng → toast + "Thử lại". 5 lần sai → toast khóa TK. |

⚡ **Partial — Platform-specific gaps:**
- Platform-specific gap (mobile-native): App lifecycle — form-draft persistence khi app vào background không addressed.
- Platform-specific gap (mobile-native): Hardware back button (Android) tại §2.2 không explicit (chỉ có nút Back trong header).
- Platform-specific gap (mobile-native): Safe-area insets cho sticky bottom button không addressed.
- Platform-specific gap (mobile-native): Accessibility labels (VoiceOver/TalkBack) cho form fields không addressed.

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function: Đăng nhập Mã định danh + Mật khẩu

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | User | Nhập Mã định danh | Bàn phím numeric mở. Auto-trim khoảng trắng. | - | On-blur: trống → "Vui lòng nhập Mã định danh"; <10 số → "Sai định dạng."; >13 → block; non-numeric → "Mã định danh chỉ gồm các số 0-9." |
| 2 | User | Nhập Mật khẩu | Ký tự masked. Max 50. | Tap icon mắt → toggle show/hide | On-blur: trống → "Vui lòng nhập Mật khẩu" |
| 3 | System | Evaluate form validity | Nút "Đăng nhập" Enabled (CMR-09) | Nếu có lỗi → Disabled | - |
| 4 | User | Tap "Đăng nhập" | Loading overlay hiển thị. API call. Debounce (CMR-18). | - | - |
| 5 | System | API response 200 | Lưu token Secure Storage. Điều hướng Trang chủ. Apply ngôn ngữ server (override local, không thông báo). | - | 401 → Toast: "Mã định danh hoặc mật khẩu không đúng. Vui lòng thử lại." |
| 5a | System | API response 5xx | - | - | Toast: "Hệ thống đang bận. Vui lòng thử lại sau." (CMR-07) |
| 5b | System | Timeout >10s | - | - | Toast: "Yêu cầu đã hết thời gian chờ. Vui lòng thử lại." + Nút "Thử lại" (CMR-16) |
| 5c | System | Mất mạng | - | - | Toast: "Không thể kết nối. Vui lòng kiểm tra mạng và thử lại." + Nút "Thử lại" |
| 5d | System | 5 lần sai liên tiếp | - | - | Toast: "Tài khoản đã bị tạm khóa do nhập sai nhiều lần. Vui lòng thử lại sau 15 phút." Counter reset sau 15 phút. |

**B. Business Rules & Validations**

| Field / Object | Required | Format / Constraint | Min / Max | Error Message (exact text) |
|----------------|----------|---------------------|-----------|----------------------------|
| Mã định danh | Yes | Chỉ số 0-9. Auto-trim. Block >13. | 10 / 13 ký tự số | "Vui lòng nhập Mã định danh" / "Sai định dạng." / "Mã định danh chỉ gồm các số 0-9." |
| Mật khẩu | Yes | Mọi ký tự. KHÔNG trim. Block >50. | 1 / 50 ký tự | "Vui lòng nhập Mật khẩu" |
| Nút Đăng nhập | - | Disabled khi form invalid; Enabled khi valid (CMR-09) | - | - |
| Account Lockout | - | 5 lần sai MĐD/MK liên tiếp → khóa 15 phút. Không tính biometric. VNeID không ảnh hưởng. | - | "Tài khoản đã bị tạm khóa do nhập sai nhiều lần. Vui lòng thử lại sau 15 phút." |

**C. UI/UX Feedback**
- **Loading States:** Loading overlay khi gọi API đăng nhập.
- **Toast Messages:** 401 / 5xx / Timeout / Mất mạng / Lockout (xem bảng trên).
- **Nút "Thử lại":** Hiển thị kèm toast cho Timeout và Mất mạng.

### 6.2 Function: Sinh trắc học (Biometric)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | User | Tap Row Biometric | OS Biometric Prompt hiển thị | - | - |
| 2 | OS | Nhận diện thành công | Callback → App auto login → Trang chủ | User cancel → quay form, focus Mã định danh | Sai mặt/vân tay → OS prompt đóng → App toast: "Không nhận diện được, vui lòng thử lại." |
| 2a | OS | 5 lần fail | - | - | Popup: "Sinh trắc học đã bị khóa do đã nhận diện sai 5 lần. Vui lòng đăng nhập bằng mật khẩu hoặc thử lại sau 15 phút." Row Biometric → Disabled. |

**Điều kiện hiển thị Row Biometric:**
- (a) User đã login thành công bằng MK ≥1 lần trên thiết bị này.
- (b) User đã bật sinh trắc trong UC254.
- Cả 2 phải thỏa mãn đồng thời.

**Reset sau khóa OS:** Login thành công bằng MK → Row Biometric Enabled lại.

### 6.3 Function: VNeID (Deep-link)

**A. Workflows**

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | User | Tap Card VNeID (§2.1) | Kiểm tra app VNeID | App chưa cài → Store | - |
| 2 | System | Mở VNeID deep-link | VNeID app mở | - | - |
| 3 | User | Xác thực trong VNeID | VNeID callback token | User bỏ dở (force-close/Back) → App quay §2.1, không loading/timeout | - |
| 4 | System | Nhận token, ánh xạ TK | Login thành công → Trang chủ | Số ĐD chưa có TK → redirect UC252, auto-fill Mã ĐD | Số ĐD đã liên kết TK khác → Lỗi: "Số định danh này đã được đăng ký. Vui lòng liên hệ hỗ trợ để được giải quyết." |

### 6.4 Function: Đa ngôn ngữ (CMR-17)

- Ngôn ngữ mặc định: theo cài đặt thiết bị.
- Đổi ngôn ngữ: Language Switcher → Bottom Sheet (VI/EN/ZH/JA/KO) → cập nhật tức thì.
- Sau đăng nhập: server override local (không thông báo).

⚡ **Partial — Platform-specific gaps:**
- Platform-specific gap (mobile-native): Form-draft persistence khi app background không addressed.
- Platform-specific gap (mobile-native): Offline startup behavior không addressed.
- Platform-specific gap (mobile-native): Biometric OS permission denied flow không addressed.

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| Login thành công (MĐD/MK) | Token lưu Secure Storage → unlock toàn bộ module yêu cầu đăng nhập (UC42-54, UC258-259). Trang chủ (UC1) hiển thị Quick Access + Badge thông báo. | Verify token tồn tại sau login. Verify Trang chủ load đúng role (CN vs DN). |
| Login thành công (Biometric) | Tương tự MĐD/MK — auto login không qua API form. | Verify token giống như login MĐD/MK. Verify session valid. |
| Login thành công (VNeID) | Token từ VNeID callback → ánh xạ tài khoản. Nếu chưa có TK → redirect UC252 với Mã ĐD auto-fill. | Verify Mã ĐD auto-fill đúng tại UC252. Verify token valid sau VNeID flow. |
| Account lockout (5 lần sai) | Tài khoản khóa 15 phút. VNeID KHÔNG bị ảnh hưởng (counter riêng). Biometric KHÔNG tính vào counter. | Verify VNeID vẫn login được khi TK bị khóa MĐD/MK. Verify counter reset sau 15 phút. |
| Đổi ngôn ngữ trước login | Cập nhật tức thì toàn bộ UI. Sau login, server override. | Verify ngôn ngữ server ghi đè local. Verify không có thông báo chuyển ngôn ngữ. |
| Biometric OS khóa (5 lần fail) | Row Biometric Disabled. User phải login bằng MK. Sau login MK thành công → Row Biometric Enabled lại. | Verify Row Biometric state sau login MK thành công. |
| VNeID bỏ dở | App quay §2.1. Không loading, không timeout. User có thể chọn lại. | Verify app state clean (không có pending request). |
| Đổi MK (UC249, BS-07) | Sau đổi MK bắt buộc đăng xuất → token invalidate → redirect login. | Verify token cũ invalid. Verify login lại bằng MK mới thành công. |

⚡ **Partial:** Thiếu integration analysis cho: (1) Push notification registration sau login. (2) Token lifecycle (expiry, refresh). (3) Multi-device login. (4) Deep-link cold start khi chưa login.

---

## 8. Acceptance Criteria

| AC # | Scenario | Given (precondition) | When (user action) | Then (expected result) |
|------|----------|----------------------|--------------------|-----------------------|
| AC-01 | §2.1 Language Switcher | User ở màn hình §2.1 | Tap Language Switcher | Bottom Sheet mở với 5 ngôn ngữ (VI/EN/ZH/JA/KO). Chọn → cập nhật nhãn. |
| AC-02 | §2.1 Card Đăng nhập | User ở màn hình §2.1 | Tap Card "Đăng nhập" | Chuyển sang §2.2. |
| AC-03 | §2.1 VNeID — có app | User ở §2.1, VNeID đã cài | Tap Card VNeID | Mở app VNeID. |
| AC-04 | §2.1 VNeID — chưa cài | User ở §2.1, VNeID chưa cài | Tap Card VNeID | Điều hướng Store. |
| AC-05 | §2.1 Link Đăng ký | User ở §2.1 | Tap "Đăng ký tài khoản" | Điều hướng UC252. |
| AC-06 | §2.1 Link Quên MK | User ở §2.1 | Tap "Quên mật khẩu" | Điều hướng UC253. |
| AC-07 | Validation MĐD — trống | User ở §2.2, MĐD trống | Focus out (on-blur) | Inline error: "Vui lòng nhập Mã định danh" |
| AC-08 | Validation MĐD — <10 số | User nhập 9 số | Focus out | Inline error: "Sai định dạng." |
| AC-09 | Validation MĐD — block >13 | User nhập 13 số | Nhập ký tự thứ 14 | Hệ thống block, không nhận thêm. |
| AC-10 | Validation MĐD — non-numeric | User nhập chữ/ký tự đặc biệt | Focus out | Inline error: "Mã định danh chỉ gồm các số 0-9." |
| AC-11 | Validation MK — trống | User ở §2.2, MK trống | Focus out | Inline error: "Vui lòng nhập Mật khẩu" |
| AC-12 | Toggle MK | User ở §2.2 | Tap icon mắt | Mật khẩu ẩn/hiện toggle. |
| AC-13 | Max 50 ký tự MK | User nhập 50 ký tự | Nhập ký tự thứ 51 | Block, không nhận thêm. |
| AC-14 | Nút Đăng nhập Disabled | Form có lỗi hoặc trường trống | Observe | Nút Disabled (nền xám, không tương tác). |
| AC-15 | Nút Đăng nhập Enabled | Tất cả trường hợp lệ | Observe | Nút Enabled (nền đỏ, có thể tap). |
| AC-16 | Login thành công | MĐD + MK hợp lệ, API 200 | Tap Đăng nhập | Loading overlay → Lưu token → Trang chủ. |
| AC-17 | Login thất bại 401 | MĐD hoặc MK sai | Tap Đăng nhập | Toast: "Mã định danh hoặc mật khẩu không đúng. Vui lòng thử lại." |
| AC-18 | Login 5xx | Server error | Tap Đăng nhập | Toast: "Hệ thống đang bận. Vui lòng thử lại sau." |
| AC-19 | Timeout >10s | API không phản hồi >10s | Tap Đăng nhập | Toast: "Yêu cầu đã hết thời gian chờ. Vui lòng thử lại." + Nút "Thử lại". |
| AC-20 | Mất mạng | Không có kết nối | Tap Đăng nhập | Toast: "Không thể kết nối. Vui lòng kiểm tra mạng và thử lại." + Nút "Thử lại". |
| AC-21 | Account lockout | 5 lần sai liên tiếp | Lần thứ 5 fail | Toast: "Tài khoản đã bị tạm khóa do nhập sai nhiều lần. Vui lòng thử lại sau 15 phút." |
| AC-22 | Lockout counter reset | TK bị khóa 15 phút | Sau 15 phút | TK mở khóa. Counter reset về 0. |
| AC-23 | Biometric hiển thị đúng | (a) đã login MK ≥1 lần + (b) bật sinh trắc UC254 | Mở §2.2 | Row Biometric visible. |
| AC-24 | Biometric thành công | Row Biometric visible + enabled | Tap → OS nhận diện OK | Auto login → Trang chủ. |
| AC-25 | Biometric fail | OS nhận diện sai | OS prompt đóng | Toast: "Không nhận diện được, vui lòng thử lại." |
| AC-26 | Biometric cancel | User cancel OS prompt | Cancel | Quay form, focus Mã định danh. |
| AC-27 | Biometric OS khóa | 5 lần fail OS | Lần thứ 5 | Popup thông báo + Row Biometric Disabled. |
| AC-28 | Biometric reset | Row Biometric Disabled | Login MK thành công | Row Biometric Enabled lại. |
| AC-29 | Sticky bottom | Nội dung dài | Scroll | Nút "Đăng nhập" cố định dưới cùng. |
| AC-30 | Debounce | User double-tap nhanh | Double-tap "Đăng nhập" | Chỉ trigger 1 lần. |
| AC-31 | VNeID auto-create | Số ĐD từ VNeID chưa có TK | VNeID callback | Redirect UC252, Mã ĐD auto-fill. |
| AC-32 | VNeID trùng | Số ĐD đã liên kết TK khác | VNeID callback | Lỗi: "Số định danh này đã được đăng ký. Vui lòng liên hệ hỗ trợ để được giải quyết." |
| AC-33 | VNeID bỏ dở | User force-close VNeID / Back | Quay app | App quay §2.1, không loading/timeout. Có thể chọn lại. |
| AC-34 | Language override | User chọn EN trước login, TK lưu VI trên server | Login thành công | UI chuyển sang VI, không thông báo. |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| Security | Jailbreak/Root detection: **Không chặn** đăng nhập trên thiết bị root/jailbreak. | NFR-SEC-01 |
| Security | Screenshot prevention: **Không block** screenshot trên màn hình có mật khẩu. | NFR-SEC-02 |
| Security | Certificate Pinning: **Không** kiểm tra SSL certificate pinning. | NFR-SEC-03 |
| Performance | ⚠️ **Missing** — Không có target response time cho API đăng nhập. | - |
| Compatibility | ⚠️ **Missing** — Không có min OS version (iOS/Android), device matrix. | - |
| Accessibility | ⚠️ **Missing** — Không có VoiceOver/TalkBack labels, Dynamic Type support. | - |
| Offline/Cache | ⚠️ **Missing** — Không có offline policy cho login screen (cache form state?). | Platform-specific gap (mobile-native) |

⚡ **Partial:** NFR section chỉ liệt kê những gì KHÔNG làm. Thiếu positive NFR targets.

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions

*(Xem Unified Gap & Question Report trong Audit Summary bên dưới)*

### 10.2 Dependencies

| Dependency | Type | Impact |
|---|---|---|
| VNeID App (external) | Integration (deep-link) | Phụ thuộc OS routing + app VNeID cài đặt. High risk. |
| UC252 — Đăng ký tài khoản | Navigation + Data | VNeID auto-create redirect. Link "Đăng ký". |
| UC253 — Quên mật khẩu | Navigation | Link "Quên mật khẩu?". |
| UC254 — Cấu hình sinh trắc | Data dependency | Điều kiện (b) hiển thị Row Biometric. |
| Backend Auth API | System | Xử lý login, lockout counter, token. |
| Secure Storage (Keychain/Keystore) | Client storage | Lưu token (BS-04). |
| OS Biometric API (FaceID/TouchID) | System (OS) | Biometric prompt + callback. |

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1 | 2026-05-19 | QC Agent (qc-uc-read) | First audit of UC256 v2.5. Score 77.7/100. Conditionally Ready. |

---

## Audit Summary

### Audit Summary Table

| # | Knowledge Area | Max Pts | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity (title, ID, context) | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 8/10 | ⚡ |
| 4 | Preconditions & Postconditions | 10 | 7/10 | ⚡ |
| 5 | UI Object Inventory & Mapping | 15 | 12/15 | ⚡ |
| 6 | Object Attributes & Behavior Definition | 20 | 15/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 16/20 | ⚡ |
| 8 | Functional Integration Analysis | 20 | 14/20 | ⚡ |
| 9 | Acceptance Criteria | 20 | 17/20 | ⚡ |
| 10 | Non-functional Requirements | 5 | 2/5 | ⚡ |
| **Total** | | **130** | **101/130** | **77.7/100** |

**Verdict:** ⚠️ **CONDITIONALLY READY** — QA có thể bắt đầu thiết kế test cho các area rõ ràng; các gap cần BA fix song song.

---

### Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|---|---|---|---|---|---|
| Q1 | 🔴 High | project-context-master §7.1: "Không giới hạn số lần nhập sai mật khẩu (BS-03)" vs UC256 §3.1: "5 lần sai liên tiếp → khóa 15 phút" | **Conflict BS-03 vs Account Lockout:** Project-level rule BS-03 nói không giới hạn nhập sai, nhưng UC256 mô tả lockout 5 lần. Cái nào đúng? UC256 đã override BS-03 hay BS-03 đã bị cập nhật? | QC không biết test lockout hay không. Nếu không có lockout → bỏ toàn bộ AC-21/AC-22 + security test. Nếu có → cần test chi tiết counter logic. | Open |
| Q2 | 🔴 High | UC256 §2.2: "min 10, max 13 số" vs project-context §7.1: "CMND/CCCD 9 hoặc 12 số (BS-09)" | **Conflict format Mã định danh:** Spec yêu cầu min 10 số nhưng CMND cũ có 9 số. User có CMND 9 số có đăng nhập được không? Hay UC256 chỉ chấp nhận CCCD (12 số) + MST (10/13 số)? | Ảnh hưởng trực tiếp validation test cases. Nếu 9 số valid → min phải là 9, không phải 10. | Open |
| Q3 | Medium | UC256 §3.1 "Khóa tài khoản" | **Lockout scope:** Counter đếm sai là per-device hay per-account (cross-device)? User sai 3 lần trên device A, 2 lần trên device B → khóa hay không? | Ảnh hưởng test scenario multi-device. | Open |
| Q4 | Medium | UC256 §3.2 "Điều kiện hiển thị" | **Biometric điều kiện (a):** "đã đăng nhập thành công bằng mật khẩu trên thiết bị này ít nhất một lần" — nếu user clear app data hoặc reinstall app, điều kiện (a) reset? | Ảnh hưởng test data setup cho biometric scenarios. | Open |
| Q5 | Medium | UC256 §3.3 "Auto-create Account" | **VNeID auto-create:** Sau redirect UC252 với Mã ĐD auto-fill, user có bắt buộc hoàn tất đăng ký ngay không? Nếu user cancel UC252 → quay về đâu? | Ảnh hưởng test flow VNeID → UC252 → cancel. | Open |
| Q6 | Medium | UC256 §3.3 "Xử lý trùng" | **VNeID trùng số ĐD:** Lỗi hiển thị ở đâu? Toast hay popup? User có thể retry hay phải liên hệ hỗ trợ (dead-end)? | Ảnh hưởng test UX error recovery. | Open |
| Q7 | Medium | UC256 §2.2 Item 8 + §3.1 | **Loading overlay dismiss:** Khi API trả lỗi (401/5xx/timeout), loading overlay tự dismiss trước khi hiển thị toast? Hay toast hiển thị trên loading? | Ảnh hưởng test UI state transitions. | Open |
| Q8 | Medium | UC256 header table: "Tổ chức: MST" | **Phân biệt CN vs DN sau login:** Trang chủ DN có menu "Quản lý doanh nghiệp" — redirect logic dựa trên gì? Loại tài khoản lưu ở đâu? | Ảnh hưởng test navigation sau login cho 2 loại user. | Open |
| Q9 | Medium | N/A (Missing) | **Postcondition khi login fail:** Sau khi API trả 401, form state như thế nào? MĐD giữ nguyên? MK bị clear? Nút Đăng nhập vẫn Enabled? | Ảnh hưởng test form state sau error. | Open |
| Q10 | Medium | N/A (Missing) | **Platform-specific gap (mobile-native): App lifecycle** — User đang nhập MĐD/MK, app vào background (incoming call, switch app), quay lại foreground. Form data có giữ không? | Ảnh hưởng test mobile-specific scenario. Nếu data mất → UX issue. | Open |
| Q11 | Medium | N/A (Missing) | **Platform-specific gap (mobile-native): Hardware back (Android)** — Tại §2.2, nhấn hardware back button (Android) = tap nút Back trong header (quay §2.1)? Hay behavior khác? | Ảnh hưởng test Android-specific navigation. | Open |
| Q12 | Medium | N/A (Missing) | **Platform-specific gap (mobile-native): Biometric OS permission** — Nếu user chưa grant biometric permission cho app (hoặc đã revoke), Row Biometric hiển thị hay ẩn? Có thông báo hướng dẫn bật permission không? | Ảnh hưởng test biometric edge case. | Open |
| Q13 | Low | N/A (Missing) | **Platform-specific gap (mobile-native): Safe-area insets** — Sticky bottom button "Đăng nhập" có respect safe-area (notch, home indicator) không? | Ảnh hưởng test UI trên thiết bị có notch/dynamic island. | Open |
| Q14 | Low | N/A (Missing) | **Platform-specific gap (mobile-native): Accessibility** — Form fields có accessibility labels cho VoiceOver/TalkBack không? Dynamic Type support? | Ảnh hưởng accessibility testing. | Open |
| Q15 | Low | N/A (Missing) | **Platform-specific gap (mobile-native): Offline startup** — Mở app khi không có mạng → hiển thị gì? Có cache login screen không? | Ảnh hưởng test offline scenario. | Open |
| Q16 | Low | N/A (Missing) | **Platform-specific gap (mobile-native): Deep-link cold start** — Push notification khi chưa login → app mở → redirect login → sau login có redirect về target của push không? | Ảnh hưởng test push notification + login integration. | Open |
| Q17 | Low | CMR-07, CMR-09, CMR-16, CMR-17, CMR-18 | **Common rules file BLOCKED:** CMR_Mobile.md không tồn tại trên disk. Không thể verify exact rule text. Spec inline đủ chi tiết nhưng có thể sai lệch. | Cần BA cung cấp lại CMR_Mobile.md để cross-check. | Open |

---

### 🟢 What's Good

- **UI behavior chi tiết xuất sắc:** Mỗi element có Quy tắc hiển thị + Quy tắc hành động rõ ràng, validation on-blur với exact error messages.
- **Error flows đầy đủ:** 401, 5xx, timeout, mất mạng, lockout — tất cả có toast message cụ thể.
- **Biometric handling tốt:** 3 exception flows (fail, cancel, OS lock) với behavior rõ ràng, bao gồm cả reset mechanism.
- **VNeID integration rõ:** Happy path + auto-create + trùng + bỏ dở — cover đủ scenarios.
- **Acceptance Criteria phong phú:** 25 AC items trong spec gốc, measurable và verifiable.
- **Changelog chi tiết:** 12 versions với before/after tracking, cho thấy spec đã qua nhiều vòng review.

---

### 🧪 Testability Outlook

**What CAN be tested now:**
- Validation Mã định danh (trống, <10, >13, non-numeric, auto-trim)
- Validation Mật khẩu (trống, max 50, không trim, toggle show/hide)
- Nút Đăng nhập Disabled/Enabled logic
- Login success flow (API 200 → token → Trang chủ)
- Login fail flows (401, 5xx)
- Biometric happy path + 3 exception flows
- VNeID happy path + bỏ dở
- Language switcher + Bottom Sheet
- Navigation links (UC252, UC253, Back)
- Debounce double-tap
- Sticky bottom button

**What CANNOT be tested yet (blocked by gaps):**
- Account lockout (Q1 — conflict BS-03 chưa resolve)
- Mã định danh 9 số CMND cũ (Q2 — format conflict)
- Multi-device lockout scope (Q3)
- VNeID auto-create cancel flow (Q5)
- VNeID trùng error UX (Q6)
- Loading overlay dismiss timing (Q7)
- CN vs DN redirect logic (Q8)
- Form state sau error (Q9)

**Suggested test focus areas (once gaps resolved):**
- Happy path: Login MĐD/MK, Biometric, VNeID cho cả CN và DN
- Alternative scenarios: Quên MK, Đăng ký, đổi ngôn ngữ, VNeID auto-create
- Boundary & validation: MĐD 10/12/13 số, MK 1/50 ký tự, lockout counter 4→5
- Error & exception: 401/5xx/timeout/mất mạng, biometric fail/cancel/lock, VNeID trùng/bỏ dở
- UI-specific: Sticky bottom, Disabled/Enabled state, inline error display/clear, toast dismiss
- Mobile-native: App lifecycle, hardware back, safe-area, accessibility

---

### 📌 Summary & Recommendation

UC256 v2.5 là một spec chất lượng cao với UI behavior chi tiết, error handling đầy đủ, và acceptance criteria phong phú. Tuy nhiên, có **1 conflict nghiêm trọng** (BS-03 vs lockout policy) cần BA xác nhận ngay vì ảnh hưởng trực tiếp đến scope test. Ngoài ra, **1 conflict format** (MĐD min 10 vs CMND 9 số) cần clarify. Wireframe và common rules file bị BLOCKED (Q-015) nhưng spec text đủ chi tiết để bắt đầu test design cho các area rõ ràng.

**Recommendation:** QA có thể bắt đầu thiết kế test scenarios cho validation, biometric, VNeID, và error flows ngay. Tạm hold lockout scenarios cho đến khi Q1 được resolve. BA cần trả lời Q1 + Q2 (High priority) trước khi finalize test cases.

---

*UC Readiness Review v1 — Generated by qc-uc-read agent, 2026-05-19*



