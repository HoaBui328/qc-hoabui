# UC347-352: Các chỉ số đánh giá hiệu quả môi trường, xã hội của doanh nghiệp sinh thái

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | yen.trinh |
| **Phân hệ** | Báo cáo KKT/KCN |
| **Mẫu biểu** | B5 |
| **Loại báo cáo** | Định kỳ năm |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Cơ quan nhận** | Ban quản lý khu công nghiệp, kinh tế |
| **Đối tượng lập** | Nhà đầu tư / Tổ chức kinh tế thực hiện dự án |
| **Giao diện** | User site |
| **Ngày tạo** | 2026-05-14 |
| **Phiên bản** | 1.1 |
| **Quy tắc sinh mã báo cáo** | EZ_B5_[ID] |
| **Loại quy trình** | Quy trình 2 bước, CMCĐT_BCTK_01 |

---

## UC347-352.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo các chỉ số đánh giá hiệu quả môi trường, xã hội của doanh nghiệp sinh thái
- Chức năng cho phép Nhà đầu tư/Tổ chức kinh tế truy cập màn hình chính để theo dõi danh sách báo cáo, được nhóm theo từng Kỳ hạn báo cáo.

Ngoài phạm vi: Quy trình xét duyệt/phê duyệt báo cáo (thuộc Admin site). Quản lý cấu hình kỳ báo cáo. Nhập từ file báo cáo chi tiết (tham chiếu CF_02).

Phân quyền: Mỗi NĐT chỉ lập 1 báo cáo duy nhất cho toàn bộ KCN mà họ quản lý. NĐT có toàn quyền: Xem, Tạo mới, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo.

Điều kiện tiên quyết: Báo cáo này sẽ xuất hiện ở site user (Nhà đầu tư, doanh nghiệp/ tổ chức). Các doanh nghiệp sẽ nhìn thấy danh sách báo cáo.

Truy cập chức năng: Phân hệ Báo cáo → Báo cáo KKT/KCN → Các chỉ số đánh giá hiệu quả môi trường, xã hội của doanh nghiệp sinh thái

Hậu điều kiện: Hiển thị danh sách các kỳ báo cáo, cấu trúc màn hình danh sách báo cáo. Tham chiếu: CS_01.

Acceptance Criteria: Hiển thị toàn bộ các kỳ báo cáo đã được admin lập và các báo cáo mà nhà đầu tư đã nộp. Tham chiếu: CS_01.

Chức năng đáp ứng usecase số: 347, 348, 349, 350, 351, 352

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: Periodic-single — Giao diện mẫu cho báo cáo có kỳ hạn và gửi lẻ từng báo cáo.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | YearPicker | Null | x | | Lọc danh sách theo năm báo cáo. Kết quả hiển thị ngay khi chọn. |
| 2 | Trạng thái kỳ | Multiple-selection Dropdown | Null | x | | Lọc theo trạng thái: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. Tham chiếu: CMR_16. |
| 3 | Trạng thái báo cáo | Multiple-selection Dropdown | Tất cả trạng thái | x | | Lọc theo trạng thái bản ghi (Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa). Chọn nhiều giá trị. Hiển thị kết quả ngay lập tức. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 4 | Mã báo cáo | Search bar | Null | x | | Search theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy: hiển thị "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách Kỳ hạn** | | | | | | |
| 5 | Kỳ hạn báo cáo | Label | Null | | | Hiển thị tên kỳ hạn. Mặc định ở trạng thái collapse; click vào mũi tên sẽ expand ra danh sách các báo cáo của kỳ đó. Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ báo cáo | Label | Null | | | Hiển thị trạng thái kỳ theo thời gian: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | Null | | | Button chỉ hiển thị và enable khi kỳ báo cáo ở trạng thái "Trong thời hạn", và sẽ ẩn đi khi kỳ báo cáo ở trạng thái "Chưa tới hạn" và "Qua kỳ báo cáo". Tham chiếu: CMR_04. |
| 8 | Nhập từ file | Button | Null | | | Button chỉ hiển thị và enable khi kỳ báo cáo ở trạng thái "Trong thời hạn", và sẽ ẩn đi khi kỳ báo cáo ở trạng thái "Chưa tới hạn" và "Qua kỳ báo cáo". Khi click vào thì mở màn hình chọn/kéo thả file nhập từ file. Tham chiếu: CMR_04. |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) | | | | | | |
| 9 | Mã báo cáo | Label | Null | | | Hiển thị mã báo cáo do hệ thống sinh theo quy tắc EZ_B5_[ID]. Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | Null | | | Hiển thị ngày giờ thao tác gần nhất (Lưu nháp / Nộp). Định dạng: dd/MM/yyyy HH:mm. |
| 11 | Trạng thái | Label | Null | | | Trạng thái bản ghi. Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | Null | | | Hiển thị các action: Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Xuất báo cáo theo trạng thái bản ghi. Tham chiếu: UC347-352.3. |

---

### 3. Mô tả các xử lý của chức năng

- Yêu cầu hiển thị:
  - Hệ thống tự động nhóm danh sách theo Kỳ hạn báo cáo, mặc định collapse.
  - Sắp xếp báo cáo bên trong kỳ theo thứ tự từ mới → cũ.
  - Phân trang: Chọn hiển thị số kỳ báo cáo/trang. Tham chiếu: CMR_10.
- Lọc & Tìm kiếm:
  - Do là User Site, danh sách chỉ hiển thị báo cáo của NĐT đang login.
- Ẩn/hiện Action theo kỳ:
  - [Lập báo cáo] và [Nhập từ file] bị ẩn với kỳ báo cáo chưa bắt đầu. Tham chiếu: CF_01.

---

## UC347-352.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập mới Báo cáo các chỉ số đánh giá hiệu quả môi trường, xã hội của doanh nghiệp sinh thái (Mẫu B5)
- Chức năng cho phép Nhà đầu tư điền biểu mẫu dạng bảng gồm 5 chỉ số chia thành 2 section (Môi trường, Xã hội). Hệ thống tự generate bảng có sẵn các dòng khi user mở form.

Phân quyền: Mỗi NĐT chỉ lập 1 báo cáo duy nhất cho toàn bộ KCN mà họ quản lý. NĐT có toàn quyền: Xem, Tạo mới, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo.

Điều kiện tiên quyết: Nhà đầu tư được phân quyền lập báo cáo này và đã đăng nhập vào hệ thống và kỳ báo cáo ở trạng thái Trong thời hạn.

Truy cập chức năng: Màn danh sách báo cáo (UC347-352.1) → Nhấn nút [Lập báo cáo]

Hậu điều kiện: Tùy thuộc vào action người dùng chọn (Hủy / Xem / Lưu nháp / Nộp báo cáo) sẽ có cách xử lý khác nhau. Khi Gửi báo cáo, bản ghi được lưu vào DB với trạng thái "Chờ duyệt", đồng thời trigger quy trình workflow tiếp theo.Tham chiếu: CF_01.

Acceptance Criteria: Phụ thuộc vào hành vi của Nhà đầu tư:
- Người dùng chọn Lưu nháp: Tham chiếu CF_01 → Xử lý nút [Lưu nháp]
- Người dùng chọn Xem chi tiết: Tham chiếu CF_01 → Xử lý nút [Xem chi tiết]
- Người dùng chọn Nộp báo cáo: Tham chiếu CF_01 → Xử lý nút [Nộp báo cáo]
- Người dùng chọn Hủy: Tham chiếu CF_01 → Xử lý nút [Hủy]

Chức năng đáp ứng usecase số: 347, 348

---

### 2. Mô tả giao diện

**Giao diện lập báo cáo**

Giao diện: Form nhập liệu dạng bảng, hệ thống tự generate sẵn 5 dòng chỉ số khi mở form.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **I. MÔI TRƯỜNG** | | | | | | |
| 1 | Áp dụng giải pháp sử dụng hiệu quả tài nguyên và sản xuất sạch hơn (RECP) (ENV.2) | Number | Null | x | x | Nhập số dương, giá trị từ 20 - 100%. Placeholder: "Nhập giá trị từ 20 - 100%". Ngoài khoảng → Error: "Giá trị hợp lệ trong khoảng từ 20 - 100%". Tooltip: Tỷ lệ phần trăm (%) các doanh nghiệp trong khu công nghiệp áp dụng các giải pháp sử dụng hiệu quả tài nguyên và sản xuất sạch hơn. Tham chiếu: CMR_05. |
| **II. XÃ HỘI** | | | | | | |
| 2 | Quy định về tiếp nhận và giải quyết khiếu nại của người lao động (SOC.1) | Number | Null | x | x | Nhập số dương, giá trị từ 75 - 100%. Placeholder: "Nhập giá trị từ 75 - 100%". Ngoài khoảng → Error: "Giá trị hợp lệ trong khoảng từ 75 - 100%". Tooltip: Tỷ lệ doanh nghiệp trong khu công nghiệp có trên 100 lao động có các quy định về việc tiếp nhận và giải quyết các khiếu nại của người lao động. Tham chiếu: CMR_05. |
| 3 | Công khai thông tin và trách nhiệm giải trình (SOC.2) | Number | Null | x | x | Nhập số dương, giá trị từ 75 - 100%. Placeholder: "Nhập giá trị từ 75 - 100%". Ngoài khoảng → Error: "Giá trị hợp lệ trong khoảng từ 75 - 100%". Tooltip: Tỷ lệ doanh nghiệp công khai thông tin (trên cổng thông tin điện tử, báo chí). Tham chiếu: CMR_05. |
| 4 | Bình đẳng giới và dịch vụ xã hội (SOC.4) | Number | Null | x | x | Nhập số dương, giá trị từ 75 - 100%. Placeholder: "Nhập giá trị từ 75 - 100%". Ngoài khoảng → Error: "Giá trị hợp lệ trong khoảng từ 75 - 100%". Tooltip: Tỷ lệ doanh nghiệp trong khu công nghiệp có trên 100 lao động thực hiện bình đẳng giới trong an sinh xã hội, an toàn lao động, vệ sinh lao động, tập huấn về áp dụng hiệu quả tài nguyên và sản xuất sạch hơn (RECP). Tham chiếu: CMR_05. |
| 5 | Phòng chống quấy rối và phân biệt đối xử (SOC.6) | Number | Null | x | x | Nhập số dương, giá trị từ 75 - 100%. Placeholder: "Nhập giá trị từ 75 - 100%". Ngoài khoảng → Error: "Giá trị hợp lệ trong khoảng từ 75 - 100%". Tooltip: Doanh nghiệp có các quy định về phòng chống quấy rối và phân biệt đối xử tại nơi làm việc. Tham chiếu: CMR_05. |
| **CÁC BUTTON** | | | | | | |
| B1 | Hủy | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
| B2 | Xem trước | Button | | | | Mở popup PDF Preview báo cáo (không rời màn Lập). Tham chiếu: CF_07.1. |
| B3 | Lưu nháp | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
| B4 | Nộp báo cáo | Button | | | | Tham chiếu: CF_01. |

---

### 3. Mô tả các xử lý của chức năng

Xử lý chung: Tham chiếu: CF_01 (Lập báo cáo), CF_04 (Xuất báo cáo), CF_05 (In).

Xử lý đặc thù biểu mẫu B5:

- Khởi tạo màn hình: Hệ thống tự generate bảng 5 dòng chỉ số thuộc 2 section (Môi trường, Xã hội). Tất cả trường ở trạng thái Enabled, giá trị trống.
- Không có bước chọn dự án (phạm vi = Không có phạm vi).
- Mỗi NĐT chỉ lập được 1 báo cáo duy nhất cho toàn bộ KCN mà họ quản lý trong mỗi kỳ.
- Validation:
  - Tất cả 5 dòng: Số dương, từ 0 - 100%. Ngoài khoảng → Error: "Giá trị hợp lệ trong khoảng từ 0 - 100%". Tham chiếu: CMR_05.
- Xuất báo cáo: Định dạng Docx.

---

## UC347-352.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ – Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa
- Chức năng cho phép Nhà đầu tư thực hiện tác vụ theo trạng thái báo cáo (Lưu nháp / Yêu cầu chỉnh sửa).

Phân quyền: Mỗi NĐT chỉ lập 1 báo cáo duy nhất cho toàn bộ KCN mà họ quản lý. NĐT có toàn quyền: Xem, Tạo mới, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo. Hành động hiển thị theo trạng thái bản ghi. Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC347-352.1) → Cột Hành động → Chọn tác vụ tương ứng

Hậu điều kiện: Tùy thuộc action: Xem chi tiết → hiển thị full-page read-only (CF_07); Xóa → bản ghi bị xóa khỏi danh sách (CF_08); Nộp → chuyển trạng thái theo CMR_03; Chỉnh sửa → mở form chỉnh sửa (CF_03).

Chức năng đáp ứng usecase số: 349, 350, 351, 352

---

### 2. Mô tả giao diện

**Màn hình Xem chi tiết (Full-Page View Screen)**

Tham chiếu: CF_07.

- Giao diện: Form đọc (toàn bộ trường Disabled), layout giống hệt màn hình Lập báo cáo.
- Nút [Chỉnh sửa]: Chỉ hiển thị khi bản ghi ở trạng thái Lưu nháp hoặc Yêu cầu chỉnh sửa. Tham chiếu: CF_07, CMR_03.
- Nút [Hủy]: Quay về màn hình Danh sách. Không cần popup xác nhận.

**Popup Xem vòng đời (Audit Trail)**

Tham chiếu: CF_06.

**Các Button theo Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Mô tả |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp | Button | Chỉ khi Lưu nháp | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa | Button | Chỉ khi Lưu nháp hoặc Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Khi click mở màn hình Xem chi tiết báo cáo. Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Khi click mở popup Vòng đời. Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Tham chiếu: CF_07.
- Xem vòng đời: Tham chiếu: CF_06.
- In báo cáo: Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file Docx. Tham chiếu: CF_04.
- Chỉnh sửa: Tham chiếu: CF_03.

---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-14 | 1.0 | Khởi tạo | — | Tạo mới UC347-352 | Init Report Flow |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (1 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | STD-01 Them CMR_16 vao filter dropdown rows (1 dong) | Chua co CMR_16 | Them tham chieu CMR_16 | Filter phai co Tat ca default |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.0 → 1.1 | Bảng thuộc tính | (Không có) | Bổ sung Loại quy trình: Quy trình 2 bước, CMCĐT_BCTK_01 | Phân loại luồng quy trình theo yêu cầu |
