# UC252 — Đăng ký tài khoản trên Mobile
**Audit Report**

| Thuộc tính | Giá trị |
|---|---|
| UC ID | UC252 |
| Tên feature | Đăng ký tài khoản trên Mobile |
| Tác giả | huy.lai2 |
| Ngày audit | 2026-05-13 |
| Auditor | Claude Code (BA-audit-SRS-mobile) |
| Phiên bản UC gốc | v1.0 |
| Phiên bản audit | v1 |

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

### 1.1 Mục tiêu
Cho phép người dùng đăng ký mới tài khoản để sử dụng hệ thống MBFS.

### 1.2 Phạm vi

**Trong phạm vi:**
- Đăng ký 3 loại tài khoản: Cá nhân Việt Nam, Tổ chức/Doanh nghiệp, Cá nhân nước ngoài (pending)
- Xác thực email sau đăng ký
- Đa ngôn ngữ (5 ngôn ngữ: VI, EN, ZH, JA, KO)

**Ngoài phạm vi:**
- Đăng nhập (UC khác)
- Quên mật khẩu (UC khác)
- Xác thực đa bước (OTP)

### 1.3 Đánh giá

| Criteria | Status | Ghi chú |
|----------|--------|---------|
| Mục tiêu rõ ràng | ✅ | Mô tả đầy đủ |
| Scope defined | ⚡ | "Cá nhân nước ngoài" còn **Pending** — BA cần confirm |
| Out-of-scope identified | ⚡ | Không list rõ out-of-scope items |

---

## 2. Actors & User Roles

| Actor | Role | Permission | Ghi chú |
|-------|------|------------|---------|
| Người dùng vãng lai | Unauthenticated user | Không cần đăng nhập | Chỉ có thể thực hiện đăng ký |

**Đánh giá:**
- ✅ Actor rõ ràng
- ✅ Role không trùng lặp
- ✅ Không có quyền đặc biệt cần lưu ý

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
| Condition | Mô tả | Nguồn |
|-----------|-------|-------|
| Không có | Người dùng chưa đăng nhập | UC252 §1 |

### 3.2 Postconditions
| Condition | Mô tả | Nguồn |
|-----------|-------|-------|
| Thành công | Email xác thực được gửi, tài khoản chờ kích hoạt | UC252 §1 |
| Sau xác thực | Tài khoản được kích hoạt trên hệ thống | UC252 §1 |

### 3.3 Đánh giá

| Criteria | Status | Ghi chú |
|----------|--------|---------|
| Preconditions đầy đủ | ✅ | Không có precondition = pass |
| Postconditions rõ ràng | ⚡ | Cần bổ sung: link xác thực hết hạn thì xử lý thế nào? |
| System state sau success | ✅ | Rõ: tài khoản chờ kích hoạt |

---

## 4. UI Object Inventory & Mapping

### 4.1 Step 1 — Chọn loại tài khoản

| # | Object | Loại | Required | Default | Placeholder/Value | Enum Values | Nguồn |
|---|--------|------|----------|---------|-------------------|-------------|-------|
| 1 | App Bar | Toolbar | N/A | - | - | - | UC252 §2.1 |
| 2 | Back Button (←) | Icon Button | No | Visible | - | - | UC252 §2.1 |
| 3 | Step Indicator | Stepper | No | Step 1 active | "1 Chọn loại - 2 Thông tin" | - | UC252 §2.1 |
| 4 | Account Type List | List | Yes | None selected | - | "Cá nhân Việt Nam", "Tổ chức / Doanh nghiệp", "Cá nhân nước ngoài [Pending]" | UC252 §2.1 |
| 5 | Account Type Item - Cá nhân VN | Radio/Tile | No | Unselected | - | - | UC252 §2.1 |
| 6 | Account Type Item - Tổ chức | Radio/Tile | No | Unselected | - | - | UC252 §2.1 |
| 7 | Account Type Item - Cá nhân NN | Radio/Tile | No | Unselected | - | - | UC252 §2.1 (Pending) |

### 4.2 Step 2 — Form Đăng ký (App Bar)

| # | Object | Loại | Required | Default | Placeholder/Value | Enum Values | Nguồn |
|---|--------|------|----------|---------|-------------------|-------------|-------|
| 8 | Back Button (←) | Icon Button | No | Visible | - | - | UC252 §2.2 |
| 9 | Page Title | Label | No | "Đăng ký tài khoản cá nhân" hoặc "Đăng ký tài khoản tổ chức" | - | - | UC252 §2.2 |

### 4.3 Step 2 — Section "Thông tin cá nhân / Tổ chức"

| # | Object | Loại | Required | Default | Placeholder/Value | Enum Values | Nguồn |
|---|--------|------|----------|---------|-------------------|-------------|-------|
| 10 | Tên tổ chức / Họ và tên | Textbox | Yes (*) | - | - | - | UC252 §2.2 |
| 11 | Mã định danh | Textbox | Yes (*) | - | - | Alphanumeric + "-", 5-20 ký tự | UC252 §2.2 |
| 12 | Icon CCCD (💳) | Icon | No | Visible | - | - | UC252 §2.2 |
| 13 | Ngày cấp | Datepicker | Yes (*) | - | - | Max: hôm nay, Min: 01/01/1900 | UC252 §2.2 |
| 14 | Icon lịch (📅) | Icon | No | Visible | - | - | UC252 §2.2 |
| 15 | Nơi cấp | Textbox | Yes (*) | - | - | 2-100 ký tự | UC252 §2.2 |
| 16 | Icon địa điểm (📍) | Icon | No | Visible | - | - | UC252 §2.2 |
| 17 | Mã số thuế | Textbox | Yes (*)/Hidden | - | - | Chỉ số, 10/13 số | UC252 §2.2 |
| 18 | Label "Mã số thuế" | Label | Conditional | Hidden cho Cá nhân NN | - | - | UC252 §2.2 |

### 4.4 Step 2 — Section "Thông tin liên hệ"

| # | Object | Loại | Required | Default | Placeholder/Value | Enum Values | Nguồn |
|---|--------|------|----------|---------|-------------------|-------------|-------|
| 19 | Số điện thoại | Textbox (tel) | Yes (*) | - | - | +84 (dropdown cờ, locked cho VN) | UC252 §2.2 |
| 20 | Dropdown cờ (+84) | Dropdown | No | +84 | - | Disabled cho Cá nhân VN/Tổ chức VN | UC252 §2.2 |
| 21 | Email | Textbox (email) | Yes (*) | - | - | - | UC252 §2.2 |

### 4.5 Step 2 — Section "Tạo mật khẩu"

| # | Object | Loại | Required | Default | Placeholder/Value | Enum Values | Nguồn |
|---|--------|------|----------|---------|-------------------|-------------|-------|
| 22 | Mật khẩu | Password Input | Yes (*) | Visible (xem được) | - | Tối thiểu 8 ký tự, 1 hoa, 1 thường, 1 số | UC252 §2.2 |
| 23 | Icon mắt (👁️) | Icon Button | No | Visible (mở) | - | Tap toggle: hiện/ẩn | UC252 §2.2 |
| 24 | Nhập lại mật khẩu | Password Input | Yes (*) | Visible (xem được) | - | - | UC252 §2.2 |
| 25 | Icon mắt (Nhập lại) | Icon Button | No | Visible (mở) | - | Tap toggle: hiện/ẩn | UC252 §2.2 |

### 4.6 Step 2 — Khu vực Button (Sticky bottom)

| # | Object | Loại | Required | Default | Placeholder/Value | Enum Values | Nguồn |
|---|--------|------|----------|---------|-------------------|-------------|-------|
| 26 | Đồng ý Điều khoản | Checkbox | Yes (*) | Unchecked | "Tôi đồng ý với [Điều khoản sử dụng] và [Chính sách bảo mật]" | - | UC252 §2.2 |
| 27 | Link "Điều khoản sử dụng" | Link Text | No | Red color | - | - | UC252 §2.2 |
| 28 | Link "Chính sách bảo mật" | Link Text | No | Red color | - | - | UC252 §2.2 |
| 29 | Nút Đăng ký tài khoản | Button | Yes (*) | Disabled (unchecked) | "Đăng ký tài khoản" | - | UC252 §2.2 |

### 4.7 Step 3 — Màn hình Thông báo xác thực

| # | Object | Loại | Required | Default | Placeholder/Value | Enum Values | Nguồn |
|---|--------|------|----------|---------|-------------------|-------------|-------|
| 30 | Popup trắng | Modal | N/A | Visible after success | - | - | UC252 §2.3 |
| 31 | Thông báo text | Label | No | "Hệ thống đã gửi thông báo qua email..." | - | - | UC252 §2.3 |
| 32 | Back Button (←) | Icon Button | No | Visible | - | - | UC252 §2.3 |
| 33 | Nút Đăng nhập | Button | No | Visible (on success verify) | "Đăng nhập" | - | UC252 §3.2 |

### 4.8 Đánh giá UI Coverage

| Criteria | Status | Ghi chú |
|----------|--------|---------|
| Tất cả elements có row riêng | ⚡ | Icon mắt trạng thái ban đầu chưa mô tả rõ (visible hay hidden?) |
| Labels match design | ✅ | Vietnamese text preserved |
| Required flags accurate | ✅ | (*) marked correctly |
| Enum values complete | ⚡ | Dropdown cờ có danh sách country codes đầy đủ không? |
| Empty state defined | ⚡ | Step 1: nếu chưa chọn loại, có empty state message không? |

---

## 5. Object Attributes & Behavior Definition

### 5.1 Object States & Behaviors

| Object | System State | Interaction | Behavior |
|--------|-------------|-------------|----------|
| Back Button (←) - Step 1 | Enabled | Tap | Quay về màn hình Đăng nhập |
| Back Button (←) - Step 2 | Enabled | Tap | Quay về màn hình Chọn loại tài khoản |
| Back Button (←) - Step 3 | Enabled | Tap / Android Back | Quay về màn hình Đăng nhập ban đầu |
| Account Type List | Enabled | Tap item | Chuyển sang Step 2 với loại tương ứng |
| Tên tổ chức / Họ và tên | Enabled | Input + Blur | Auto-trim (CMR-09), validate: required, max 50 chars |
| Mã định danh | Enabled | Input + Blur | Validate: required, 5-20 alphanumeric + "-", format check |
| Ngày cấp | Enabled | Tap | Open datepicker, max = today, min = 01/01/1900 |
| Nơi cấp | Enabled | Input + Blur | Validate: required, 2-100 chars |
| Mã số thuế | Hidden (Cá nhân NN) / Enabled (VN) | Input + Blur | Validate: required (VN), 10 or 13 digits |
| Số điện thoại | Enabled | Input + Blur | Validate: required, đầu số VN (03/05/07/08/09) |
| Dropdown cờ (+84) | Disabled (VN flow) / Enabled (NN) | Tap | Locked hard-code +84 cho Cá nhân VN/Tổ chức VN |
| Email | Enabled | Input + Blur | Validate: required, email format |
| Mật khẩu | Enabled | Input + Blur + Toggle eye | Default: visible. Validate: required, 8+ chars, 1 upper, 1 lower, 1 number |
| Icon mắt (Mật khẩu) | Enabled | Tap | Toggle visible/hidden, icon thay đổi |
| Nhập lại mật khẩu | Enabled | Input + Blur + Toggle eye | Validate: required, match Mật khẩu |
| Icon mắt (Nhập lại) | Enabled | Tap | Toggle visible/hidden, icon thay đổi |
| Đồng ý Điều khoản | Enabled | Tap | Toggle checked/unchecked |
| Link Điều khoản | Enabled | Tap | Mở UC83-86 |
| Link Chính sách bảo mật | Enabled | Tap | Mở UC83-86 |
| Nút Đăng ký tài khoản | Disabled (unchecked) / Enabled (checked) | Tap | Validate toàn bộ form → Gọi API |
| Nút Đăng nhập (Step 3) | Enabled | Tap | Redirect về màn hình Đăng nhập |

### 5.2 Đánh giá

| Criteria | Status | Ghi chú |
|----------|--------|---------|
| Tất cả Section 4 objects có behavior | ⚡ | Icon mắt trạng thái ban đầu: "Mặc định xem được" - nhưng Step 2 đang hiển thị text hay ***? |
| System states defined | ⚡ | Dropdown cờ disabled cho VN - cần disabled hay hidden? |
| Interaction matrix complete | ✅ | Click/Tap behaviors defined |
| Error states described | ⚡ | Inline errors có, nhưng loading state khi submit không mô tả |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Main Flow — Đăng ký thành công

```
[Start] → Tap "Đăng ký" (Login screen)
  → Step 1: Chọn loại tài khoản
    → Tap 1 trong 3 loại
  → Step 2: Điền form
    → Tên/Họ và tên (required)
    → Mã định danh (required)
    → Ngày cấp (required)
    → Nơi cấp (required)
    → Mã số thuế (required VN, hidden NN)
    → Số điện thoại (required)
    → Email (required)
    → Mật khẩu (required)
    → Nhập lại mật khẩu (required)
    → Check "Đồng ý Điều khoản"
  → Tap "Đăng ký tài khoản"
    → Validate toàn bộ form (on blur fields + final check)
    → Gọi API đăng ký
    → API success
  → Step 3: Màn hình thông báo
    → "Hệ thống đã gửi thông báo qua email..."
    → User click link trong email
  → Deep link về app
    → Xác thực thành công
    → Hiển thị màn hình trắng thành công
    → Tap "Đăng nhập"
  → Redirect về Login
[End]
```

### 6.2 Alternative Flows

**AF-01: Chọn loại tài khoản → Quay lại Step 1**
- User đang ở Step 2 → Tap Back → Quay về Step 1 (đã chọn được giữ nguyên không?)

**AF-02: Mở Điều khoản trước khi đăng ký**
- User tap link Điều khoản/Chính sách → Mở UC83-86 → Quay lại form

### 6.3 Exception & Error Flows

**EF-01: Validation Error (Inline)**
- Rời trường (on blur) → Hiển thị inline error ngay dưới trường
- Error message theo CMR-09 format

**EF-02: Duplicate Detection**
- Submit form → API check duplicate
- Email trùng → "Email đã được đăng ký."
- SĐT trùng → "Số điện thoại đã được đăng ký."
- Mã định danh trùng → "Mã định danh đã được đăng ký."

**EF-03: API Error**
- 500 → "Hệ thống đang bận. Vui lòng thử lại sau." (CMR-07)
- Timeout → "Yêu cầu đã hết thời gian chờ. Vui lòng thử lại." (CMR-07)

**EF-04: Email Verification Link Expired**
- Click link hết hạn → **???** (Không mô tả trong UC)

### 6.4 Business Rules & Validations

| Rule ID | Rule | Loại | Nguồn |
|---------|------|------|-------|
| BR-01 | Auto-trim whitespace đầu/cuối cho text fields | Validation | CMR-09 |
| BR-02 | Validation inline on blur | Validation | CMR-09, UC252 §2.2 |
| BR-03 | Submit button disabled khi checkbox chưa check | UI Logic | UC252 §2.2 |
| BR-04 | Đầu số VN hợp lệ: 03, 05, 07, 08, 09 | Validation | UC252 §2.2 |
| BR-05 | Mật khẩu: tối thiểu 8 ký tự, 1 hoa, 1 thường, 1 số | Validation | UC252 §2.2 |
| BR-06 | Mã số thuế: 10 hoặc 13 số | Validation | UC252 §2.2 |
| BR-07 | Ngày cấp: max = hôm nay, min = 01/01/1900 | Validation | UC252 §2.2 |
| BR-08 | Mã định danh: 5-20 ký tự alphanumeric + "-" | Validation | UC252 §2.2 |
| BR-09 | Nơi cấp: 2-100 ký tự | Validation | UC252 §2.2 |
| BR-10 | Mật khẩu không trim whitespace | Exception | CMR-09 |

### 6.5 Đánh giá

| Criteria | Status | Ghi chú |
|----------|--------|---------|
| Happy path đầy đủ | ✅ | Rõ ràng, từ Step 1 → Step 3 |
| Alternative flows | ⚡ | Quay lại Step 1 có giữ nguyên selection không? |
| Exception flows | ⚡ | Link hết hạn không mô tả |
| Validation rules | ✅ | Đầy đủ |
| Error messages | ⚡ | CMR-07 có nhưng không reference đầy đủ |

---

## 7. Functional Integration Analysis

### 7.1 Impact Analysis

| Function A | Function B | Impact | Description |
|------------|------------|--------|-------------|
| Đăng ký | Email Service | Direct | Gửi email xác thực sau đăng ký thành công |
| Đăng ký | Deep Link | Direct | Link xác thực redirect về app |
| Đăng ký | Account Activation | Direct | Sau xác thực → tài khoản kích hoạt |

### 7.2 Data Consistency

| Data Field | Storage | Consistency |
|------------|---------|-------------|
| Email | User account | Không được trùng lặp |
| SĐT | User account | Không được trùng lặp |
| Mã định danh | User account | Không được trùng lặp |

### 7.3 Đánh giá

| Criteria | Status | Ghi chú |
|----------|--------|---------|
| Integration points identified | ✅ | Email, Deep Link |
| Data consistency rules | ⚡ | Duplicate check có, nhưng không mô tả conflict resolution |
| Cross-function dependencies | ✅ | Rõ ràng |

---

## 8. Acceptance Criteria

| # | AC | Pass Condition | Status | Nguồn |
|---|-----|---------------|--------|-------|
| AC-01 | Đăng ký thành công | Form valid → Submit → Nhận màn hình "Đăng ký thành công" + Email xác thực | ✅ | UC252 §4 |
| AC-02 | Format Inline Error | Lỗi hiển thị ngay dưới trường khi focus out, text đúng chuẩn | ✅ | UC252 §4, CMR-09 |
| AC-03 | Lỗi trùng lặp | Báo đúng trường bị trùng (SĐT, Email, Mã định danh) | ✅ | UC252 §4 |
| AC-04 | Logic Datepicker | Không cho chọn ngày > hôm nay hoặc < 01/01/1900 | ✅ | UC252 §4 |
| AC-05 | Nút Đăng ký disabled | Disabled khi chưa check "Đồng ý Điều khoản" | ✅ | UC252 §4 |

**Generated AC (inferred):**

| # | AC | Pass Condition |
|---|-----|---------------|
| AC-06 | Dropdown cờ locked cho VN | Dropdown +84 bị disabled (không đổi) khi luồng Cá nhân VN hoặc Tổ chức VN |
| AC-07 | Mật khẩu visible by default | Mật khẩu hiển thị dạng text (không ***) khi mới vào form |
| AC-08 | Đa ngôn ngữ | Tất cả text cứng thay đổi theo ngôn ngữ app (VI/EN/ZH/JA/KO) |
| AC-09 | Back Step 2 → Step 1 | Tap Back ở Step 2 → Quay về Step 1, đã chọn loại được giữ |
| AC-10 | Email verification link hết hạn | Click link hết hạn → Hiển thị thông báo (UC không mô tả) |

---

## 9. Non-functional Requirements

| NFR | Mô tả | Nguồn | Status |
|-----|-------|-------|--------|
| Performance | API response ≤ 10s (CMR-16) | CMR-16 | ⚡ Không reference trong UC |
| Multi-language | 5 ngôn ngữ VI/EN/ZH/JA/KO | CMR-17 | ✅ Đề cập §3.3 |
| Error Handling | CMR-07 error messages | CMR-07 | ⚡ Không reference trong UC |
| Date Format | dd/MM/yyyy | CMR-12 | ⚡ Không reference trong UC |
| Form Validation | CMR-09 inline validation | CMR-09 | ✅ Đề cập |

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | UC252 §2.1 | "Cá nhân nước ngoài" đang **Pending** — BA confirm loại giấy tờ nào được chấp nhận (Hộ chiếu? Giấy tờ tương đương nào?) | Không thể test flow này khi còn Pending | Open |
| Q2 | High | UC252 §3.2 | Link xác thực email có thời hạn 1 ngày. Khi user click link **hết hạn**, hệ thống xử lý thế nào? | Không có error flow cho EF-04 | Open |
| Q3 | Medium | UC252 §2.2 | Mật khẩu "Mặc định là xem được" — Step 2 khi mới vào, ô Mật khẩu hiển thị text rõ hay dạng `***`? | UI behavior không rõ | Open |
| Q4 | Medium | UC252 §2.2 | Dropdown cờ (+84) cho Cá nhân NN — có những country codes nào? Có lock +84 không? | Không mô tả | Open |
| Q5 | Medium | UC252 §2.1 | Step 1: Nếu user chưa chọn loại và tap nút Back, có empty state message không? | UI coverage gap | Open |
| Q6 | Medium | UC252 §3.2 | Link xác thực có hoạt động trên nhiều devices không? (Session validation?) | Integration chưa rõ | Open |
| Q7 | Low | UC252 §2.2 | Khi đang ở Step 2, tap Back → Quay về Step 1, **đã chọn loại tài khoản có được giữ nguyên không?** | UX consistency | Open |
| Q8 | Low | UC252 §3.2 | Email xác thực có retry mechanism không? (Gửi lại email) | Missing feature | Open |
| Q9 | Low | CMR-07, CMR-16 | UC không reference CMR-07 (error handling) và CMR-16 (API timeout 10s) — có áp dụng không? | NFR completeness | Open |

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|---------------|---------|-------|--------|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 4/5 | ⚡ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 9/10 | ⚡ |
| 5 | UI Object Inventory & Mapping | 15 | 12/15 | ⚡ |
| 6 | Object Attributes & Behavior Definition | 20 | 14/20 | ⚡ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 16/20 | ⚡ |
| 8 | Functional Integration Analysis | 10 | 8/10 | ⚡ |
| 9 | Acceptance Criteria | 10 | 8/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 4/5 | ⚡ |
| **Total** | | **110** | **90/110** | **81.8/100** |

---

## 🟢 What's Good

- **Feature identity** rõ ràng: UC ID, mô tả, actor, preconditions đầy đủ
- **UI specification** chi tiết: labels, required flags, validation rules, enum values đều có
- **AC definitions** có 5 criteria rõ ràng, pass conditions cụ thể
- **Business rules** đầy đủ: validation formats, date range, password requirements
- **Multi-language** support được đề cập (CMR-17)
- **Duplicate detection** error messages cụ thể cho từng trường

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- [x] Happy path đăng ký thành công (AC-01)
- [x] Inline validation cho tất cả fields (AC-02)
- [x] Datepicker boundary: > hôm nay và < 01/01/1900 bị disable (AC-04)
- [x] Nút Đăng ký disabled khi chưa check checkbox (AC-05)
- [x] Validation format: email, phone (03/05/07/08/09), password (8+ chars, 1 upper, 1 lower, 1 number)
- [x] Mã số thuế: 10 hoặc 13 số
- [x] Duplicate detection: Email, SĐT, Mã định danh (AC-03)

**What CANNOT be tested yet (blocked by gaps):**
- [ ] "Cá nhân nước ngoài" flow — PENDING (Q1)
- [ ] Email verification link expired behavior — không mô tả (Q2)
- [ ] Password field initial visibility state — không rõ (Q3)
- [ ] Country code dropdown values cho NN — không mô tả (Q4)
- [ ] Back navigation Step 2→1 giữ selected item — không rõ (Q7)

**Suggested test focus areas** *(once gaps are resolved)*:
- Happy path: Đăng ký thành công với từng loại tài khoản
- Alternative scenarios: Quay lại Step 1 từ Step 2, mở Điều khoản trước khi submit
- Boundary & validation tests: Datepicker min/max, password format, phone prefix VN, tax code digits
- Error & exception scenarios: Inline errors on blur, duplicate detection, API errors (CMR-07)
- UI-specific checks: Toggle password visibility, checkbox enable button, step indicator

---

## 📌 Summary & Recommendation

**Overall State:** UC252 v1.0 là tài liệu **khá đầy đủ** về đăng ký tài khoản mobile. Happy path, validation rules, AC definitions đều rõ ràng. Tuy nhiên, có **2 blocker items** cần resolve trước khi test design có thể bắt đầu hoàn chỉnh: (1) "Cá nhân nước ngoài" còn Pending, và (2) Email verification link expired handling không mô tả. Ngoài ra, một số UI behaviors cần làm rõ (password initial visibility, dropdown cờ cho NN).

**Key Actions Required:**
1. **High**: BA confirm "Cá nhân nước ngoài" - giấy tờ nào và validation tương ứng
2. **High**: BA mô tả xử lý khi email verification link hết hạn
3. **Medium**: Làm rõ password field initial visibility (text hay ***)
4. **Medium**: Bổ sung country code list cho Cá nhân nước ngoài
5. **Low**: Confirm Back navigation behavior Step 2→1

**Verdict: ⚠️ CONDITIONALLY READY (81.8/100)**
QA có thể bắt đầu test design cho các flows đầy đủ (Cá nhân VN, Tổ chức VN) trong khi chờ BA answer các open questions cho Cá nhân nước ngoài và expired link handling.

---

## 🟡 Blockers

| Blocker | Description | Impact |
|---------|-------------|--------|
| B1 | "Cá nhân nước ngoài" còn **Pending** | Không thể test complete registration flow |
| B2 | Email verification link expired handling không mô tả | Không biết expected behavior khi user click expired link |

---

*Audit completed: 2026-05-13*
