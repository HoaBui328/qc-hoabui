C299-304: Tình hình thu hút dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng trong khu kinh tế lũy kế đến cuối kỳ báo cáo

(Không bao gồm các dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng trong KCN, KCX)

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | Yen.trinh |
| **Phân hệ** | Quản lý KCN, KKT |
| **Mẫu biểu** | 2111.H.QLKKT [MBFS] |
| Phân hệ Báo cáo | KCN, KKT |
| **Loại báo cáo** | Định kỳ (Quý / Năm) |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Phạm vi báo cáo** | Không có phạm vi |
| **File xuất** | .doc |
| **Cơ quan nhận** | Cục Đầu tư nước ngoài |
| **Đối tượng lập** | Ban Quản lý các khu công nghiệp, kinh tế |
| **Giao diện** | Admin site |
| **Ngày tạo** | 2026-04-22 |
| **Phiên bản** | 1.6 |
| **Quy tắc sinh mã báo cáo** | EZ_2111HQLKKT_[ID] |
| **Loại quy trình** | Quy trình > 2 bước, CMCĐT_BCTK_04 |

---

## Điều kiện tiên quyết & Hậu điều kiện

**1. Điều kiện tiên quyết**
- **Xem danh sách báo cáo**: Admin hệ thống phải thiết lập Kỳ báo cáo (nếu chưa thiết lập, danh sách sẽ hiển thị trống). Danh sách báo cáo hiển thị phía site user (Nhà đầu tư, tổ chức kinh tế) và site admin dành cho các role phải nộp báo cáo cho cấp trên (CB chuyên môn BQL/Bộ).
- **Lập báo cáo**: Hệ thống cần có sẵn dữ liệu Master Data (KKT, Dự án, NĐT) để auto-fill. Đối tượng được phép lập báo cáo sẽ được cấu hình cụ thể trong Kỳ báo cáo.

**2. Hậu điều kiện**
- **Lưu nháp**: Báo cáo lưu ở trạng thái "Lưu nháp", hiển thị trên danh sách.
- **Nộp báo cáo**: Khi nộp, bản ghi được lưu vào DB với trạng thái "Chờ duyệt", đồng thời trigger quy trình workflow tiếp theo.

---

## UC299-304.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách Biểu tổng hợp tình hình xây dựng và phát triển các KKT (Biểu số 2111.H.QLKKT)
- Chức năng cho phép Cán bộ chuyên môn Ban Quản lý khu truy cập màn hình chính để theo dõi danh sách các báo cáo định kỳ theo kỳ hạn Quý/Năm. Danh sách hiển thị theo cấu trúc kỳ hạn (collapsible), mỗi kỳ chứa các báo cáo đã gửi.

Phân quyền: Cán bộ chuyên môn Ban Quản lý khu.

Truy cập chức năng: Phân hệ Báo cáo → Quản lý KCN, KKT → Biểu tổng hợp KKT

Chức năng đáp ứng usecase số: 299, 300

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện:

**Periodic-single**: Giao diện mẫu cho loại Báo cáo đơn lẻ có kỳ hạn (Quý/Năm). Kỳ hạn mặc định collapse, khi click vào mũi tên sẽ expand ra danh sách các báo cáo đã gửi.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | Yearpicker | Null | x | | Lọc danh sách theo năm báo cáo. Kết quả hiển thị ngay khi chọn. |
| 2 | Trạng thái báo cáo | Multiple-selection Dropdown | Null | x | | Lọc theo trạng thái của báo cáo. Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả hiển thị ngay khi chọn. Tham chiếu: CMR_07., CMR_16 |
| 3 | Mã báo cáo | Search bar | Null | x | | Search theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy: hiển thị màn hình trắng với text "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| 4 | Trạng thái kỳ | Multiple-selection Dropdown | Null | x | | Lọc theo trạng thái:Chưa tới hạn/ Trong thời hạn/ Qua kỳ báo cáo. Tham chiếu: CMR_04. Tham chiếu: CMR_16. |
| **Khung Kỳ hạn báo cáo (Collapsible Section)** | | | | | | |
| 5 | Kỳ báo cáo | Label (collapsible) | Mặc định: collapse | | | Hiển thị tên kỳ (VD: "Quý I/2026", "Năm 2026"). Mặc định collapse. Khi click → expand ra bảng danh sách báo cáo. Tham chiếu: CMR_08. |
| 6 | Trạng thái kỳ báo cáo | Label | | | | Trạng thái kỳ hạn: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 7 | Lập báo cáo | Button | | | | Ẩn khi kỳ "Chưa tới hạn". Luôn enable khi hiển thị (cho phép lập cả khi quá hạn). Khi click vào sẽ hiển thị giao diện Lập báo cáo. Tham chiếu: CF_01, CMR_04. |
| 8 | Nhập từ file | Button | | | | Ẩn khi kỳ "Chưa tới hạn". Luôn enable khi hiển thị. Khi click vào sẽ hiển thị giao diện luồng nhập từ file. Tham chiếu: CF_02, CMR_04. |
| **Bảng danh sách báo cáo (trong mỗi kỳ)** | | | | | | |
| 9 | Mã báo cáo | Label | | | | Mã hệ thống sinh tự động. Tham chiếu: CMR_09. |
| 10 | Ngày cập nhật | Label | | | | Thời điểm thao tác gần nhất. Định dạng: dd/MM/yyyy HH:mm. |
| 11 | Trạng thái báo cáo | Label | | | | Trạng thái báo cáo. Tham chiếu: CMR_03. |
| 12 | Hành động | Button group | | | | Hiển thị các nút thao tác theo trạng thái bản ghi và phân quyền. Chi tiết tham chiếu: UC299-304.3. |

---

### 3. Mô tả các xử lý của chức năng

- Yêu cầu về hiển thị danh sách:
  - Sort: theo thứ tự từ mới → cũ (giảm dần theo ngày cập nhật).
  - Phân trang: Số kỳ báo cáo / trang + điều hướng trang. Tham chiếu: CMR_10.

- Thao tác lọc & tìm kiếm:
  - Tất cả bộ lọc (Kỳ báo cáo — Yearpicker, Trạng thái) và ô tìm kiếm Mã báo cáo đều hiển thị kết quả ngay lập tức, không cần nhấn nút xác nhận.
  - Nếu không có kết quả: hiển thị text "Không tìm thấy kết quả".

---


## UC299-304.2: Lập Báo Cáo (Dạng Bảng)

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập Biểu tổng hợp tình hình xây dựng và phát triển các KKT (2111.H.QLKKT)
- Chức năng cho phép Cán bộ chuyên môn nhập liệu báo cáo dạng bảng. Mỗi dòng (row) tương ứng với 1 KKT/dự án. Bảng gồm 20 cột thông tin. Dòng cuối cùng là dòng Tổng (auto-sum các cột số). Tham chiếu: CF_01.

Phân quyền: Cán bộ chuyên môn Ban Quản lý khu.

Truy cập chức năng: Màn danh sách báo cáo (UC299-304.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 299, 300

---

### 2. Mô tả giao diện

**Giao diện thêm mới — Dạng bảng (Table-based Form)**

Giao diện: Màn hình nhập liệu dạng lưới (grid), 20 cột, nhiều dòng, dòng Tổng cuối bảng.

**Quy tắc Add/Remove Row:** Tham chiếu: CMR_15.

Mô tả giao diện:

| Col# | Tên cột | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | STT | Number | Null | x | x | Cho phép người dùng input STT. Tham chiếu: CMR_05. |
| 2 | KKT | Dropdown | Null | x | x | Dropdown hiển thị danh sách Khu Kinh Tế từ Master Data hệ thống. Cho phép chọn 1 giá trị. Cho phép chọn trùng khu ở các dòng khác nhau. Tham chiếu: CMR_07. |
| 3 | Loại hình | Textbox | Null | | x | Auto fill dữ liệu theo Cột 2. Disabled. Tham chiếu: CMR_06. |
| 4 | Tên dự án/khu chức năng | Dropdown | Null | x | x | Hiển thị danh sách dự án/khu chức năng thuộc KKT đã chọn ở Cột 2. Dữ liệu lấy từ IRC, filtered theo KKT. Chọn 1 giá trị. Khi chọn → auto-fill Cột 5 (Địa điểm). Khi người dùng chọn dự án, nếu dự án đó đã được chọn ở dòng khác thì không cho chọn và hiển thị message lỗi inline "Dự án đã được chọn trước đó. Vui lòng kiểm tra lại". Tham chiếu: CMR_07, CMR_12. |
| 5 | Địa điểm | Textbox | Null | | x | Auto-fill theo Tên dự án/Khu chức năng đã chọn (Cột 4). Disabled. Tham chiếu: CMR_12. |
| 6 | Văn bản thành lập hoặc tương đương | Textarea | Null | | x | Auto fill dữ liệu theo Cột 2. Disabled. Tham chiếu: CMR_06. |
| 7 | Tên nhà đầu tư xây dựng kết cấu hạ tầng | Dropdown (multi) | Null | x | x | Dữ liệu lấy từ IRC. Cho phép chọn nhiều NĐT. Khi chọn → auto-fill Col#8 (Quốc tịch). Tham chiếu: CMR_07, CMR_12. |
| 8 | Quốc tịch nhà đầu tư | Text | Null | | x | Auto-fill theo Tên NĐT đã chọn (Col#7). Disabled, không cho phép sửa. Tham chiếu: CMR_12. |
| 9 | Tình trạng | Dropdown | Null | x | x | 2 giá trị: Đang xây dựng / Đã đi vào hoạt động. Chọn 1 giá trị. Tham chiếu: CMR_07. |
| 10 | Quy mô DT đất quy hoạch (ha) | Number | Null | x | x | Cho phép số thập phân. Tham chiếu: CMR_05. |
| 11 | Quy mô DT đất thành lập (ha) | Number | Null | x | x | Cho phép số thập phân. Tham chiếu: CMR_05. |
| 12 | Quy mô DT đã đi vào hoạt động (ha) | Number | Null | x | x | Cho phép số thập phân. Tham chiếu: CMR_05. |
| 13 | Vốn ĐTNN — Vốn đăng ký (tr.USD) | Number | Null | | x | Auto-fill từ IRC theo từng dự án/KKT. Disabled. Tham chiếu: CMR_12. |
| 14 | Vốn ĐTNN — Vốn thực hiện (tr.USD) | Number | Null | | x | Auto-fill từ IRC. Disabled. Tham chiếu: CMR_12. |
| 15 | Vốn ĐTTN — Vốn đăng ký (tỷ VNĐ) | Number | Null | | x | Auto-fill từ IRC. Disabled. Tham chiếu: CMR_12. |
| 16 | Vốn ĐTTN — Vốn thực hiện (tỷ VNĐ) | Number | Null | | x | Auto-fill từ IRC. Disabled. Tham chiếu: CMR_12. |
| 17 | Doanh thu (tr.USD) | Number | Null | x | x | Người dùng nhập. Validate: >= 0. Tham chiếu: CMR_05. |
| 18 | Giá trị xuất khẩu (nếu có) (tr.USD) | Number | Null | x | x | Người dùng nhập. Validate: >= 0. Tham chiếu: CMR_05. |
| 19 | Giá trị nhập khẩu (nếu có) (tr.USD) | Number | Null | x | x | Người dùng nhập. Validate: >= 0. Tham chiếu: CMR_05. |
| 20 | Nộp ngân sách (tỷ VNĐ) | Number | Null | x | x | Người dùng nhập. Validate: >= 0. Tham chiếu: CMR_05. |

**Dòng Tổng (Summary Row — cuối bảng):**

| Cột | Công thức | Ghi chú |
| --- | --- | --- |
| Col#10 – Col#20 | Auto-sum toàn bộ giá trị cùng cột của các dòng dữ liệu | Disabled. Tính tự động real-time khi dữ liệu thay đổi. |

**Các Button:**

| # | Tên | Ghi chú |
| --- | --- | --- |
| 21 | Hủy | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
| 22 | Xem trước | Popup PDF/Doc Preview. Tham chiếu: CF_07.1. |
| 23 | Lưu nháp | Tham chiếu: CF_01. Chỉ cần ít nhất 1 thông tin có dữ liệu là button Enable. Không validate bất kỳ định dạng hay trường bắt buộc nào. |
| 24 | Nộp báo cáo | Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |

---

### 3. Mô tả các xử lý của chức năng

**Xử lý chung:** Tham chiếu: CF_01 (Lập báo cáo), CF_04 (Xuất báo cáo), CF_05 (In), CF_07 (nút [Xem trước]).

**Xử lý đặc thù biểu mẫu 2111.H.QLKKT:**

- Khởi tạo màn hình: Form mở ra với 1 dòng trống. Cột KKT (Col#2) ở trạng thái Enabled. Cột Tên dự án (Col#4) Disabled cho đến khi chọn KKT. Các cột auto-fill (Col#5, #8, #13-#16) Disabled cho đến khi chọn dự án. Tham chiếu: CMR_12.
- Cascade Dropdown:
  - Chọn KKT (Col#2) → Enable Col#4 (Tên dự án/khu chức năng) và load danh sách filtered theo KKT đã chọn.
  - Chọn Tên dự án (Col#4) → Auto-fill Col#5 (Địa điểm) từ IRC. Tham chiếu: CMR_12.
  - Chọn NĐT (Col#7) → Auto-fill Col#8 (Quốc tịch) từ IRC. Tham chiếu: CMR_12.
- Auto-fill vốn đầu tư (Col#13-#16): Sau khi chọn Tên dự án (Col#4), hệ thống gọi API/IRC và điền tự động 4 cột vốn đầu tư. Disabled. Tham chiếu: CMR_12.
- Dòng Tổng: Auto-sum real-time cho Col#10 đến Col#20. Disabled, không cho phép sửa.
- Add/Remove Row: Tham chiếu: CMR_15.

---


## UC299-304.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ — Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Xóa
- Quyền truy cập kiểm soát theo CMR_03.

Phân quyền: Cán bộ chuyên môn Ban Quản lý khu (người tạo). Tham chiếu: CMR_03.

Truy cập: Màn danh sách báo cáo (UC299-304.1) → Cột Hành động

Chức năng đáp ứng usecase số: 301, 302, 303, 304

---

### 2. Mô tả giao diện

**Màn hình Xem chi tiết (Full-Page View Screen)**

Tham chiếu: CF_07.

- Giao diện: Form đọc (toàn bộ trường Disabled), layout giống màn hình Chỉnh sửa (CF_03). Hiển thị bảng full + dòng Tổng.
- Nút [Chỉnh sửa]: Chỉ hiển thị khi bản ghi ở trạng thái Lưu nháp hoặc Yêu cầu chỉnh sửa VÀ người dùng là người tạo. Tham chiếu: CF_07, CMR_03.
- Nút [Xem trước]: Popup Doc Preview. Tham chiếu: CF_07.1.
- Nút [Hủy]: Quay về Danh sách. Không cần popup xác nhận.

**Popup Xem vòng đời:** Tham chiếu: CF_06.

**Action Mapping:**

| # | Tên | Kiểu | Điều kiện hiển thị | Phân quyền | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp báo cáo | Button | Lưu nháp, Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_03. |
| 2 | Chỉnh sửa | Button | Lưu nháp, Yêu cầu chỉnh sửa | Người tạo | Tham chiếu: CF_03, CMR_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Người tạo, và các role cán bộ khác trong quy trình nộp | Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Người tạo, các role cán bộ khác trong quy trình nộp | Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | Người tạo, các role cán bộ khác trong quy trình nộp | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Người tạo, các role cán bộ khác trong quy trình nộp | .doc. Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp VÀ chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Nộp báo cáo: Tham chiếu: CF_09. Tham chiếu: CF_01. Cho phép gửi từ trạng thái Lưu nháp và Yêu cầu chỉnh sửa (theo CMR_03).
- Chỉnh sửa: Tham chiếu: CF_03.
- Xem chi tiết: Tham chiếu: CF_07. Nút [Chỉnh sửa] ẩn nếu không đủ điều kiện (CMR_03).
- Xem vòng đời: Tham chiếu: CF_06.
- In: Tham chiếu: CF_05.
- Xuất báo cáo: .doc. Tham chiếu: CF_04.
- Xóa: Tham chiếu: CF_08.

---



---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-06 | 1.0 → 1.1 | Điều kiện tiên quyết & Hậu điều kiện | (Không có) | Bổ sung đầy đủ cho luồng xem DS và lập báo cáo | Bổ sung theo QnA |
| 2026-05-06 | 1.0 → 1.1 | Số lượng cột bảng lưới | Bảng gồm 18 cột | Bảng gồm 20 cột | Sửa lỗi mô tả mâu thuẫn |
| 2026-05-06 | 1.0 → 1.1 | Tên nút Submit | Nộp báo cáo | Nộp báo cáo | Đổi tên nút theo CF_01 |
| 2026-05-06 | 1.0 → 1.1 | Nút Lưu nháp | Chỉ tham chiếu CF_01 | Enable khi có >= 1 thông tin, không validate | Làm rõ behavior theo QnA |
| 2026-05-06 | 1.1 → 1.2 | Thuộc tính Phạm vi báo cáo | (Không có) | Bổ sung: Không có phạm vi | Phân loại báo cáo theo cấu trúc mới |
| 2026-05-08 | 1.2 → 1.3 | Quy tắc Add/Remove Row | Inline rule chi tiết | Tham chiếu: CMR_15 | Chuẩn hóa quy tắc thêm/xóa hàng |
| 2026-05-08 | 1.3 → 1.4 | Tên nút Submit | Nộp báo cáo (6 lần) | Nộp báo cáo | Thống nhất tên nút toàn hệ thống |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | 1.2 → 1.3 | Hậu điều kiện | Báo cáo chuyển trạng thái sang "Chờ duyệt" hoặc "Đã tiếp nhận" | Khi nộp, bản ghi được lưu vào DB với trạng thái "Chờ duyệt", đồng thời trigger quy trình workflow tiếp theo. | Cập nhật Hậu điều kiện luồng nộp báo cáo |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (1 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | STD-01 Them CMR_16 vao filter dropdown rows (1 dong) | Chua co CMR_16 | Them tham chieu CMR_16 | Filter phai co Tat ca default |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.3 → 1.4 | Bảng thuộc tính | (Không có) | Bổ sung Loại quy trình: Quy trình > 2 bước, CMCĐT_BCTK_04 | Phân loại luồng quy trình theo yêu cầu |
| 2026-05-21 | 1.4 → 1.5 | Nhãn bộ lọc danh sách | Kỳ báo cáo | Năm | Thay đổi đồng bộ theo ý kiến người dùng để khớp Wireframe |
| 2026-05-21 | 1.4 → 1.5 | Tên cột danh sách | Trạng thái | Trạng thái báo cáo | Đồng bộ với Wireframe thiết kế |
| 2026-05-21 | 1.4 → 1.5 | Tên nút bấm | Nhập từ file / Xuất báo cáo | Import / Export | Thay đổi sang tiếng Anh để đồng bộ theo comment của người dùng |
| 2026-05-21 | 1.4 → 1.5 | Tên cột lập báo cáo | Tên NĐT xây dựng kết cấu hạ tầng | Tên nhà đầu tư xây dựng kết cấu hạ tầng | Viết đầy đủ theo thống nhất giao diện |
| 2026-05-23 | 1.5 → 1.6 | Giá trị mặc định Col#5, #8, #13–#16 | Từ IRC | Null | Phản ánh trạng thái ban đầu khi chưa chọn dự án/NĐT |
| 2026-05-23 | 1.5 → 1.6 | Ghi chú các dòng Auto fill (Col#3, #5, #6, #8, #13–#16) | (Không có) | Bổ sung "Không hiển thị placeholder" ở đầu ghi chú | Yêu cầu nghiệp vụ mới |
| 2026-05-23 | 1.5 → 1.6 | Ghi chú Col#2 (KKT) | Cho phép chọn 1 giá trị. Tham chiếu: CMR_07. | Cho phép chọn 1 giá trị. Cho phép chọn trùng khu ở các dòng khác nhau. Tham chiếu: CMR_07. | Bổ sung quy tắc chọn trùng KKT |
| 2026-05-23 | 1.5 → 1.6 | Ghi chú Col#4 (Tên dự án) | Khi chọn → auto-fill Cột 5 (Địa điểm). Tham chiếu: CMR_07, CMR_12. | Bổ sung validate: không cho chọn trùng dự án, hiển thị message lỗi inline | Bổ sung quy tắc unique dự án |
| 2026-05-23 | 1.5 → 1.6 | Kiểu trường Col#3, #5 | Text | Textbox | Thay đổi kiểu trường theo yêu cầu |
| 2026-05-23 | 1.5 → 1.6 | Kiểu trường Col#6 | Text | Textarea | Thay đổi kiểu trường theo yêu cầu |
| 2026-05-23 | 1.5 → 1.6 | Cột "Được sửa" Col#3, #6 | x | (Trống — Disabled) | Các trường auto-fill không cho phép sửa |
