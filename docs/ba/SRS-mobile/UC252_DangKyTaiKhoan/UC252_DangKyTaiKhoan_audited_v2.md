# UC252 — Đăng ký tài khoản trên Mobile
**Audit Report**

| Thuộc tính | Giá trị |
|---|---|
| UC ID | UC252 |
| Tên feature | Đăng ký tài khoản trên Mobile |
| Tác giả | huy.lai2 |
| Ngày audit | 2026-05-14 |
| Auditor | Claude Code (BA-audit-SRS-mobile) |
| Phiên bản UC gốc | v1.0 |
| Phiên bản audit | v2 |

---

## 0. Feature Identity

| Thuộc tính | Giá trị |
|---|---|
| UC ID | UC252 |
| Tên chức năng | Đăng ký tài khoản trên Mobile |
| Mô tả | Cho phép người dùng đăng ký mới tài khoản (Cá nhân VN, Tổ chức, Cá nhân nước ngoài pending) |
| Phân hệ | Ứng dụng Di động (Mobile App) |
| Loại chức năng | Quản lý tài khoản |
| Actor chính | Người dùng vãng lai (Chưa đăng nhập) |
| Điều kiện tiên quyết | Không có |
| Điều kiện kết thúc | Đăng ký thành công, gửi email xác thực, tài khoản kích hoạt sau xác thực |

---

## 1. Objective & Scope

**Trong phạm vi:** Đăng ký 3 loại tài khoản, xác thực email, đa ngôn ngữ (VI/EN/ZH/JA/KO)
**Ngoài phạm vi:** Đăng nhập, quên mật khẩu, OTP

| Criteria | Status | Ghi chú |
|----------|--------|---------|
| Mục tiêu rõ ràng | ✅ | |
| Scope defined | ⚡ | "Cá nhân nước ngoài" còn **Pending** |
| Out-of-scope identified | ⚡ | Không list rõ out-of-scope items |

---

## 2. Actors & User Roles

| Actor | Role | Permission | Ghi chú |
|-------|------|------------|---------|
| Người dùng vãng lai | Unauthenticated | Không cần đăng nhập | |

---

## 3. Preconditions & Postconditions

| Condition | Mô tả | Nguồn |
|-----------|-------|-------|
| Precondition | Không có | UC252 §1 |
| Postcondition (success) | Email xác thực gửi, tài khoản chờ kích hoạt | UC252 §1 |
| Postcondition (verified) | Tài khoản kích hoạt trên hệ thống | UC252 §1 |

| Criteria | Status | Ghi chú |
|----------|--------|---------|
| Preconditions đầy đủ | ✅ | |
| Postconditions rõ ràng | ⚡ | Link hết hạn → xử lý thế nào? |

---

## 4. UI Object Inventory & Mapping

### 4.1 Step 1 — Chọn loại tài khoản

| # | Object | Loại | Required | Default | Placeholder/Value | Enum Values | Nguồn |
|---|--------|------|----------|---------|-------------------|-------------|-------|
| 1 | App Bar | Toolbar | N/A | - | - | - | §2.1 |
| 2 | Back Button (←) | Icon Button | No | Visible | - | - | §2.1 |
| 3 | Step Indicator | Stepper | No | Step 1 active | "1 Chọn loại - 2 Thông tin" | - | §2.1 |
| 4 | Account Type Tile - Cá nhân VN | Tile | No | Unselected | - | - | §2.1 |
| 5 | Account Type Tile - Tổ chức | Tile | No | Unselected | - | - | §2.1 |
| 6 | Account Type Tile - Cá nhân NN | Tile | No | Unselected | - | - | §2.1 (Pending) |

### 4.2 Step 2 — Form Đăng ký (App Bar)

| # | Object | Loại | Required | Default | Placeholder/Value | Enum Values | Nguồn |
|---|--------|------|----------|---------|-------------------|-------------|-------|
| 7 | Back Button (←) | Icon Button | No | Visible | - | - | §2.2 |
| 8 | Page Title | Label | No | Dynamic: "Cá nhân" / "Tổ chức" | - | - | §2.2 |

### 4.3 Step 2 — Section "Thông tin cá nhân / Tổ chức"

| # | Object | Loại | Required | Default | Placeholder/Value | Enum Values | Nguồn |
|---|--------|------|----------|---------|-------------------|-------------|-------|
| 9 | Tên tổ chức / Họ và tên | Textbox | Yes (*) | - | - | Max 50 chars, trim | §2.2 |
| 10 | Mã định danh | Textbox | Yes (*) | - | - | 5-20 alphanumeric + "-", no space? | §2.2 |
| 11 | Icon CCCD (💳) | Icon | No | Visible | - | - | §2.2 |
| 12 | Ngày cấp | Datepicker | Yes (*) | - | dd/mm/yyyy | Max: today, Min: 01/01/1900 | §2.2 |
| 13 | Icon lịch (📅) | Icon | No | Visible | - | - | §2.2 |
| 14 | Nơi cấp | Textbox | Yes (*) | - | - | 2-100 chars, allowed chars? | §2.2 |
| 15 | Icon địa điểm (📍) | Icon | No | Visible | - | - | §2.2 |
| 16 | Mã số thuế | Textbox | Yes (*)/Hidden | - | - | 10 or 13 digits | §2.2 (hidden NN) |
| 17 | Label "Mã số thuế" | Label | Conditional | Hidden cho NN | - | - | §2.2 |

### 4.4 Step 2 — Section "Thông tin liên hệ"

| # | Object | Loại | Required | Default | Placeholder/Value | Enum Values | Nguồn |
|---|--------|------|----------|---------|-------------------|-------------|-------|
| 18 | Số điện thoại | Textbox (tel) | Yes (*) | - | - | +84 locked VN, prefix: 03/05/07/08/09 | §2.2 |
| 19 | Dropdown cờ (+84) | Dropdown | No | +84 | - | Disabled cho VN; Enabled cho NN (values?) | §2.2 |
| 20 | Email | Textbox (email) | Yes (*) | - | - | Email format rule? | §2.2 |

### 4.5 Step 2 — Section "Tạo mật khẩu"

| # | Object | Loại | Required | Default | Placeholder/Value | Enum Values | Nguồn |
|---|--------|------|----------|---------|-------------------|-------------|-------|
| 21 | Mật khẩu | Password Input | Yes (*) | **Visible** (text rõ) | - | Min 8 chars, 1 upper, 1 lower, 1 digit, max?, special chars? | §2.2 |
| 22 | Icon mắt (👁️) | Icon Button | No | Open state | - | Toggle: hiện/ẩn | §2.2 |
| 23 | Nhập lại mật khẩu | Password Input | Yes (*) | **Visible** (text rõ) | - | Must match Mật khẩu | §2.2 |
| 24 | Icon mắt (Nhập lại) | Icon Button | No | Open state | - | Toggle: hiện/ẩn | §2.2 |

### 4.6 Step 2 — Sticky Bottom

| # | Object | Loại | Required | Default | Placeholder/Value | Enum Values | Nguồn |
|---|--------|------|----------|---------|-------------------|-------------|-------|
| 25 | Đồng ý Điều khoản | Checkbox | Yes (*) | Unchecked | "Tôi đồng ý với [Điều khoản]..." | - | §2.2 |
| 26 | Link Điều khoản | Link | No | Red | - | → UC83-86 | §2.2 |
| 27 | Link Chính sách bảo mật | Link | No | Red | - | → UC83-86 | §2.2 |
| 28 | Nút Đăng ký tài khoản | Button | Yes (*) | Disabled | "Đăng ký tài khoản" | Enabled when checked | §2.2 |
| 29 | Loading spinner (Submit) | Spinner | No | Hidden | - | Visible khi đang submit? | MISSING |

### 4.7 Step 3 — Thông báo xác thực

| # | Object | Loại | Required | Default | Placeholder/Value | Enum Values | Nguồn |
|---|--------|------|----------|---------|-------------------|-------------|-------|
| 30 | Modal popup | Modal | N/A | Visible after success | - | - | §2.3 |
| 31 | Thông báo text | Label | No | "Hệ thống đã gửi..." | - | - | §2.3 |
| 32 | Back Button (←) | Icon Button | No | Visible | - | - | §2.3 |
| 33 | Nút Đăng nhập | Button | No | Visible after verify | "Đăng nhập" | - | §3.2 |

### 4.8 Màn hình xác thực thành công

| # | Object | Loại | Required | Default | Placeholder/Value | Enum Values | Nguồn |
|---|--------|------|----------|---------|-------------------|-------------|-------|
| 34 | Success screen | Screen | N/A | Visible | - | - | §3.2 |
| 35 | Nút Đăng nhập | Button | No | Visible | "Đăng nhập" | - | §3.2 |

---

## 5. Object Attributes & Behavior Definition

| Object | System State | Interaction | Behavior |
|--------|-------------|-------------|----------|
| Back Button (←) - Step 1 | Enabled | Tap | → Login screen |
| Back Button (←) - Step 2 | Enabled | Tap | → Step 1, **giữ selected?** |
| Back Button (←) - Step 3 | Enabled | Tap / Android Back | → Login screen |
| Account Type Tile - VN | Unselected → Selected | Tap | Highlight, → Step 2 |
| Account Type Tile - Tổ chức | Unselected → Selected | Tap | Highlight, → Step 2 |
| Account Type Tile - NN | Unselected → Selected | Tap | Highlight, → Step 2 (Pending) |
| Tên / Họ và tên | Enabled | Input + Blur | Trim, validate: required, max 50 |
| Mã định danh | Enabled | Input + Blur | Validate: required, 5-20 alphanumeric + "-", **space?** |
| Ngày cấp | Enabled | Tap | Datepicker: max=today, min=1900-01-01 |
| Nơi cấp | Enabled | Input + Blur | Validate: required, 2-100 chars, **allowed chars?** |
| Mã số thuế | Hidden (NN) / Enabled (VN) | Input + Blur | Validate: required VN, 10 or 13 digits |
| SĐT | Enabled | Input + Blur | Validate: required, prefix 03/05/07/08/09, **space?** |
| Dropdown cờ | Disabled (VN) / Enabled (NN) | Tap | VN locked +84; NN → **dropdown values?** |
| Email | Enabled | Input + Blur | Validate: required, **email format rule?** |
| Mật khẩu | Enabled (visible default) | Input + Blur + Toggle | Validate: required, 8+ chars, 1 upper, 1 lower, 1 digit, **max? special chars?** |
| Icon mắt | Enabled | Tap | Toggle visible/hidden, icon thay đổi |
| Nhập lại mật khẩu | Enabled (visible default) | Input + Blur + Toggle | Validate: required, match Mật khẩu |
| Đồng ý Điều khoản | Enabled | Tap | Toggle; unchecked → button disabled |
| Link Điều khoản | Enabled | Tap | → UC83-86, **back preserves form?** |
| Link Chính sách | Enabled | Tap | → UC83-86, **back preserves form?** |
| Nút Đăng ký | Disabled / Enabled | Tap | Validate all → API call, **show spinner?** |
| Nút Đăng nhập (Step 3) | Enabled | Tap | → Login screen |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Main Flow — Đăng ký thành công

```
[Start] Login → Tap "Đăng ký"
  → Step 1: Chọn loại
    → Tap tile → Selected + Highlight
  → Step 2: Điền form
    → All fields + validation on blur
    → Check "Đồng ý Điều khoản"
    → Tap "Đăng ký tài khoản" (loading spinner?)
      → Validate toàn bộ form
      → API đăng ký
      → API success
  → Step 3: Thông báo
    → "Hệ thống đã gửi thông báo qua email..."
    → Click link trong email
  → Deep link → App
    → Verify token
    → Success: màn hình trắng + "Đăng nhập"
    → Tap "Đăng nhập" → Login
[End]
```

### 6.2 Alternative Flows

**AF-01: Back Step 2 → Step 1**
- Step 2 → Tap Back → Step 1, **selected tile được giữ nguyên?** (Không mô tả)

**AF-02: Mở Điều khoản trước khi đăng ký**
- Tap link → UC83-86 → **Back → form data có bị mất không?** (Không mô tả)

**AF-03: Quay lại sửa sau khi vào Step 2**
- User đã điền partial form → quay Step 1 → chọn tile khác → form reset hay giữ data?

### 6.3 Exception & Error Flows

**EF-01: Validation Error (Inline)**
- Blur field → inline error ngay dưới field

**EF-02: Duplicate Detection**
- Submit → API check
- Email trùng → "Email đã được đăng ký."
- SĐT trùng → "Số điện thoại đã được đăng ký."
- Mã định danh trùng → "Mã định danh đã được đăng ký."

**EF-03: API Error**
- 500 → "Hệ thống đang bận. Vui lòng thử lại sau." (CMR-07)
- Timeout (10s) → "Yêu cầu đã hết thời gian chờ. Vui lòng thử lại." (CMR-07)
- **MISSING: Email send failed** → xử lý thế nào?

**EF-04: Email Verification Link Issues**
- Link hết hạn (>1 ngày) → **???**
- Token không hợp lệ → **???**
- Link đã click rồi (already verified) → **???**
- **MISSING: tất cả scenarios**

### 6.4 Business Rules & Validations

| Rule ID | Rule | Loại | Nguồn |
|---------|------|------|-------|
| BR-01 | Auto-trim whitespace text fields | Validation | CMR-09 |
| BR-02 | Validation inline on blur | Validation | CMR-09 |
| BR-03 | Submit disabled when checkbox unchecked | UI Logic | §2.2 |
| BR-04 | SĐT prefix: 03, 05, 07, 08, 09 | Validation | §2.2 |
| BR-05 | Mật khẩu: min 8, 1 upper, 1 lower, 1 digit | Validation | §2.2 |
| BR-06 | Mật khẩu: **max length?** | MISSING | - |
| BR-07 | Mật khẩu: **special characters?** | MISSING | - |
| BR-08 | Mật khẩu: **repeated chars?** (VD: `aaaaaaaa`) | MISSING | - |
| BR-09 | Mật khẩu: **consecutive chars?** (VD: `12345678`) | MISSING | - |
| BR-10 | Mã số thuế: 10 or 13 digits | Validation | §2.2 |
| BR-11 | Ngày cấp: max=today, min=1900-01-01 | Validation | §2.2 |
| BR-12 | Mã định danh: 5-20 alphanumeric + "-" | Validation | §2.2 |
| BR-13 | Mã định danh: **space allowed?** (VD: `"AB 123"`) | MISSING | - |
| BR-14 | Nơi cấp: 2-100 chars, **allowed chars?** | MISSING | - |
| BR-15 | Email: **RFC 5322 format?** | MISSING | - |
| BR-16 | SĐT: **space allowed?** (VD: `"0912 345 678"`) | MISSING | - |
| BR-17 | Password: không trim whitespace | Exception | CMR-09 |

---

## 7. Functional Integration Analysis

| Function A | Function B | Impact | Description |
|------------|------------|--------|-------------|
| Đăng ký | Email Service | Direct | Gửi email xác thực sau đăng ký |
| Đăng ký | Deep Link | Direct | Verify link → activate |
| Đăng ký | Account Activation | Direct | Token verified → account active |

**Missing integration details:**
- Email send failure: retry? manual resend?
- Token security: expiry enforcement, single-use?
- Already activated account + click link again: error?

---

## 8. Acceptance Criteria

| # | AC | Pass Condition | Status |
|---|-----|---------------|--------|
| AC-01 | Đăng ký thành công | Form valid → Submit → Success screen + Email | ✅ |
| AC-02 | Format Inline Error | Lỗi dưới field khi blur, đúng chuẩn CMR-09 | ✅ |
| AC-03 | Lỗi trùng lặp | Báo đúng trường trùng | ✅ |
| AC-04 | Logic Datepicker | Không chọn ngày > hôm nay / < 1900 | ✅ |
| AC-05 | Nút disabled | Disabled khi chưa check checkbox | ✅ |
| AC-06 | Dropdown cờ locked VN | +84 disabled cho VN flow | ✅ |
| AC-07 | Mật khẩu visible default | Text rõ (không ***) khi mới vào | ✅ |
| AC-08 | Đa ngôn ngữ | 5 ngôn ngữ VI/EN/ZH/JA/KO | ✅ |
| AC-09 | Back Step 2→1 | Giữ selected item | ⚠️ Không mô tả |
| AC-10 | Loading spinner on Submit | Spinner visible khi submit | ⚠️ Không mô tả |
| AC-11 | Email verification expired | Hiển thị message | ⚠️ Không mô tả |
| AC-12 | Invalid verify token | Hiển thị message | ⚠️ Không mô tả |
| AC-13 | Already verified + click again | Hiển thị message | ⚠️ Không mô tả |
| AC-14 | Email send failed | Error message | ⚠️ Không mô tả |

---

## 9. Non-functional Requirements

| NFR | Mô tả | Nguồn | Status |
|-----|-------|-------|--------|
| Performance | API ≤ 10s timeout | CMR-16 | ⚡ Không reference |
| Multi-language | 5 ngôn ngữ | CMR-17 | ✅ |
| Error Handling | CMR-07 messages | CMR-07 | ⚡ Không reference |
| Date Format | dd/MM/yyyy | CMR-12 | ⚡ Không reference |
| Form Validation | CMR-09 inline | CMR-09 | ✅ |

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | §2.1 | "Cá nhân nước ngoài" **Pending** — BA confirm giấy tờ nào? | Không test được flow này | Open |
| Q2 | High | §3.2 | Link xác thực hết hạn → xử lý thế nào? | Không có error flow | Open |
| Q3 | High | §3.2 | Link xác thực có token không hợp lệ → xử lý thế nào? | Không mô tả | Open |
| Q4 | High | §2.2 | Mật khẩu: **max length** là bao nhiêu? | Không viết boundary test | Open |
| Q5 | High | §2.2 | Mật khẩu: **special characters** có được chấp nhận không? | Không rõ validation | Open |
| Q6 | High | §2.2 | Email: **exact format rule** là gì? RFC 5322? | Không viết negative test | Open |
| Q7 | High | §3.2 | Email gửi thất bại (SMTP error, inbox full) → xử lý thế nào? | Không có error flow | Open |
| Q8 | Medium | §3.2 | Tài khoản đã xác thực rồi + click link lại → xử lý thế nào? | UX edge case | Open |
| Q9 | Medium | §2.2 | SĐT: dấu space có được chấp nhận không? VD: `"0912 345 678"` | Không rõ input rule | Open |
| Q10 | Medium | §2.2 | Mã định danh: dấu space có được chấp nhận không? | Không rõ input rule | Open |
| Q11 | Medium | §2.2 | Nơi cấp: **allowed characters** là gì? (chỉ chữ? hay số + special chars?) | Không viết validation test | Open |
| Q12 | Medium | §3.2 | Submit button có **loading spinner** khi đang xử lý không? | UX + test coverage | Open |
| Q13 | Medium | §2.2 | Tap link Điều khoản → Back: **form data có bị mất không?** | UX data persistence | Open |
| Q14 | Medium | §2.2 | Step 2 → Back Step 1: **selected tile có được giữ nguyên không?** | UX consistency | Open |
| Q15 | Low | §2.2 | Mật khẩu: repeated chars (`aaaaaaaa`) có được chấp nhận không? | Password strength | Open |
| Q16 | Low | §2.2 | Mật khẩu: consecutive chars (`12345678`) có được chấp nhận không? | Password strength | Open |
| Q17 | Low | §3.2 | Có tính năng **"Gửi lại email xác thực"** không? | Missing feature | Open |
| Q18 | Low | §3.2 | Có giới hạn **số lần gửi lại email** không? | Rate limit | Open |
| Q19 | Low | §2.2 | Sticky bottom: khi keyboard hiện, có bị che không? | UX edge case | Open |
| Q20 | Low | CMR-07, CMR-16 | UC không reference CMR-07/CMR-16 — có áp dụng không? | NFR completeness | Open |

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|---------------|---------|-------|--------|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 4/5 | ⚡ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 8/10 | ⚡ |
| 5 | UI Object Inventory & Mapping | 15 | 11/15 | ⚡ |
| 6 | Object Attributes & Behavior Definition | 20 | 12/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 14/20 | ⚡ |
| 8 | Functional Integration Analysis | 10 | 7/10 | ⚡ |
| 9 | Acceptance Criteria | 10 | 8/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 3/5 | ⚡ |
| **Total** | | **110** | **82/110** | **74.5/100** |

---

## 🟢 What's Good

- Feature identity, actor, preconditions đầy đủ
- UI spec chi tiết: labels, required flags, validation rules
- AC definitions rõ ràng cho happy path
- Business rules đầy đủ (password format, phone prefix, date range)
- Multi-language support
- Duplicate detection error messages cụ thể

---

## 🟡 Blockers

| Blocker | Description | Impact |
|---------|-------------|--------|
| B1 | "Cá nhân nước ngoài" còn **Pending** | Không test complete flow |
| B2 | Email verification link expired handling **không mô tả** | Không biết expected behavior |
| B3 | **Invalid token** + **already verified** + **email send failed** flows không mô tả | Nhiều edge case không test được |
| B4 | Mật khẩu max length + special chars không mô tả | Không viết boundary test |

---

## 📌 Summary & Recommendation

**Overall State:** UC252 v1.0 đã đầy đủ về happy path và validation rules cơ bản. Tuy nhiên, nhiều **edge cases** và **boundary conditions** không được mô tả, đặc biệt:
- Email verification flows (expired, invalid, already verified)
- Password validation details (max length, special chars)
- Input format rules (spaces in fields)
- Loading states và data persistence

**Verdict: ⚠️ CONDITIONALLY READY (74.5/100)**
QA có thể bắt đầu test happy path + basic validations. Cần BA answer questions trước khi test edge cases.

---

*Audit completed: 2026-05-14*