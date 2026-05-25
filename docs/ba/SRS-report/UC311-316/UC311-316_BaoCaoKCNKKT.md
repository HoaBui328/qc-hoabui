# UC311-316: Báo cáo Tình hình thu hút dự án đầu tư sản xuất kinh doanh trong khu kinh tế lũy kế đến cuối kỳ báo cáo

| Thuộc tính               | Giá trị                                      |
| --- | --- |
| **BA phụ trách**   | yen.trinh                                     |
| **Phân hệ**        | Báo cáo KKT/KCN                                |
| **Mẫu biểu**       | Biểu số 2113.H.QLKKT                           |
| **Loại báo cáo**  | Định kỳ Quý/Năm                                 |
| **Phạm vi dữ liệu đầu vào** | Không có phạm vi |
| **Hình thức nộp** | Báo cáo đơn lẻ (Single report form)           |
| **Cơ quan nhận**   | Cục Đầu tư nước ngoài                          |
| **Đối tượng lập** | Ban Quản lý các khu công nghiệp, kinh tế      |
| **Giao diện**      | Admin site                                     |
| **Ngày tạo**       | 2026-04-22                                     |
| **Phiên bản**      | 1.6                                            |
| **Quy tắc sinh mã báo cáo** | EZ_2113HQLKKT_[ID]                    |
| **Loại quy trình** | Quy trình > 2 bước, CMCĐT_BCTK_04 |

---

## UC311-316.1: Xem Danh Sách Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Xem danh sách Báo cáo Tình hình thu hút dự án đầu tư sản xuất kinh doanh trong khu kinh tế lũy kế đến cuối kỳ báo cáo.
- Chức năng cho phép Ban Quản lý các khu công nghiệp, kinh tế truy cập màn hình chính để theo dõi danh sách các báo cáo định kỳ Quý/Năm.

**Precondition:** Người dùng đã đăng nhập thành công và được phân quyền "Cán bộ chuyên môn Ban Quản lý các khu công nghiệp, kinh tế".

Phân quyền: Ban Quản lý các khu công nghiệp, kinh tế.

Truy cập chức năng: Phân hệ Báo cáo KKT/KCN → Tình hình thu hút dự án đầu tư.

Chức năng đáp ứng usecase số: 311, 312, 313, 314, 315, 316

---

### 2. Mô tả giao diện

**Giao diện danh sách**

Giao diện:

**Periodic-single**: Giao diện mẫu cho báo cáo có kỳ hạn và gửi lẻ từng báo cáo

Mô tả giao diện:

| #                                                     | Tên trường           | Kiểu trường              | Giá trị mặc định | Được sửa | Bắt buộc | Mô tả                                                                                                                                                                                                                                                                                                         |
| --- | --- | --- | --- | --- | --- | --- |
| **Khung Điều kiện Lọc & Tìm kiếm**        |                         |                             |                       |              |            |                                                                                                                                                                                                                                                                                                                 |
| 1 | Năm | YearPicker | Null | x | | Lọc danh sách theo năm báo cáo. Kết quả hiển thị ngay khi chọn. |
| 2                                                     | Trạng thái kỳ        | Multiple-selection Dropdown | Null                  | x            |            | Lọc theo trạng thái của kỳ hạn. Tham chiếu: CMR_04, CMR_07., CMR_16                                                                                        |
| 3                                                     | Trạng thái báo cáo  | Multiple-selection Dropdown | Null                  | x            |            | Người dùng chọn một hoặc nhiều giá trị: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Kết quả lọc hiển thị ngay sau khi chọn. Tham chiếu: CMR_03, CMR_07., CMR_16 |
| 4                                                     | Mã báo cáo           | Search bar                  | Null                  | x            |            | Tìm kiếm theo mã báo cáo. Kết quả hiển thị ngay khi nhập. Tham chiếu: CMR_06, CMR_09. Placeholder: "Tìm kiếm nhanh theo mã báo cáo". |
| **Khung Danh sách Kỳ hạn**                  |                         |                             |                       |              |            |                                                                                                                                                                                                                                                                                                                 |
| 5                                                     | Kỳ hạn báo cáo        | Label                       | Null                  |              |            | Mặc định collapse; click mũi tên để expand danh sách. Tham chiếu: CMR_08. |
| 6                                                     | Trạng thái kỳ báo cáo | Label                       | Null                  |              |            | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| 7                                                     | Lập báo cáo           | Button                      | Null                  |              |            | Luôn enable. Chỉ hiển thị khi kỳ ở trạng thái Trong thời hạn. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CF_01, CMR_04. |
| 8                                                     | Nhập từ file                | Button                      | Null                  |              |            | Luôn enable. Mở màn hình chọn/kéo thả file. Chỉ hiển thị khi kỳ ở trạng thái Trong thời hạn. Ẩn khi Chưa tới hạn hoặc Qua kỳ báo cáo. Tham chiếu: CMR_04. |
| **Khung Danh sách Báo cáo**                 |                         |                             |                       |              |            |                                                                                                                                                                                                                                                                                                                 |
| 5                                                     | Mã báo cáo           | Label                       | Null                  |              |            | Hiển thị mã báo cáo do hệ thống sinh cho mỗi báo cáo. Tham chiếu: CMR_09.                                                                                                                                                                                                                                 |
| 6                                                     | Ngày cập nhật | Label                       | Null                  |              |            | Định dạng ngày giờ.                                                                                                                                                                                                                                             |
| 7                                                     | Trạng thái            | Label                       | Null                  |              |            | Hiển thị trạng thái báo cáo. Tham chiếu: CMR_03.                                                                                                                                                                                  |
| 8                                                     | Hành động            | Button group                | Null                  |              |            | Nộp, Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Xuất báo cáo. Chi tiết tham chiếu UC311-316.3.                                                                                                                                                                                                                  |

---

### 3. Mô tả các xử lý của chức năng

- Thao tác lọc & tìm kiếm: Hiển thị kết quả ngay lập tức sau khi người dùng tương tác. Tham chiếu: CMR_07.
- Quy tắc quyền truy cập danh sách: Áp dụng CMR_02 cho các tài khoản Ban Quản lý khác nhau.

---

## UC311-316.2: Lập Báo Cáo

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Tạo mới Báo cáo Tình hình thu hút dự án đầu tư sản xuất kinh doanh trong khu kinh tế lũy kế đến cuối kỳ báo cáo.
- Chức năng cho phép người dùng thêm nhiều dự án vào báo cáo. Dữ liệu một số trường được Auto-fill từ API dự án. Tham chiếu: CF_01, CMR_18.

**Precondition:** Dữ liệu Master Data về danh sách dự án phải có sẵn trên hệ thống. Tài khoản có quyền lập báo cáo.

**Postcondition:** Khi Lưu nháp, báo cáo có trạng thái "Lưu nháp". Khi nộp, bản ghi được lưu vào DB với trạng thái "Chờ duyệt", đồng thời trigger quy trình workflow tiếp theo.

Phân quyền: Ban Quản lý các khu công nghiệp, kinh tế. Chỉ người lập báo cáo mới có quyền chỉnh sửa, các tài khoản khác chỉ có quyền xem (Tham chiếu CMR_02).

Truy cập chức năng: Màn danh sách báo cáo (UC311-316.1) → Nhấn nút [Lập báo cáo].

Chức năng đáp ứng usecase số: 311, 312

---

### 2. Mô tả giao diện

**Giao diện thêm mới**

Giao diện: Periodic-single

Mô tả giao diện:

| #                                                              | Tên trường                                                                                                | Kiểu trường | Giá trị mặc định | Được sửa | Bắt buộc | Ghi chú                                                                                                                                                                                                                                                                                 |
| --- | --- | --- | --- | --- | --- | --- |
| **BẢNG DANH SÁCH DỰ ÁN**                        |                                                                                                              |                |                       |              |            | Hệ thống cho phép bấm "Thêm dòng" để chọn nhiều dự án. Không cho phép chọn trùng dự án ở hai dòng khác nhau. Thêm cột/nút "Xóa" tại mỗi dòng. Hành vi: Cho phép xóa dòng, khi bảng còn 1 dòng thì sẽ ẩn icon xóa đi (vì lúc đó báo cáo tối thiểu yêu cầu 1 dòng dữ liệu).                                                                                                                            |
| Thêm dòng                                                              | Thêm dòng                                                                                                        | Button         |                       | x            |            | Luôn enable, khi click vào hệ thống sẽ thêm 1 dòng mới vào cuối bảng trước dòng tính tổng. |
| Xóa                                                                    | Xóa                                                                                                              | Button         |                       | x            |            | Chỉ hiển thị và enable khi bảng có ít nhất 2 dòng. Nếu bảng chỉ có 1 dòng thì button "Xóa" sẽ ẩn đi. Khi click vào nút Xóa thì dòng chứa nó sẽ bị xóa và các dòng dưới dòng xóa sẽ được đẩy lên. Tổng tiền sẽ tự động được tính lại. |
| 1                                                              | STT                                                                                                        | Label          | Tính tự động      |              |            | Số thứ tự dòng.                                                                                                                                                                                                                                                                          |
| 2                                                              | Tên dự án sản xuất kinh doanh                                                                           | Dropdown       | Null                  | x            | x          | Khi người dùng click vào Tên dự án sản xuất kinh doanh thì sẽ hiển thị ra các dự án/ khu chức năng của KKT được trả qua API. Sau khi chọn dự án, hệ thống sẽ autofill các thông tin về vốn đầu tư đăng ký, vốn đầu tư thực hiện theo dự án (Nếu thay đổi dự án, các thông tin autofill cũng sẽ thay đổi giá trị theo dự án mới). Khi người dùng chọn dự án đã được chọn trước ở dòng trước đó trong báo cáo thì không cho chọn và hiển thị thông báo lỗi như sau: Dự án này đã được chọn trước ở dòng trước đó trong báo cáo. Vui lòng kiểm tra lại. Tham chiếu: CF_01, CMR_18, CMR_07. |
| 3                                                              | Tình trạng                                                                                                 | Dropdown       | Null                  | x            | x          | Gồm: đang xây dựng; đã đi vào hoạt động. Tham chiếu: CMR_07.                                                                                                                                                                                                              |
| 4                                                              | Quy mô diện tích thực hiện (ha)                                                                           | Number        | Null               |              | x          | Tự động điền từ API. Mặc định bị khóa (Disabled) theo CMR_12. Nếu API không trả về dữ liệu, hệ thống tự động mở khóa (Enable) để người dùng điền tay. Tham chiếu: CMR_05. |
| 5                                                              | Ngành nghề                                                                                                 | String        | Null                  |              | x          | Autofill theo tên dự án cột 2 (nếu trả về nhiều giá trị hiển thị liệt kê cách nhau bởi dấu ";"). Mặc định bị khóa (Disabled) theo CMR_12. Nếu API không trả về dữ liệu, hệ thống mở khóa (Enable). Tham chiếu: CMR_06, CMR_05. |
| **DỰ ÁN ĐẦU TƯ VỐN NƯỚC NGOÀI**                 |                                                                                                              |                |                       |              |            |                                                                                                                                                                                                                                                                                          |
| 6                                                              | Vốn đầu tư đăng ký (tr. USD)                                                                            | Number        | Null               |              | x          | Tự động điền từ API. Mặc định bị khóa (Disabled) theo CMR_12. Nếu API không trả về dữ liệu, hệ thống mở khóa (Enable). Tham chiếu: CMR_05.  |
| 7                                                              | Vốn đầu tư thực hiện (tr. USD)                                                                           | Number        | Null               |              | x          | Tự động điền từ API. Mặc định bị khóa (Disabled) theo CMR_12. Nếu API không trả về dữ liệu, hệ thống mở khóa (Enable). Tham chiếu: CMR_05.  |
| 8                                                              | Doanh thu (tr. USD)                                                                                        | Number        | Null                  | x            | x          | Nhập giá trị >= 0. Tham chiếu: CMR_05.                                                                                                                                                                                                                                   |
| 9                                                              | Xuất khẩu (tr. USD)                                                                                        | Number        | Null                  | x            | x          | Nhập giá trị >= 0. Tham chiếu: CMR_05.                                                                                                                                                                                                                                   |
| 10                                                             | Nhập khẩu (tr. USD)                                                                                        | Number        | Null                  | x            | x          | Nhập giá trị >= 0. Tham chiếu: CMR_05.                                                                                                                                                                                                                                   |
| 11                                                             | Nộp ngân sách (tỷ VNĐ)                                                                                     | Number        | Null                  | x            | x          | Nhập giá trị >= 0. Tham chiếu: CMR_05.                                                                                                                                                                                                                                   |
| **DỰ ÁN ĐẦU TƯ VỐN TRONG NƯỚC**                 |                                                                                                              |                |                       |              |            |                                                                                                                                                                                                                                                                                          |
| 12                                                             | Vốn đầu tư đăng ký (tỷ VNĐ)                                                                             | Number        | Null                  |              | x          | Tự động điền từ API. Mặc định bị khóa (Disabled) theo CMR_12. Nếu API không trả về dữ liệu, hệ thống mở khóa (Enable). Tham chiếu: CMR_05.                                                                                                                                                                                                                                   |
| 13                                                             | Vốn đầu tư thực hiện (tỷ VNĐ)                                                                            | Number        | Null                  |              | x          | Tự động điền từ API. Mặc định bị khóa (Disabled) theo CMR_12. Nếu API không trả về dữ liệu, hệ thống mở khóa (Enable). Tham chiếu: CMR_05.                                                                                                                                                                                                                                   |
| 14                                                             | Doanh thu (tỷ VNĐ)                                                                                         | Number        | Null                  | x            | x          | Nhập giá trị >= 0. Tham chiếu: CMR_05.                                                                                                                                                                                                                                   |
| 15                                                             | Xuất khẩu (tr. USD)                                                                                        | Number        | Null                  | x            | x          | Nhập giá trị >= 0. Tham chiếu: CMR_05.                                                                                                                                                                                                                                   |
| 16                                                             | Nhập khẩu (tr. USD)                                                                                        | Number        | Null                  | x            | x          | Nhập giá trị >= 0. Tham chiếu: CMR_05.                                                                                                                                                                                                                                   |
| 17                                                             | Nộp ngân sách (tỷ VNĐ)                                                                                     | Number        | Null                  | x            | x          | Nhập giá trị >= 0. Tham chiếu: CMR_05.                                                                                                                                                                                                                                   |
| **LAO ĐỘNG**                                            |                                                                                                              |                |                       |              |            |                                                                                                                                                                                                                                                                                          |
| 18                                                             | Trong nước                                                                                                 | Number        | Null                  | x            | x          | Nhập giá trị >= 0. Tham chiếu: CMR_06. Placeholder: "Nhập Trong nước". |
| 19                                                             | Nước ngoài                                                                                                 | Number        | Null                  | x            | x          | Nhập giá trị >= 0. Tham chiếu: CMR_06. Placeholder: "Nhập Nước ngoài". |
| **DÒNG TỔNG CỘNG**                                     |                                                                                                              |                |                       |              |            |                                                                                                                                                                                                                                                                                          |
| 20                                                             | Tổng cộng                                                                                                  | Number          | Tính tự động      |              |            | Auto-sum tất cả các dòng phía trên cho tất cả các cột số (Trừ cột 3: Tình trạng, 5: Ngành nghề). Không cho phép chỉnh sửa. Tham chiếu: CMR_05, CMR_06.                                                                                                                           |
| Lập báo cáo                                                    | Lập báo cáo                                                                                                | Button         | Null                  | x            |            | Chỉ hiển thị và enable khi Kỳ báo cáo ở trạng thái "Trong thời hạn", các trạng thái khác của kỳ báo cáo thì button này sẽ bị ẩn đi. Tham chiếu CF_01, CMR_04. |
| Nhập từ file                                                         | Nhập từ file                                                                                                     | Button         | Null                  | x            |            | Chỉ hiển thị và enable khi Kỳ báo cáo ở trạng thái "Trong thời hạn", các trạng thái khác của kỳ báo cáo thì button này sẽ bị ẩn đi. Tham chiếu CF_01, CMR_04. |
| **Các Button**                                          |                                                                                                              |                |                       |              |            |                                                                                                                                                                                                                                                                                          |
|  | Hủy                                                                                                         | Button         |                       |              |            | Tham chiếu: CF_01, CMR_18. |
|  | Xem trước | Button |                       |              |            | Mở popup PDF Preview. Tham chiếu: CF_07.1. |
|  | Lưu nháp                                                                                                   | Button         |                       |              |            | Tham chiếu: CF_01, CMR_18. Các tài khoản khác sẽ chỉ có quyền View. Tham chiếu: CMR_02. |
|  | Nộp báo cáo                                                                                               | Button         |                       |              |            | Tham chiếu: CF_01, CMR_18. |

---

### 3. Mô tả các xử lý của chức năng

- Quản lý dòng báo cáo: Bắt buộc người dùng nhấn "Thêm dòng" để chọn và điền từng dự án. Hệ thống thực hiện check trùng lặp dự án giữa các dòng.
- Xử lý Auto-fill (CMR_05): Tự động điền diện tích, vốn đăng ký, vốn thực hiện và khóa trường. Trong trường hợp API không trả về data, hệ thống phải xử lý mở khóa trường (Enable) để hỗ trợ nhập liệu thủ công.
- API Error / Timeout: Thêm kịch bản ngoại lệ khi gọi API danh sách dự án từ Master Data/IRC bị lỗi hoặc timeout. Nếu thất bại, hệ thống sẽ mở khóa trường (Enable) để người dùng nhập tay. Tham chiếu CMR_12.
- Xử lý phân quyền: Gán quyền cho người tạo. Các người dùng cùng tổ chức (BQL) không khởi tạo báo cáo chỉ có quyền xem, tương tự logic NĐT khác của CMR_02.

---

## UC311-316.3: Các Tác Vụ Bổ Trợ

### 1. Mô tả chức năng

Mô tả:

- Tên chức năng: Các tác vụ bổ trợ - Xem chi tiết, Xem vòng đời, In, Kết xuất, Nộp, Chỉnh sửa.

Phân quyền: Tuân thủ theo phân quyền tại chức năng Danh sách và CMR_03, CMR_02 (Ai lập mới được quyền sửa, người khác chỉ xem).

Truy cập chức năng: Màn danh sách báo cáo (UC311-316.1) → Cột Hành động.

Chức năng đáp ứng usecase số: 313, 314, 315, 316

---

### 2. Mô tả giao diện

Tham chiếu: CF_07, CF_06, CF_05, CF_04, CF_03.

**Các Button theo Action Mapping:**

| # | Tên            | Kiểu  | Điều kiện hiển thị                                          | Phân quyền                  | Mô tả                       |
| --- | --- | --- | --- | --- | --- |
| 1 | Nộp            | Button | Lưu nháp, Yêu cầu chỉnh sửa                        | Người khởi tạo bản ghi | Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_18. |
| 2 | Chỉnh sửa     | Button | Chỉ hiển thị khi Lưu nháp và Yêu cầu chỉnh sửa    | Người khởi tạo bản ghi | Tham chiếu: CF_03. |
| 3 | Xem chi tiết   | Button | Tất cả trạng thái                                            | Tất cả người dùng        | Tham chiếu: CF_07. |
| 4 | Xem vòng đời | Button | Tất cả trạng thái                                            | Tất cả người dùng        | Tham chiếu: CF_06. |
| 5 | In              | Button | Tất cả trạng thái                                            | Tất cả người dùng        | Tham chiếu: CF_05. |
| 6 | Xuất báo cáo         | Button | Tất cả trạng thái                                            | Tất cả người dùng        | Tham chiếu: CF_04. |
| 7 | Xóa | Button | Lưu nháp **VÀ** chưa từng nộp | Người khởi tạo bản ghi | Tham chiếu: CF_08. |

---

### 3. Mô tả các xử lý của chức năng

- Nộp: Tham chiếu: CF_09. Tham chiếu: CF_01, CMR_18. Cho phép nộp từ Lưu nháp và YCCSR (CMR_03).
- Chỉnh sửa: Tham chiếu: CF_03.
- Xem chi tiết: Tham chiếu: CF_07. Nút [Chỉnh sửa] ẩn nếu không đủ điều kiện (CMR_03).
- Xem vòng đời: Tham chiếu: CF_06.
- In: Tham chiếu: CF_05.
- Xuất báo cáo: .docx. Tham chiếu: CF_04.
- Xóa: Tham chiếu: CF_08.

---



---

## 4. Tiêu chí chấp nhận (Acceptance Criteria)

- **AC-01**: Lập báo cáo thành công với đầy đủ các trường bắt buộc.
- **AC-02**: Validate bỏ trống trường bắt buộc.
- **AC-03**: Xóa dòng và tự động tính lại dòng tổng.

---

## 5. Lịch sử cập nhật

| Ngày | Phiên bản | Mục cập nhật | Before | After | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| 2026-05-03 | N/A | Trạng thái báo cáo | Đã nộp | Chờ duyệt / Đã tiếp nhận | Thay đổi theo bộ trạng thái mới của hệ thống (CMR_03) |
| 2026-05-07 | 1.0 → 1.1 | Cập nhật theo Audit | (Nhiều mục) | (Đã cập nhật theo Implementation Plan) | Thêm nút Xóa/Thêm dòng, Pre/Post conditions, đổi tên nút |
| 2026-05-07 | 1.1 → 1.2 | Thuộc tính chung | Phạm vi báo cáo | Phạm vi dữ liệu đầu vào | Thay đổi tên thuộc tính theo yêu cầu |
| 2026-05-07 | 1.1 → 1.2 | Khung lọc & tìm kiếm | Kỳ báo cáo | Năm (YearPicker) | Cập nhật điều kiện lọc theo yêu cầu |
| 2026-05-08 | 1.2 → 1.3 | UI/UX & Hành vi | N/A | Bổ sung nút Thêm dòng, Xóa dòng, Lập báo cáo, Nhập từ file | Cập nhật theo Implementation Plan |
| 2026-05-08 | 1.2 → 1.3 | UI/UX & Hành vi | Chọn dự án bình thường | Xử lý autofill và validate trùng lặp dự án | Cập nhật theo Implementation Plan |
| 2026-05-08 | 1.2 → 1.3 | Exception Flow | N/A | Bổ sung kịch bản ngoại lệ khi API lỗi/timeout | Cập nhật theo Implementation Plan |
| 2026-05-08 | 1.2 → 1.3 | Acceptance Criteria | N/A | Bổ sung AC-01 đến AC-03 | Cập nhật theo Implementation Plan |
| 2026-05-11 | +1 | Tên cột | `Ngày cập nhật / Nộp` | `Ngày cập nhật` | Đồng bộ tên cột theo CS_02 (INS-03) |
| 2026-05-11 | 1.3 → 1.4 | Hậu điều kiện | ...Khi Nộp, bản ghi được lưu vào DB với trạng thái "Đã tiếp nhận" hoặc "Chờ duyệt"... | ...Khi nộp, bản ghi được lưu vào DB với trạng thái "Chờ duyệt"... | Cập nhật Hậu điều kiện luồng nộp báo cáo |
| 2026-05-17 | 1.4 → 1.5 | UC311-316.1 UI | (Không có) | Bổ sung Khung Danh sách Kỳ hạn | Chuyển nút Lập báo cáo, Nhập từ file ra ngoài danh sách để đồng bộ với các màn hình báo cáo định kỳ khác |
| 2026-05-17 | 1.4 → 1.5 | UC311-316.2 UI | Chứa 2 nút Lập báo cáo, Nhập từ file | (Đã xóa) | Xóa vì bị dư thừa do đã chuyển ra màn hình UC311-316.1 |
| 2026-05-17 | CMR v2.0 | Placeholder Search bar (1 dong) | Nhap du lieu | Tim kiem nhanh theo ma bao cao | Chuan hoa CMR_06 v2.0 STD-04b |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_16 (2 dong filter dropdown) | Chua co CMR_16 | Them , CMR_16 sau CMR_07 tren cac dong Multiple-selection Dropdown | Filter dropdown phai co option Tat ca (CMR_16) |
| 2026-05-17 | CMR v2.0 | Them tham chieu CMR_18 (Tab Navigation) | Chua co CMR_18 | Them CMR_18 vao tham chieu CF_01 | Tuan thu CMR_18 Tab Navigation tren form nhap lieu |
| 2026-05-17 | CMR v2.0 | STD-04a Placeholder text/numeric (2 truong) | Nhap du lieu | Nhap [ten truong cu the] | CMR_06 STD-04a |
| 2026-05-18 | CMR v2.0 -> 2.1 | Thuật ngữ nút bấm | Export / Import | Xuất báo cáo / Nhập từ file | Cập nhật đồng bộ tiếng Việt |
| 2026-05-18 | 1.4 → 1.5 | Bảng thuộc tính | (Không có) | Bổ sung Loại quy trình: Quy trình > 2 bước, CMCĐT_BCTK_04 | Phân loại luồng quy trình theo yêu cầu |
| 2026-05-23 | 1.5 → 1.6 | Dòng 4, 5, 6, 7, 12, 13 — Ghi chú | (Không có prefix) | Thêm "Không hiển thị placeholder" vào đầu Ghi chú | Trường autofill không hiển thị placeholder |
| 2026-05-23 | 1.5 → 1.6 | Dòng 4, 6, 7 — Giá trị mặc định | Từ API | Null | Đồng bộ giá trị mặc định cho trường autofill |
| 2026-05-23 | 1.5 → 1.6 | Dòng 4, 5, 6, 7, 12, 13 — Được sửa | x | (Trống) | Trường autofill mặc định không cho sửa, CMR_12 quy định ngoại lệ |
| 2026-05-23 | 1.5 → 1.6 | Dòng 18, 19 — Kiểu trường | Textbox | Number | Đổi kiểu trường phù hợp dữ liệu số |
| 2026-05-23 | 1.5 → 1.6 | Dòng 20 — Kiểu trường | Label | Number | Đổi kiểu trường phù hợp dữ liệu số |
| 2026-05-23 | 1.5 → 1.6 | Dòng 20 — Tham chiếu | CMR_06 | CMR_05, CMR_06 | Thêm tham chiếu CMR_05 cho dòng tổng |
