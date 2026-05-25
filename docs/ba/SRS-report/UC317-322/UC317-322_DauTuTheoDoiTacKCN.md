# UC317-322: Tình hình đầu tư nước ngoài vào các KCN, KKT phân theo đối tác đầu tư lũy kế đến cuối kỳ báo cáo

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | yen.trinh |
| **Phân hệ** | Báo cáo KKT/KCN |
| **Mẫu biểu** | 2114.H.QLKKT |
| **Loại báo cáo** | Định kỳ quý/năm |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Cơ quan nhận** | Cục Đầu tư nước ngoài |
| **Đối tượng lập** | Ban Quản lý các khu công nghiệp, kinh tế |
| **Giao diện** | Admin site |
| **Ngày tạo** | 2026-04-23 |
| **Phiên bản** | 1.7 |
| **Quy tắc sinh mã báo cáo** | EZ_2114HQLKKT_[ID] |
| **Loại quy trình** | Quy trình > 2 bước, CMCĐT_BCTK_04 |

**Lịch sử cập nhật:**
- v1.1: Khởi tạo tài liệu.
- v1.2: Cập nhật "Phạm vi dữ liệu đầu vào", đổi tên trường thành "Năm" (YearPicker).

---

## UC317-322.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tình hình đầu tư nước ngoài vào các KCN, KKT phân theo đối tác đầu tư lũy kế đến cuối kỳ báo cáo
- Chức năng cho phép Ban Quản lý các KCN, KKT truy cập màn hình chính để theo dõi danh sách báo cáo, được nhóm theo từng Kỳ hạn báo cáo.

**Precondition:** Người dùng đã đăng nhập thành công và được phân quyền "Cán bộ chuyên môn Ban Quản lý các khu công nghiệp, kinh tế".

Phân quyền: Ban Quản lý các khu công nghiệp, kinh tế. Tham chiếu: CMR_02.

Truy cập chức năng: Phân hệ Báo cáo → Báo cáo KKT/KCN → Tình hình đầu tư nước ngoài phân theo đối tác đầu tư lũy kế (Mẫu 2114.H)

Chức năng đáp ứng usecase số: 317, 318, 319, 320, 321, 322

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: Periodic-single — Giao diện mẫu cho báo cáo có kỳ hạn và gửi lẻ từng báo cáo.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | YearPicker | Null | x | | Lọc danh sách theo năm báo cáo. Kết quả hiển thị ngay khi chọn. |
| 2 | Trạng thái | Multiple-selection Dropdown | Tất cả trạng thái | x | | Lọc theo trạng thái báo cáo. Chọn nhiều giá trị. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 3 | Mã báo cáo | Search bar | Null | x | | Search theo mã báo cáo. Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| 4 | Trạng thái kỳ | Multiple-selection Dropdown | Null | x | | Lọc theo trạng thái:Chưa tới hạn/ Trong thời hạn/ Qua kỳ báo cáo. Tham chiếu: CMR_04. Tham chiếu: CMR_16. |
| **Khung Danh sách Kỳ hạn** | | | | | | |
| 5 | Kỳ hạn báo cáo | Label | Null | | | Mặc định collapse; click mũi tên để expand danh sách. Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ báo cáo | Label | Null | | | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Luôn enable. Chỉ hiển thị khi kỳ ở trạng thái Trong thời hạn. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_04. |
| 8 | Nhập từ file | Button | Null | | | Luôn enable. Mở màn hình chọn/kéo thả file. Chỉ hiển thị khi kỳ ở trạng thái Trong thời hạn. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| **Khung Danh sách Báo cáo** | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | Mã hệ thống sinh. Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | Null | | | Định dạng: dd/MM/yyyy HH:mm. |
| 11 | Trạng thái | Label | Null | | | Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | Null | | | Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Xuất báo cáo theo trạng thái. Tham chiếu: UC317-322.3. |

---

### 3. Mô tả các xử lý của chức năng

- Hệ thống tự động nhóm danh sách theo Kỳ hạn báo cáo (Quý/Năm), mặc định collapse.
- Sắp xếp báo cáo bên trong kỳ theo thứ tự từ mới → cũ.
- [Lập báo cáo] và [Nhập từ file] bị ẩn với kỳ báo cáo chưa bắt đầu. Tham chiếu: CF_01.
- Phân trang. Tham chiếu: CMR_10.

---


## UC317-322.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập mới Báo cáo tình hình đầu tư nước ngoài vào các KCN, KKT phân theo đối tác đầu tư lũy kế (Mẫu 2114.H)
- Chức năng cho phép Ban Quản lý các KCN, KKT tạo báo cáo. Đây là báo cáo tổng hợp (Aggregated Grid Report): hệ thống tự động quét toàn bộ dự án trong kỳ, phân loại theo "Đối tác đầu tư" và tổng hợp số liệu từ 3 nguồn (API nội bộ, IRC, BC 2115.H, BC 2116.H). Người dùng không nhập liệu thủ công vào lưới.

**Precondition:** Dữ liệu Master Data về danh sách dự án phải có sẵn trên hệ thống. Tài khoản có quyền lập báo cáo. Phải có ít nhất 1 báo cáo thuộc 2115.H, 2116.H đã được phê duyệt.

**Postcondition:** Khi Lưu nháp, báo cáo có trạng thái "Lưu nháp". Khi nộp, bản ghi được lưu vào DB với trạng thái "Chờ duyệt", đồng thời trigger quy trình workflow tiếp theo.

Phân quyền: Ban Quản lý các khu công nghiệp, kinh tế. Tham chiếu: CMR_02.

Truy cập chức năng: Màn danh sách báo cáo (UC317-322.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 317, 318

---

### 2. Mô tả giao diện

**Giao diện lập báo cáo**

Giao diện: Aggregated Grid Report — Lưới dữ liệu tổng hợp, toàn bộ Disabled. Hàng được hệ thống tự sinh. Nếu không có dự án nào trong kỳ, Grid hiển thị màn hình trống với Text "Không có dữ liệu đầu tư phát sinh trong kỳ báo cáo" (Empty State).

**Cấu trúc lưới (Grid):**

Mô tả giao diện:

| # | Tên cột | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | STT | Label | Auto | | | Số thứ tự dòng. Hệ thống tự sinh. |
| 2 | Đối tác đầu tư (quốc gia/vùng lãnh thổ) | Label | Null | | x | Hệ thống tự phân loại theo Logic 4-case. Disabled. Tham chiếu: CMR_12. |
| **Khung Trong kỳ báo cáo** | | | | | | |
|  | **Khung Số dự án đầu tư**| | | | | |
| 3 | Cấp mới đầu tư | Number (Disabled) | Null | | x | Auto-fill. Nguồn: API Quản lý dự án nội bộ. Tham chiếu: CMR_12. |
| 4 | Tăng vốn | Number (Disabled) | Null | | x | Auto-fill. Nguồn: BC 2115.H (tổng hợp từ báo cáo điều chỉnh vốn). Tham chiếu: CMR_12. |
| 5 | Giảm vốn | Number (Disabled) | Null | | x | Auto-fill. Nguồn: BC 2115.H. Tham chiếu: CMR_12. |
| 6 | Thu hồi/chấm dứt hoạt động | Number (Disabled) | Null | | x | Auto-fill. Nguồn: BC 2116.H (tổng hợp từ báo cáo thu hồi). Tham chiếu: CMR_12. |
|  |**Khung Tổng vốn đầu tư đăng ký (tr.USD)** | | | | | |
| 7 | Cấp mới đầu tư | Number (Disabled) | Null | | x | Auto-fill. Nguồn: Cục ĐTNN (IRC). Tham chiếu: CMR_12. |
| 8 | Tăng vốn | Number (Disabled) | Null | | x | Auto-fill. Nguồn: BC 2115.H. Tham chiếu: CMR_12. |
| 9 | Giảm vốn | Number (Disabled) | Null | | x | Auto-fill. Nguồn: BC 2115.H. Tham chiếu: CMR_12. |
| 10 | Thu hồi/chấm dứt hoạt động | Number (Disabled) | Null | | x | Auto-fill. Nguồn: BC 2116.H. Tham chiếu: CMR_12. |
| **Khung Lũy kế đến cuối kỳ báo cáo** | | | | | | |
|  |**Khung Số dự án đầu tư còn hiệu lực** | | | | | |
| 11 | Trong các KCN (tính cả các KCN trong KKT ven biển, KKT cửa khẩu) | Number (Disabled) | Null | | x | Auto-fill. Nguồn: API nội bộ. Ghi chú: Tính cả KCN trong KKT ven biển và KKT cửa khẩu. Tham chiếu: CMR_12. |
| 12 | Trong KKT ven biển (không bao gồm các KCN trong KKT) | Number (Disabled) | Null | | x | Auto-fill. Nguồn: API nội bộ. Ghi chú: Không bao gồm các KCN trong KKT. Tham chiếu: CMR_12. |
| 13 | Trong KKT cửa khẩu (không bao gồm các KCN trong KKT) | Number (Disabled) | Null | | x | Auto-fill. Nguồn: API nội bộ. Ghi chú: Không bao gồm các KCN trong KKT. Tham chiếu: CMR_12. |
|  |**Khung Tổng vốn đầu tư đăng ký (tr.USD) ** | | | | | |
| 14 | Trong các KCN (tính cả các KCN trong KKT ven biển, KKT cửa khẩu) | Number (Disabled) | Null | | x | Auto-fill. Nguồn: API nội bộ. Tham chiếu: CMR_12. |
| 15 | Trong KKT ven biển (không bao gồm các KCN trong KKT) | Number (Disabled) | Null | | x | Auto-fill. Nguồn: API nội bộ. Tham chiếu: CMR_12. |
| 16 | Trong KKT cửa khẩu (không bao gồm các KCN trong KKT) | Number (Disabled) | Null | | x | Auto-fill. Nguồn: API nội bộ. Tham chiếu: CMR_12. |
|  |**Khung Tổng vốn đầu tư thực hiện (tr.USD)** | | | | | |
| 17 | Trong các KCN (tính cả các KCN trong KKT ven biển, KKT cửa khẩu) | Number (Disabled) | Null | | x | Auto-fill. Nguồn: API nội bộ. Tham chiếu: CMR_12. |
| 18 | Trong KKT ven biển (không bao gồm các KCN trong KKT) | Number (Disabled) | Null | | x | Auto-fill. Nguồn: API nội bộ. Tham chiếu: CMR_12. |
| 19 | Trong KKT cửa khẩu (không bao gồm các KCN trong KKT) | Number (Disabled) | Null | | x | Auto-fill. Nguồn: API nội bộ. Tham chiếu: CMR_12. |
| **HÀNG TỔNG CỘNG** | | | | | | |
| T | Tổng cộng | Number | Null | | | Hệ thống tự tính tổng cột 3→19 cho tất cả nhóm đối tác. Disabled. Tham chiếu: CMR_05 |
| **CÁC BUTTON** | | | | | | |
| B1 | Hủy | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
| B2 | Xem trước | Button | | | | Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1. |
| B3 | Lưu nháp | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
| B4 | Nộp báo cáo | Button | | | | Tham chiếu: CF_01. |

---

### 3. Mô tả các xử lý của chức năng

Xử lý chung: Tham chiếu: CF_01 (Lập báo cáo), CF_04 (Xuất báo cáo), CF_05 (In).

Xử lý đặc thù biểu mẫu 2114.H (Aggregated Grid):

- Khởi tạo màn hình: Khi người dùng nhấn [Lập báo cáo] cho một kỳ, hệ thống tự động kích hoạt quy trình tổng hợp dữ liệu (không có màn hình chọn dự án).
- Logic sinh dòng – Phân loại Đối tác đầu tư: Hệ thống quét toàn bộ dự án thuộc kỳ báo cáo, xác định nhóm "Đối tác đầu tư" theo Logic 4-case:
  - Nếu 100% vốn Việt Nam → Nhóm: "Việt Nam"
  - Nếu 100% vốn 1 quốc gia nước ngoài → Nhóm: "[Tên quốc gia]"
  - Nếu liên doanh có Việt Nam → Nhóm: "Liên doanh Việt Nam - [QG1] - ... - [QGN]"
  - Nếu liên doanh nhiều quốc gia không có Việt Nam → Nhóm: "Liên doanh khác (không có Việt Nam)"
- Tổng hợp dữ liệu từ nhiều nguồn: Với mỗi nhóm Đối tác, hệ thống SUM dữ liệu tương ứng từ 3 nguồn:
  - Cột 3, 11–19: API Quản lý dự án nội bộ (anh Chí).
  - Cột 7: IRC (Cục ĐTNN).
  - Cột 4, 5, 8, 9: BC 2115.H (lấy dữ liệu điều chỉnh vốn đã được gửi trong kỳ có trạng thái "Đã tiếp nhận").
  - Cột 6, 10: BC 2116.H (lấy dữ liệu thu hồi đã được gửi trong kỳ có trạng thái "Đã tiếp nhận").
- Hàng Tổng cộng: Hệ thống tự tính tổng tất cả các cột số liệu (cột 3→19) từ tất cả các dòng Đối tác. Không cho chỉnh sửa.
- Toàn bộ lưới Disabled: Người dùng chỉ có thể xem và nộp, không nhập liệu. Tham chiếu: CMR_12.
- Định dạng số: Tham chiếu: CMR_08.

---


## UC317-322.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ – Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa

Phân quyền: Ban Quản lý các khu công nghiệp, kinh tế. Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC317-322.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 319, 320, 321, 322

---

### 2. Mô tả giao diện

Các Button theo Action Mapping:

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Chỉ khi Lưu nháp | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa | | Hệ thống tái tổng hợp dữ liệu từ các nguồn. Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Mở màn hình xem toàn bộ lưới (Disabled). Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Mở popup Vòng đời. Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | Kết xuất file Docx. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file Docx. Tham chiếu: CF_04.
- Chỉnh sửa: Khi người dùng mở lại báo cáo ở chế độ sửa, hệ thống có thể tái tổng hợp dữ liệu để cập nhật nếu có thay đổi từ các BC 2115/2116 nguồn. Tham chiếu: CF_03.

---

## 4. Acceptance Criteria

| ID | Kịch bản kiểm thử (Scenario) | Điều kiện (Given) | Hành động (When) | Kết quả mong đợi (Then) |
|---|---|---|---|---|
| AC1 | Kiểm tra logic gom nhóm: Việt Nam | Hệ thống quét dự án trong kỳ | Gặp dự án 100% vốn Việt Nam | Nhóm vào dòng "Việt Nam" |
| AC2 | Kiểm tra logic gom nhóm: 1 Quốc gia nước ngoài | Hệ thống quét dự án | Gặp dự án 100% vốn 1 quốc gia nước ngoài | Nhóm vào dòng "[Tên quốc gia]" (VD: Hàn Quốc) |
| AC3 | Kiểm tra logic gom nhóm: Liên doanh có VN | Hệ thống quét dự án | Gặp dự án có Việt Nam và Hàn Quốc | Nhóm vào dòng "Liên doanh Việt Nam - Hàn Quốc" |
| AC4 | Kiểm tra logic gom nhóm: Liên doanh không VN | Hệ thống quét dự án | Gặp dự án có Nhật Bản và Hàn Quốc | Nhóm vào dòng "Liên doanh khác (không có Việt Nam)" |
| AC5 | Kiểm tra tính tổng Auto-sum | Các dòng đối tác đã có số liệu Cột 3-19 | Hệ thống tính hàng Tổng cộng | Tổng cộng = Sum tất cả các dòng phía trên. Dữ liệu Disabled |

---

## 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-07 | 1.0 → 1.1 | Cập nhật theo Audit | (Nhiều mục) | (Đã cập nhật theo Implementation Plan) | Thêm điều kiện 2115, empty state, AC gom nhóm, đổi nút |
| 2026-05-07 | 1.1 → 1.2 | Thuộc tính chung | Phạm vi báo cáo | Phạm vi dữ liệu đầu vào | Thay đổi tên thuộc tính theo yêu cầu |
| 2026-05-07 | 1.1 → 1.2 | Khung lọc & tìm kiếm | Năm (Yearpicker) | Năm (YearPicker) | Cập nhật điều kiện lọc theo yêu cầu |
| 2026-05-08 | 1.2 → 1.3 | Empty State | 1 dòng trống | Màn hình trống (Empty State) | Cập nhật theo Implementation Plan |
| 2026-05-11 | 1.3 → 1.4 | Quy tắc sinh mã báo cáo | `EZ_2114H_[ID]` | `EZ_2114HQLKKT_[ID]` | Chuẩn hóa suffix HQLKKT đầy đủ theo appendices.md v2.0 |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | +1 | Điều kiện hiển thị nút | `Luôn hiển thị` | `Tất cả trạng thái` | Chuẩn hóa điều kiện (INS-07) |
| 2026-05-11 | 1.3 → 1.4 | Hậu điều kiện | ...Khi Nộp, bản ghi được lưu vào DB với trạng thái "Đã tiếp nhận" hoặc "Chờ duyệt"... | ...Khi nộp, bản ghi được lưu vào DB với trạng thái "Chờ duyệt"... | Cập nhật Hậu điều kiện luồng nộp báo cáo |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (1 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | STD-01 Them CMR_16 vao filter dropdown rows (1 dong) | Chua co CMR_16 | Them tham chieu CMR_16 | Filter phai co Tat ca default |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.4 → 1.5 | Bảng thuộc tính | (Không có) | Bổ sung Loại quy trình: Quy trình > 2 bước, CMCĐT_BCTK_04 | Phân loại luồng quy trình theo yêu cầu |
| 2026-05-21 | 1.5 → 1.6 | Cấu trúc cột & Tên cột Grid Lập báo cáo | (Nhiều cột) | Chèn các dòng tiêu đề phân nhóm và cập nhật tên 17 cột dữ liệu | Đồng bộ hóa cấu trúc bảng theo thiết kế Wireframe của dự án |
| 2026-05-23 | 1.6 → 1.7 | UC317-322.2 Grid – Cột Ghi chú các dòng Auto-fill (cột 3→19) | Auto-fill. Nguồn: ... | Auto-fill. Nguồn: ... | Bổ sung quy tắc không hiển thị placeholder cho các trường autofill |
| 2026-05-23 | 1.6 → 1.7 | UC317-322.2 Grid – Hàng Tổng cộng: Kiểu trường | Label | Number | Đổi kiểu trường phù hợp dữ liệu số |
| 2026-05-23 | 1.6 → 1.7 | UC317-322.2 Grid – Hàng Tổng cộng: Ghi chú | Hệ thống tự tính tổng cột 3→19 cho tất cả nhóm đối tác. Disabled. | Hệ thống tự tính tổng cột 3→19 cho tất cả nhóm đối tác. Disabled. Tham chiếu: CMR_05 | Bổ sung tham chiếu CMR_05 |
