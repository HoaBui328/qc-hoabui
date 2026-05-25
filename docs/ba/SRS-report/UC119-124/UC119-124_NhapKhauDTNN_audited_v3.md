# UC Readiness Review
**Functional / Black-box Test Readiness Template**

**Tài liệu:** UC119-124_NhapKhauDTNN_audited_v3.md
**Ngày tạo:** 2026-05-07
**Tác giả:** QC Auditor Agent
**Phiên bản:** v3 (Re-Audit sau SRS v1.2 / v2.0)

---

## Feature Brief

UC119-124 mô tả chức năng **Báo cáo tình hình nhập khẩu của tổ chức kinh tế có vốn đầu tư nước ngoài (Mẫu A.IV.8c)** — báo cáo định kỳ năm, single report form, đối tượng lập là Cục Hải quan / Bộ Tài chính, nộp lên Cục Đầu tư nước ngoài (Bộ Tài chính). Giao diện Admin site.

Chức năng chính gồm: Xem danh sách báo cáo (UC119-124.1), Lập báo cáo (UC119-124.2) với bảng dữ liệu động (Dynamic Table — max 500 dòng) chứa danh sách doanh nghiệp FDI nhập khẩu, và Các tác vụ bổ trợ (UC119-124.3: Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Export Excel, Xóa).

Bảng dữ liệu gồm 6 cột: C1 (STT), C2 (MST — 10/14 số), C3 (Ngày cấp), C4 (Tên doanh nghiệp), C5 (Tỉnh/Thành phố — 63 tỉnh/TP), C6 (Nhập khẩu kỳ báo cáo USD — decimal 2 chữ số thập phân, round half up, ≥ 0). Dòng Tổng cộng SUM(C6) real-time.

**Đặc thù quan trọng (SRS v1.2 / v2.0):**
- **Cơ chế chuyển đổi Mode A / Mode B auto-detect** — không có toggle/switch trên UI:
  - **Mode A (Thủ công):** Kích hoạt khi API Tổng cục Hải quan KHÔNG khả dụng. User nhập tay. Nhập MST C2 hợp lệ → gọi API CSDL Đăng ký KD auto-fill C3/C4/C5. Validate MST on-blur + debounce 500ms.
  - **Mode B (API Hải quan):** Kích hoạt khi API Tổng cục Hải quan khả dụng. Hệ thống quét tờ khai NK trong kỳ theo danh sách MST FDI, SUM theo MST → auto-fill toàn bộ dòng. Dòng API = Disabled toàn bộ C2-C6, không có icon Xóa. Phân biệt visual bằng icon/tag "API". User vẫn thêm được dòng manual bổ sung.
- **API Partial Failure:** Mode B vẫn chạy với data có, dòng API Disabled, Toast warning, user thêm manual bổ sung, không rollback.
- **Liên kết 8c → 8a (UC107-112):** Manual — user Mẫu 8a nhấn [Tổng hợp] → query 8c Đã nộp, Group By Tỉnh, SUM C6. KHÔNG auto real-time.
- **Concurrency:** Optimistic locking (user lưu sau → conflict + refresh).
- **MST trùng giữa 8b (xuất) và 8c (nhập):** Cho phép, không cảnh báo.

Mã báo cáo: `DTNN_A4_8C_[ID]` (SRS đã nêu đề xuất bổ sung tiền tố "DTNN" vào CMR_09).

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `87.3 / 100` | READY (With Minor Gaps) |

**Giải thích:** Raw score 96/110 → Normalized = 96/110 × 100 ≈ 87.3. SRS v1.2 đã cải thiện đáng kể so với v1.1: đã giải đáp hầu hết Open Questions từ v2 audit (Q1 Mode detect, Q3 partial failure, Q4-Q5 decimal precision, Q6 max rows, Q7 empty table submit, Q8 8c→8a relationship, Q9 MST cross-report, Q14 concurrent edit). Còn một số gap nhỏ về placeholder, error message verbatim, audit log chi tiết, browser compatibility — không block test design.

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC119-124 | Báo cáo tình hình nhập khẩu TCKT có vốn ĐTNN (Mẫu A.IV.8c) | 1.2 / 2.0 | Reviewed |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| yen.le2 | N/A | 2026-04-24 | 2026-05-07 |

| Thuộc tính | Giá trị |
|---|---|
| Phân hệ | Quản lý đầu tư nước ngoài vào Việt Nam |
| Mẫu biểu | A.IV.8c |
| Loại báo cáo | Định kỳ năm |
| Hình thức nộp | Báo cáo đơn lẻ (Single report form) |
| Cơ quan nhận | Cục Đầu tư nước ngoài, Bộ Tài chính |
| Đối tượng lập | Cục Hải quan / Bộ Tài chính |
| Giao diện | Admin site |
| Quy tắc sinh mã BC | `DTNN_A4_8C_[ID]` (Đề xuất bổ sung "DTNN" vào CMR_09) |

---

## 1. Objective & Scope

### 1.1 Objective
Cho phép Cục Hải quan / Bộ Tài chính lập và nộp báo cáo định kỳ năm về tình hình nhập khẩu của các tổ chức kinh tế có vốn ĐTNN (FDI), gửi Cục Đầu tư nước ngoài (Bộ Tài chính). Là nguồn dữ liệu tổng hợp nhập khẩu cho Mẫu A.IV.8a (UC107-112).

### 1.2 In Scope
- UC119-124.1: Xem danh sách báo cáo (nhóm theo kỳ năm, filter, search).
- UC119-124.2: Lập báo cáo (Dynamic Table max 500 dòng, Mode A/B auto-detect, API CSDL Đăng ký KD, API Hải quan, validate MST).
- UC119-124.3: Các tác vụ bổ trợ (Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Export Excel, Xóa).
- UC119: Xem danh sách
- UC120: Lập báo cáo
- UC121: Nộp báo cáo
- UC122: Chỉnh sửa báo cáo
- UC123: Xem chi tiết / In / Export
- UC124: Xóa báo cáo
- Liên kết 8c → 8a: cung cấp dữ liệu nguồn cho Mẫu 8a tổng hợp.

### 1.3 Out of Scope
- Không cho phép nộp báo cáo trễ hạn.
- Việc duyệt báo cáo được thực hiện ở UC chuyên biệt của Cục ĐTNN.
- Quản lý master data MST FDI (thuộc phân hệ khác).

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|--------------------|
| Cục Hải quan | Primary | Lập, Chỉnh sửa, Nộp, Xóa, Xem, In, Export báo cáo. Cách ly theo đơn vị. Tham chiếu: CMR_02. |
| Bộ Tài chính | Primary | Đồng quyền với Cục Hải quan. Cách ly theo đơn vị. Tham chiếu: CMR_02. |
| Hệ thống (API CSDL Đăng ký KD) | System | Cung cấp dữ liệu DN khi nhập MST C2 (Mode A). Auto-fill C3/C4/C5. |
| Hệ thống (API Tổng cục Hải quan) | System | Cung cấp dữ liệu tờ khai NK theo danh sách MST FDI (Mode B). Auto-fill toàn bộ dòng. |
| Cục Đầu tư nước ngoài (Bộ Tài chính) | Receiver | Nhận notification khi báo cáo được nộp. Không thao tác trực tiếp trong UC này. |
| Hệ thống Mẫu 8a (UC107-112) | Consumer | Đọc dữ liệu 8c "Đã nộp" để tổng hợp (Group By Tỉnh, SUM C6) khi user Mẫu 8a nhấn [Tổng hợp]. |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Tài khoản đã đăng nhập thuộc đơn vị Cục Hải quan / Bộ Tài chính.
- Kỳ hạn báo cáo đang ở trạng thái "Trong thời hạn" (để Lập mới). Tham chiếu: CMR_04.
- Hệ thống kiểm tra kết nối API Tổng cục Hải quan (health-check) khi mở form Lập BC để quyết định Mode A/B.
- API CSDL Đăng ký KD khả dụng (hỗ trợ auto-fill ở Mode A). Không khả dụng → nhập thủ công C3/C4/C5.

### 3.2 Postconditions

| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Lập BC + Lưu nháp | Bản ghi xuất hiện trong danh sách. Trạng thái "Lưu nháp". Mã BC: `DTNN_A4_8C_[ID]`. |
| Nộp báo cáo | Trạng thái chuyển "Chờ duyệt". Notification gửi Cục ĐTNN. Toast T02. Audit log ghi nhận. |
| Chỉnh sửa + Lưu nháp | Dữ liệu cập nhật. Trạng thái bảo toàn. |
| Xóa báo cáo | Bản ghi bị soft-delete. Audit log ghi nhận. Toast T08. |
| Export | File Excel tải xuống theo template. |
| Sau Nộp (consumer side) | Dữ liệu 8c "Đã nộp" sẵn sàng cho Mẫu 8a query (Group By Tỉnh, SUM C6) khi user Mẫu 8a nhấn [Tổng hợp]. |

---

## 4. UI Object Inventory & Mapping — GRANULARITY RULE

### 4.1 Màn hình Danh sách (UC119-124.1)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 1 | Danh sách > Bộ lọc | "Năm" | Yearpicker | No | Năm hiện tại | — | N/A | Lọc theo năm. Kết quả ngay. Tham chiếu: CMR_07. | SRS #1 |
| 2 | Danh sách > Bộ lọc | "Trạng thái kỳ" | Multiple-selection Dropdown | No | Null | — | "Chưa tới hạn" / "Trong thời hạn" / "Qua kỳ báo cáo" | Lọc theo trạng thái kỳ. Kết quả ngay. Tham chiếu: CMR_04, CMR_07. | SRS #2 |
| 3 | Danh sách > Bộ lọc | "Trạng thái báo cáo" | Multiple-selection Dropdown | No | Null | — | "Lưu nháp" / "Chờ duyệt" / "Đã tiếp nhận" / "Yêu cầu chỉnh sửa" | Tham chiếu: CMR_03, CMR_07. | SRS #3 |
| 4 | Danh sách > Bộ lọc | "Mã báo cáo" | Search bar | No | Null | "Nhập dữ liệu" | N/A | Tìm theo mã BC. Không tìm thấy → "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. | SRS #4 |
| 5 | Kỳ hạn Header | "Kỳ hạn báo cáo" | Label (collapsible) | — | Collapse | — | N/A | VD: "Năm 2026". Click để expand. Tham chiếu: CMR_08. | SRS #5 |
| 6 | Kỳ hạn Header | "Trạng thái kỳ" | Label (badge) | — | — | — | "Chưa tới hạn" / "Trong thời hạn" / "Qua kỳ báo cáo" | Tham chiếu: CMR_04. | SRS #6 |
| 7 | Kỳ hạn Header | "Lập báo cáo" | Button | — | — | — | N/A | Chỉ hiển thị khi "Trong thời hạn". Ẩn khi khác. Tham chiếu: CF_01. | SRS #7 |
| 8 | Kỳ hạn Header | "Import" | Button | — | — | — | N/A | Chỉ hiển thị khi "Trong thời hạn". | SRS #8 |
| 9 | Bảng Danh sách | "Mã báo cáo" | Label | — | — | — | N/A | Mã hệ thống: `DTNN_A4_8C_[ID]`. Tham chiếu: CMR_09. | SRS #9 |
| 10 | Bảng Danh sách | "Ngày nộp/cập nhật" | Label | — | — | — | N/A | Định dạng: dd/MM/yyyy HH:mm. | SRS #10 |
| 11 | Bảng Danh sách | "Trạng thái báo cáo" | Label | — | — | — | N/A | Tham chiếu: CMR_03. | SRS #11 |
| 12 | Bảng Danh sách | "Hành động" | Button group | — | — | — | N/A | Tham chiếu: UC119-124.3. | SRS #12 |

### 4.2 Màn hình Lập báo cáo (UC119-124.2) — Header

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| H1 | Lập BC > Header | "Năm báo cáo" | Number | Yes | Năm hiện tại | — | N/A | Validate: Số nguyên 4 chữ số, ≤ năm hiện tại. Lỗi inline: "Năm báo cáo không hợp lệ". Tham chiếu: CMR_05. | SRS H1 |

### 4.3 Màn hình Lập báo cáo (UC119-124.2) — Bảng Dynamic Table (max 500 dòng)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| C1 | Bảng | "STT" | Integer (auto) | — | Auto-fill | — | N/A | Tăng dần từ 1. Re-index sau thêm/xóa dòng. Read-only. | SRS C1 |
| C2 | Bảng | "Mã số thuế của doanh nghiệp" | Text input | Yes | Null | — | N/A | **Mode A (dòng manual):** User nhập; validate on-blur + **debounce 500ms**; format 10 hoặc 14 chữ số; validate trùng on-blur. MST hợp lệ → gọi API CSDL Đăng ký KD auto-fill C3/C4/C5. **Mode B (dòng API):** Auto-fill, Disabled. Tham chiếu: CMR_05, CMR_06. | SRS C2 |
| C3 | Bảng | "Ngày cấp" | Date Picker | Yes | API auto-fill | — | N/A | **Mode A:** Auto-fill → Disabled; không tìm thấy → Enabled nhập tay. **Mode B:** Disabled. Validate ≤ ngày hiện tại. Định dạng: dd/MM/yyyy. Tham chiếu: CMR_05, CMR_12. | SRS C3 |
| C4 | Bảng | "Tên doanh nghiệp" | Text | Yes | API auto-fill | — | N/A | **Mode A:** Auto-fill hoặc Enabled. **Mode B:** Disabled. Tham chiếu: CMR_06, CMR_12. | SRS C4 |
| C5 | Bảng | "Tỉnh/Thành phố" | Dropdown | Yes | API auto-fill | — | Danh mục 63 Tỉnh/TP | **Mode A:** Auto-fill hoặc Enabled. **Mode B:** Disabled. Tham chiếu: CMR_07, CMR_12. | SRS C5 |
| C6 | Bảng | "Nhập khẩu kỳ báo cáo (USD)" | Decimal | Yes | Null / API | — | N/A | **Decimal precision: 2 chữ số thập phân, round half up.** **Mode A:** User nhập, validate ≥ 0 (cấm số âm). **Mode B:** Auto-fill từ SUM tờ khai, Disabled. Tham chiếu: CMR_05. | SRS C6 |
| T1 | Dòng Tổng cộng | "Tổng cộng — Nhập khẩu (USD)" | Calculated | — | Auto | — | N/A | Read-only. SUM(C6) bao gồm cả dòng API + dòng manual. Decimal 2 chữ số thập phân. Real-time. | SRS T1 |

### 4.4 Màn hình Lập báo cáo — Footer & Buttons

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| F1 | Footer | "Nơi lập báo cáo" | Text (auto-fill) | — | Tỉnh/TP theo trụ sở Cục HQ | — | N/A | Disabled. Tham chiếu: CMR_12. | SRS F1 |
| F2 | Footer | "Ngày, tháng, năm" | Date (auto-fill) | — | Current system date | — | N/A | Disabled. Real-time. Tham chiếu: CMR_12. | SRS F2 |
| B1 | Buttons | "Thêm dòng" | Button | — | — | — | N/A | Thêm 1 dòng manual cuối bảng. STT tự tăng. Max 500 dòng; vượt → Toast "Vượt quá số dòng tối đa cho phép (500)". | SRS B1 |
| B2 | Mỗi dòng manual | "Xóa dòng" | Icon Button | — | — | — | N/A | **Chỉ hiển thị trên dòng manual.** Dòng API KHÔNG có icon Xóa. Click → popup xác nhận [Đồng ý]/[Hủy]. STT re-index. Tham chiếu: CMR_06. | SRS B2 |
| B3 | Buttons | "Lưu nháp" | Button | — | — | — | N/A | Tham chiếu: CF_01. | SRS B3 |
| B4 | Buttons | "Nộp báo cáo" | Button | — | — | — | N/A | Validate toàn bộ + Empty table rule (0 dòng → Toast chặn). Tham chiếu: CF_01. | SRS B4 |
| B5 | Buttons | "Hủy" | Button | — | — | — | N/A | Dirty form guard (CMR_14). Tham chiếu: CF_01. | SRS B5 |

### 4.5 Màn hình Danh sách — Cột Hành động (UC119-124.3)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|--------------------------|--------|
| A1 | Hành động | "Nộp" | Button | — | — | N/A | Chỉ khi "Lưu nháp" / "Yêu cầu chỉnh sửa". Chỉ người tạo. Tham chiếu: CF_09, CF_01. | SRS UC119-124.3 #1 |
| A2 | Hành động | "Chỉnh sửa" | Button | — | — | N/A | Chỉ khi "Lưu nháp" / "Yêu cầu chỉnh sửa". Chỉ người tạo. Tham chiếu: CF_03. | SRS UC119-124.3 #2 |
| A3 | Hành động | "Xem chi tiết" | Button | — | — | N/A | Luôn hiển thị. Read-only. Tham chiếu: CF_07. | SRS UC119-124.3 #3 |
| A4 | Hành động | "Xem vòng đời" | Button | — | — | N/A | Luôn hiển thị. Popup Audit Trail. Tham chiếu: CF_06. | SRS UC119-124.3 #4 |
| A5 | Hành động | "In" | Button | — | — | N/A | Luôn hiển thị. Tham chiếu: CF_05. | SRS UC119-124.3 #5 |
| A6 | Hành động | "Export" | Button | — | — | N/A | Luôn hiển thị. File Excel. Tham chiếu: CF_04. | SRS UC119-124.3 #6 |
| A7 | Hành động | "Xóa" | Button | — | — | N/A | "Lưu nháp" VÀ chưa từng nộp. Chỉ người tạo. Tham chiếu: CF_08. | SRS UC119-124.3 #7 |

---

## 5. Object Attributes & Behavior Definition

### 5.1 Màn hình Danh sách (UC119-124.1)

| Object / Component | System States | Interaction Matrix | Object Behavior |
|--------------------|---------------|--------------------|-----------------|
| Yearpicker "Năm" | Enabled. Default: Năm hiện tại. | Click: Mở picker. | Thay đổi → lọc danh sách kỳ hạn ngay. Tham chiếu: CMR_07. |
| Dropdown "Trạng thái kỳ" | Enabled. Default: Null. | Click: Mở checkbox list. | Multi-select. Lọc ngay. Tham chiếu: CMR_04. |
| Dropdown "Trạng thái báo cáo" | Enabled. Default: Null. | Click: Mở checkbox list. | Multi-select. Lọc ngay. Tham chiếu: CMR_03. |
| Search "Mã báo cáo" | Enabled. | Gõ: lọc ngay. | Không tìm thấy → "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. |
| Label "Kỳ hạn báo cáo" | Default: Collapse. | Click: Toggle expand/collapse. | Expand → hiển thị BC trong kỳ, sắp xếp mới → cũ. |
| Button "Lập báo cáo" | Visible khi "Trong thời hạn". Hidden khác. | Click: Mở form Lập BC. | Tham chiếu: CF_01, CMR_04. |
| Button "Import" | Visible khi "Trong thời hạn". Hidden khác. | Click: Mở popup Import. | — |
| Button "Nộp" (Hành động) | Visible khi "Lưu nháp" / "YCCS". Chỉ người tạo. | Click: Validate → Popup xác nhận. | Tham chiếu: CF_09. Notification → Cục ĐTNN. |
| Button "Chỉnh sửa" (Hành động) | Visible khi "Lưu nháp" / "YCCS". Chỉ người tạo. | Click: Mở màn Chỉnh sửa. | Tham chiếu: CF_03. |
| Button "Xem chi tiết" | Visible tất cả trạng thái. | Click: Mở full-page read-only. | Tham chiếu: CF_07. |
| Button "Xem vòng đời" | Visible tất cả trạng thái. | Click: Popup Timeline. | Tham chiếu: CF_06. |
| Button "In" | Visible tất cả trạng thái. | Click: Print Preview. | Tham chiếu: CF_05. |
| Button "Export" | Visible tất cả trạng thái. | Click: Tải Excel. | Tham chiếu: CF_04. |
| Button "Xóa" | Visible khi "Lưu nháp" VÀ chưa từng nộp. Chỉ người tạo. | Click: Popup P04. | Soft-delete + audit log. Tham chiếu: CF_08. |

### 5.2 Màn hình Lập báo cáo (UC119-124.2)

| Object / Component | System States | Interaction Matrix | Object Behavior |
|--------------------|---------------|--------------------|-----------------|
| Mode Detect (khi mở form) | Background health-check | Auto khi mount form | API OK → Mode B (auto-fill toàn bộ dòng FDI). API Fail/Timeout → Mode A + Toast T05: "Không kết nối được API Tổng cục Hải quan. Vui lòng nhập thủ công." Không có toggle/switch UI. |
| Number "Năm báo cáo" (H1) | Enabled. Default năm hiện tại. | Nhập/chọn. | Validate: 4 chữ số, ≤ năm hiện tại. Lỗi: "Năm báo cáo không hợp lệ". |
| Text "MST" (C2) — Dòng manual | Enabled. Default Null. | Blur: validate + debounce 500ms → gọi API CSDL ĐK KD. | Debounce 500ms: sửa MST trong 500ms → cancel API call cũ. Validate định dạng 10/14 số; trùng trong bảng → lỗi inline "Mã số thuế này đã được nhập ở dòng [STT]. Vui lòng kiểm tra lại.". MST hợp lệ → API tìm thấy → auto-fill C3/C4/C5 + Disabled; không tìm thấy → C3/C4/C5 Enabled. |
| Text "MST" (C2) — Dòng API | Disabled. | N/A. | Auto-fill từ API Hải quan. Không sửa. |
| Date "Ngày cấp" (C3) — Dòng manual | Disabled (sau API fill) / Enabled (fallback). | Nhập tay khi Enabled. | Validate ≤ ngày hiện tại. Định dạng dd/MM/yyyy. Tham chiếu: CMR_12. |
| Date "Ngày cấp" (C3) — Dòng API | Always Disabled. | N/A. | Auto-fill từ API Hải quan. |
| Text "Tên DN" (C4) | Manual: Disabled/Enabled tương tự C3. API: Always Disabled. | Nhập tay khi Enabled. | Tham chiếu: CMR_06, CMR_12. |
| Dropdown "Tỉnh/TP" (C5) | Manual: Disabled/Enabled tương tự C3. API: Always Disabled. | Click mở danh mục 63 Tỉnh/TP khi Enabled. | Tham chiếu: CMR_07, CMR_12. |
| Decimal "Nhập khẩu USD" (C6) — Manual | Enabled. | Nhập số. | **Precision 2 chữ số thập phân, round half up.** Validate ≥ 0 (cấm âm). Thay đổi → T1 update real-time. Tham chiếu: CMR_05. |
| Decimal "Nhập khẩu USD" (C6) — API | Disabled. | N/A. | Auto-fill từ SUM tờ khai. **Bảo toàn nguồn chính thống Hải quan (không cho sửa).** |
| Calculated "Tổng cộng" (T1) | Always Disabled. | N/A. | SUM(C6) cả dòng API + manual. Real-time mỗi khi C6/thêm/xóa dòng. Decimal 2dp. |
| Label "Nơi lập báo cáo" (F1) | Disabled. | N/A. | Auto-fill tên Tỉnh/TP theo trụ sở Cục HQ đăng nhập. Tham chiếu: CMR_12. |
| Date "Ngày/tháng/năm" (F2) | Disabled. | N/A. | Auto-fill current system date. Real-time. Tham chiếu: CMR_12. |
| Button "Thêm dòng" (B1) | Enabled khi < 500 dòng. Disabled khi = 500. | Click: Thêm dòng manual cuối bảng. | STT tự tăng. Vượt 500 → Toast "Vượt quá số dòng tối đa cho phép (500)". |
| Icon "Xóa dòng" (B2) | **Chỉ hiện trên dòng manual.** Dòng API: không có icon. | Click: Popup [Đồng ý]/[Hủy]. | Sau xóa → STT re-index. T1 recalculate. Tham chiếu: CMR_06. |
| Button "Lưu nháp" (B3) | Enabled. | Click: Lưu. | Toast T01 "Thành công" / T07 "Lưu nháp không thành công" (bảng rỗng) / T05 lỗi hệ thống. Tham chiếu: CF_01. |
| Button "Nộp báo cáo" (B4) | Enabled. | Click: Validate → Popup P01 xác nhận. | Validate C2-C6 trên toàn bộ dòng → thiếu → inline "Trường bắt buộc". Empty table (0 dòng) → Toast "Vui lòng nhập ít nhất 1 dòng dữ liệu". Nộp OK → Toast T02 + Notification. Tham chiếu: CF_01. |
| Button "Hủy" (B5) | Enabled. | Click: Dirty check → Popup CMR_14 hoặc quay về. | Tham chiếu: CF_01, CMR_14. |

### 5.3 Mode A vs Mode B — Row Mix & Visual Identification

| Khía cạnh | Dòng API (Mode B) | Dòng Manual (Mode A / bổ sung Mode B) |
|-----------|-------------------|---------------------------------------|
| Nguồn | API Tổng cục Hải quan (SUM tờ khai) | User nhập tay + API CSDL ĐK KD |
| C2-C6 trạng thái | **Disabled toàn bộ** | Enabled (hoặc Disabled sau API CSDL fill C3-C5) |
| Icon Xóa (B2) | **Không có** | Có |
| Visual | Icon/tag "API" | Không có tag |
| Thêm/Sửa/Xóa | Không | Có (tất cả) |
| Tổng cộng (T1) | Tính vào SUM | Tính vào SUM |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Xem danh sách báo cáo (UC119)

**A. Workflows**

| Step | Actor | Action | System Response (Happy) | Alternative | Exception |
|------|-------|--------|-------------------------|-------------|-----------|
| 1 | User | Truy cập menu: Báo cáo → Quản lý ĐTNN vào VN → Nhập khẩu TCKT (Mẫu 8c) | Hệ thống hiển thị danh sách kỳ hạn năm, collapse mặc định, sắp xếp giảm dần. Năm = năm hiện tại. | — | Lỗi tải → Toast T05. |
| 2 | User | Click expand kỳ | Hiển thị BC trong kỳ, sắp xếp mới → cũ. | Kỳ chưa có BC → Empty State "Chưa có báo cáo nào cho kỳ này". | — |
| 3 | User | Dùng bộ lọc (Năm / Trạng thái kỳ / Trạng thái BC / Mã BC) | Lọc instant, kết quả hiển thị ngay. | Không kết quả → "Không tìm thấy kết quả". | — |
| 4 | User | Click [Lập báo cáo] | Mở form Lập BC. Trigger Mode detect. | — | Nút ẩn nếu không "Trong thời hạn". |

**B. Business Rules**
- Mỗi đơn vị chỉ thấy BC của đơn vị mình (CMR_02).
- Sắp xếp kỳ hạn giảm dần (mới nhất lên đầu).
- Nút [Lập báo cáo] và [Import] chỉ hiển thị khi "Trong thời hạn".
- Phân trang (CMR_10).

### 6.2 Mode Detect & Lập BC (UC120)

**A. Workflows — Mode Detect (Pre-step)**

| Step | Actor | Action | System Response |
|------|-------|--------|-----------------|
| 0a | System | Khi form Lập BC mount | Gọi health-check API Tổng cục Hải quan. |
| 0b | System | API OK | **Mode B kích hoạt.** Auto-scan tờ khai NK trong kỳ theo danh sách MST FDI, SUM theo MST, auto-fill toàn bộ dòng. Dòng API = Disabled. |
| 0c | System | API Fail/Timeout | **Mode A kích hoạt.** Toast T05: "Không kết nối được API Tổng cục Hải quan. Vui lòng nhập thủ công." Form Enabled để nhập tay. |
| 0d | System | API trả partial (VD: 50/200 MST) | **Mode B + Partial.** Dòng API fill với data có. Toast warning: "Dữ liệu API có thể chưa đầy đủ, vui lòng kiểm tra và bổ sung thủ công." User thêm dòng manual bổ sung. **Không rollback** dòng API đã fill. |

**B. Workflows — Mode A (Nhập thủ công)**

| Step | Actor | Action | System Response (Happy) | Alternative | Exception |
|------|-------|--------|-------------------------|-------------|-----------|
| 1 | User | Nhấn [Thêm dòng] | Thêm 1 dòng manual. STT tự tăng. C2-C6 Enabled. | — | Đạt 500 dòng → Toast "Vượt quá số dòng tối đa cho phép (500)". Chặn thêm. |
| 2 | User | Nhập MST vào C2 + blur (debounce 500ms) | Validate định dạng (10/14 số). Validate trùng trong bảng. MST hợp lệ + không trùng → gọi API CSDL ĐK KD. Tìm thấy → auto-fill C3/C4/C5 + Disabled. Không tìm thấy → C3/C4/C5 Enabled. | User sửa MST trong 500ms → cancel API call cũ. | Sai format → inline error. Trùng → "Mã số thuế này đã được nhập ở dòng [STT]. Vui lòng kiểm tra lại." |
| 3 | User | Nhập C6 (Nhập khẩu USD) | Validate ≥ 0. Precision 2 chữ số thập phân round half up. T1 update real-time. | — | C6 < 0 → inline error. |
| 4 | User | Nhấn [Xóa dòng] (B2) trên dòng manual | Popup xác nhận → Đồng ý → xóa. STT re-index. T1 recalculate. | User chọn [Hủy] → đóng popup. | — |
| 5 | User | Nhấn [Lưu nháp] | Lưu trạng thái "Lưu nháp". Toast T01. | Bảng rỗng → Toast T07 "Lưu nháp không thành công / Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp". | Lỗi server → Toast T05. |

**C. Workflows — Mode B (API Tổng cục Hải quan)**

| Step | Actor | Action | System Response (Happy) | Alternative | Exception |
|------|-------|--------|-------------------------|-------------|-----------|
| 1 | System | Sau Mode detect OK | Quét toàn bộ tờ khai NK đã thông quan trong kỳ có MST ∈ danh sách FDI. SUM theo MST → điền C2-C6. Tất cả dòng API Disabled. Icon/tag "API". Không có icon Xóa. | — | — |
| 2 | User | Thêm dòng manual bổ sung (B1) | Hành vi như Mode A (Workflow B bước 1-4). | — | — |
| 3 | User | Hiệu chỉnh dòng API | **Không cho phép.** C2-C6 dòng API Disabled, không có icon Xóa. | Có thể thêm dòng manual bổ sung. | — |
| 4 | T1 | SUM auto | SUM(C6) tính cả dòng API + manual. Real-time. | — | — |

**D. Workflows — Nộp (UC121)**

| Step | Actor | Action | System Response (Happy) | Alternative | Exception |
|------|-------|--------|-------------------------|-------------|-----------|
| 1 | User | Nhấn [Nộp báo cáo] | Validate C2-C6 trên toàn bộ dòng + empty table check. | — | Thiếu trường → inline "Trường bắt buộc" tại từng ô. Chặn nộp. Empty table (0 dòng) → Toast "Vui lòng nhập ít nhất 1 dòng dữ liệu". |
| 2 | System | Popup P01 xác nhận | "Bạn có chắc chắn muốn nộp báo cáo này?" | User chọn [Hủy] → quay lại form. | — |
| 3 | User | Xác nhận nộp | Trạng thái "Chờ duyệt". Toast T02. Notification → Cục ĐTNN. Audit log. | — | Lỗi server → Toast T05. Concurrent conflict (optimistic locking) → thông báo conflict, yêu cầu refresh. |

**E. Workflows — Chỉnh sửa (UC122)**

| Step | Actor | Action | System Response (Happy) |
|------|-------|--------|-------------------------|
| 1 | User | Nhấn [Chỉnh sửa] (Hành động) | Mở form Edit. Dữ liệu load. Dòng API vẫn Disabled. |
| 2 | User | Sửa + Lưu nháp / Nộp | Validate + lưu. Concurrent conflict → thông báo + refresh. |

- Điều kiện: "Lưu nháp" hoặc "Yêu cầu chỉnh sửa". Chỉ người tạo. Tham chiếu: CF_03.

**F. Workflows — Xem / In / Export (UC123)**

- Xem chi tiết: CF_07 — Full-page, toàn bộ Disabled.
- Xem vòng đời: CF_06 — Popup Timeline / Audit Trail.
- In: CF_05 — Print Preview PDF → hộp thoại in trình duyệt.
- Export: CF_04 — File Excel (.xlsx), tên file theo quy tắc CF_04.

**G. Workflows — Xóa (UC124)**

- Điều kiện: "Lưu nháp" VÀ chưa từng nộp. Chỉ người tạo.
- Popup P04 xác nhận → Đồng ý → soft-delete + audit log + Toast T08.
- Tham chiếu: CF_08.

**H. Business Rules & Validations**

| Field | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|-------|----------|---------------------|-----------|-------------------------------|
| H1 Năm BC | Yes | Số nguyên 4 chữ số, ≤ năm hiện tại | — | "Năm báo cáo không hợp lệ" |
| C2 MST | Yes | 10 hoặc 14 chữ số; unique trong bảng | — | "Trường bắt buộc" / "Mã số thuế này đã được nhập ở dòng [STT]. Vui lòng kiểm tra lại." / (sai định dạng — cần BA xác nhận verbatim) |
| C3 Ngày cấp | Yes | dd/MM/yyyy, ≤ today | — | "Trường bắt buộc" / "Ngày cấp không được lớn hơn ngày hiện tại" *(đề xuất)* |
| C4 Tên DN | Yes | Text. CMR_06. | — | "Trường bắt buộc" |
| C5 Tỉnh/TP | Yes | Dropdown 63 Tỉnh/TP | — | "Trường bắt buộc" |
| C6 Nhập khẩu USD | Yes | Decimal ≥ 0, precision 2dp round half up | ≥ 0 | "Trường bắt buộc" / "Giá trị phải ≥ 0" *(đề xuất)* |
| Max rows | — | Dynamic Table tối đa 500 dòng | ≤ 500 | "Vượt quá số dòng tối đa cho phép (500)" |
| Empty table (Nộp) | — | Bảng ≥ 1 dòng | ≥ 1 | "Vui lòng nhập ít nhất 1 dòng dữ liệu" |

**I. UI/UX Feedback**

| Type | Content | Trigger |
|------|---------|---------|
| Toast T01 | "Đã lưu báo cáo thành công" | Lưu nháp thành công |
| Toast T02 | "Đã nộp báo cáo thành công" | Nộp thành công |
| Toast T05 | "Không kết nối được API Tổng cục Hải quan. Vui lòng nhập thủ công." | API Hải quan fail/timeout (Mode A kích hoạt) |
| Toast T05 (chung) | Lỗi hệ thống chung | Lưu/Nộp lỗi server |
| Toast T07 | "Lưu nháp không thành công / Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp" | Lưu nháp với bảng rỗng |
| Toast T08 | "Xóa báo cáo thành công" | Sau khi xóa |
| Toast (Max) | "Vượt quá số dòng tối đa cho phép (500)" | Thêm dòng thứ 501 |
| Toast (Empty) | "Vui lòng nhập ít nhất 1 dòng dữ liệu" | Nộp với 0 dòng |
| Toast (Partial) | "Dữ liệu API có thể chưa đầy đủ, vui lòng kiểm tra và bổ sung thủ công." | API Hải quan trả partial |
| Popup P01 | "Bạn có chắc chắn muốn nộp báo cáo này?" | Nhấn [Nộp báo cáo] |
| Popup P04 | "Bạn có chắc chắn muốn xóa?" | Nhấn [Xóa] |
| Popup CMR_14 | "Dữ liệu chưa được lưu. Bạn có chắc chắn muốn rời khỏi trang này không?" | Nhấn [Hủy] khi dirty form |
| Inline (MST trùng) | "Mã số thuế này đã được nhập ở dòng [STT]. Vui lòng kiểm tra lại." | Validate MST trùng on-blur |
| Inline (Required) | "Trường bắt buộc" | Validate trường bắt buộc khi Nộp |

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis | Data Consistency Verification |
|---------------------------|-----------------|-------------------------------|
| Mode Detect (health-check API Hải quan) | Quyết định Mode A vs Mode B khi mở form. | Không có toggle UI — đảm bảo hành vi deterministic dựa trên trạng thái API. |
| API CSDL Đăng ký KD (Mode A blur C2) | Auto-fill C3/C4/C5 từ MST. Không tìm thấy → Enabled fallback. | Khóa cứng C3-C5 sau fill (CMR_12) → đảm bảo nguồn chính thống không bị sửa. |
| API Tổng cục Hải quan (Mode B scan) | Quét tờ khai NK, SUM theo MST ∈ FDI → auto-fill C2-C6. | Dòng API Disabled toàn bộ + không có icon Xóa → bảo toàn tính toàn vẹn dữ liệu Hải quan. |
| API Partial Failure | Mode B vẫn chạy với data có; dòng API Disabled; user thêm manual bổ sung. | **Không rollback** dòng API đã fill → đảm bảo dữ liệu Hải quan được giữ nguyên. Trách nhiệm verification thuộc user (Toast warning). |
| C6 change / thêm / xóa dòng | T1 SUM(C6) real-time (cả API + manual). | Tổng luôn đồng bộ với các dòng hiện tại. Decimal 2dp. |
| Nộp BC → Notification | Sau Nộp thành công → notification cho Cục ĐTNN. | Cần xác nhận kênh notification (web push / in-app / email). |
| 8c "Đã nộp" → Mẫu 8a (UC107-112) | User Mẫu 8a nhấn [Tổng hợp] → query 8c Đã nộp → Group By Tỉnh (C5), SUM C6. | **Manual, không auto real-time.** 8c sửa sau → 8a KHÔNG tự cập nhật. Trách nhiệm user Mẫu 8a tổng hợp lại nếu cần. |
| MST trùng giữa 8b (xuất) và 8c (nhập) | **Cho phép** — 1 DN FDI có thể vừa XK vừa NK. | Không cần cross-report warning. |
| Concurrent edit (2 user cùng BC) | Optimistic locking. User lưu sau → conflict + phải refresh. | Không cho ghi đè dữ liệu user trước. |
| Xóa BC → Audit Log | Soft-delete + ghi log (Actor, Action, Timestamp). | Log cần đủ thông tin để rollback nếu cần. |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given *(precondition)* | When *(user action)* | Then *(expected result)* |
|------|----------|------------------------|----------------------|--------------------------|
| AC-01 | Validate MST sai định dạng | User ở form Lập BC, Mode A, nhập MST không đúng 10/14 số (VD: "ABC123") | Blur khỏi ô MST (debounce 500ms) | Hệ thống hiển thị lỗi inline tại ô C2. *(Nội dung exact message — BA xác nhận)* |
| AC-02 | Validate MST trùng | Dòng 1 đã nhập MST "1234567890" | Nhập cùng MST "1234567890" ở dòng 2 và blur | Inline: "Mã số thuế này đã được nhập ở dòng 1. Vui lòng kiểm tra lại." |
| AC-03 | Auto-fill CSDL ĐK KD thành công (Mode A) | User Mode A, nhập MST hợp lệ + không trùng | Blur (debounce 500ms) | API gọi thành công → C3/C4/C5 auto-fill và Disabled. |
| AC-04 | Auto-fill CSDL ĐK KD không tìm thấy — Fallback (Mode A) | User Mode A, nhập MST hợp lệ | Blur + API trả null/rỗng | C3/C4/C5 chuyển Enabled để nhập tay. |
| AC-05 | Mode Detect | User nhấn [Lập báo cáo] | Form mount | API OK → Mode B + auto-fill toàn bộ dòng FDI. API Fail/Timeout → Mode A + Toast T05 "Không kết nối được API Tổng cục Hải quan. Vui lòng nhập thủ công." |
| AC-06 | Mode B — Dòng API Disabled | Mode B đã kích hoạt | Scan + SUM hoàn tất | Dòng API C2-C6 Disabled, có tag "API", KHÔNG có icon Xóa. User vẫn thêm được dòng manual bằng [Thêm dòng]. |
| AC-07 | API Partial Failure | Mode B nhưng API trả 50/200 MST | — | Dòng API fill với data có (Disabled). Toast warning "Dữ liệu API có thể chưa đầy đủ, vui lòng kiểm tra và bổ sung thủ công.". Không rollback. User thêm dòng manual bổ sung. |
| AC-08 | Tính tổng real-time | Bảng có ít nhất 1 dòng với C6 có giá trị | User nhập/sửa/xóa C6 hoặc thêm/xóa dòng manual | T1 = SUM(C6) cả dòng API + manual. Cập nhật ngay. Decimal 2dp. |
| AC-09 | Validate bắt buộc khi Nộp | Bảng có dòng với C2-C6 một số bị trống | Nhấn [Nộp báo cáo] | Inline "Trường bắt buộc" tại từng ô vi phạm. Popup P01 không mở. Chặn nộp. |
| AC-10 | Empty table submit | Form có 0 dòng dữ liệu | Nhấn [Nộp báo cáo] | Toast "Vui lòng nhập ít nhất 1 dòng dữ liệu". Chặn nộp. |
| AC-11 | Max rows (500) | Bảng đã có 500 dòng | Nhấn [Thêm dòng] | Toast "Vượt quá số dòng tối đa cho phép (500)". Không thêm dòng. |
| AC-12 | Decimal precision C6 | User nhập 1234.567 vào C6 | Blur | C6 hiển thị 1234.57 (round half up, 2 chữ số thập phân). |
| AC-13 | Validate C6 âm | User nhập -100 vào C6 | Blur / Lưu / Nộp | Inline error "Giá trị phải ≥ 0" *(verbatim cần BA)*. Chặn lưu/nộp. |
| AC-14 | Lưu nháp thành công | Ít nhất 1 dòng đã điền dữ liệu | Nhấn [Lưu nháp] | Toast T01 "Đã lưu báo cáo thành công". Trạng thái "Lưu nháp". |
| AC-15 | Lưu nháp — Bảng rỗng | Form không có dòng nào / chưa điền gì | Nhấn [Lưu nháp] | Toast T07 "Lưu nháp không thành công / Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp". |
| AC-16 | Xóa dòng — chỉ dòng manual | Mode B có 10 dòng API + 2 dòng manual | Xem icon Xóa | Chỉ 2 dòng manual có icon Xóa; 10 dòng API không có. |
| AC-17 | Hủy với dirty form | User đã thay đổi dữ liệu nhưng chưa lưu | Nhấn [Hủy] | Popup CMR_14: "Dữ liệu chưa được lưu. Bạn có chắc chắn muốn rời khỏi trang này không?" |
| AC-18 | Liên kết 8c → 8a | BC 8c Trạng thái "Đã nộp" với C5/C6 đầy đủ | User Mẫu 8a nhấn [Tổng hợp] | Mẫu 8a query 8c Đã nộp, Group By Tỉnh (C5), SUM C6 → điền cột Nhập khẩu. **Manual, không auto real-time.** |
| AC-19 | Concurrent edit | User A và User B cùng mở 1 BC ở Edit mode. A lưu trước. | B nhấn [Lưu nháp] | B nhận thông báo conflict, phải refresh trước khi lưu lại (optimistic locking). |
| AC-20 | MST trùng giữa 8b và 8c | 1 DN FDI xuất hiện ở cả 8b và 8c | — | **Cho phép**, không cảnh báo cross-report. |
| AC-21 | Nộp thành công | BC "Lưu nháp", đủ trường bắt buộc | Nhấn [Nộp] → Popup P01 [Xác nhận] | Trạng thái "Chờ duyệt". Toast T02. Notification → Cục ĐTNN. Audit log. |
| AC-22 | Xóa BC | BC "Lưu nháp", chưa từng nộp, chính người tạo | Nhấn [Xóa] → P04 [Đồng ý] | Soft-delete. Toast T08. Audit log. |

---

## 9. Non-functional Requirements (NFR)

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| Performance — API | API CSDL Đăng ký KD và API Tổng cục Hải quan: response time ≤ 5 giây. Quá 5s (timeout) → Toast T05 + Mode A fallback (nhập tay). | SRS 3.5 |
| Performance — UI | Validate MST on-blur + debounce 500ms (cancel API call cũ nếu user sửa trong 500ms). | SRS C2 |
| Performance — Max rows | Dynamic Table tối đa 500 dòng. | SRS bảng dữ liệu |
| Security & Audit | Chỉ user thuộc Cục Hải quan / Bộ Tài chính thấy và lập BC. Mọi thao tác Lưu/Xóa/Nộp ghi audit log (Actor, Action, Timestamp). | SRS 3.5 |
| Concurrency | Optimistic locking — user lưu sau nhận conflict, phải refresh trước khi lưu lại. Không cho ghi đè. | SRS 3.5 |
| Data Precision | C6 (Nhập khẩu USD): Decimal 2 chữ số thập phân, round half up. T1 cùng precision. | SRS C6, T1 |
| Data Integrity | Dòng API Disabled toàn bộ, không có icon Xóa → bảo toàn nguồn Hải quan. | SRS Mode B |
| Data Retention | Chưa quy định thời gian lưu trữ BC. | Gap (Q1 — Minor) |
| Browser Compatibility | Chưa quy định trong SRS. | Gap (Q2 — Minor) |
| Accessibility | Chưa quy định (WCAG / RTL / font-scaling). | Gap (Q3 — Minor) |
| Notification Channel | Sau Nộp → notification Cục ĐTNN. Kênh cụ thể (web push / in-app / email) chưa chỉ định. | Gap (Q4 — Minor) |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions (Minor — không block test design)

| Q# | Câu hỏi | Liên quan | Mức độ | Trạng thái |
|----|---------|-----------|--------|------------|
| Q1 | Data Retention: Thời gian lưu trữ BC (đặc biệt BC đã xóa soft-delete)? | NFR | Low | Open |
| Q2 | Browser Compatibility: Hệ thống support những trình duyệt/phiên bản nào? | NFR | Low | Open |
| Q3 | Accessibility: Có yêu cầu WCAG (A/AA/AAA) không? Hỗ trợ screen reader, keyboard navigation, font scaling? | NFR | Low | Open |
| Q4 | Notification Channel: Kênh notification sau Nộp (web push / in-app / email / SMS)? | Section 7 | Low | Open |
| Q5 | Verbatim error messages: Nội dung chính xác cho các inline error (MST sai định dạng, C6 âm, C3 future date)? | Section 6.2.H | Low | Open |
| Q6 | Audit log — chi tiết: Log có ghi IP / user-agent / giá trị trước-sau không? | NFR Security | Low | Open |
| Q7 | Empty State visual cho Mode B khi API trả 0 MST FDI: Hiển thị gì (bảng rỗng + banner, hay auto-switch Mode A)? | Mode B edge case | Low | Open |
| Q8 | Placeholder cho C2 (MST): Có placeholder gợi ý nhập không? (VD: "Nhập 10 hoặc 14 chữ số") | UI | Low | Open |
| Q9 | Import button (Kỳ hạn Header): Luồng Import chi tiết cho Mẫu 8c (CF_02 Case nào)? | Section 4.1 #8 | Low | Open |
| Q10 | Visual "tag API" cho dòng API: Hiển thị cụ thể như thế nào (badge / icon / màu nền)? | Section 5.3 | Low | Open |

### 10.2 Dependencies

- **API CSDL Đăng ký Kinh doanh** — cung cấp dữ liệu DN khi nhập MST (Mode A).
- **API Tổng cục Hải quan** — cung cấp dữ liệu tờ khai NK, SUM theo MST FDI (Mode B).
- **Master data MST FDI** — danh sách MST của các DN FDI (dùng để filter trong Mode B).
- **Danh mục 63 Tỉnh/Thành phố** — cho C5.
- **UC107-112 (Mẫu 8a)** — consumer đọc dữ liệu 8c "Đã nộp" khi nhấn [Tổng hợp].
- **UC113-118 (Mẫu 8b — Xuất khẩu)** — cross-report: MST có thể trùng, không cảnh báo.
- **Common Rules:** CMR_02, CMR_03, CMR_04, CMR_05, CMR_06, CMR_07, CMR_08, CMR_09, CMR_10, CMR_12, CMR_14.
- **Common Flows:** CF_01, CF_02, CF_03, CF_04, CF_05, CF_06, CF_07, CF_08, CF_09.

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|-------------------|
| v1 | 2026-05-06 | QC Auditor (AI) | Fast-track Audit — cho điểm 100/100 không phân tích sâu. Không có câu hỏi nào. |
| v2 | 2026-05-07 | QC Auditor Agent | Deep Audit. Hạ điểm xuống ~72.7/100. Phát hiện 10 Open Questions (Q1 Mode detect, Q2 MST partial, Q3 API partial, Q4-Q5 decimal, Q6 max rows, Q7 empty table, Q8 8c→8a, Q9 cross-report, Q10 prefix). 4 Blocking Gaps. |
| v3 | 2026-05-07 | QC Auditor Agent | Re-Audit sau khi SRS được nâng cấp lên v1.2 / v2.0. BA đã giải quyết hầu hết Blocking Gaps từ v2: Mode A/B auto-detect + no UI toggle (Q1), debounce 500ms (Q2), API partial failure handling (Q3), decimal precision 2dp round half up (Q4-Q5), max 500 dòng (Q6), empty table rule (Q7), 8c→8a manual link (Q8), MST cross-report allowed (Q9), optimistic locking (new). Score nâng từ 72.7 → **87.3/100** (READY with Minor Gaps). Chỉ còn 10 Open Questions mức Low (NFR hoàn chỉnh, verbatim messages, placeholders) — không block test design. |

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status | Ghi chú |
|---|---------------|---------|-------|--------|---------|
| 1 | Feature Identity (Document Metadata) | 5 | 5/5 | PASS | UC-ID, biểu mẫu, kỳ năm, đối tượng lập, quy tắc mã BC rõ ràng. SRS đã nêu đề xuất bổ sung "DTNN" vào CMR_09. |
| 2 | Objective & Scope | 5 | 5/5 | PASS | Objective + In/Out of Scope đầy đủ. Liên kết 8c → 8a được nêu rõ. |
| 3 | Actors & User Roles | 10 | 9/10 | PARTIAL | 6 actor rõ ràng (Cục HQ, Bộ TC, API CSDL ĐK KD, API Hải quan, Cục ĐTNN, Mẫu 8a). Trừ 1 điểm: mức độ phân biệt quyền giữa Cục HQ và Bộ TC chưa sâu (assume ngang quyền). |
| 4 | Preconditions & Postconditions | 10 | 9/10 | PARTIAL | Preconditions đầy đủ (bao gồm health-check API). Postconditions rõ cho Lưu/Nộp/Chỉnh sửa/Xóa/Export + tác động đến 8a. Trừ 1 điểm: thiếu postcondition cho Mode A fallback và Mode B Partial (đã có trong workflow nhưng chưa tổng hợp). |
| 5 | UI Object Inventory & Mapping | 15 | 13/15 | PARTIAL | 34 objects chi tiết (5 sub-tables). Trừ 2 điểm: thiếu placeholder C2 (Q8), chi tiết visual "tag API" (Q10), luồng Import chi tiết (Q9). |
| 6 | Object Attributes & Behavior Definition | 20 | 17/20 | PARTIAL | Behavior rõ ràng cho Mode A / Mode B / Mode detect / Partial failure. Phân biệt dòng API vs manual chi tiết. Trừ 3 điểm: Empty State Mode B khi API trả 0 MST (Q7), verbatim error messages (Q5), audit log chi tiết (Q6). |
| 7 | Functional Logic & Workflow Decomposition | 20 | 17/20 | PARTIAL | 7 sub-workflows (Danh sách, Mode Detect, Mode A, Mode B, Nộp, Chỉnh sửa, Xem/In/Export, Xóa). Business rules + validations + UI feedback đầy đủ. Trừ 3 điểm: Import workflow (CF_02 Case) chưa làm rõ (Q9), 2 verbatim messages cần BA, edge case khi user chuyển mode giữa chừng (nếu API connect/disconnect trong session). |
| 8 | Functional Integration Analysis | 10 | 8/10 | PARTIAL | 10 integration points rõ ràng (Mode detect, API CSDL, API Hải quan, API Partial, SUM realtime, Notification, 8c→8a manual, 8b↔8c cross-report, Concurrent, Audit log). Trừ 2 điểm: kênh notification chưa xác định (Q4), log chi tiết chưa spec (Q6). |
| 9 | Acceptance Criteria | 10 | 9/10 | PARTIAL | 22 AC bao phủ: validate MST, Mode detect, Mode B API, Partial, real-time SUM, validate required, empty table, max rows, decimal precision, C6 âm, Lưu/Nộp thành công/fail, xóa dòng API vs manual, dirty form, 8c→8a, concurrent, cross-report, Nộp, Xóa. Trừ 1 điểm: thiếu AC cho Accessibility / Browser compat. |
| 10 | Non-functional Requirements | 5 | 4/5 | PARTIAL | Performance (API 5s, debounce 500ms, max 500 dòng), Security + Audit, Concurrency (optimistic locking), Data Precision, Data Integrity đã có. Trừ 1 điểm: Data Retention, Browser Compatibility, Accessibility, Notification Channel chưa có (Q1-Q4). |
| **Total** | | **110** | **96/110** | | |

> **Normalized Score:** 96/110 × 100 ≈ **87.3/100** (READY with Minor Gaps)

---

## Unified Gap & Question Report

### Tổng hợp Gaps

| Gap # | Section | Loại | Mô tả | Mức độ | Đề xuất |
|-------|---------|------|-------|--------|---------|
| GAP-01 | 9 | Missing | Data Retention chưa quy định. | Low | BA/PO xác nhận thời gian lưu trữ BC (đặc biệt sau soft-delete). |
| GAP-02 | 9 | Missing | Browser Compatibility chưa quy định. | Low | BA/Dev confirm matrix trình duyệt + phiên bản tối thiểu. |
| GAP-03 | 9 | Missing | Accessibility chưa quy định. | Low | BA/UX confirm yêu cầu WCAG (A/AA/AAA), keyboard navigation, screen reader. |
| GAP-04 | 7 | Missing | Notification channel sau Nộp BC: web push / in-app / email? | Low | BA/Dev xác nhận. |
| GAP-05 | 6.2.H / 8 | Ambiguity | Verbatim error messages cho MST sai định dạng, C6 âm, C3 future. | Low | BA cung cấp nội dung exact text. |
| GAP-06 | 9 Security | Missing | Audit log chi tiết: IP / user-agent / before-after? | Low | BA/Security xác nhận trường ghi log. |
| GAP-07 | 5.2 / 6.2.C | Missing | Empty State Mode B khi API trả 0 MST FDI. | Low | BA xác nhận hành vi (bảng trống + banner / fallback Mode A). |
| GAP-08 | 4.3 C2 | Missing | Placeholder C2 MST. | Low | BA đề xuất text (VD: "Nhập 10 hoặc 14 chữ số"). |
| GAP-09 | 4.1 #8 | Missing | Import button workflow chi tiết cho Mẫu 8c. | Low | BA confirm CF_02 Case áp dụng. |
| GAP-10 | 5.3 | Clarification | Visual "tag API" cho dòng API — cụ thể là badge / icon / màu. | Low | BA/UX cung cấp mockup hoặc spec visual. |

### Đánh giá Blocking

- **Blocking Gaps:** 0 (tất cả Open Questions đều ở mức Low, không cản trở test design).
- **Minor Gaps:** 10 (đều có thể dùng default assumption / thống nhất với BA trong giai đoạn test design, không block triển khai test scenario / test case).

### Recommendation

SRS v1.2 / v2.0 đã giải quyết toàn bộ 4 Blocking Gaps từ audit v2 (G-03 phân quyền — đã rõ Cục HQ + Bộ TC + API actor; G-07 Mode B — đã có auto-detect + Partial failure; G-05 UI — đã có decimal precision + max 500 + empty rule; G-08 Integration — đã có 8c→8a manual). Có thể chuyển sang giai đoạn **Test Scenario Design** và **Test Case Design** ngay với 22 AC hiện tại. Các Minor Gaps (Q1-Q10) nên được BA làm rõ trong giai đoạn test case review để hoàn thiện coverage, nhưng không cản trở bắt đầu work.
