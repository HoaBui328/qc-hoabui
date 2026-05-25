# UC335-340: Báo Cáo Audit — Các chỉ số đánh giá hiệu quả kinh tế, xã hội, môi trường của KCN sinh thái

| Thuộc tính | Giá trị |
| --- | --- |
| **Tài liệu** | UC Readiness Review Report |
| **UC ID** | UC335-340 |
| **Tên chức năng** | Các chỉ số đánh giá hiệu quả kinh tế, xã hội, môi trường của khu công nghiệp sinh thái |
| **Ngày audit** | 2026-05-14 |
| **Auditor** | QC Agent |
| **Phiên bản** | v1 |
| **Nguồn tài liệu** | UC335-340_ChiSoDanhGiaHieuQuaKCNST.md |

---

## Section 0: Feature Identity

| Thuộc tính | Giá trị | Status |
| --- | --- | --- |
| UC ID | UC335-340 | ✅ |
| Tên chức năng | Các chỉ số đánh giá hiệu quả kinh tế, xã hội, môi trường của khu công nghiệp sinh thái | ✅ |
| Phân hệ | Báo cáo KKT/KCN | ✅ |
| Mẫu biểu | Mẫu A.5 | ✅ |
| Loại báo cáo | Định kỳ năm | ✅ |
| Hình thức nộp | Báo cáo đơn lẻ (Single report form) | ✅ |
| Giao diện | User site | ✅ |
| Quy tắc sinh mã | EZ_A5_[ID] | ✅ |
| Phạm vi dữ liệu đầu vào | Không có phạm vi | ✅ |

---

## Section 1: Objective & Scope

**Mục tiêu:** ✅ Complete

Cho phép Nhà đầu tư / Tổ chức kinh tế thực hiện dự án lập và nộp báo cáo các chỉ số đánh giá hiệu quả kinh tế, xã hội, môi trường của khu công nghiệp sinh thái (Mẫu A.5) theo kỳ hạn năm.

**Phạm vi (In-scope):** ✅ Complete
- Xem danh sách báo cáo (UC335-340.1)
- Lập báo cáo mới (UC335-340.2)
- Các tác vụ bổ trợ: Xem chi tiết, Xem vòng đời, In, Export, Nộp, Chỉnh sửa, Xóa (UC335-340.3)

**Ngoài phạm vi (Out-of-scope):** ✅ Complete
- Quy trình xét duyệt/phê duyệt báo cáo (thuộc Admin site)
- Quản lý cấu hình kỳ báo cáo
- Import báo cáo chi tiết (tham chiếu CF_02)

---

## Section 2: Actors & User Roles

| Actor | Vai trò | Quyền | Status |
| --- | --- | --- | --- |
| Nhà đầu tư (NĐT) / Tổ chức kinh tế thực hiện dự án | Người lập và nộp báo cáo | Xem, Tạo mới, Chỉnh sửa, Nộp, Xóa, In, Export | ✅ |

**Phân quyền đặc biệt:** ✅ Complete
- Mỗi NĐT chỉ lập 1 báo cáo duy nhất cho toàn bộ KCN mà họ quản lý trong mỗi kỳ.
- NĐT có toàn quyền: Xem, Tạo mới, Chỉnh sửa, Nộp, Xóa, In, Export.

**Cơ quan nhận:** Ban quản lý khu công nghiệp, kinh tế.

---

## Section 3: Preconditions & Postconditions

### Preconditions

| # | Điều kiện | Status |
| --- | --- | --- |
| 1 | Nhà đầu tư được phân quyền lập báo cáo này và đã đăng nhập vào hệ thống | ✅ |
| 2 | Báo cáo xuất hiện ở site user (Nhà đầu tư, doanh nghiệp/tổ chức) | ✅ |
| 3 | Kỳ báo cáo ở trạng thái "Trong thời hạn" để lập mới (CMR_04) | ✅ |

### Postconditions

| # | Chức năng | Hậu điều kiện | Status |
| --- | --- | --- | --- |
| 1 | Xem danh sách | Hiển thị danh sách các kỳ báo cáo, cấu trúc theo CS_01 | ✅ |
| 2 | Lập báo cáo | Tùy thuộc action: Hủy / Xem / Lưu nháp / Gửi báo cáo (CF_01) | ✅ |
| 3 | Tác vụ bổ trợ | Xem chi tiết → full-page read-only (CF_07); Xóa → bản ghi bị xóa (CF_08); Nộp → chuyển trạng thái (CMR_03); Chỉnh sửa → mở form (CF_03) | ✅ |

---

## Section 4: UI Object Inventory & Mapping

### 4.1. Màn hình Danh sách (UC335-340.1)

| # | Tên trường / Label | Kiểu component | Bắt buộc | Giá trị mặc định | Placeholder | Enum values | Section | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Năm | YearPicker | Không | Null | — | Enable/Disable theo data (CS_01) | Khung Điều kiện Lọc & Tìm kiếm | ✅ |
| 2 | Trạng thái kỳ | Multiple-selection Dropdown | Không | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo (CMR_04) | Khung Điều kiện Lọc & Tìm kiếm | ✅ |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Không | Tất cả trạng thái | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa (CMR_03, CMR_07) | Khung Điều kiện Lọc & Tìm kiếm | ✅ |
| 4 | Mã báo cáo | Search bar | Không | Null | "Nhập dữ liệu" | — | Khung Điều kiện Lọc & Tìm kiếm | ✅ |
| 5 | Kỳ hạn báo cáo | Label | — | Null | — | — | Khung Danh sách Kỳ hạn | ✅ |
| 6 | Trạng thái kỳ báo cáo | Label | — | Null | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo (CMR_04) | Khung Danh sách Kỳ hạn | ✅ |
| 7 | Lập báo cáo | Button | — | Null | — | — | Khung Danh sách Kỳ hạn | ✅ |
| 8 | Import | Button | — | Null | — | — | Khung Danh sách Kỳ hạn | ✅ |
| 9 | Mã báo cáo | Label | — | Null | — | — | Khung Danh sách Báo cáo | ✅ |
| 10 | Ngày cập nhật | Label | — | Null | — | — | Khung Danh sách Báo cáo | ✅ |
| 11 | Trạng thái | Label | — | Null | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa (CMR_03) | Khung Danh sách Báo cáo | ✅ |
| 12 | Hành động | Button group | — | Null | — | Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Export, Xóa | Khung Danh sách Báo cáo | ✅ |

### 4.2. Màn hình Lập Báo Cáo (UC335-340.2)

| # | Tên trường / Label | Kiểu component | Bắt buộc | Giá trị mặc định | Placeholder | Enum values | Section | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13 | Cộng sinh công nghiệp (ENV.1) | Number | Có | Null | "Nhập giá trị" | — | I. Môi trường | ✅ |
| 14 | Tuần hoàn tái sử dụng nước thải công nghiệp (EVN.3) | Number | Có | Null | "Nhập giá trị từ 0 - 100%" | 0–100% | I. Môi trường | ✅ |
| 15 | Giám sát giảm phát thải khí nhà kính (EVN.4) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | I. Môi trường | ✅ |
| 16 | Xây dựng và thực hiện cơ chế phối hợp giám sát... (ENV.5) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | I. Môi trường | ✅ |
| 17 | Báo cáo phát triển bền vững (ENV.6) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | I. Môi trường | ✅ |
| 18 | Hệ thống giám sát khung về rủi ro (PM.1) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | II. Quản lý KCN | ✅ |
| 19 | Kế hoạch ứng phó rủi ro (PM.2) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | II. Quản lý KCN | ✅ |
| 20 | Đơn vị hỗ trợ phát triển KCN sinh thái (PM.3) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | II. Quản lý KCN | ✅ |
| 21 | Thành lập mới KCN sinh thái (PM.4) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | II. Quản lý KCN | ✅ |
| 22 | Cơ sở hạ tầng xã hội phục vụ người lao động (SOC.3) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | III. Xã hội | ✅ |
| 23 | Cán bộ quản lý KCN (SOC.5) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | III. Xã hội | ✅ |
| 24 | Duy trì kết nối và đối thoại với cộng đồng (SOC.7) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | III. Xã hội | ✅ |
| 25 | Hợp tác kinh tế (ECO.1) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | IV. Kinh tế | ✅ |
| 26 | Quảng bá thông tin về phát triển KCN sinh thái (ECO.2) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | IV. Kinh tế | ✅ |
| 27 | Tối đa hóa lợi ích cho lao động địa phương (ECO.3) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | IV. Kinh tế | ✅ |
| 28 | Phát triển doanh nghiệp vừa và nhỏ (ECO.4) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | IV. Kinh tế | ✅ |
| 29 | Thúc đẩy doanh nghiệp địa phương (ECO.5) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | IV. Kinh tế | ✅ |
| 30 | Giá trị dịch vụ khu công nghiệp (ECO.6) | Dropdown | Có | Null | "Chọn giá trị" | Có / Không | IV. Kinh tế | ✅ |

### 4.3. Buttons — Màn hình Lập Báo Cáo

| # | Tên | Kiểu component | Điều kiện hiển thị | Section | Status |
| --- | --- | --- | --- | --- | --- |
| B1 | Lưu nháp | Button | Tất cả trạng thái trên form Lập (CF_01) | Khung Button | ✅ |
| B2 | Gửi báo cáo | Button | Tất cả trạng thái trên form Lập (CF_01) | Khung Button | ✅ |
| B3 | Hủy | Button | Tất cả trạng thái trên form Lập (CF_01) | Khung Button | ✅ |
| B4 | Xem chi tiết | Button | Disabled khi chưa lưu nháp lần nào; Enabled sau khi đã lưu (CF_01) | Khung Button | ✅ |

### 4.4. Buttons — Màn hình Tác vụ bổ trợ (UC335-340.3)

| # | Tên | Kiểu component | Điều kiện hiển thị | Phân quyền | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Chỉ khi Lưu nháp (CMR_03) | Người tạo | ✅ |
| 2 | Chỉnh sửa | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa (CMR_03) | Người tạo | ✅ |
| 3 | Xem chi tiết | Button | Tất cả trạng thái (CMR_03) | Tất cả người dùng | ✅ |
| 4 | Xem vòng đời | Button | Tất cả trạng thái (CMR_03) | Tất cả người dùng | ✅ |
| 5 | In | Button | Tất cả trạng thái (CMR_03) | Tất cả người dùng | ✅ |
| 6 | Export | Button | Tất cả trạng thái (CMR_03) | Tất cả người dùng | ✅ |
| 7 | Xóa | Button | Lưu nháp VÀ chưa từng nộp (CF_08) | Người tạo | ✅ |

---

## Section 5: Object Attributes & Behavior Definition

### 5.1. Màn hình Danh sách (UC335-340.1)

| # | Object / Component | System States | Interaction | Behavior | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Năm (YearPicker) | Enabled. Chỉ Enable các năm có data đã nộp hoặc năm tài chính hiện tại (CS_01) | Click → mở picker chọn năm | Chọn năm → lọc danh sách ngay lập tức (real-time filter) | ✅ |
| 2 | Trạng thái kỳ (Multiple Dropdown) | Enabled | Click → mở dropdown multi-select (CMR_07.2) | Chọn/bỏ chọn → lọc real-time. Tag-based input, Counter Tag (+N...) | ✅ |
| 3 | Trạng thái báo cáo (Multiple Dropdown) | Enabled. Default: Tất cả trạng thái | Click → mở dropdown multi-select (CMR_07.2) | Chọn/bỏ chọn → lọc real-time. Giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | ✅ |
| 4 | Mã báo cáo (Search bar) | Enabled | Nhập text → live search (CMR_06) | Debounce 300-500ms. Partial match, case-insensitive. Empty state: "Không tìm thấy kết quả" | ✅ |
| 5 | Kỳ hạn báo cáo (Label) | Read-only. Mặc định Collapse | Click mũi tên → Expand/Collapse | Expand hiển thị danh sách báo cáo trong kỳ. Tham chiếu: CMR_08 | ✅ |
| 6 | Trạng thái kỳ báo cáo (Label) | Read-only | N/A | Hiển thị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo (CMR_04) | ✅ |
| 7 | Lập báo cáo (Button) | Hiển thị + Enabled khi kỳ = "Trong thời hạn". Ẩn khi "Chưa tới hạn" hoặc "Qua kỳ báo cáo" (CMR_04) | Click → mở form Lập báo cáo (CF_01) | Điều hướng sang UC335-340.2 | ✅ |
| 8 | Import (Button) | Hiển thị + Enabled khi kỳ = "Trong thời hạn". Ẩn khi "Chưa tới hạn" hoặc "Qua kỳ báo cáo" (CMR_04) | Click → mở popup Import (CF_02) | Mở màn hình chọn/kéo thả file import | ✅ |
| 9 | Mã báo cáo (Label) | Read-only | N/A | Hiển thị mã theo quy tắc EZ_A5_[ID] (CMR_09) | ✅ |
| 10 | Ngày cập nhật (Label) | Read-only | N/A | Định dạng: dd/MM/yyyy HH:mm | ✅ |
| 11 | Trạng thái (Label) | Read-only | N/A | Hiển thị trạng thái bản ghi (CMR_03) | ✅ |
| 12 | Hành động (Button group) | Hiển thị theo trạng thái bản ghi (CMR_03, UC335-340.3) | Click từng action | Điều hướng theo action tương ứng | ✅ |

### 5.2. Màn hình Lập Báo Cáo (UC335-340.2)

| # | Object / Component | System States | Interaction | Behavior | Status |
| --- | --- | --- | --- | --- | --- |
| 13 | ENV.1 — Cộng sinh công nghiệp (Number) | Enabled | Nhập số | Chỉ chấp nhận số dương (CMR_05). Tooltip: "Nhập số lượng cộng sinh công nghiệp đã thực hiện trong KCN" | ✅ |
| 14 | EVN.3 — Tuần hoàn tái sử dụng nước thải (Number) | Enabled | Nhập số | Số dương, 0-100%. Ngoài khoảng → Error: "Giá trị hợp lệ trong khoảng từ 0 - 100%" (CMR_05). Tooltip: "Tỷ lệ phần trăm nước thải công nghiệp..." | ✅ |
| 15 | EVN.4 — Giám sát giảm phát thải khí nhà kính (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip: "Chương trình và kế hoạch cụ thể để giám sát..." | ✅ |
| 16 | ENV.5 — Cơ chế phối hợp giám sát (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip mô tả chi tiết | ✅ |
| 17 | ENV.6 — Báo cáo phát triển bền vững (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip mô tả chi tiết | ✅ |
| 18 | PM.1 — Hệ thống giám sát khung về rủi ro (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip mô tả chi tiết | ✅ |
| 19 | PM.2 — Kế hoạch ứng phó rủi ro (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip mô tả chi tiết | ✅ |
| 20 | PM.3 — Đơn vị hỗ trợ phát triển KCN sinh thái (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip mô tả chi tiết | ✅ |
| 21 | PM.4 — Thành lập mới KCN sinh thái (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip mô tả chi tiết | ✅ |
| 22 | SOC.3 — Cơ sở hạ tầng xã hội (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip mô tả chi tiết | ✅ |
| 23 | SOC.5 — Cán bộ quản lý KCN (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip mô tả chi tiết | ✅ |
| 24 | SOC.7 — Duy trì kết nối cộng đồng (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip mô tả chi tiết | ✅ |
| 25 | ECO.1 — Hợp tác kinh tế (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip mô tả chi tiết | ✅ |
| 26 | ECO.2 — Quảng bá thông tin (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip mô tả chi tiết | ✅ |
| 27 | ECO.3 — Tối đa hóa lợi ích lao động (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip mô tả chi tiết | ✅ |
| 28 | ECO.4 — Phát triển doanh nghiệp vừa và nhỏ (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip mô tả chi tiết | ✅ |
| 29 | ECO.5 — Thúc đẩy doanh nghiệp địa phương (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip mô tả chi tiết | ✅ |
| 30 | ECO.6 — Giá trị dịch vụ KCN (Dropdown) | Enabled | Click → mở dropdown | Giá trị: Có / Không (CMR_07). Tooltip mô tả chi tiết | ✅ |
| B1 | Lưu nháp (Button) | Enabled | Click | Validate tối thiểu (CF_01 Case 2: ít nhất 1 trường có data). Thành công → Toast T01, quay lại Danh sách. Thất bại → Toast T05 | ✅ |
| B2 | Gửi báo cáo (Button) | Enabled | Click | Validate tất cả trường bắt buộc → Popup P01 xác nhận → Nộp thành công → Toast T02, chuyển trạng thái (CMR_03) | ✅ |
| B3 | Hủy (Button) | Enabled | Click | Dirty check (CMR_14). Dirty → Popup P02. Không dirty → quay lại Danh sách | ✅ |
| B4 | Xem chi tiết (Button) | Disabled khi chưa lưu nháp; Enabled sau khi đã lưu | Click | Mở popup PDF Preview (CF_01 — Xem chi tiết) | ✅ |

### 5.3. Màn hình Tác vụ bổ trợ (UC335-340.3)

| # | Object / Component | System States | Interaction | Behavior | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp (Button) | Hiển thị khi Lưu nháp (CMR_03) | Click | CF_09: Validate → Popup P01 → Nộp thành công → Toast T02 | ✅ |
| 2 | Chỉnh sửa (Button) | Hiển thị khi Lưu nháp hoặc YC chỉnh sửa (CMR_03) | Click | Mở form chỉnh sửa (CF_03) | ✅ |
| 3 | Xem chi tiết (Button) | Hiển thị tất cả trạng thái | Click | Mở màn hình full-page read-only (CF_07) | ✅ |
| 4 | Xem vòng đời (Button) | Hiển thị tất cả trạng thái | Click | Mở popup Timeline (CF_06) | ✅ |
| 5 | In (Button) | Hiển thị tất cả trạng thái | Click | Mở Print Preview PDF → hộp thoại in (CF_05) | ✅ |
| 6 | Export (Button) | Hiển thị tất cả trạng thái | Click | Kết xuất file Docx (CF_04). Toast T04 thành công / T05 thất bại | ✅ |
| 7 | Xóa (Button) | Hiển thị khi Lưu nháp VÀ chưa từng nộp (CF_08) | Click | Popup P04 xác nhận → Xóa thành công → Toast T08 | ✅ |

---

## Section 6: Functional Logic & Workflow Decomposition

### 6.1. UC335-340.1 — Xem Danh Sách Báo Cáo

#### A. Main Flow (Happy Path)

1. NĐT đăng nhập → Truy cập: Phân hệ Báo cáo → Báo cáo KKT/KCN → Các chỉ số đánh giá hiệu quả KCN sinh thái
2. Hệ thống hiển thị danh sách kỳ báo cáo, mặc định Collapse (CS_01)
3. Danh sách chỉ hiển thị báo cáo của NĐT đang login (User Site)
4. Sắp xếp báo cáo trong kỳ: mới → cũ
5. Phân trang: Chọn hiển thị số kỳ báo cáo/trang (CMR_10)

#### B. Business Rules

| # | Rule | Mô tả | Tham chiếu |
| --- | --- | --- | --- |
| BR1 | Nhóm theo kỳ hạn | Hệ thống tự động nhóm danh sách theo Kỳ hạn báo cáo | CS_01 |
| BR2 | Ẩn/hiện nút theo kỳ | [Lập báo cáo] và [Import] ẩn khi kỳ "Chưa tới hạn" hoặc "Qua kỳ báo cáo" | CMR_04, CF_01 |
| BR3 | Phân quyền hiển thị | Mỗi NĐT chỉ thấy báo cáo của mình | UC335-340.1 §3 |
| BR4 | Phân trang | Chọn hiển thị số kỳ/trang. Mặc định 10 kỳ/trang. Options: 10, 20, 50, 100 | CMR_10 |

#### C. Error Codes / Toast Messages

| Mã | Trường hợp | Nội dung | Tham chiếu |
| --- | --- | --- | --- |
| — | Empty state (tìm kiếm không có kết quả) | "Không tìm thấy kết quả" | CMR_06, CMR_09 |

---

### 6.2. UC335-340.2 — Lập Báo Cáo

#### A. Main Flow (Happy Path)

1. NĐT nhấn [Lập báo cáo] tại màn hình Danh sách (kỳ "Trong thời hạn")
2. Hệ thống mở form nhập liệu, tự generate bảng 18 dòng chỉ số (4 section: Môi trường, Quản lý KCN, Xã hội, Kinh tế)
3. Không có bước chọn dự án (Phạm vi = Không có phạm vi)
4. NĐT nhập liệu các chỉ số
5. NĐT chọn action: [Lưu nháp] / [Gửi báo cáo] / [Xem chi tiết] / [Hủy]

#### B. Business Rules

| # | Rule | Mô tả | Tham chiếu |
| --- | --- | --- | --- |
| BR5 | 1 báo cáo/NĐT/kỳ | Mỗi NĐT chỉ lập được 1 báo cáo duy nhất cho toàn bộ KCN mà họ quản lý trong mỗi kỳ | UC335-340.2 §3 |
| BR6 | Bảng cố định 18 dòng | Hệ thống tự generate sẵn 18 dòng, không thêm/xóa hàng | UC335-340.2 §3 |
| BR7 | Validate ENV.1 | Số dương. Ký tự hợp lệ: 0-9, dấu chấm, dấu phẩy (CMR_05 — trường ≥ 0) | CMR_05 |
| BR8 | Validate EVN.3 | Số dương, 0-100%. Ngoài khoảng → Error: "Giá trị hợp lệ trong khoảng từ 0 - 100%" | UC335-340.2 §3 |
| BR9 | Validate Dòng 3-18 | Dropdown bắt buộc chọn (Có / Không) | CMR_07 |
| BR10 | Lưu nháp (Case 2) | Ít nhất 1 trường phải có dữ liệu. Tất cả trống → Toast T07: "Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp" | CF_01 |
| BR11 | Nộp báo cáo | Validate tất cả trường bắt buộc. Thiếu → lỗi inline V01: "Trường bắt buộc" | CF_01 |
| BR12 | Export | Định dạng Docx | UC335-340.2 §3 |
| BR13 | Tooltip | Mỗi chỉ số có tooltip giải thích (CMR_11). Icon ℹ️ bên cạnh label | CMR_11 |

#### C. Error Codes / Toast Messages

| Mã | Trường hợp | Tiêu đề | Nội dung | Tham chiếu |
| --- | --- | --- | --- | --- |
| T01 | Lưu nháp thành công | Thành công | Đã lập báo cáo thành công | CF_01 |
| T02 | Nộp thành công | Thành công | Đã nộp báo cáo thành công | CF_01 |
| T05 | Lỗi hệ thống | Lỗi hệ thống | Không thể kết nối đến hệ thống. Vui lòng thử lại sau. | CF_01 |
| T07 | Lưu nháp khi tất cả trống | Lưu nháp không thành công | Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp | CF_01 |
| V01 | Trường bắt buộc bỏ trống | — | Trường bắt buộc | CMR_05, CMR_07 |
| V03 | ENV.1: nhập số âm | — | Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy | CMR_05 |
| — | EVN.3: ngoài khoảng 0-100% | — | Giá trị hợp lệ trong khoảng từ 0 - 100% | UC335-340.2 |
| P01 | Popup xác nhận nộp | Bạn có chắc muốn nộp? | Checkbox: "Tôi đã kiểm tra toàn bộ thông tin..." | CF_01 |
| P02 | Dirty Form Guard | Dữ liệu chưa được lưu | Bạn có chắc chắn muốn rời khỏi trang này không? | CMR_14 |

---

### 6.3. UC335-340.3 — Các Tác Vụ Bổ Trợ

#### A. Main Flow (Happy Path)

Từ màn hình Danh sách → Cột Hành động → Chọn tác vụ tương ứng:

| Tác vụ | Luồng | Tham chiếu |
| --- | --- | --- |
| Xem chi tiết | Mở full-page read-only, layout giống form Lập. Nút [Chỉnh sửa] chỉ hiện khi Lưu nháp/YC chỉnh sửa | CF_07 |
| Xem vòng đời | Mở popup Timeline lịch sử thao tác | CF_06 |
| In | Mở Print Preview PDF → hộp thoại in trình duyệt | CF_05 |
| Export | Kết xuất file Docx | CF_04 |
| Chỉnh sửa | Mở form chỉnh sửa, điền sẵn dữ liệu hiện tại | CF_03 |
| Nộp | Validate → Popup P01 → Nộp | CF_09 |
| Xóa | Popup P04 xác nhận → Xóa bản ghi | CF_08 |

#### B. Business Rules

| # | Rule | Mô tả | Tham chiếu |
| --- | --- | --- | --- |
| BR14 | Action mapping theo trạng thái | Hành động hiển thị theo trạng thái bản ghi | CMR_03 |
| BR15 | Xóa chỉ khi chưa từng nộp | Nút [Xóa] chỉ hiện khi Lưu nháp VÀ chưa từng nộp | CF_08 |
| BR16 | Nút [Hủy] tại Xem chi tiết | Quay về Danh sách, không cần popup xác nhận | CF_07 |

---

## Section 7: Functional Integration Analysis

| # | Chức năng nguồn | Chức năng đích | Ảnh hưởng | Data Consistency | Status |
| --- | --- | --- | --- | --- | --- |
| INT-1 | Lập báo cáo (UC335-340.2) → Lưu nháp | Danh sách (UC335-340.1) | Bản ghi mới xuất hiện trong danh sách kỳ tương ứng, trạng thái "Lưu nháp" | Mã báo cáo EZ_A5_[ID] sinh tự động, Ngày cập nhật = thời điểm lưu | ✅ |
| INT-2 | Lập báo cáo (UC335-340.2) → Nộp | Danh sách (UC335-340.1) | Trạng thái chuyển sang "Chờ duyệt" hoặc "Đã tiếp nhận" (CMR_03) | Action buttons cập nhật theo trạng thái mới | ✅ |
| INT-3 | Chỉnh sửa (CF_03) → Lưu nháp | Danh sách (UC335-340.1) | Ngày cập nhật refresh. Trạng thái bảo toàn (Lưu nháp giữ Lưu nháp, YC chỉnh sửa giữ YC chỉnh sửa) | Dữ liệu form đồng bộ với DB | ✅ |
| INT-4 | Xóa (CF_08) | Danh sách (UC335-340.1) | Bản ghi biến mất khỏi danh sách | Counter kỳ giảm 1 | ✅ |
| INT-5 | Import (CF_02) | Lập báo cáo (UC335-340.2) | Dữ liệu từ file map vào form Lập. Tất cả trường Enabled cho chỉnh sửa | Form chuyển sang chế độ Tạo mới tiêu chuẩn | ✅ |
| INT-6 | Nộp từ Danh sách (CF_09) | Danh sách (UC335-340.1) | Validate pass → Popup P01 → Nộp thành công → trạng thái chuyển | Nếu validate fail → mở form Lập với lỗi inline | ✅ |

---

## Section 8: Acceptance Criteria

### AC — UC335-340.1: Xem Danh Sách

| # | Given | When | Then | Status |
| --- | --- | --- | --- | --- |
| AC-1 | NĐT đã đăng nhập và có quyền lập báo cáo Mẫu A.5 | Truy cập Phân hệ Báo cáo → Báo cáo KKT/KCN → Các chỉ số đánh giá hiệu quả KCN sinh thái | Hiển thị danh sách kỳ báo cáo, mặc định Collapse, chỉ hiển thị báo cáo của NĐT đang login | ✅ |
| AC-2 | Kỳ báo cáo ở trạng thái "Trong thời hạn" | NĐT xem danh sách | Nút [Lập báo cáo] và [Import] hiển thị và Enabled | ✅ |
| AC-3 | Kỳ báo cáo ở trạng thái "Chưa tới hạn" hoặc "Qua kỳ báo cáo" | NĐT xem danh sách | Nút [Lập báo cáo] và [Import] bị ẩn | ✅ |
| AC-4 | Có nhiều kỳ báo cáo | NĐT sử dụng filter Năm, Trạng thái kỳ, Trạng thái báo cáo | Danh sách lọc real-time theo giá trị đã chọn | ✅ |
| AC-5 | NĐT nhập mã báo cáo vào Search bar | Hệ thống tìm kiếm | Kết quả hiển thị ngay (live search). Không tìm thấy → "Không tìm thấy kết quả" | ✅ |

### AC — UC335-340.2: Lập Báo Cáo

| # | Given | When | Then | Status |
| --- | --- | --- | --- | --- |
| AC-6 | NĐT mở form Lập báo cáo | Form load | Hệ thống generate bảng 18 dòng chỉ số (4 section), tất cả trường trống | ✅ |
| AC-7 | NĐT nhập đầy đủ 18 chỉ số hợp lệ | Nhấn [Gửi báo cáo] | Popup P01 hiển thị. Tick checkbox + nhấn [Xác nhận] → Toast T02, trạng thái chuyển theo CMR_03 | ✅ |
| AC-8 | NĐT nhập ít nhất 1 trường | Nhấn [Lưu nháp] | Toast T01 "Đã lập báo cáo thành công", quay lại Danh sách | ✅ |
| AC-9 | NĐT không nhập bất kỳ trường nào | Nhấn [Lưu nháp] | Toast T07 "Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp" | ✅ |
| AC-10 | NĐT nhập ENV.1 = số âm | Hệ thống validate | Error inline V03: "Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy" | ✅ |
| AC-11 | NĐT nhập EVN.3 = 150 (ngoài 0-100%) | Hệ thống validate | Error: "Giá trị hợp lệ trong khoảng từ 0 - 100%" | ✅ |
| AC-12 | NĐT bỏ trống trường bắt buộc | Nhấn [Gửi báo cáo] | Lỗi inline V01 "Trường bắt buộc" tại từng trường lỗi. Không mở popup | ✅ |
| AC-13 | NĐT đã thay đổi dữ liệu trên form (dirty) | Nhấn [Hủy] | Popup P02 "Dữ liệu chưa được lưu". [Đồng ý] → quay lại DS. [Hủy] → ở lại form | ✅ |
| AC-14 | NĐT chưa thay đổi gì trên form | Nhấn [Hủy] | Quay lại Danh sách ngay, không popup | ✅ |

### AC — UC335-340.3: Tác Vụ Bổ Trợ

| # | Given | When | Then | Status |
| --- | --- | --- | --- | --- |
| AC-15 | Bản ghi ở trạng thái Lưu nháp, chưa từng nộp | NĐT nhấn [Xóa] | Popup P04 xác nhận. [Đồng ý] → xóa, Toast T08. [Hủy] → giữ nguyên | ✅ |
| AC-16 | Bản ghi ở trạng thái Lưu nháp | NĐT nhấn [Nộp] từ Danh sách | Validate → Pass → Popup P01 → Nộp thành công | ✅ |
| AC-17 | Bản ghi ở bất kỳ trạng thái | NĐT nhấn [Xem chi tiết] | Mở full-page read-only, layout giống form Lập, tất cả trường Disabled | ✅ |
| AC-18 | Bản ghi ở bất kỳ trạng thái | NĐT nhấn [Export] | Kết xuất file Docx. Toast T04 thành công | ✅ |
| AC-19 | Bản ghi ở bất kỳ trạng thái | NĐT nhấn [In] | Mở Print Preview PDF → hộp thoại in trình duyệt | ✅ |

---

## Section 9: Non-functional Requirements

| # | Loại NFR | Yêu cầu | Nguồn | Status |
| --- | --- | --- | --- | --- |
| NFR-1 | Performance | Search bar: Debounce 300-500ms | CS_01 | ✅ |
| NFR-2 | Performance | Toast tự biến mất sau 3-5 giây | CF_01 | ✅ |
| NFR-3 | Usability | Tooltip hiển thị khi hover icon ℹ️ cho mỗi chỉ số | CMR_11 | ✅ |
| NFR-4 | Data Format | Ngày cập nhật: dd/MM/yyyy HH:mm | UC335-340.1 | ✅ |
| NFR-5 | Export | Định dạng Docx | UC335-340.2 §3 | ✅ |
| NFR-6 | Security | Mỗi NĐT chỉ thấy báo cáo của mình (User Site isolation) | UC335-340.1 §3 | ✅ |

⚡ **Partial:** Không có yêu cầu cụ thể về response time, concurrent users, hoặc accessibility (WCAG). Tuy nhiên đây là pattern chung cho toàn hệ thống, không riêng UC này.

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
| --- | --- | --- | --- | --- |
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 15/15 | ✅ |
| 6 | Object Attributes & Behavior Definition | 20 | 20/20 | ✅ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 19/20 | ⚡ |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | Non-functional Requirements | 5 | 4/5 | ⚡ |
| **Total** | | **110** | **108/110** | **98.2/100** |

**Normalization:** Raw 108 / 110 → Final Score = round((108 / 110) × 100, 1) = **98.2 / 100**

**Verdict:** ✅ **READY** — QA can begin test design immediately.

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
| --- | --- | --- | --- | --- | --- |
| Q1 | Low | UC335-340.2 §3: "Dòng 1 (ENV.1): Số dương" | ENV.1 chỉ ghi "Số dương" — cần xác nhận: có giới hạn max value không? Có cho phép số thập phân không? Nếu có thì bao nhiêu chữ số thập phân? | Ảnh hưởng đến boundary value testing. Nếu không giới hạn, tester cần biết max length áp dụng (mặc định 500 ký tự theo CMR_05) | Open |
| Q2 | Low | UC335-340.2 §3: "Export: Định dạng Docx" | Xác nhận: Export từ popup PDF Preview (CF_01 — nút [Xem chi tiết]) cũng ra Docx? Hay chỉ Export từ cột Hành động trên Danh sách? | Cần rõ scope export để thiết kế test case cho cả 2 entry point | Open |
| Q3 | Low | N/A (Missing) | Tài liệu không mô tả rõ NFR về response time, số lượng concurrent users, hoặc accessibility. Đây có phải là yêu cầu chung cho toàn hệ thống hay cần bổ sung riêng cho UC này? | Ảnh hưởng đến performance testing và accessibility testing | Open |

---

## 🟢 What's Good

- Tài liệu mô tả rõ ràng, đầy đủ 3 sub-functions (Xem danh sách, Lập báo cáo, Tác vụ bổ trợ) với cấu trúc nhất quán.
- Bảng giao diện liệt kê chi tiết từng trường với kiểu component, placeholder, tooltip, validation rules.
- Tham chiếu đến CMR/CF/CS rất tốt — mỗi behavior đều có nguồn tham chiếu rõ ràng.
- Phân quyền và action mapping theo trạng thái được mô tả cụ thể.
- Validation rules cho 2 trường Number (ENV.1, EVN.3) được định nghĩa rõ ràng với error messages cụ thể.
- Form cố định 18 dòng — đơn giản, không có dynamic rows, giảm complexity cho test design.

---

## 🧪 Testability Outlook

**What CAN be tested now:**

- Toàn bộ luồng Xem danh sách: filter, search, expand/collapse kỳ, phân trang
- Luồng Lập báo cáo: nhập liệu 18 chỉ số, validation, Lưu nháp, Nộp
- Tất cả tác vụ bổ trợ: Xem chi tiết, Chỉnh sửa, Xóa, In, Export, Xem vòng đời, Nộp từ Danh sách
- Dirty Form Guard (CMR_14)
- Action mapping theo trạng thái (CMR_03)
- Ẩn/hiện nút theo kỳ hạn (CMR_04)

**What CANNOT be tested yet (blocked by gaps):**

- Boundary value testing cho ENV.1 (Q1 — chưa rõ max value / decimal precision)

**Suggested test focus areas** *(once gaps are resolved)*:

- Happy path: Lập báo cáo đầy đủ 18 chỉ số → Lưu nháp → Nộp thành công
- Alternative scenarios: Lưu nháp với 1 trường có data, Nộp từ Danh sách (CF_09), Import file
- Boundary & validation tests: ENV.1 (số dương, ký tự không hợp lệ), EVN.3 (0%, 100%, 101%, -1%), Dropdown bắt buộc
- Error & exception scenarios: Lưu nháp khi tất cả trống (T07), Nộp khi thiếu trường bắt buộc (V01), Lỗi server (T05)
- UI-specific checks: Tooltip hiển thị cho 18 chỉ số, Dirty Form Guard popup, Button disable/enable states

---

## 📌 Summary & Recommendation

Tài liệu UC335-340 đạt chất lượng cao với điểm **98.2/100**. Tất cả các knowledge area critical đều được mô tả đầy đủ và rõ ràng. Form nhập liệu đơn giản (18 dòng cố định, chủ yếu Dropdown Có/Không) giúp giảm complexity. Các gap còn lại (Q1-Q3) đều ở mức Low priority và không block test design. **Recommendation: Proceed now** — QA có thể bắt đầu thiết kế test case ngay lập tức.
