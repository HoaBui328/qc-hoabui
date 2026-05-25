# UC329-334: Tình hình thu hồi quyết định chủ trương đầu tư/GCNĐKĐT tại các KCN, KKT trong kỳ báo cáo

| Thuộc tính | Giá trị |
| --- | --- |
| **BA phụ trách** | yen.trinh |
| **Phân hệ** | Báo cáo KKT/KCN |
| **Mẫu biểu** | 2116.H.QLKKT |
| **Loại báo cáo** | Định kỳ quý/năm |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form) |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Cơ quan nhận** | Cục Đầu tư nước ngoài |
| **Đối tượng lập** | Ban Quản lý các khu công nghiệp, kinh tế |
| **Giao diện** | Admin site |
| **Ngày tạo** | 2026-04-23 |
| **Phiên bản** | 1.7 |
| **Quy tắc sinh mã báo cáo** | EZ_2116HQLKKT_[ID] |
| **Loại quy trình** | Quy trình > 2 bước, CMCĐT_BCTK_04 |

---

## UC329-334.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách báo cáo tình hình thu hồi quyết định chủ trương đầu tư/GCNĐKĐT tại các KCN, KKT trong kỳ báo cáo
- Chức năng cho phép Ban Quản lý các KCN, KKT truy cập màn hình chính để theo dõi danh sách báo cáo, được nhóm theo từng Kỳ hạn báo cáo.

Phân quyền: Ban Quản lý các khu công nghiệp, kinh tế.

Truy cập chức năng: Phân hệ Báo cáo → Báo cáo KKT/KCN → Tình hình thu hồi quyết định chủ trương đầu tư/GCNĐKĐT tại các KCN, KKT

Chức năng đáp ứng usecase số: 329, 330, 331, 332, 333, 334

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện: Periodic-single — Giao diện mẫu cho báo cáo có kỳ hạn và gửi lẻ từng báo cáo.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm** | | | | | | |
| 1 | Năm | YearPicker | Null | x | | Lọc danh sách theo năm báo cáo. Kết quả hiển thị ngay khi chọn. |
| 2 | Trạng thái | Multiple-selection Dropdown | Tất cả trạng thái | x | | Lọc theo trạng thái của báo cáo. Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 3 | Mã báo cáo | Search bar | Null | x | | Search theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Nếu không tìm thấy kết quả: hiển thị màn hình trắng với text "Không tìm thấy kết quả". Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| 4 | Trạng thái kỳ | Multiple-selection Dropdown | Null | x | | Lọc theo trạng thái:Chưa tới hạn/ Trong thời hạn/ Qua kỳ báo cáo. Tham chiếu: CMR_04. Tham chiếu: CMR_16. |
| 5 | Năm | Yearpicker | | | | Lọc danh sách theo năm báo cáo. Kết quả hiển thị ngay khi chọn. Tham chiếu: CMR_07. |
| **Khung Danh sách Kỳ hạn** | | | | | | |
| 6 | Kỳ hạn báo cáo | Label | Null | | | Hiển thị tên kỳ hạn. Mặc định ở trạng thái collapse; khi click vào mũi tên sẽ expand ra danh sách các báo cáo đã gửi của kỳ đó. Tham chiếu: CMR_08. |
| 7 | Trạng thái kỳ báo cáo | Label | Null | | | Hiển thị trạng thái kỳ theo thời gian: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 8 | Lập báo cáo | Button | Null | | | Chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi kỳ ở trạng thái Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_04. Tham chiếu: CF_01. |
| 9 | Nhập từ file | Button | Null | | | Chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi kỳ ở trạng thái Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| **Khung Danh sách Báo cáo** (trong mỗi kỳ) | | | | | | |
| 10 | Mã báo cáo | Label | Null | | | Hiển thị mã báo cáo do hệ thống sinh theo quy tắc. Tham chiếu: CMR_09. |
| 11 | Ngày cập nhật | Label | Null | | | Hiển thị ngày giờ của thao tác gần nhất (Lưu nháp / Nộp). Định dạng: dd/MM/yyyy HH:mm. |
| 12 | Trạng thái | Label | Null | | | Trạng thái của bản ghi báo cáo. Tham chiếu: CMR_03. |
| 13 | Hành động | Button group | Null | | | Hiển thị các nút thao tác theo trạng thái bản ghi. Chi tiết tham chiếu: UC329-334.3. |

---

### 3. Mô tả các xử lý của chức năng

- Yêu cầu về hiển thị tại khung danh sách kỳ hạn:
  - Hệ thống tự động nhóm danh sách theo Kỳ hạn báo cáo.
  - Sắp xếp báo cáo bên trong mỗi kỳ theo thứ tự từ mới → cũ.
  - Phân trang: Chọn hiển thị số kỳ báo cáo/trang. Tham chiếu: CMR_10.
- Thao tác lọc & tìm kiếm:
  - Tất cả bộ lọc và ô tìm kiếm hiển thị kết quả ngay lập tức, không cần nhấn thêm nút.
  - Nếu không có kết quả: màn hình trắng hiển thị text "Không tìm thấy kết quả".
- Xử lý hiển thị Action theo kỳ báo cáo:
  - Nút [Lập báo cáo] và [Nhập từ file] chỉ hiển thị khi kỳ ở trạng thái **Trong thời hạn**. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_04. Tham chiếu: CF_01.

---


## UC329-334.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Lập mới báo cáo tình hình thu hồi quyết định chủ trương đầu tư/GCNĐKĐT tại các KCN, KKT trong kỳ báo cáo
- Chức năng cho phép Ban Quản lý chọn các dự án bị thu hồi trong kỳ và điền thông tin văn bản thu hồi tương ứng. Bảng dữ liệu phân làm 2 mục theo loại hình dự án. Hệ thống tự động phân loại dự án khi chọn. Tham chiếu: CF_01.

**Precondition:** Dữ liệu Master Data về danh sách dự án phải có sẵn trên hệ thống. Tài khoản có quyền lập báo cáo.

**Postcondition:** Khi Lưu nháp, báo cáo có trạng thái "Lưu nháp". Khi nộp, bản ghi được lưu vào DB với trạng thái "Chờ duyệt", đồng thời trigger quy trình workflow tiếp theo.

Phân quyền: Ban Quản lý các khu công nghiệp, kinh tế. Tham chiếu: CMR_04.

Truy cập chức năng: Màn danh sách báo cáo (UC329-334.1) → Nhấn nút [Lập báo cáo]

Chức năng đáp ứng usecase số: 329, 330

---

### 2. Mô tả giao diện

**Giao diện lập báo cáo**

Giao diện: Màn hình nhập liệu dạng bảng Grid với 2 Section phân nhóm.

Mô tả giao diện:

| # | Tên trường | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả/Ghi chú |
| --- | --- | --- | --- | --- | --- | --- |
| **MỤC 1 – DỰ ÁN ĐẦU TƯ XÂY DỰNG VÀ KINH DOANH KẾT CẤU HẠ TẦNG KCN, KKT** | | | | | | Hệ thống tự động phân loại bản ghi vào mục này nếu dự án thuộc loại hình đầu tư xây dựng và kinh doanh hạ tầng theo API. |
| **MỤC 2 – DỰ ÁN ĐẦU TƯ SẢN XUẤT KINH DOANH TRONG KCN, KKT** | | | | | | Hệ thống tự động phân loại bản ghi vào mục này nếu dự án thuộc loại hình đầu tư sản xuất kinh doanh theo API. |
| **CỘT THÔNG TIN (áp dụng cho tất cả bản ghi trong cả 2 mục)** | | | | | | |
| 1 | STT | Label | Tự tăng | | | Số thứ tự tự động tăng theo từng dòng trong mỗi mục, bắt đầu từ 1. |
| 2 | Tên dự án đầu tư | Dropdown | Null | x | x | Lấy danh sách dự án từ API Quản lý dự án nội bộ, filter theo quyền của BQL. Ngay khi chọn, hệ thống gọi song song 2 API (nội bộ + IRC) để điền tự động các cột 3–8 và phân loại bản ghi vào Mục 1 hoặc Mục 2. Khi chọn dự án đã được chọn trước đó thì không cho chọn và hiển thị message lỗi inline "Dự án được chọn trước đó. Vui lòng kiểm tra lại". Tham chiếu: CF_01, CMR_07. |
| 3 | Tên KCN/KK | Textbox | Null | | x | Tự động điền từ API Quản lý dự án nội bộ theo dự án đã chọn ở cột 2. Trạng thái: Disabled. Tham chiếu: CMR_12, CMR_06. |
| 4 | Văn bản thành lập hoặc tương đương | Textbox | Null | | x | Tự động điền từ API Quản lý dự án nội bộ theo dự án đã chọn ở cột 2. Trạng thái: Disabled. Tham chiếu: CMR_12, CMR_06. |
| 5 | Nhà đầu tư | Textbox | Null | | x | Tự động điền từ API Quản lý dự án nội bộ theo dự án đã chọn ở cột 2. Với dự án có nhiều nhà đầu tư, hệ thống liệt kê tên các NĐT ngăn cách bằng dấu phẩy. Trạng thái: Disabled. Tham chiếu: CMR_12, CMR_06. |
| 6 | Quốc tịch nhà đầu tư | Textbox | Null | | x | Tự động điền từ API Quản lý dự án nội bộ theo dự án đã chọn ở cột 2. Hiển thị tương ứng với danh sách nhà đầu tư ở cột 5. Trạng thái: Disabled. Tham chiếu: CMR_12, CMR_06. |
| **Vốn đầu tư đã đăng ký** (chỉ áp dụng cho cột 7,8) | | | | | | |
| 7 | Vốn đầu tư nước ngoài (tr. USD) | Number | Null | | x | Tự động điền từ API IRC (Cổng 1 cửa QG) theo dự án đã chọn ở cột 2. Trạng thái: Disabled. Tham chiếu: CMR_12, CMR_05. |
| 8 | Vốn đầu tư trong nước (tỷ VNĐ) | Number | Null | | x | Tự động điền từ API IRC (Cổng 1 cửa QG) theo dự án đã chọn ở cột 2. Trạng thái: Disabled. Tham chiếu: CMR_12, CMR_05. |
| 9 | Văn bản thu hồi chủ trương đầu tư/giấy CNĐKĐT | Textbox | Null | x | x | Nhập tay. Người dùng nhập số/ký hiệu văn bản thu hồi. Hiển thị lỗi "Vui lòng nhập Văn bản thu hồi chủ trương đầu tư/giấy CNĐKĐT" nếu để trống khi Lưu nháp/Nộp. Tham chiếu: CMR_06. Placeholder: "Nhập Văn bản thu hồi chủ trương đầu tư/giấy CNĐKĐT". |
| B0a | Thêm dòng mục DA ĐT & KD kết cấu hạ tầng KCN, KKT | Button | | | x | Button luôn enable, khi người dùng click → hệ thống thêm 1 dòng vào cuối section Mục 1 – Dự án đầu tư xây dựng và kinh doanh kết cấu hạ tầng KCN, KKT. |
| B0b | Thêm dòng mục dự án SXKD trong KCN, KKT | Button | | | x | Button luôn enable, khi người dùng click → hệ thống thêm 1 dòng vào cuối section Mục 2 – Dự án đầu tư sản xuất kinh doanh trong KCN, KKT. |
| **CÁC BUTTON** | | | | | | |
| B1 | Hủy | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"). |
| B2 | Xem trước | Button | | | | Tham chiếu: CF_07.1. |
| B3 | Lưu nháp | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Lưu nháp]"). |
| B4 | Nộp báo cáo | Button | | | | Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |

---

### 3. Mô tả các xử lý của chức năng

Xử lý chung: Tham chiếu: CF_01 (Lập báo cáo), CMR_18, CF_04 (Xuất báo cáo), CF_05 (In).

Xử lý đặc thù biểu mẫu 2116.H:

- Khởi tạo màn hình: Bảng mở ra với 1 dòng trống mặc định. Các cột 3–8 ở trạng thái Disabled cho đến khi Dự án ở cột 2 được chọn. Tham chiếu: CF_01.
- Chọn Dự án (Cột 2): Ngay khi chọn, hệ thống gọi song song 2 API: (1) API Quản lý dự án nội bộ để điền cột 3, 4, 5, 6; (2) API IRC để điền cột 7, 8. Đồng thời hệ thống đọc thuộc tính loại hình dự án để phân loại bản ghi vào Mục 1 hoặc Mục 2. Tham chiếu: CMR_12.
- Cột 9 (Văn bản thu hồi): Trường duy nhất do người dùng nhập tay trong màn hình lập báo cáo. Validate bắt buộc khi Lưu nháp và Nộp (xử lý đặc thù biểu mẫu 2116.H — do tất cả cột khác auto-fill từ API, cột 9 phải required để đảm bảo có ít nhất 1 trường thông tin nhập). Tham chiếu: CMR_06.

---


## UC329-334.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ – Xem chi tiết, Xem vòng đời, In, Xuất báo cáo, Nộp, Chỉnh sửa
- Chức năng cho phép người dùng thực hiện các tác vụ bổ trợ tương ứng trạng thái bản ghi. Quyền truy cập được kiểm soát theo CMR_03.

Phân quyền: Ban Quản lý các KCN, KKT. Tham chiếu: CMR_03.

Truy cập chức năng: Màn danh sách báo cáo (UC329-334.1) → Cột Hành động → Chọn tác vụ tương ứng

Chức năng đáp ứng usecase số: 331, 332, 333, 334

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
| 1 | Nộp | Button | Chỉ khi báo cáo ở trạng thái Lưu nháp | Người tạo | Tham chiếu: CF_09. Tham chiếu: CF_01 (mục "Xử lý nút [Nộp báo cáo]"). |
| 2 | Chỉnh sửa | Button | Chỉ khi báo cáo ở trạng thái Yêu cầu chỉnh sửa và Lưu nháp | Người tạo | Tham chiếu: CF_03. |
| 3 | Xem chi tiết | Button | Tất cả trạng thái | Tất cả người dùng | Khi click vào sẽ mở màn hình Xem chi tiết báo cáo (toàn trang, toàn bộ Disabled). Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái | Tất cả người dùng | Khi click vào sẽ mở màn hình popup Vòng đời của báo cáo. Tham chiếu: CF_06. |
| 5 | In | Button | Tất cả trạng thái | | Khi click vào sẽ mở màn hình In. Tham chiếu: CF_05. |
| 6 | Xuất báo cáo | Button | Tất cả trạng thái | Tất cả người dùng | Khi click vào sẽ mở màn hình chọn ổ lưu file (định dạng Docx). Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người tạo | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Xem chi tiết: Form đọc toàn trang. Tham chiếu: CF_07.
- Xem vòng đời: Hiển thị Audit log. Tham chiếu: CF_06.
- In báo cáo: Kết xuất PDF/In. Tham chiếu: CF_05.
- Xuất báo cáo: Kết xuất ra file Docx. Tham chiếu: CF_04.
- Chỉnh sửa báo cáo: Cho phép sửa khi bản ghi Lưu nháp hoặc Yêu cầu chỉnh sửa. Tham chiếu: CF_03.

---


---

## 4. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | Bảng thuộc tính | (Không có) | Thêm dòng: Loại báo cáo = Có phạm vi (Chọn dự án); Phạm vi báo cáo = Không có phạm vi | Bổ sung theo yêu cầu BA |
| 2026-05-07 | 1.0 → 1.1 | UC329-334.2 > Mô tả giao diện > Bảng trường | (Không có) | Thêm 2 button: B0a – Thêm dòng mục DA ĐT & KD kết cấu hạ tầng KCN, KKT; B0b – Thêm dòng mục dự án SXKD trong KCN, KKT | Bổ sung cơ chế thêm nhiều dòng dự án (audit Q3) |
| 2026-05-07 | 1.0 → 1.1 | UC329-334.2 > CÁC BUTTON | (Không có) | Thêm B4: Xem chi tiết. Tham chiếu CF_01 (mục "Xử lý nút [Xem chi tiết]") | Bổ sung button Xem chi tiết (audit Q3) |
| 2026-05-07 | 1.0 → 1.1 | UC329-334.2 > Mô tả xử lý > Cột 9 | Validate bắt buộc khi Nộp | Validate bắt buộc khi Lưu nháp và Nộp (xử lý đặc thù biểu mẫu 2116.H) | Làm rõ validate Cột 9 (audit Q5) |
| 2026-05-07 | 1.1 → 1.2 | Bảng thuộc tính > Loại báo cáo | Loại báo cáo = Có phạm vi (Chọn dự án) | (Đã xóa) | Xóa dòng thừa theo yêu cầu BA |
| 2026-05-07 | 1.1 → 1.2 | Bảng thuộc tính > Quy tắc sinh mã báo cáo | KCN_2116H_[ID] | EZ_2116H_[ID] | Sửa tiền tố mã báo cáo |
| 2026-05-07 | 1.1 → 1.2 | UC329-334.1 > Khung Điều kiện Lọc & Tìm kiếm | (Không có) | Thêm trường #5: Năm (Yearpicker) — Lọc danh sách theo năm báo cáo. Tham chiếu: CMR_07 | Bổ sung filter Năm |
| 2026-05-07 | 1.1 → 1.2 | UC329-334.2 > Cột 2 Tên dự án đầu tư > Mô tả | Tham chiếu: CF_01, CMR_04 | Tham chiếu: CF_01, CMR_04, CMR_07 | Bổ sung CMR_07 cho Dropdown |
| 2026-05-07 | 1.2 → 1.3 | Thuộc tính chung | Phạm vi báo cáo | Phạm vi dữ liệu đầu vào | Thay đổi tên thuộc tính theo yêu cầu |
| 2026-05-07 | 1.2 → 1.3 | Khung lọc & tìm kiếm | Kỳ báo cáo (Dropdown) | Năm (YearPicker) | Cập nhật điều kiện lọc theo yêu cầu |
| 2026-05-11 | 1.3 → 1.4 | Quy tắc sinh mã báo cáo | `EZ_2116H_[ID]` | `EZ_2116HQLKKT_[ID]` | Chuẩn hóa suffix HQLKKT đầy đủ theo appendices.md v2.0 |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | +1 | Điều kiện hiển thị nút | `Luôn hiển thị` | `Tất cả trạng thái` | Chuẩn hóa điều kiện (INS-07) |
| 2026-05-11 | 1.3 → 1.4 | Precondition & Postcondition | (Không có) | Bổ sung Precondition và Postcondition | Bổ sung Hậu điều kiện và Tiền điều kiện lập báo cáo |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (1 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them , CMR_18 vao tham chieu CF_01 tren man hinh lap bao cao | Tuan thu CMR_18 Tab Navigation (STD-07) |
| 2026-05-17 | CMR v2.0 | STD-02 Required messages (1 truong) | Truong bat buoc | Vui long nhap/chon [ten truong] | Dong bo CMR_05/06/07 v2.0 |
| 2026-05-17 | CMR v2.0 | STD-01 Them CMR_16 vao filter dropdown rows (1 dong) | Chua co CMR_16 | Them tham chieu CMR_16 | Filter phai co Tat ca default |
| 2026-05-17 | CMR v2.0 | STD-04a Placeholder text/numeric (1 truong) | Nhap du lieu | Nhap [ten truong cu the] | CMR_06 STD-04a |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.4 → 1.5 | Bảng thuộc tính | (Không có) | Bổ sung Loại quy trình: Quy trình > 2 bước, CMCĐT_BCTK_04 | Phân loại luồng quy trình theo yêu cầu |
| 2026-05-21 | 1.5 → 1.6 | Bảng mô tả giao diện Lập báo cáo (UC329-334.2) | Cấu trúc cũ với tên cột cũ | Thêm dòng "Vốn đầu tư đã đăng ký" ngay dưới "Quốc tịch nhà đầu tư"; chuyển STT 7, 8 xuống dưới khung này; cập nhật tên các cột STT 3, 7, 8, 9 | Cập nhật cấu trúc bảng và thuộc tính theo yêu cầu nghiệp vụ mới của người dùng |
| 2026-05-23 | 1.6 → 1.7 | UC329-334.2 > Dòng 2 (Tên dự án đầu tư) > Ghi chú | (Không có validate trùng) | Thêm: Khi chọn dự án đã được chọn trước đó thì không cho chọn và hiển thị message lỗi inline "Dự án được chọn trước đó. Vui lòng kiểm tra lại" | Bổ sung validate trùng dự án |
| 2026-05-23 | 1.6 → 1.7 | UC329-334.2 > Dòng 3,4,5,6 > Giá trị mặc định | Từ API | Null | Chuẩn hóa giá trị mặc định |
| 2026-05-23 | 1.6 → 1.7 | UC329-334.2 > Dòng 3,4,5,6 > Ghi chú | (Không có) | Thêm đầu: "Không hiển thị placeholder." — Thêm cuối: CMR_06 | Bổ sung quy tắc placeholder và tham chiếu CMR_06 |
| 2026-05-23 | 1.6 → 1.7 | UC329-334.2 > Dòng 7,8 > Kiểu trường | Textbox | Number | Chuẩn hóa kiểu dữ liệu số |
| 2026-05-23 | 1.6 → 1.7 | UC329-334.2 > Dòng 7,8 > Giá trị mặc định | Từ IRC | Null | Chuẩn hóa giá trị mặc định |
| 2026-05-23 | 1.6 → 1.7 | UC329-334.2 > Dòng 7,8 > Ghi chú | (Không có) | Thêm đầu: "Không hiển thị placeholder." — Thêm cuối: CMR_05 | Bổ sung quy tắc placeholder và tham chiếu CMR_05 |
