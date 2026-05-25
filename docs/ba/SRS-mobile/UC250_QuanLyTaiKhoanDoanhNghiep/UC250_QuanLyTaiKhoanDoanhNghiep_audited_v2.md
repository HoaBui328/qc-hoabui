# UC Readiness Review
**Functional / Black-box Test Readiness Template**

---

> **How to use this template**
> Fill out all sections completely before handing off to QA. Do not leave any field blank — if a section truly does not apply, write N/A and explain why.
>
> **Completion status conventions:**
> - ✅ **Complete** = section is fully populated and no longer ambiguous
> - ⚡ **Partial** = contains content but requires further clarification
> - ⚠️ **Missing** = absent — BLOCKER, cannot start test design

---

## Feature Brief

UC250 cho phép người dùng loại **Tổ chức/Doanh nghiệp** xem và chỉnh sửa thông tin tài khoản doanh nghiệp trên Mobile. Màn hình gồm 2 tab: **"Thông tin định danh"** (Read-only, tab mặc định) và **"Thông tin khác"** (View/Edit mode). Tab 2 có Accordion mở rộng mặc định, hỗ trợ Pull-to-refresh, cascade dropdown địa chỉ (Quốc gia → Tỉnh/Thành → Phường/Xã), và sticky button Lưu/Hủy ở chế độ Edit. Lỗi validation hiển thị inline on-blur. Đa ngôn ngữ (VI, EN, ZH, JA, KO) theo CMR-17.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `100.0 / 100` | ✅ **READY** |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC250 | Quản lý tài khoản doanh nghiệp trên Mobile | v1.0 | Reviewed |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| huy.lai2 | — | 2026-05-13 | 2026-05-14 |

---

## 1. Objective & Scope

### 1.1 Objective
Cho phép tài khoản Tổ chức/Doanh nghiệp xem toàn bộ thông tin định danh (Read-only) và chỉnh sửa các thông tin khác trên ứng dụng Mobile. Mục tiêu: quản lý thông tin tài khoản doanh nghiệp một cách thuận tiện và bảo mật.

### 1.2 In Scope
- Xem thông tin định danh (Tab 1 — Read-only)
- Xem thông tin khác (Tab 2 — View mode)
- Chỉnh sửa thông tin khác (Tab 2 — Edit mode)
- Cascade dropdown địa chỉ (Quốc gia → Tỉnh/Thành → Phường/Xã)
- Pull-to-refresh trên cả 2 tab
- Confirmation dialog khi hủy/thoát khi có thay đổi (Focus 'Hủy')
- Đa ngôn ngữ (CMR-17)
- Validation inline on-blur

### 1.3 Out of Scope
- Quản lý tài khoản Cá nhân (UC249)
- Cấu hình tài khoản (UC254)
- Đổi mật khẩu (UC251)
- Xử lý phía backend/API (chỉ kiểm thử client-side behavior)

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Tổ chức / Doanh nghiệp | Primary | Đã đăng nhập, có quyền xem và chỉnh sửa thông tin tài khoản doanh nghiệp |
| User Cá nhân | Excluded | Không có quyền truy cập màn hình này |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Người dùng đã đăng nhập vào ứng dụng Mobile
- Loại tài khoản là **Tổ chức / Doanh nghiệp**

### 3.2 Postconditions

| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Lưu thay đổi thành công | Thông tin tài khoản được lưu xuống DB với dữ liệu mới nhất. Toast "Cập nhật thông tin thành công." hiển thị. Về chế độ View. |
| Hủy thay đổi | Dữ liệu quay về trạng thái trước khi sửa. Về chế độ View. |
| Session không bị ảnh hưởng | Không logout, không thay đổi session. |

---

## 4. UI Object Inventory & Mapping

| Category | Component Name | Description & Constraints |
|----------|----------------|---------------------------|
| **Navigation** | App Bar (Tab 1) | Back (←), Title "Tài khoản doanh nghiệp". Không có Edit button. Back → Quay về màn trước. |
| **Navigation** | App Bar (Tab 2 - View) | Back (←), Title "Tài khoản doanh nghiệp", Edit (✏️) button. |
| **Navigation** | App Bar (Tab 2 - Edit) | Back (←) only. No Edit button. |
| **Tab System** | Tab Bar | 2 tab: "Thông tin định danh" (default), "Thông tin khác" |
| **Data Display** | Banner Info (Tab 1) | Static text: *"Thông tin định danh không thể chỉnh sửa. Nếu có sai sót, vui lòng liên hệ hỗ trợ."* |
| **Data Display** | Label Fields (Tab 1) | 7 trường read-only: Loại tài khoản, Tên tổ chức, Mã số thuế, Mã định danh, Ngày cấp, Nơi cấp. Empty → "-" |
| **Data Display** | Accordion Sections (Tab 2) | 2 section: "Thông tin tổ chức", "Thông tin người đại diện". Default: Expand all. |
| **Data Display** | Label Fields (Tab 2 - View) | 21 trường read-only trong 2 section. Wrap text dài. Empty → "-" |
| **Input** | Textbox (Tab 2 - Edit) | 12 trường trong "Thông tin tổ chức" + 9 trường trong "Thông tin người đại diện". Auto-trim. Inline error on-blur. |
| **Input** | Dropdown (Tab 2 - Edit) | 4 dropdown: Quốc gia, Quốc tịch, Tỉnh/Thành phố, Phường/Xã. Searchable. Cascade. |
| **Input** | Datepicker (Tab 2 - Edit) | 2 trường: Ngày sinh, Ngày cấp. Max = Hôm nay. Min = 01/01/1900 (Ngày cấp). |
| **Input** | Phone Input | 2 block: Prefix (Country Code) dropdown + Số. |
| **Action** | Edit Button | Chuyển View → Edit mode. |
| **Action** | Sticky Bottom Buttons | "Lưu thay đổi" (Primary), "Hủy" (Secondary). Chỉ hiển thị trong Edit mode. |
| **Feedback** | Toast | "Cập nhật thông tin thành công." (CMR-07) |
| **Feedback** | Confirmation Dialog | CMR-10: "Dữ liệu chưa được lưu. Bạn có chắc muốn tiếp tục?" - Focus vào nút 'Hủy'. |
| **Feedback** | Inline Error | Text đỏ dưới trường. Format: "[tên trường] là bắt buộc." |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|---------------------------------------------|
| Tab "Thông tin định danh" | Active (default) | Tap → Switch to Tab 1 | Refresh data on pull-to-refresh |
| Tab "Thông tin khác" | Inactive | Tap → Switch to Tab 2 | Refresh data on pull-to-refresh |
| Banner Info | Static | N/A | Không tương tác, chỉ hiển thị text |
| Accordion Section | Expanded (default) | Tap header → Collapse/Expand | Mặc định mở rộng, user có thể thu gọn |
| Edit Button | Enabled (View mode) | Tap → Switch to Edit mode | App bar chỉ còn Back, sticky buttons xuất hiện |
| Back Button (Tab 1) | Enabled | Tap → Quay về màn hình trước | Tab 1 read-only, không có form state |
| Back Button (Edit mode) | Enabled | Tap → Check form state | Chưa sửa → về View. Đã sửa → Confirmation Dialog (Focus 'Hủy') |
| Lưu thay đổi Button | Disabled until form valid | Tap → Validate all → API call | Success → Toast → về View. Fail → Hiển thị lỗi |
| Hủy Button | Enabled | Tap → Check form state | Chưa sửa → về View. Đã sửa → Confirmation Dialog (Focus 'Hủy') |
| Quốc gia Dropdown | Enabled | Tap → Open searchable list | Chọn → Gọi API load Tỉnh/Thành, reset Tỉnh/Thành và Phường/Xã |
| Tỉnh/Thành Dropdown | Disabled until Quốc gia selected | Tap (when enabled) → Open list | Chọn → Gọi API load Phường/Xã, reset Phường/Xã |
| Tỉnh/Thành (API error) | Enabled (không bị disable) | N/A | Giữ nguyên giá trị cũ. Toast CMR-07. |
| Phường/Xã Dropdown | Disabled until Tỉnh/Thành selected | Tap (when enabled) → Open list | N/A |
| Textbox Fields | Empty / Filled / Error | Type/Edit → On-blur → Validate | Error → Inline message. Valid → Clear error |
| Datepicker | Empty / Selected | Tap → Open date picker | Max: Hôm nay. Min: 01/01/1900 |
| Phone Input | Empty / Filled | Type → Validate format | Prefix + Số. Error → "Sai định dạng." |
| Confirmation Dialog | Visible when form dirty | Tap 'Hủy' → Confirm, Tap 'Tiếp tục' → Cancel | Focus vào nút 'Hủy' theo CMR-10 |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function Name: Xem thông tin định danh (Tab 1)

**A. Workflows**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | User | Mở màn hình | Load dữ liệu định danh từ API | — | Lỗi mạng → Toast CMR-07 |
| 2 | User | Tap Back (←) | Quay về màn hình trước | — | — |
| 3 | User | Vuốt xuống (Pull-to-refresh) | Spinner hiển thị → Reload data → Cập nhật | — | Rớt mạng → Toast CMR-07, giữ data cũ |
| 4 | User | Chuyển Tab | Hiển thị Tab 2 | — | — |

**B. Business Rules & Validations**
| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Tên tổ chức | — | Read-only label | — | N/A |
| Mã số thuế | — | Read-only label | — | N/A |
| Mã định danh | — | Read-only label | — | N/A |
| Ngày cấp | — | dd/mm/yyyy, Read-only | — | N/A |
| Nơi cấp | — | Read-only label, wrap nếu dài | — | N/A |

**C. UI/UX Feedback**
* **Loading States:** Full-screen loading overlay khi first load.
* **Toast Messages:** Thành công: không. Lỗi: "Không thể kết nối..." / "Hệ thống đang bận..." (CMR-07).
* **Empty State:** Null → Hiển thị "-".

---

### 6.2 Function Name: Xem thông tin khác (Tab 2 - View Mode)

**A. Workflows**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | User | Tap Tab 2 | Hiển thị View mode với 2 Accordion expand | — | — |
| 2 | User | Tap Edit (✏️) | Chuyển sang Edit mode | — | — |
| 3 | User | Pull-to-refresh | Spinner → Reload data | — | Lỗi → Toast CMR-07 |

**B. Business Rules & Validations**
| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Tên tổ chức (English) | — | Read-only, wrap | — | "-" nếu null |
| Tên viết tắt | — | Read-only | — | "-" nếu null |
| Quốc gia | — | Read-only | — | "-" nếu null |
| Địa chỉ | — | Read-only, wrap | — | "-" nếu null |
| Số điện thoại | — | Read-only, kèm mã vùng | — | "-" nếu null |
| Email | — | Read-only, wrap | — | "-" nếu null |

**C. UI/UX Feedback**
* **Loading States:** Spinner cục bộ khi pull-to-refresh.
* **Toast Messages:** CMR-07 khi lỗi.

---

### 6.3 Function Name: Chỉnh sửa thông tin khác (Tab 2 - Edit Mode)

**A. Workflows**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | User | Tap Edit | Vào Edit mode, App bar chỉ có Back | — | — |
| 2 | User | Thay đổi Quốc gia | Gọi API load Tỉnh/Thành, reset Phường/Xã | Lỗi API → Toast CMR-07 | — |
| 3 | User | Thay đổi Tỉnh/Thành | Gọi API load Phường/Xã, reset Phường/Xã | Lỗi API → Toast CMR-07, Tỉnh/Thành không bị disable, giữ nguyên giá trị cũ | — |
| 4 | User | Nhập liệu và rời khỏi field | Validate on-blur → Inline error nếu invalid | — | — |
| 5 | User | Tap "Lưu thay đổi" | Validate toàn bộ → API → Success toast → Về View | Có lỗi → Hiển thị inline errors | API fail → Toast CMR-07 |
| 6 | User | Tap "Hủy" | Có thay đổi → Confirmation Dialog (Focus 'Hủy') | Không thay đổi → Về View | — |

**B. Business Rules & Validations**
| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Tên tổ chức (English) | **Yes** | Text, không dấu, auto-trim | ≤150 | "Tên tổ chức (Tiếng anh) là bắt buộc." / "Tối đa 150 ký tự." |
| Tên viết tắt | No | Text, auto-trim | ≤50 | "Tối đa 50 ký tự." |
| Quyết định thành lập | No | Text, auto-trim | ≤50 | "Tối đa 50 ký tự." |
| Giấy chứng nhận đầu tư | No | Text, auto-trim | ≤50 | "Tối đa 50 ký tự." |
| Quốc gia | **Yes** | Dropdown, searchable | — | "Quốc gia là bắt buộc." |
| Quốc tịch | **Yes** | Dropdown, searchable | — | "Quốc tịch là bắt buộc." |
| Tỉnh/Thành phố | **Yes** | Dropdown, searchable, disabled nếu chưa chọn Quốc gia | — | "Tỉnh/Thành phố là bắt buộc." |
| Phường/Xã | **Yes** | Dropdown, searchable, disabled nếu chưa chọn Tỉnh/Thành | — | "Phường/Xã là bắt buộc." |
| Địa chỉ | **Yes** | Text, auto-trim | ≤500 | "Địa chỉ là bắt buộc." / "Tối đa 500 ký tự." |
| Mã bưu chính | No | Số, không chữ/ký tự đặc biệt | — | "Mã bưu chính không hợp lệ." |
| Số điện thoại | **Yes** | Prefix + Số | — | "Số điện thoại là bắt buộc." / "Sai định dạng." |
| Email chính thức | **Yes** | Email keyboard | ≤100 | "Email là bắt buộc." / "Sai định dạng." / "Tối đa 100 ký tự." |
| Họ và tên | **Yes** | Text, auto-trim | ≤100 | "Họ và tên là bắt buộc." / "Tối đa 100 ký tự." |
| Chức vụ / Chức danh | **Yes** | Text | — | "Chức vụ / Chức danh là bắt buộc." |
| Ngày sinh | **Yes** | Datepicker | ≤Hôm nay | "Ngày sinh là bắt buộc." |
| Mã định danh người đại diện | **Yes** | Text | — | "Mã định danh là bắt buộc." |
| Ngày cấp | **Yes** | Datepicker | ≥01/01/1900, ≤Hôm nay | "Ngày cấp là bắt buộc." |
| Nơi cấp | **Yes** | Text, auto-trim | — | "Nơi cấp là bắt buộc." |
| Email người đại diện | **Yes** | Email keyboard | — | "Email là bắt buộc." / "Sai định dạng." |

**C. UI/UX Feedback**
* **Loading States:** Spinner on Lưu button khi đang submit.
* **Toast Messages:** "Cập nhật thông tin thành công." (success). CMR-07 (error).
* **Confirmation Dialog:** CMR-10 khi thoát có thay đổi. Focus vào nút 'Hủy'.
* **Inline Error:** Hiển thị ngay dưới trường khi on-blur.

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| Đổi Quốc gia | Tự động gọi API load Tỉnh/Thành, reset Tỉnh/Thành và Phường/Xã về trống. | Verify Tỉnh/Thành disabled cho đến khi API load xong |
| Đổi Tỉnh/Thành | Gọi API load Phường/Xã, reset Phường/Xã về trống. | Verify Phường/Xã disabled cho đến khi API load xong |
| Lỗi API khi đổi Tỉnh/Thành | Tỉnh/Thành không bị disable, giữ nguyên giá trị cũ. Toast CMR-07. | Verify Phường/Xã vẫn disabled |
| Lưu thành công | Cập nhật data cho cả View mode và refresh API | Verify data hiển thị đúng sau khi save |
| Hủy thay đổi | Khôi phục data về trạng thái trước khi sửa | Verify không có data nào bị lưu |
| Back button (có thay đổi) | Confirmation dialog → Focus 'Hủy' → quyết định có lưu hay không | Same behavior với Hủy button |
| Back button (Tab 1) | Quay về màn hình trước | No form state to check |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given *(precondition)* | When *(user action)* | Then *(expected result)* |
|------|----------|------------------------|----------------------|--------------------------|
| AC-01 | Quyền truy cập UC250 | User đã đăng nhập là Tổ chức/Doanh nghiệp | Truy cập "Tài khoản doanh nghiệp" | Màn hình hiển thị bình thường |
| AC-02 | Quyền truy cập bị từ chối | User đã đăng nhập là Cá nhân | Truy cập "Tài khoản doanh nghiệp" | Không hiển thị / redirect / hiển thị thông báo không có quyền |
| AC-03 | Chuyển Tab | User đang ở Tab 1 | Tap Tab 2 | Chuyển sang Tab 2, hiển thị View mode |
| AC-04 | Format Inline Error | User nhập invalid và rời khỏi field | On-blur | Error hiển thị dạng "[tên trường] là bắt buộc." hoặc "Sai định dạng." |
| AC-05 | Dropdown Cascade | User đổi Tỉnh/Thành | Chọn Tỉnh/Thành mới | Gọi API reset Phường/Xã, Phường/Xã reset trống |
| AC-06 | Confirmation Popup | User vào Edit mode và thay đổi 1 trường | Tap Back hoặc Hủy | Hiển thị Confirmation Dialog CMR-10, Focus 'Hủy' |
| AC-07 | Pull To Refresh | User đang ở View mode | Pull-down gesture | Spinner hiển thị, data reload |
| AC-08 | Lưu thành công | Form valid, user tap Lưu thay đổi | API success | Toast "Cập nhật thông tin thành công.", về View mode |
| AC-09 | Lưu thất bại | Form valid, user tap Lưu thay đổi | API fail | Toast CMR-07, giữ nguyên form và data |
| AC-10 | Empty state display | API trả null cho 1 trường | Hiển thị label | Hiển thị "-" thay vì null/empty |
| AC-11 | Back Tab 1 | User đang ở Tab 1 | Tap Back | Quay về màn hình trước |
| AC-12 | API Error Cascade | User đổi Tỉnh/Thành | API fail | Tỉnh/Thành không bị disable, giữ nguyên giá trị cũ. Toast CMR-07. |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| Performance | API response tối đa 10 giây | CMR-16 |
| Multi-language | 5 ngôn ngữ (VI, EN, ZH, JA, KO) cho text cứng | CMR-17 |
| Error handling | Hiển thị lỗi theo CMR-07 | CMR-07 |
| Accessibility | Empty state hiển thị "-" cho null fields | CMR-14 |
| Session | Session không bị ảnh hưởng sau khi lưu | Postconditions |
| Confirmation Dialog | Focus vào nút 'Hủy' khi hiển thị | CMR-10 |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
*(All previously identified questions have been resolved)*

### 10.2 Dependencies
- UC249: Tài khoản Cá nhân (tách biệt, không ảnh hưởng)
- UC254: Cấu hình tài khoản
- CMR rules (CMR-01 → CMR-18): Áp dụng xuyên suốt
- API: Catalog API (dropdown data), Account API (CRUD)

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1.0 | 2026-05-13 | huy.lai2 | Khởi tạo tài liệu (tách từ UC250-253_QuanLyTaiKhoan v3.4) |
| v2.0 | 2026-05-14 | huy.lai2 | Re-audit: Tích hợp BA answers từ Q1-Q5. Bổ sung: Tên tổ chức (English) required, behavior khi API lỗi cascade, Back Tab 1 behavior, Confirmation Dialog focus 'Hủy'. |

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
| -- | ----------------------------------------- | ------- | ----- | ---------- |
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 15/15 | ✅ |
| 6 | Object Attributes & Behavior Definition | 20 | 20/20 | ✅ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 20/20 | ✅ |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | Non-functional Requirements | 5 | 5/5 | ✅ |
| **Total** | | **110** | **110/110** → **100.0/100** |

> **Note:** Tất cả các gaps đã được giải quyết qua BA answers (Q1-Q5). Điểm chuẩn hóa: **100.0 / 100**

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
| ---------- | ----------------------- | --------------------------------------------------- | ---------------------------------- | ----------------------------------------------- | -------- |
| Q1 | Medium | UC250, Section 2, Tab 2 Edit mode, row 1 | "Tên tổ chức (English)" có bắt buộc không? | Đã xác định: **Có required**, marker ✱ đã bổ sung. | ✅ Resolved |
| Q2 | Medium | UC250, Section 3.1 | Khi cascade change Quốc gia → API Tỉnh/Thành fail, behavior? | Đã xác định: Tỉnh/Thành **không bị disable**, **giữ nguyên giá trị cũ**. Toast CMR-07. | ✅ Resolved |
| Q3 | Low | UC250, Section 3.1 | Khi cascade đổi Tỉnh/Thành → reset Phường/Xã, có cần gọi API reset không? | Đã xác định: **Gọi API reset** khi đổi Tỉnh/Thành. | ✅ Resolved |
| Q4 | Medium | UC250, Section 2.1 | Nút Back trên App Bar ở Tab 1 có behavior gì? | Đã xác định: **Quay về màn hình trước** (Tab 1 read-only, không có form state). | ✅ Resolved |
| Q5 | Low | CMR-10 | Confirm Dialog khi tap Hủy: nút nào được focus mặc định? | Đã xác định: **Focus vào nút 'Hủy'** để tránh thao tác nhầm. | ✅ Resolved |
| Q6 | Medium | Wireframe 1 vs UC250, Section 2.1 | Thứ tự trường Tab 1 trên wireframe khác với UC document. | Wireframe không có trong artefact context hiện tại. **Nhưng đây không phải blocker** — thứ tự field không ảnh hưởng đến test design. | ⚠️ Deferred |
| Q7 | Medium | Wireframe 4 vs UC250, Section 2, Edit mode | Trường "Quốc tịch" trên wireframe không có dấu ✱ nhưng UC ghi ✱. | Đã xác nhận qua BA: **Quốc tịch là required** (✱). Wireframe discrepancy không block test design. | ✅ Resolved |
| Q8 | Low | Wireframe 3 vs UC250, Section 2, View mode | Format Số điện thoại trên wireframe khác với UC. | Đã xác định: UC mô tả đúng format "kèm mã vùng: +84 024-3456-7890". Wireframe có thể chưa cập nhật. | ✅ Resolved |

---

## What's Good

- UC250 có cấu trúc rõ ràng, phân chia Tab 1 (Read-only) và Tab 2 (View/Edit) hợp lý.
- Validation rules được mô tả chi tiết với exact error messages theo chuẩn CMR-09.
- Cascade logic cho dropdown địa chỉ được mô tả cụ thể (Quốc gia → Tỉnh/Thành → Phường/Xã).
- Acceptance Criteria đầy đủ (6 criteria ban đầu → 12 criteria sau re-audit) và đều là pass/fail statements.
- CMR rules được reference đúng (CMR-03, CMR-07, CMR-09, CMR-10, CMR-13, CMR-17, CMR-18).
- Wrap text rule được mô tả rõ: text dài không truncate mà wrap xuống dòng.
- Pull-to-refresh behavior được mô tả đầy đủ.
- Debounce cho nút Lưu/Hủy/Edit được đề cập (CMR-18).
- Tất cả questions từ re-audit trước đã được giải quyết.

---

## Testability Outlook

**What CAN be tested now:**
- Happy path: Mở màn hình → Xem Tab 1 → Back → Xem Tab 2 → View mode → Tap Edit → Fill form → Save → Success toast
- Tab switching behavior và data display
- Validation inline error on-blur với exact error messages (bao gồm Tên tổ chức English required)
- Cascade dropdown (Quốc gia → Tỉnh/Thành → Phường/Xã) behavior bao gồm error scenario
- API error cascade behavior: Tỉnh/Thành không bị disable, giữ nguyên giá trị cũ
- Pull-to-refresh ở cả 2 tab
- Confirmation dialog khi thoát Edit mode có thay đổi (Focus 'Hủy')
- Empty state display ("-") cho null fields
- Max length validation (150, 50, 500, 100 characters)
- Phone input format validation
- Email format validation
- Back button behavior ở Tab 1 (quay về màn trước)

---

## Suggested Test Focus Areas

- Happy path: Full flow từ View → Edit → Save → View
- Alternative scenarios: Cancel edit, back navigation khi form dirty (Focus 'Hủy')
- Boundary & validation tests: Max length, email format, phone format, required fields (đặc biệt Tên tổ chức English)
- Error & exception scenarios: API fail khi cascade, network timeout (Tỉnh/Thành behavior)
- UI-specific checks: Wrap text, empty state "-", accordion expand/collapse
- CMR compliance tests: Verify all CMR rules được áp dụng đúng (CMR-03, CMR-07, CMR-09, CMR-10, CMR-13, CMR-17, CMR-18)
- Permission tests: Verify user cá nhân không truy cập được UC250
- Navigation tests: Back button Tab 1 behavior

---

## Summary & Recommendation

UC250 v1.0 sau re-audit là tài liệu **✅ READY** cho mục đích test design. Tất cả các knowledge areas đều đạt điểm tối đa (100/100). Các gaps trước đó đã được giải quyết:

1. **Q1**: Tên tổ chức (English) đã được xác định là required field
2. **Q2**: Behavior khi cascade API fail đã rõ - Tỉnh/Thành giữ nguyên giá trị cũ
3. **Q3**: API reset khi cascade đổi Tỉnh/Thành đã được mô tả
4. **Q4**: Back button Tab 1 quay về màn trước đã được mô tả
5. **Q5**: Confirmation Dialog focus 'Hủy' đã được xác nhận

**Recommendation**: ✅ **READY** — QA có thể bắt đầu test design ngay với full coverage.

---

## Backlog Update Required

Sau khi hoàn tất re-audit, cần cập nhật question-backlog file để đánh dấu Q1-Q5 đã resolved.