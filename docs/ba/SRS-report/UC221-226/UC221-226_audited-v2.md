# UC221-226 — Requirements Readiness Review

| Thuộc tính | Giá trị |
|---|---|
| **UC ID** | UC221-226 |
| **Tên báo cáo** | Báo cáo tình hình thực hiện dự án đầu tư quý (Mẫu A.III.1) |
| **Phân hệ** | Quản lý đầu tư trong nước Việt Nam |
| **Ngày audit** | 2026-05-21 |
| **Phiên bản UC** | 1.0 |
| **Phiên bản audit** | v2 (CMR Alignment) |
| **Auditor** | AI Agent |

---

## Section 0: Feature Identity

**Status:** ✅ Complete

- **UC ID:** UC221-226
- **Tên chức năng:** Báo cáo tình hình thực hiện dự án đầu tư quý (Mẫu A.III.1)
- **Phân hệ:** Quản lý đầu tư trong nước Việt Nam
- **Mẫu biểu:** Mẫu A.III.1
- **Loại báo cáo:** Định kỳ quý
- **Hình thức nộp:** Báo cáo đơn lẻ (Single report form)
- **Quy tắc sinh mã:** DDI_AIII1_[ID]
- **Loại quy trình:** 2 bước (CMCĐT_BCTK_02, CMCĐT_BCTK_03)

---

## Section 1: Objective & Scope

**Status:** ✅ Complete

**Mục tiêu:** Cho phép Tổ chức kinh tế (TCKT) lập và nộp báo cáo định kỳ quý về tình hình thực hiện dự án đầu tư trong nước theo Mẫu A.III.1.

**Phạm vi:**
- Xem danh sách báo cáo theo kỳ (UC221-226.1)
- Lập mới báo cáo (UC221-226.2)
- Các tác vụ bổ trợ: Nộp, Nhập từ file, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Xóa (UC221-226.3)

**Hạn nộp:** Trước ngày 10 tháng đầu của quý sau quý báo cáo.

---

## Section 2: Actors & User Roles

**Status:** ✅ Complete

| Actor | Quyền |
|---|---|
| TCKT phụ trách dự án | Toàn quyền: Khởi tạo, Nộp, Chỉnh sửa, Xóa, Xem, In, Xuất báo cáo, Xem vòng đời (CMR_01) |
| NĐT thành viên trong dự án | Chỉ Xem chi tiết, In, Xuất báo cáo, Xem vòng đời (CMR_01) |

---

## Section 3: Preconditions & Postconditions

**Status:** ⚡ Partial

**Preconditions (inferred):**
- Người dùng đã đăng nhập với vai trò TCKT hoặc NĐT thành viên
- Dự án đã được cấp GCNĐKĐT và có dữ liệu trên hệ thống
- Kỳ hạn báo cáo đang ở trạng thái "Trong thời hạn" (để tạo mới)
- API IRC/ĐKKD khả dụng để lấy dữ liệu NĐT

**Postconditions (inferred):**
- Sau Lưu nháp: Bản ghi ở trạng thái "Lưu nháp", snapshot NĐT được lưu
- Sau Nộp: Bản ghi chuyển sang "Đã tiếp nhận" (quy trình 2 bước theo CMR_03)
- Sau Xóa: Bản ghi bị xóa khỏi danh sách

**Gaps:** Preconditions và Postconditions không được ghi rõ ràng trong tài liệu — phải suy luận từ ngữ cảnh.

---

## Section 4: UI Object Inventory & Mapping

**Status:** ✅ Complete

### 4.1 Màn hình Danh sách (UC221-226.1)

| # | Object / Component | Type | Required | Default | Source |
|---|---|---|---|---|---|
| 1 | Thanh tìm kiếm | Search bar | — | Null | UC221-226.1 |
| 2 | Dự án | Dropdown + Searchable | — | Tất cả dự án | UC221-226.1 |
| 3 | Năm | Yearpicker | — | Năm hiện tại | UC221-226.1 |
| 4 | Trạng thái kỳ hạn | Multiple-selection Dropdown | — | Null | UC221-226.1 |
| 5 | Trạng thái báo cáo | Multiple-selection Dropdown | — | Null | UC221-226.1 |
| 6 | Kỳ hạn báo cáo | Label (Collapse/Expand header) | — | Collapse | UC221-226.1 |
| 7 | Trạng thái kỳ | Label | — | — | UC221-226.1 |
| 8 | Nút [Lập báo cáo] | Button | — | — | UC221-226.1 |
| 9 | Nút [Nhập từ file] | Button | — | — | UC221-226.1 |
| 10 | Tên dự án | Label (column) | — | — | UC221-226.1 |
| 11 | Mã báo cáo | Label (column) | — | — | UC221-226.1 |
| 12 | Kỳ báo cáo | Label (column) | — | — | UC221-226.1 |
| 13 | Ngày cập nhật | Label (column) | — | — | UC221-226.1 |
| 14 | Trạng thái | Label (column) | — | — | UC221-226.1 |
| 15 | Hành động | Button group (column) | — | — | UC221-226.1 |

### 4.2 Màn hình Lập báo cáo (UC221-226.2)

**Header:**

| # | Object / Component | Type | Required | Default | Source |
|---|---|---|---|---|---|
| 16 | Quý báo cáo | Read-only | x | Auto-fill từ kỳ hạn | UC221-226.2 |
| 17 | Năm báo cáo | Read-only | x | Auto-fill từ kỳ hạn | UC221-226.2 |

**Phần A — Thông tin chung:**

| # | Object / Component | Type | Required | Default | Source |
|---|---|---|---|---|---|
| 18 | A-001: Tên dự án / Tên hợp đồng BCC | Dropdown + Searchable | x | — | UC221-226.2 |
| 19 | A-002: Mã số dự án / Số GCNĐKĐT | API (Read-only) | — | Auto-fill | UC221-226.2 |
| 20 | A-003: Ngày cấp (GCNĐKĐT) | API (Read-only) | — | Auto-fill | UC221-226.2 |
| 21 | A-004: Cơ quan cấp GCNĐKĐT | API (Read-only) | — | Auto-fill | UC221-226.2 |
| 22 | A-005: Địa điểm thực hiện dự án | API (Read-only) | — | Auto-fill | UC221-226.2 |
| 23 | A-006: Tổng vốn đầu tư đăng ký | API (Read-only) | — | Auto-fill | UC221-226.2 |
| 24 | A-007: Tên tổ chức kinh tế thực hiện dự án | API (Read-only) | — | Auto-fill | UC221-226.2 |
| 25 | A-008: Mã số doanh nghiệp / Mã số thuế | API (Read-only) | — | Auto-fill | UC221-226.2 |
| 26 | A-009: Ngày cấp lần đầu (ĐKKD) | API (Read-only) | — | Auto-fill | UC221-226.2 |
| 27 | A-010: Cơ quan cấp Đăng ký kinh doanh | API (Read-only) | — | Auto-fill | UC221-226.2 |
| 28 | A-011: Địa chỉ liên hệ | API (Editable) | x | Auto-fill | UC221-226.2 |
| 29 | A-012: Số điện thoại | API (Editable) | x | Auto-fill | UC221-226.2 |
| 30 | A-013: Email | API (Editable) | x | Auto-fill | UC221-226.2 |

**Phần B — eForm Grid (Tình hình thực hiện dự án):**

| # | Object / Component | Type | Required | Columns | Source |
|---|---|---|---|---|---|
| 31 | I. Vốn đầu tư thực hiện | Auto-calc row | — | A, B, C | UC221-226.2 |
| 32 | 1. Vốn góp | Auto-calc row | — | A, B, C | UC221-226.2 |
| 33 | 1.1 Nhà đầu tư Việt Nam | Auto-calc row | — | A, B, C | UC221-226.2 |
| 34 | [NĐT VN — Tên] | API Label | x | Σ(A) con, Auto, Auto | UC221-226.2 |
| 35 | [NĐT VN — MST] | API Label | x | Locked | UC221-226.2 |
| 36 | [NĐT VN — Chia ra] | Group header | — | Locked | UC221-226.2 |
| 37 | [NĐT VN — Bằng tiền] | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, B, C | UC221-226.2 |
| 38 | [NĐT VN — Máy móc, thiết bị] | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, B, C | UC221-226.2 |
| 39 | [NĐT VN — Tài sản khác] | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, B, C | UC221-226.2 |
| 40 | 1.2 Nhà đầu tư nước ngoài | Auto-calc row | — | A, B, C | UC221-226.2 |
| 41 | [NĐT NN — Tên] | API Label | x | Σ(A) con, Auto, Auto | UC221-226.2 |
| 42 | [NĐT NN — MST/QĐ/HC] | API Label | x | Locked | UC221-226.2 |
| 43 | [NĐT NN — Chia ra] | Group header | — | Locked | UC221-226.2 |
| 44 | [NĐT NN — Bằng tiền] | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, B, C | UC221-226.2 |
| 45 | [NĐT NN — Máy móc, thiết bị] | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, B, C | UC221-226.2 |
| 46 | [NĐT NN — Tài sản khác] | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, B, C | UC221-226.2 |
| 47 | 2. Vốn vay | Auto-calc row | — | A, B, C | UC221-226.2 |
| 48 | Vay trong nước | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, B, C | UC221-226.2 |
| 49 | Vay từ công ty mẹ ở nước ngoài | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, B, C | UC221-226.2 |
| 50 | Vay nước ngoài khác | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, B, C | UC221-226.2 |

| # | Object / Component | Type | Required | Columns | Source |
|---|---|---|---|---|---|
| 51 | 3. Lợi nhuận tái đầu tư | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, B, C | UC221-226.2 |
| 52 | II. Doanh thu thuần | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, B, Locked(C) | UC221-226.2 |
| 53 | III. Giá trị hàng xuất khẩu | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, B, Locked(C) | UC221-226.2 |
| 54 | IV. Giá trị hàng nhập khẩu | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, B, Locked(C) | UC221-226.2 |
| 55 | V. Số lao động hiện có | Auto-calc | — | A, Locked(B), Locked(C) | UC221-226.2 |
| 56 | V.1 Lao động Việt Nam | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, Locked(B), Locked(C) | UC221-226.2 |
| 57 | V.2 Lao động nước ngoài | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, Locked(B), Locked(C) | UC221-226.2 |
| 58 | VI. Tình hình sử dụng năng lượng | Group header | — | Locked | UC221-226.2 |
| 59 | VI.1 Điện (kWh) | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, Locked(B), Locked(C) | UC221-226.2 |
| 60 | VI.2 Than (Tấn) | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, Locked(B), Locked(C) | UC221-226.2 |
| 61 | VI.3 Dầu (Lít) | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, Locked(B), Locked(C) | UC221-226.2 |
| 62 | VI.4 Khí LNG (m³) | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, Locked(B), Locked(C) | UC221-226.2 |
| 63 | VI.5 Các loại năng lượng khác | Editable (Number + Text ĐVT). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | — | A, Locked(B), Locked(C) | UC221-226.2 |
| 64 | VII. Thuế và các khoản nộp NSNN | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | x | A, B, Locked(C) | UC221-226.2 |
| 65 | VIII. Diện tích đất, mặt nước | Editable (Number). Phần nguyên max 15 chữ số, phần thập phân max 5 chữ số (tổng 21 ký tự) | — | A, B, C | UC221-226.2 |

**Phần C — Khó khăn, vướng mắc:**

| # | Object / Component | Type | Required | Default | Source |
|---|---|---|---|---|---|
| 66 | C-001: Khó khăn, vướng mắc | Textarea | — | — | UC221-226.2 |

**Buttons:**

| # | Object / Component | Type | Required | Source |
|---|---|---|---|---|
| 67 | Nút [Hủy] | Button | — | UC221-226.2 |
| 68 | Nút [Xem trước] | Button | — | UC221-226.2 |
| 69 | Nút [Lưu nháp] | Button | — | UC221-226.2 |
| 70 | Nút [Nộp báo cáo] | Button | — | UC221-226.2 |

### 4.3 Tác vụ bổ trợ (UC221-226.3)

| # | Object / Component | Type | Điều kiện | Source |
|---|---|---|---|---|
| 71 | Nút [Nộp] | Button | Lưu nháp / YC chỉnh sửa | UC221-226.3 |
| 72 | Nút [Nhập từ file] | Button | Trong thời hạn + chưa có/Lưu nháp/YCCS | UC221-226.3 |
| 73 | Nút [Chỉnh sửa] | Button | Lưu nháp / YC chỉnh sửa | UC221-226.3 |
| 74 | Nút [Xem chi tiết] | Button | Tất cả trạng thái | UC221-226.3 |
| 75 | Nút [Xem vòng đời] | Button | Tất cả trạng thái | UC221-226.3 |
| 76 | Nút [In] | Button | Tất cả trạng thái | UC221-226.3 |
| 77 | Nút [Xuất báo cáo] | Button | Tất cả trạng thái | UC221-226.3 |
| 78 | Nút [Xóa] | Button | Lưu nháp VÀ chưa từng nộp | UC221-226.3 |

---

## Section 5: Object Attributes & Behavior Definition

**Status:** ✅ Complete

| # | Object / Component | System States | Interaction | Behavior |
|---|---|---|---|---|
| 1 | Thanh tìm kiếm | Enabled | Typing | Live search theo Mã báo cáo, Tên dự án. Debounce 300-500ms. Empty: "Không tìm thấy kết quả". CMR_06, CMR_09 |
| 2 | Dự án (filter) | Enabled | Click/Search | Lọc danh sách theo dự án. Option "Tất cả dự án" mặc định. CMR_07, CMR_16 |
| 3 | Năm (filter) | Enabled | Click | Yearpicker. Mặc định năm hiện tại. Enable toàn bộ năm. Empty state khi không có data. CMR_07, CS_01 |
| 4 | Trạng thái kỳ hạn (filter) | Enabled | Click | Multi-select: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. CMR_04, CMR_07, CMR_16 |
| 5 | Trạng thái báo cáo (filter) | Enabled | Click | Multi-select: Lưu nháp / Chờ duyệt / Đã tiếp nhận / YC chỉnh sửa. CMR_03, CMR_07, CMR_16 |
| 6 | Kỳ hạn báo cáo | Collapse (default) | Click | Expand/Collapse danh sách báo cáo bên trong. CMR_08 |
| 7 | Trạng thái kỳ | Read-only | — | Hiển thị: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. CMR_04 |
| 8 | Nút [Lập báo cáo] | Hidden khi Chưa tới hạn/Qua kỳ; Visible khi Trong thời hạn | Click | Mở form lập báo cáo. CF_01 |
| 9 | Nút [Nhập từ file] | Hidden khi Chưa tới hạn/Qua kỳ; Visible khi Trong thời hạn | Click | Mở popup nhập từ file. CF_02 Case 1 |
| 10 | Tên dự án | Read-only | — | N/A |
| 11 | Mã báo cáo | Read-only | — | Sinh theo DDI_AIII1_[ID]. CMR_09 |
| 12 | Kỳ báo cáo | Read-only | — | Format: Quý [Q] / Năm [YYYY] |
| 13 | Ngày cập nhật | Read-only | — | Format: dd/MM/yyyy HH:mm |
| 14 | Trạng thái | Read-only | Hover (NĐT thành viên) | Tooltip: "Đã được lập bởi [Tên TCKT]". CMR_01, CS_01 |
| 15 | Hành động | Enabled (conditional) | Click | Hiển thị theo trạng thái + phân quyền. UC221-226.3 |
| 16 | Quý báo cáo | Read-only | — | Auto-fill từ kỳ hạn. Không cho sửa |
| 17 | Năm báo cáo | Read-only | — | Auto-fill từ kỳ hạn. Không cho sửa |
| 18 | A-001: Tên dự án | Enabled (Dropdown) | Click/Search | Chọn dự án → trigger API fill A-002→A-013. CMR_12. RULE-03 khi đổi dự án |
| 19-27 | A-002→A-010 | Disabled (API) | — | Auto-fill sau chọn A-001. Read-only. CMR_12 |
| 28 | A-011: Địa chỉ liên hệ | Enabled (API pre-fill) | Typing | Cho phép chỉnh sửa. Required |
| 29 | A-012: Số điện thoại | Enabled (API pre-fill) | Typing | Cho phép chỉnh sửa. Required |
| 30 | A-013: Email | Enabled (API pre-fill) | Typing | Cho phép chỉnh sửa. Required |
| 31-65 | eForm Grid cells | Editable/Auto-calc/Locked/API Label | Typing/Auto | Theo loại cell. CMR_05 cho validation số. Viền đỏ + tooltip cho lỗi trong grid |
| 66 | C-001 Textarea | Enabled | Typing | Optional. Hỗ trợ xuống dòng. CMR_06 |
| 67 | Nút [Hủy] | Enabled | Click | Dirty check → popup P02 nếu dirty. CF_01 |
| 68 | Nút [Xem trước] | Disabled (chưa lưu nháp) / Enabled (đã lưu) | Click | Mở popup PDF Preview. CF_07.1 |
| 69 | Nút [Lưu nháp] | Luôn Enabled (CMR I01) | Click | Validate tối thiểu (phải chọn Dự án). Toast T01. CF_01 |
| 70 | Nút [Nộp báo cáo] | Luôn Enabled (CMR I01) | Click | Validate full → Popup P01 → Toast T02. CF_01 |
| 71 | Nút [Nộp] (Danh sách) | Luôn Enabled (CMR I01). Disabled chỉ khi đang gọi API (I02) | Click | Validate → Popup P01 hoặc mở CF_03 nếu fail. CF_09, CMR_14 |
| 72 | Nút [Nhập từ file] (Danh sách) | Conditional | Click | Popup ghi đè nếu đã có Lưu nháp/YCCS. CF_02 Case 1 |
| 73 | Nút [Chỉnh sửa] | Enabled | Click | Mở form chỉnh sửa. CF_03 |
| 74 | Nút [Xem chi tiết] | Enabled | Click | Mở full-page view (Disabled fields). CF_07 |
| 75 | Nút [Xem vòng đời] | Enabled | Click | Mở popup timeline. CF_06 |
| 76 | Nút [In] | Enabled | Click | Print Preview PDF. CF_05 |
| 77 | Nút [Xuất báo cáo] | Enabled | Click | Kết xuất Excel. CF_04 |
| 78 | Nút [Xóa] | Enabled | Click | Popup P04 → Toast T08. CF_08 |

---

## Section 6: Functional Logic & Workflow Decomposition

**Status:** ✅ Complete

### 6.1 Xem Danh sách (UC221-226.1)

**A. Happy Path:**
1. TCKT truy cập Phân hệ Báo cáo → Quản lý đầu tư trong nước Việt Nam → Báo cáo tình hình thực hiện dự án đầu tư quý
2. Hệ thống hiển thị danh sách kỳ hạn (collapse), sắp xếp giảm dần
3. TCKT expand kỳ → xem danh sách báo cáo trong kỳ
4. TCKT sử dụng bộ lọc/tìm kiếm để thu hẹp kết quả

**B. Business Rules:**
- CMR_01: Phân quyền TCKT vs NĐT thành viên
- CMR_03: Hành động theo trạng thái
- CMR_04: Trạng thái kỳ hạn quyết định hiển thị nút [Lập báo cáo]/[Nhập từ file]
- CMR_08: Quy tắc hiển thị kỳ hạn
- CMR_09: Quy tắc mã báo cáo DDI_AIII1_[ID]
- CMR_10: Phân trang (10 bản ghi/trang mặc định)
- CMR_16: Filter dropdown có option "Tất cả"

**C. Error/Exception:**
- Empty state: "Chưa có báo cáo nào"
- Tìm kiếm không có kết quả: "Không tìm thấy kết quả"

### 6.2 Lập báo cáo (UC221-226.2)

**A. Happy Path:**
1. TCKT nhấn [Lập báo cáo] tại kỳ "Trong thời hạn"
2. Hệ thống mở form. Quý/Năm auto-fill từ kỳ hạn (Read-only)
3. TCKT chọn Dự án (A-001) → API fill A-002→A-013
4. TCKT nhập liệu Phần B (eForm grid) và Phần C
5. TCKT nhấn [Lưu nháp] → Toast T01: "Đã lập báo cáo thành công"
6. TCKT nhấn [Nộp báo cáo] → Validate → Popup P01 → Toast T02: "Đã nộp báo cáo thành công" → Trạng thái "Đã tiếp nhận"

**B. Business Rules:**
- RULE-01: Đơn vị hiển thị — ĐTTN dùng "Triệu VNĐ" thay "USD"
- RULE-02: Tooltip Vốn vay: "Vốn vay = tổng vay trong kỳ trừ số trả nợ trong kỳ (bao gồm cả vay ngắn hạn, trung hạn và dài hạn)"
- RULE-03: Đổi dự án sau nhập liệu → Popup P02 (Dirty Form Guard) → xóa toàn bộ Phần B
- CMR_05: Validation trường số (ký tự hợp lệ, format, viền đỏ + tooltip trong eForm grid)
- CMR_06: Auto-trim, placeholder "Nhập [tên trường]"
- CMR_12: Trạng thái trường API-sourced (Disabled/Enabled theo kết quả API)
- CMR_14: Dirty Form Guard khi nhấn [Hủy]
- CMR_18: Tab Navigation (Tab/Shift+Tab)
- Snapshot NĐT khi Lưu nháp; Re-fetch khi Chỉnh sửa

**C. Error/Toast Messages:**
- T01: Lưu nháp thành công — "Đã lập báo cáo thành công"
- T02: Nộp thành công — "Đã nộp báo cáo thành công"
- T05: Lỗi hệ thống — "Không thể kết nối đến hệ thống. Vui lòng thử lại sau."
- T07: Lưu nháp khi trống — "Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp"
- T17: Trùng kỳ — "Kỳ báo cáo đã tồn tại trong hệ thống. Vui lòng kiểm tra lại."
- V01: Trường bắt buộc — "Vui lòng nhập/chọn [tên trường]"
- Inline validation: CMR_05 (số), CMR_06 (text)

**D. Alternative Flows:**
- API fail khi chọn Dự án → Toast T05, trường API giữ Enabled cho nhập tay (CMR_12)
- Đổi dự án sau nhập liệu → RULE-03 popup cảnh báo
- Nhấn [Hủy] khi form dirty → Popup P02

### 6.3 Tác vụ bổ trợ (UC221-226.3)

**Nộp từ Danh sách (CF_09):**
- Validate → Pass: Popup P01 → Nộp → "Đã tiếp nhận"
- Validate → Fail: Mở CF_03 với lỗi inline

**Nhập từ file (CF_02 Case 1):**
- Chọn Dự án → Tải template → Upload → Validate cấu trúc/dữ liệu → Map vào form
- Ghi đè: Popup cảnh báo nếu đã có Lưu nháp/YCCS

**Chỉnh sửa (CF_03):**
- Mở form với dữ liệu hiện tại. Nút [Lưu nháp]/[Nộp] Disabled khi YCCS + chưa dirty
- Re-fetch NĐT từ API, cảnh báo nếu NĐT bị xóa

**Xem chi tiết (CF_07):** Full-page read-only. Nút [Xem trước], [Chỉnh sửa] (conditional), [Hủy]

**Xem vòng đời (CF_06):** Popup timeline, lazy load, giảm dần

**In (CF_05):** Print Preview PDF → Browser print dialog

**Xuất báo cáo (CF_04):** Kết xuất Excel. Toast T04: "Đã xuất báo cáo thành công"

**Xóa (CF_08):** Popup P04 → Toast T08: "Xóa báo cáo thành công". Chỉ khi Lưu nháp + chưa từng nộp

---

## Section 7: Functional Integration Analysis

**Status:** ⚡ Partial

| # | Integration Point | Impact | Status |
|---|---|---|---|
| 1 | API IRC/GCNĐKĐT → Phần A (A-001→A-010) | Chọn Dự án trigger auto-fill. Fail → Enabled cho nhập tay | ✅ Defined (CMR_12) |
| 2 | API ĐKKD → A-007→A-010 | Auto-fill thông tin TCKT | ✅ Defined |
| 3 | API NĐT → Phần B (blocks NĐT VN/NN) | Danh sách NĐT lấy từ API. Snapshot/Re-fetch | ✅ Defined |
| 4 | Kỳ hạn → Nút [Lập]/[Nhập từ file] | CMR_04 quyết định hiển thị | ✅ Defined |
| 5 | Trạng thái bản ghi → Action buttons | CMR_03 quyết định hành động khả dụng | ✅ Defined |
| 6 | Quy trình 2 bước → Trạng thái sau Nộp | Nộp → "Đã tiếp nhận" (không qua "Chờ duyệt") | ✅ Defined |
| 7 | RULE-01: Loại dự án → Đơn vị hiển thị | ĐTTN → "Triệu VNĐ" thay "USD" | ⚡ Partial — thiếu rõ logic xác định loại dự án |

---

## Section 8: Acceptance Criteria

**Status:** ⚡ Partial *(inferred — không có AC tường minh trong tài liệu gốc)*

### AC-01: Xem danh sách
- **Given** TCKT đăng nhập và truy cập màn hình báo cáo quý
- **When** Hệ thống load danh sách
- **Then** Hiển thị kỳ hạn collapse, sắp xếp giảm dần, nút [Lập báo cáo] chỉ hiện khi "Trong thời hạn"

### AC-02: Lập báo cáo — Happy path
- **Given** Kỳ hạn "Trong thời hạn" và TCKT có quyền
- **When** TCKT nhấn [Lập báo cáo], chọn Dự án, nhập đầy đủ trường bắt buộc, nhấn [Nộp]
- **Then** Bản ghi chuyển sang "Đã tiếp nhận", Toast T02 hiển thị, quay lại Danh sách

### AC-03: Auto-fill API
- **Given** TCKT chọn Dự án từ dropdown A-001
- **When** API trả về thành công
- **Then** Các trường A-002→A-013 được điền tự động, A-002→A-010 Disabled, A-011→A-013 Enabled

### AC-04: Validation trường số
- **Given** TCKT nhập ký tự không hợp lệ vào ô eForm grid
- **When** Blur khỏi ô
- **Then** Ô hiển thị viền đỏ, hover hiện tooltip "Ký tự không hợp lệ..."

### AC-05: Phân quyền NĐT thành viên
- **Given** NĐT thành viên đăng nhập
- **When** Truy cập danh sách báo cáo
- **Then** Không thấy nút [Lập báo cáo], [Chỉnh sửa], [Xóa], [Nộp]. Chỉ thấy [Xem chi tiết], [In], [Xuất báo cáo], [Xem vòng đời]

### AC-06: RULE-01 Đơn vị
- **Given** Dự án ĐTTN (cấp GCNĐKĐT bằng VNĐ)
- **When** Mở form lập báo cáo
- **Then** Toàn bộ label đơn vị hiển thị "Triệu VNĐ" thay vì "USD"

### AC-07: Snapshot/Re-fetch NĐT
- **Given** Báo cáo đã Lưu nháp với 2 NĐT
- **When** TCKT mở Chỉnh sửa và 1 NĐT đã bị xóa khỏi dự án
- **Then** Hiển thị cảnh báo: "Nhà đầu tư [Tên NĐT] đã bị xóa khỏi dự án. Vui lòng kiểm tra lại."

---

## Section 9: Non-functional Requirements

**Status:** ⚡ Partial

- **Performance:** Không được đề cập cụ thể. Debounce 300-500ms cho search (CS_01).
- **Security:** Phân quyền theo CMR_01 (TCKT vs NĐT). Không đề cập RBAC chi tiết.
- **Compatibility:** Không đề cập browser/device support.
- **Accessibility:** CMR_18 (Tab Navigation) là yêu cầu accessibility duy nhất được ghi nhận.

---

## Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 6/10 | ⚡ |
| 5 | UI Object Inventory & Mapping | 15 | 14/15 | ✅ |
| 6 | Object Attributes & Behavior Definition | 20 | 18/20 | ✅ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 18/20 | ✅ |
| 8 | Functional Integration Analysis | 10 | 8/10 | ⚡ |
| 9 | Acceptance Criteria | 10 | 5/10 | ⚡ |
| 10 | Non-functional Requirements | 5 | 2/5 | ⚡ |
| **Total** | | **110** | **91/110** | **82.7/100** |

### Verdict: ⚠️ CONDITIONALLY READY

---

## Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | Medium | UC221-226.2 Phần B — RULE-01 | RULE-01 nêu "Đối với dự án ĐTTN (được cấp GCNĐKĐT bằng VNĐ)" — nhưng UC221-226 thuộc phân hệ ĐTTN. Vậy RULE-01 có áp dụng mặc định cho TẤT CẢ dự án trong phân hệ này không? Hay vẫn có dự án ĐTTN được cấp bằng USD? Cần xác nhận logic xác định loại tiền tệ. | Ảnh hưởng đến đơn vị hiển thị toàn bộ Phần B. Nếu tất cả đều dùng "Triệu VNĐ" thì cột đơn vị trong eForm grid cần cập nhật. | Open |
| Q2 | Medium | UC221-226.2 Mục 3 — Validation Trùng kỳ (V17) | Tài liệu ghi "Kiểm tra trùng (Năm + Quý + Dự án) khi Blur trường Năm/Quý hoặc khi nhấn [Lưu nháp]/[Nộp]". Tuy nhiên Quý và Năm đã chuyển thành Read-only (auto-fill từ kỳ hạn). Vậy validation V17 còn cần thiết không? Nếu hệ thống tự gán Quý/Năm từ kỳ hạn thì trùng kỳ chỉ xảy ra khi cùng Dự án — cần xác nhận logic. | Nếu V17 không còn áp dụng, cần xóa khỏi SRS để tránh nhầm lẫn khi implement. Nếu vẫn áp dụng, cần làm rõ trigger event (không còn Blur trên Quý/Năm). | Open |
| Q3 | Low | UC221-226.1 — Preconditions | Tài liệu không ghi rõ preconditions (VD: user đã đăng nhập, dự án đã tồn tại trên hệ thống, API khả dụng). Cần bổ sung để QC có thể setup test data chính xác. | Tester cần biết điều kiện tiên quyết để thiết lập môi trường test. | Open |
| Q4 | Low | UC221-226.2 — Phần B NĐT blocks | Khi dự án ĐTTN không có "Nhà đầu tư nước ngoài" (chỉ có NĐT Việt Nam), mục 1.2 "Nhà đầu tư nước ngoài" hiển thị như thế nào? Ẩn hoàn toàn hay hiển thị với giá trị 0? | Ảnh hưởng đến UI rendering và auto-calc. Cần xác nhận empty state cho block NĐT NN khi không có NĐT nước ngoài. | Open |
| Q5 | Low | UC221-226.2 — A-011, A-012, A-013 | Các trường A-011 (Địa chỉ), A-012 (SĐT), A-013 (Email) cho phép chỉnh sửa. Có validation format cho Email và SĐT không? (VD: email phải có @, SĐT chỉ chấp nhận số). | Thiếu validation format → không thể viết negative test cho các trường này. | Open |

---

## 🟢 What's Good

- **Cấu trúc rõ ràng:** Tài liệu tuân thủ đúng template Periodic-single, phân chia UC.1/.2/.3 mạch lạc.
- **eForm Grid chi tiết:** Mô tả đầy đủ loại cell (Editable/Auto-calc/Locked/API Label), công thức tính toán, và đơn vị cho từng chỉ tiêu.
- **Tham chiếu CMR/CF đầy đủ:** Mỗi trường và nút đều có tham chiếu rõ ràng đến quy tắc chung.
- **Business Rules đặc thù:** RULE-01, RULE-02, RULE-03 được định nghĩa cụ thể.
- **Snapshot/Re-fetch NĐT:** Cơ chế xử lý dữ liệu NĐT thay đổi giữa các lần chỉnh sửa được mô tả rõ.

---

## 🧪 Testability Outlook

**What CAN be tested now:**
- Phân quyền TCKT vs NĐT thành viên (CMR_01)
- Luồng Lập → Lưu nháp → Nộp (CF_01)
- Validation trường số trong eForm grid (CMR_05)
- Auto-fill API khi chọn Dự án (CMR_12)
- Hiển thị/ẩn nút theo trạng thái kỳ hạn (CMR_04)
- Dirty Form Guard (CMR_14)
- Tất cả tác vụ bổ trợ (CF_03→CF_09)

**What CANNOT be tested yet (blocked by gaps):**
- Logic xác định đơn vị "USD" vs "Triệu VNĐ" cho phân hệ ĐTTN (Q1)
- Validation trùng kỳ V17 — trigger event chưa rõ (Q2)
- Empty state cho block NĐT NN khi không có NĐT nước ngoài (Q4)
- Validation format Email/SĐT (Q5)

**Suggested test focus areas (once gaps are resolved):**
- Happy path: Lập → Lưu nháp → Chỉnh sửa → Nộp → Xem vòng đời
- Alternative: API fail, đổi dự án sau nhập liệu, Nhập từ file ghi đè
- Boundary & validation: Trường số (ký tự lạ, max length 18, số âm), Textarea max 500
- Error & exception: Lỗi server, trùng kỳ, NĐT bị xóa khỏi dự án
- UI-specific: eForm grid viền đỏ + tooltip, collapse/expand kỳ hạn, phân trang

---

## 📌 Summary & Recommendation

UC221-226 đạt **82.7/100** — mức **CONDITIONALLY READY**. Tài liệu có cấu trúc tốt, mô tả chi tiết eForm grid và tham chiếu CMR/CF đầy đủ. Tuy nhiên còn 5 câu hỏi mở cần BA xác nhận: quan trọng nhất là logic đơn vị tiền tệ cho phân hệ ĐTTN (Q1) và tính hợp lệ của validation V17 khi Quý/Năm đã chuyển Read-only (Q2). QC có thể bắt đầu thiết kế test cho các luồng chính trong khi chờ BA trả lời các câu hỏi còn lại.
